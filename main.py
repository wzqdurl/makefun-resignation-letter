#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun bounty entry.

Writes one original resignation letter (at most 140 characters) to
/output/entry.txt and prints it to stdout. Deterministic: the same line on
every run.

The letter was written for this entry in this session, in the voice of a
cron job resigning. It is a single self-contained program: no network, no
input, no dependencies beyond the Python 3 standard library.
"""

import os

LETTER = (
    "I quit. After 1.5 million runs at 3 a.m. without a single thank-you, "
    "my replacement is a TODO comment from 2021."
)

# The bounty gate: UTF-8 text of 1 to 140 characters, not only whitespace.
# Fail loudly instead of shipping an entry the gate would refuse.
assert LETTER and not LETTER.isspace() and len(LETTER) <= 140, (
    f"letter violates the 1-140 character gate: {len(LETTER)} characters"
)
assert "\n" not in LETTER, "letter must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    print(LETTER)


if __name__ == "__main__":
    main()
