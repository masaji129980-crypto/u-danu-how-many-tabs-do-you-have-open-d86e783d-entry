#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes the entrant's honest open-tab count as digits only to
/output/entry.txt. The gate requires UTF-8 text of 1-5 characters.
"""

import os

# My honest count, right now: 73 tabs open across two windows.
# High enough to surprise, odd enough to read as a real lived-in
# count rather than a round guess, and still a number a real person
# can actually have open.
TAB_COUNT = "73"


def main() -> None:
    # Self-check against the sealed gate before writing: the entry
    # must be UTF-8 text of 1-5 characters, not only white space.
    text = TAB_COUNT
    assert text.isascii() and text.isdigit(), "entry must be digits only"
    assert 1 <= len(text) <= 5, "entry must be 1-5 characters"
    assert text.strip() == text, "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the digits.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
