#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh — make.fun entry.

Writes a single-line warning label for humans to /output/entry.txt.
Stdlib only, fully deterministic.
"""

import os

LABEL = (
    "WARNING: This human runs on caffeine and unresolved childhood issues. "
    "Do not shake. Do not operate before 9 a.m. "
    "Side effects include sarcasm."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
