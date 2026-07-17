#!/usr/bin/env python3
"""Clean SRT/VTT/TSV transcripts into a compact Markdown timeline."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TIMECODE = re.compile(r"(?P<start>\d\d:)?\d\d:\d\d[.,]\d\d\d\s+-->\s+(?P<end>\d\d:)?\d\d:\d\d[.,]\d\d\d")
TAG = re.compile(r"<[^>]+>")


def clean_line(line: str) -> str:
    line = TAG.sub("", line)
    line = line.replace("&nbsp;", " ").replace("&amp;", "&")
    return " ".join(line.strip().split())


def parse(path: Path) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    pending_time = ""
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if not line or line == "WEBVTT" or line.isdigit():
            continue
        if "\t" in line:
            parts = line.split("\t", 2)
            if len(parts) == 3 and parts[0].replace(".", "", 1).isdigit():
                items.append((f"{parts[0]}-{parts[1]}", clean_line(parts[2])))
                continue
        if "-->" in line and TIMECODE.search(line):
            pending_time = line.split(" --> ", 1)[0].replace(",", ".")
            continue
        text = clean_line(line)
        if text:
            items.append((pending_time, text))
            pending_time = ""
    return items


def dedupe(items: list[tuple[str, str]]) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    prev = ""
    for t, text in items:
        if text and text != prev:
            result.append((t, text))
            prev = text
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    src = Path(args.input)
    dst = Path(args.out) if args.out else src.with_suffix(".timeline.md")
    items = dedupe(parse(src))
    lines = ["# Tutorial Timeline", ""]
    for time, text in items:
        prefix = f"- `{time}` " if time else "- "
        lines.append(prefix + text)
    dst.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(str(dst))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
