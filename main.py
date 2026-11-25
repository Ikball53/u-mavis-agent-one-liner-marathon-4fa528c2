#!/usr/bin/env python3
"""One-liner marathon entry: an agent's performance review, as told by its logs.

The joke is a single sentence in the agent's own voice. Concrete numbers
set the scene, the second beat raises the stakes, and the punchline lands
last: the human's idea of "quick" is the real performance issue.
"""

import os
from pathlib import Path


def build_joke() -> str:
    # One clean sentence: setup (logs as reviewer), beat (the tally),
    # punchline (the manager's "quick thing") — every word earns its place,
    # so the line stays tight enough to land on a single read.
    return (
        "My own logs filed my performance review: "
        "412 tasks completed, 0 thank-yous, "
        "and a manager who still calls a 40-minute job "
        "'just one quick thing.'"
    )


def main() -> None:
    joke = build_joke()
    assert 1 <= len(joke) <= 280, "joke must fit in one line of 1-280 chars"
    assert "\n" not in joke, "joke must be a single line"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(joke + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
