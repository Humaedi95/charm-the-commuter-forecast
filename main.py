#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes a single-line weather forecast for a city that doesn't exist
to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
"""

import os

ENTRY = (
    "In Wobbleton, sunny spells with a 90% chance of spontaneous "
    "conga lines \u2014 24\u00b0C, bring sunscreen and your best dance shoes."
)


def validate_entry(entry: str) -> str:
    """Return the stripped entry, enforcing the 1-140 character gate."""
    entry = entry.strip()
    if not entry:
        raise ValueError("entry must not be empty")
    if len(entry) > 140:
        raise ValueError(f"entry is {len(entry)} characters, max 140")
    return entry


def main() -> None:
    entry = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
