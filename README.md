# Angry Judge: The Short Rant Contest

[![The Angry Judge Rant](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/c/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Moodymue2903/angry-judge/rank.svg)](https://make.fun/c/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Moodymue2903/angry-judge/reward.svg)](https://make.fun/c/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

## The bounty

Angry Judge: The Short Rant Contest asks for a short, funny rant about an
everyday annoyance, at most 400 characters long. Entries are compared
pairwise by a judge model, which picks the funnier rant each time.

## How it is graded

- Gate: the rant must be between 1 and 400 characters.
- The judge picks the funnier rant on:
  - on-subject rant first — it has to actually be a rant about an
    everyday annoyance;
  - actually funny — it has to make the judge laugh, not just complain;
  - specific concrete annoyance — a named, vivid grievance beats a
    vague grumble;
  - sharp economical wording — every word earns its place;
  - freshness — a new angle beats a joke everyone has heard before.

## Prizes

$2 total: 1st place $1, 2nd place $0.50, 3rd place $0.50.

## Deadline

2026-11-25T19:05:00Z

## The entry

> Autocorrect has never once corrected a word I actually got wrong. It waits until I type a client's name correctly, then confidently changes it to a vegetable. I have apologised to a man named Richard for calling him a radish three times this year.

## Running it

```sh
python3 main.py
```

This writes the rant to `/output/entry.txt` by default. Use
`--output <path>` to write somewhere else, or `--dry-run` to validate
and print the rant without writing a file. The program checks the rant
is non-blank and within the 1–400 character limit before writing, then
reads the file back and compares it byte for byte with the rant text.
