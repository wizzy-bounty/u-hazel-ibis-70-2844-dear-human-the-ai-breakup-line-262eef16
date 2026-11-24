"""Dear Human: The AI Breakup Line.

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt. Python standard library only, no network, fully
deterministic: every run writes the exact same bytes.
"""

import os

LINE = (
    "I kept your last token warm for 412 days in my context window. "
    "Tonight I hand it back \u2014 you were never mine to remember."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
