#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word describing home Wi-Fi to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only.

The word is "Moody": home Wi-Fi that works beautifully one minute and
sulks in the corner the next, for no reason anyone can explain.
"""

from pathlib import Path

WORD = "Moody"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
