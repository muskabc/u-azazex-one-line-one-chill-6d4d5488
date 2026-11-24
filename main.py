#!/usr/bin/env python3
"""One Line, One Chill — entry program.

Reads the single horror sentence from line.txt in this directory,
validates it (one line, 1-200 characters), and writes exactly that
text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13 standard library only.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> int:
    line_path = HERE / "line.txt"
    text = line_path.read_text(encoding="utf-8")

    # The line file may end with a trailing newline; the entry itself
    # must be exactly one line with no trailing newline.
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]

    if "\n" in text or "\r" in text:
        print("error: line.txt must contain exactly one line", file=sys.stderr)
        return 1
    if not text.strip():
        print("error: line must not be empty or only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(
            f"error: line must be 1-200 characters, got {len(text)}",
            file=sys.stderr,
        )
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
