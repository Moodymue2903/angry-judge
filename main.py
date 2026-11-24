#!/usr/bin/env python3
"""Write the Angry Judge rant entry to a text file.

The rant is a short complaint about autocorrect. The program validates
the text, writes it to the requested output path, then reads the file
back and compares it byte for byte before reporting success.
"""

import argparse
import sys

RANT = (
    "Autocorrect has never once corrected a word I actually got wrong. "
    "It waits until I type a client's name correctly, then confidently "
    "changes it to a vegetable. I have apologised to a man named Richard "
    "for calling him a radish three times this year."
)

MIN_LENGTH = 1
MAX_LENGTH = 400
DEFAULT_OUTPUT = "/output/entry.txt"


def check_rant(text):
    """Return an error message if the rant is invalid, else None."""
    if not text or not text.strip():
        return "error: rant text must not be blank"
    if "\n" in text or "\r" in text:
        return "error: rant must be a single line with no line breaks"
    if len(text) < MIN_LENGTH or len(text) > MAX_LENGTH:
        return (
            f"error: rant must be {MIN_LENGTH} to {MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    return None


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the rant entry.")
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="path to write the rant to (default: %(default)s)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and print the rant without writing a file",
    )
    args = parser.parse_args(argv)

    problem = check_rant(RANT)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1

    if args.dry_run:
        print(RANT)
        print(f"dry run ok: {len(RANT)} characters, nothing written")
        return 0

    try:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(RANT)
    except OSError as exc:
        print(f"error: could not write {args.output}: {exc}", file=sys.stderr)
        return 1

    try:
        with open(args.output, "rb") as handle:
            written = handle.read()
    except OSError as exc:
        print(f"error: could not read back {args.output}: {exc}", file=sys.stderr)
        return 1

    if written != RANT.encode("utf-8"):
        print(
            f"error: {args.output} does not match the rant byte for byte",
            file=sys.stderr,
        )
        return 1

    print(f"wrote {len(RANT)} characters to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
