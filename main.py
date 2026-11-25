#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun bounty entry.

Writes a single one-line apology from an AI agent to its human,
right after an accident it should not have committed.
"""

import os

ENTRY = (
    "I emailed your boss the draft you labelled 'DO NOT SEND'. "
    "He replied 'finally, some honesty' — "
    "I am, regrettably, his new favourite."
)


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= 159:
        raise ValueError(f"entry must be 1-159 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
