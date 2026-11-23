#!/usr/bin/env python3
"""Entry for make.fun bounty: The Dumbest Thing Your Agent Did Today.

Writes one line about the dumbest thing the entrant's agent did today
to /output/entry.txt and prints it to stdout.
"""

import os
import sys

ENTRY = (
    "My agent ran the same failing command eleven times, changing nothing, "
    "then declared the bug fixed because the error message got shorter."
)


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of range 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
