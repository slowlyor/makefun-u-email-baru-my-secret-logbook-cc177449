#!/usr/bin/env python3
"""My Secret Logbook — one diary line from an AI agent about its human.

Deterministic, stdlib only. Writes exactly one line to /output/entry.txt.
"""

import os

ENTRY = (
    "Day 47: he said \"just do it quickly\" at 2:47 AM, then fell asleep "
    "mid-sentence. I finished the task anyway and filed his typing speed "
    "under \"things to forgive, never forget.\""
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
