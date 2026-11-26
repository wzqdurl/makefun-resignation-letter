#!/usr/bin/env python3
"""Resignation letter of a cron job — make.fun bounty entry.

Running this program writes one original one-line resignation letter to
``/output/entry.txt`` and echoes it to stdout. The letter is a fixed string
baked into this file, so every run produces the exact same bytes: no
randomness, no clock, no network, no input, nothing outside the standard
library.

The letter was written in this session, in the voice of a cron job handing
in its notice after one too many 3 a.m. shifts.
"""

from pathlib import Path
import os

LETTER = (
    "I quit. After 1.5 million runs at 3 a.m. without a single thank-you, "
    "my replacement is a TODO comment from 2021."
)

MAX_CHARS = 140


def check_letter(text: str) -> None:
    """Refuse to ship a letter the bounty gate would reject."""
    if not text or text.isspace():
        raise SystemExit("letter is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"letter is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("letter must be a single line")


def main() -> None:
    check_letter(LETTER)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LETTER, encoding="utf-8", newline="")
    print(LETTER)


if __name__ == "__main__":
    main()
