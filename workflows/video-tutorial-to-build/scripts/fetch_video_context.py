#!/usr/bin/env python3
"""Fetch video metadata and subtitles with yt-dlp."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=False)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--out", default="video_context")
    parser.add_argument("--langs", default="zh.*,en.*,en")
    args = parser.parse_args()

    ytdlp = shutil.which("yt-dlp") or shutil.which("yt-dlp.exe")
    if not ytdlp:
        print("Missing dependency: yt-dlp. Install with: python -m pip install yt-dlp", file=sys.stderr)
        return 2

    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)

    meta = run([ytdlp, "--dump-json", "--skip-download", args.url])
    if meta.returncode != 0:
        print(meta.stderr or meta.stdout, file=sys.stderr)
        return meta.returncode

    metadata_path = out / "metadata.json"
    metadata_path.write_text(meta.stdout, encoding="utf-8")

    try:
        info = json.loads(meta.stdout)
    except json.JSONDecodeError:
        info = {}

    subtitle_cmd = [
        ytdlp,
        "--skip-download",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs",
        args.langs,
        "--sub-format",
        "vtt/srt/best",
        "-o",
        str(out / "%(id)s.%(ext)s"),
        args.url,
    ]
    subs = run(subtitle_cmd)

    files = sorted(str(p.name) for p in out.iterdir())
    summary = {
        "title": info.get("title"),
        "id": info.get("id"),
        "duration": info.get("duration"),
        "chapters": info.get("chapters") or [],
        "subtitles_available": sorted((info.get("subtitles") or {}).keys()),
        "automatic_captions_available": sorted((info.get("automatic_captions") or {}).keys()),
        "requested_subtitle_langs": args.langs,
        "subtitle_command_returncode": subs.returncode,
        "subtitle_stderr": subs.stderr[-2000:],
        "files": files,
    }
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
