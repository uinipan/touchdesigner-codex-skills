#!/usr/bin/env python3
"""Download audio and transcribe locally with faster-whisper."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=False)


def missing(name: str, install_hint: str) -> None:
    print(f"Missing dependency: {name}. Install with: {install_hint}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--out", default="video_context")
    parser.add_argument("--model", default="small")
    parser.add_argument("--language", default=None)
    args = parser.parse_args()

    ytdlp = shutil.which("yt-dlp") or shutil.which("yt-dlp.exe")
    ffmpeg = shutil.which("ffmpeg") or shutil.which("ffmpeg.exe")
    if not ytdlp:
        missing("yt-dlp", "python -m pip install yt-dlp")
        return 2
    if not ffmpeg:
        missing("ffmpeg", "winget install Gyan.FFmpeg or install ffmpeg and add it to PATH")
        return 2

    try:
        from faster_whisper import WhisperModel
    except Exception:
        missing("faster-whisper", "python -m pip install faster-whisper")
        return 2

    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    audio_template = str(out / "audio.%(ext)s")
    dl = run([ytdlp, "-x", "--audio-format", "wav", "-o", audio_template, args.url])
    if dl.returncode != 0:
        print(dl.stderr or dl.stdout, file=sys.stderr)
        return dl.returncode

    audio_files = sorted(out.glob("audio.*"))
    if not audio_files:
        print("Audio download completed but no audio file was found.", file=sys.stderr)
        return 1

    model = WhisperModel(args.model, device="auto", compute_type="auto")
    segments, info = model.transcribe(str(audio_files[0]), language=args.language)

    transcript_path = out / "transcript.tsv"
    md_path = out / "transcript.md"
    rows: list[str] = []
    md: list[str] = [f"# Transcript\n\nDetected language: {info.language}\n"]
    for seg in segments:
        rows.append(f"{seg.start:.2f}\t{seg.end:.2f}\t{seg.text.strip()}")
        md.append(f"\n[{seg.start:0.2f} - {seg.end:0.2f}] {seg.text.strip()}")

    transcript_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    md_path.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(str(md_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
