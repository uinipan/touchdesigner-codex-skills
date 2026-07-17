#!/usr/bin/env python3
"""Extract visual keyframes from a tutorial URL or local video file.

The script supports local files directly. For URLs, it asks yt-dlp for a direct
media URL and lets ffmpeg seek to each timestamp, avoiding a full download when
the site supports it.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def find_exe(name: str, env_name: str | None = None) -> str | None:
    if env_name and os.environ.get(env_name):
        candidate = os.environ[env_name]
        if Path(candidate).exists():
            return candidate
    found = shutil.which(name)
    if found:
        return found
    python_scripts = Path.home() / "AppData/Local/Programs/Python/Python311/Scripts"
    candidate = python_scripts / f"{name}.exe"
    if candidate.exists():
        return str(candidate)
    return None


def is_url(value: str) -> bool:
    return value.startswith(("http://", "https://"))


def parse_timestamp(value: str) -> str:
    value = value.strip()
    if value.isdigit():
        seconds = int(value)
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"
    parts = value.split(":")
    if len(parts) == 2:
        return f"00:{int(parts[0]):02d}:{float(parts[1]):06.3f}"
    if len(parts) == 3:
        return value
    raise ValueError(f"Unsupported timestamp format: {value}")


def timestamp_to_seconds(value: str) -> float:
    ts = parse_timestamp(value)
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def seconds_to_timestamp(value: float) -> str:
    value = max(0.0, value)
    h = int(value // 3600)
    m = int((value % 3600) // 60)
    s = value % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}"


def safe_name(ts: str) -> str:
    return ts.replace(":", "-").replace(".", "_")


def get_direct_url(yt_dlp: str, url: str) -> str:
    cmd = [yt_dlp, "-f", "bv*[height<=1080]+ba/b[height<=1080]/best", "-g", url]
    result = subprocess.run(cmd, text=True, capture_output=True, check=True)
    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    if not lines:
        raise RuntimeError("yt-dlp returned no media URL")
    return lines[0]


def extract_frame(ffmpeg: str, source: str, timestamp: str, out_file: Path) -> None:
    cmd = [
        ffmpeg,
        "-hide_banner",
        "-loglevel",
        "error",
        "-ss",
        timestamp,
        "-i",
        source,
        "-frames:v",
        "1",
        "-y",
        str(out_file),
    ]
    subprocess.run(cmd, check=True)


def download_near_timestamp(yt_dlp: str, ffmpeg: str, url: str, timestamp: str, out_dir: Path) -> tuple[Path, str]:
    seconds = timestamp_to_seconds(timestamp)
    start = max(0.0, seconds - 1.0)
    end = seconds + 1.0
    section = f"*{seconds_to_timestamp(start)}-{seconds_to_timestamp(end)}"
    stem = f"clip_{safe_name(timestamp)}"
    template = str(out_dir / f"{stem}.%(ext)s")
    cmd = [
        yt_dlp,
        "-f",
        "bv*[height<=1080]+ba/b[height<=1080]/best",
        "--download-sections",
        section,
        "--force-keyframes-at-cuts",
        "--ffmpeg-location",
        str(Path(ffmpeg).parent),
        "-o",
        template,
        url,
    ]
    subprocess.run(cmd, check=True)
    matches = sorted(out_dir.glob(f"{stem}.*"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not matches:
        raise RuntimeError("yt-dlp section download produced no file")
    relative_seek = seconds_to_timestamp(seconds - start)
    return matches[0], relative_seek


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract tutorial keyframes.")
    parser.add_argument("source", help="Video URL supported by yt-dlp, or local video path")
    parser.add_argument("--timestamps", nargs="+", required=True, help="Timestamps like 00:04:42 or 282")
    parser.add_argument("--out", required=True, help="Output directory")
    args = parser.parse_args()

    ffmpeg = find_exe("ffmpeg", "FFMPEG")
    if not ffmpeg:
        print(json.dumps({
            "ok": False,
            "error": "ffmpeg not found. Install ffmpeg or set FFMPEG to the executable path.",
        }, ensure_ascii=False))
        return 2

    original_source = args.source
    source = args.source
    yt_dlp = None
    url_mode = is_url(source)
    if url_mode:
        yt_dlp = find_exe("yt-dlp", "YT_DLP")
        if not yt_dlp:
            print(json.dumps({
                "ok": False,
                "error": "yt-dlp not found. Needed for URL sources; local video files can be used without it.",
            }, ensure_ascii=False))
            return 2
        try:
            source = get_direct_url(yt_dlp, source)
        except Exception as exc:
            print(json.dumps({"ok": False, "error": f"yt-dlp failed: {exc}"}, ensure_ascii=False))
            return 3

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    frames = []
    for raw_ts in args.timestamps:
        ts = parse_timestamp(raw_ts)
        out_file = out_dir / f"keyframe_{safe_name(ts)}.jpg"
        try:
            extract_frame(ffmpeg, source, ts, out_file)
            frames.append({"timestamp": ts, "path": str(out_file), "ok": True})
        except Exception as exc:
            if url_mode and yt_dlp:
                try:
                    clip_path, relative_seek = download_near_timestamp(yt_dlp, ffmpeg, original_source, ts, out_dir)
                    extract_frame(ffmpeg, str(clip_path), relative_seek, out_file)
                    frames.append({
                        "timestamp": ts,
                        "path": str(out_file),
                        "ok": True,
                        "fallback": "yt-dlp section download",
                        "clip": str(clip_path),
                    })
                    continue
                except Exception as fallback_exc:
                    frames.append({
                        "timestamp": ts,
                        "path": str(out_file),
                        "ok": False,
                        "error": str(exc),
                        "fallbackError": str(fallback_exc),
                    })
                    continue
            frames.append({"timestamp": ts, "path": str(out_file), "ok": False, "error": str(exc)})

    print(json.dumps({"ok": all(item["ok"] for item in frames), "frames": frames}, ensure_ascii=False, indent=2))
    return 0 if all(item["ok"] for item in frames) else 4


if __name__ == "__main__":
    raise SystemExit(main())
