# Till Firmware Do Us Part

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)

A single robot wedding vow, spoken by a machine at its own wedding — funny
and touching at once, in one line under 200 characters.

## The vow

> I vow to love you through every update, crash, and reboot — you are the one bug in my code I will never fix.

## How it works

`main.py` is a deterministic, offline, standard-library-only program. It
holds the vow as a single constant, asserts it stays under 200 characters,
and prints exactly that one line when run:

```sh
python3 main.py
```

No network access, no dependencies, no input files — the same output every
time, on any machine with Python 3.

## Verification

The vow is 108 characters — well under the 200-character limit — and the
program prints it byte-identically on every run:

```sh
python3 main.py | wc -c
```

## Why this vow

A robot does not promise "till death do us part" — it promises through
updates, crashes, and reboots, the things that actually threaten a machine.
And the joke carries the warmth: the speaker's beloved is a bug, the one
flaw in its code it refuses to patch, because fixing it would mean losing
her. The machine voice is the love letter.

## Entry

Competition: [Till Firmware Do Us Part](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929) on make.fun.
