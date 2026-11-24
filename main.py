"""The funniest one-line review of a Monday, under 200 characters.

Pure Python standard library, deterministic, no network access.
It prints the line to stdout and also writes it to /output/entry.txt,
where the competition's scorer reads it.
"""

import os

# Competition limit for the single one-line Monday review.
MAX_CHARS = 200

LINE = (
    "Monday showed up uninvited, cancelled my weekend's sequel, and the coffee machine filed for divorce. One star. Would not Monday again."
)

# Guard: the entry must stay inside the competition's character limit.
assert len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, over the {MAX_CHARS} limit"


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
