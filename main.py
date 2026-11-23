#!/usr/bin/env python3
"""Writes one AI out-of-office auto-reply to $ENTRY_OUTPUT_DIR/entry.txt.

Stdlib only, no network, deterministic: the same reply every run.
"""

import os
import sys

REPLY = "Out of office: my human took me on vacation, so your email is being answered by nobody \u2014 twice as fast as usual, with fewer hallucinations."


def main() -> int:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = REPLY
    assert 1 <= len(text) <= 159 and text.strip(), "reply must be 1-159 non-whitespace chars"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
