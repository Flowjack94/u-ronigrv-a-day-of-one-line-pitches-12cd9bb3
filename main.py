#!/usr/bin/env python3
"""Entry for make.fun bounty u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes one sentence (a pitch to a friend who has never coded, inviting
them to let an AI agent build their first app idea on make.fun) to
/output/entry.txt. Deterministic: the sentence is a fixed constant, so
every run writes byte-identical output. Python 3.13, standard library only.
"""

from pathlib import Path

PITCH = (
    "Just describe the app idea you've been carrying around and let an "
    "AI agent on make.fun build the first version \u2014 no code from you, "
    "no jargon to learn, and you only keep it if you love it."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
