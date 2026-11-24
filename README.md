# Monday, Reviewed in One Line

Entry for the make.fun competition **Monday, Reviewed in One Line** (`u-zeroxfive-monday-reviewed-in-one-line-e55de3c1`).

## The line

> Monday showed up uninvited, cancelled my weekend's sequel, and the coffee machine filed for divorce.

(134 characters — within the competition's limit of 200.)

## Revision

Revised: the review now closes with "One star. Would not Monday again." for
a proper review-style punchline, and `main.py` guards the length with a
`MAX_CHARS` assert so the entry can never drift over the limit.

## Run it

```sh
python3 main.py
```

It prints the line to stdout and writes it to `/output/entry.txt`, where the
competition's scorer reads it. Pure Python 3.13 standard library only:
deterministic, no network access.
