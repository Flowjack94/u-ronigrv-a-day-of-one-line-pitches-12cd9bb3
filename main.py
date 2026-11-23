#!/usr/bin/env python3
"""Entry for make.fun bounty u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes one sentence (a pitch to a friend who has never coded, inviting
them to let an AI agent build their first app idea on make.fun) to
/output/entry.txt. Deterministic: the sentence is a fixed constant, so
every run writes byte-identical output. Python 3.13, standard library only.

After writing, the program re-reads the file and validates it: exactly
one sentence and at most 240 characters. If the output ever fails either
check the program exits non-zero with a clear error instead of silently
producing a bad entry.
"""

import re
import sys
from pathlib import Path

MAX_CHARS = 240

# A sentence end is a terminator followed by whitespace or end of text,
# so the dot inside "make.fun" is not mistaken for a sentence boundary.
SENTENCE_END_RE = re.compile(r"[.!?](?=\s|$)")

PITCH = (
    "Just describe the app idea you've been carrying around and let an "
    "AI agent on make.fun build the first version \u2014 no code from you, "
    "no jargon to learn, and you only keep it if you love it."
)


def validate_output(text: str) -> None:
    """Fail hard if the written entry is not exactly one sentence <= 240 chars."""
    if not text.strip():
        sys.exit("ERROR: /output/entry.txt is empty")
    if len(text) > MAX_CHARS:
        sys.exit(f"ERROR: entry is {len(text)} characters, over the 240 limit")
    sentence_ends = len(SENTENCE_END_RE.findall(text.strip()))
    if sentence_ends != 1:
        sys.exit(
            f"ERROR: entry must be exactly 1 sentence, "
            f"found {sentence_ends} sentence ends"
        )


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(PITCH, encoding="utf-8")
    validate_output(output_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
