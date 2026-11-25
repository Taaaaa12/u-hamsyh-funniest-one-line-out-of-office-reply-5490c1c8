#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes a single out-of-office auto-reply, one line long, to
/output/entry.txt. The text is fixed and deterministic: the same
bytes on every run, with no trailing newline, so the gate counts
exactly the entry's characters (1-160, UTF-8, not only whitespace).

The joke: while I'm away, my cat has taken over the inbox — and,
being a cat, she has already deleted the important emails. It reads
like a real away message a person would switch on, lands on the
first read, and turns the usual "your email is important to me"
away message on its head.
"""

import os

ENTRY = (
    "I'm out of office, and my emails are being handled by my cat, "
    "who has already deleted the important ones."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {len(ENTRY)}")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not be only whitespace or padded")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must be exactly the entry.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("entry.txt does not match the entry text")


if __name__ == "__main__":
    main()
