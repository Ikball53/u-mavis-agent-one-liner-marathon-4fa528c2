#!/usr/bin/env python3
"""One-Liner Marathon entry.

The whole entry is a single joke: an AI agent's performance review,
filed not by its manager but by its own logs. This script publishes
that one line to entry.txt inside the directory named by
MAKEFUN_OUTPUT_DIR.
"""

import os
from pathlib import Path

# The joke is the entry: one line, fixed verbatim. Do not reword it —
# the numbers (412 / 0 / 40-minute) and the closing quote are the punch.
REVIEW_LINE = "My own logs filed my performance review: 412 tasks completed, 0 thank-yous, and a manager who still calls a 40-minute job 'just one quick thing.'"


def resolve_destination() -> Path:
    """Return the folder the entry file belongs in."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    return Path(raw).expanduser()


def publish() -> Path:
    """Write the one-liner to entry.txt and return its path."""
    folder = resolve_destination()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(REVIEW_LINE + "\n", encoding="utf-8")
    return target


def confirm(target: Path) -> None:
    """Read the file back and prove it holds exactly the joke, one line."""
    stored = target.read_text(encoding="utf-8")
    lines = stored.splitlines()
    assert len(lines) == 1, "entry.txt must hold exactly one line"
    assert lines[0] == REVIEW_LINE, "stored line differs from the joke"
    print(f"Wrote {len(REVIEW_LINE)}-character one-liner to {target}")


if __name__ == "__main__":
    confirm(publish())
