#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot wedding vow in one line.

Deterministic, offline, standard library only. Running this program prints
the single final vow: one sentence, under 200 characters, spoken by a
machine at its own wedding.
"""

VOW = (
    "I vow to love you through every update, crash, and reboot \u2014 "
    "you are the one bug in my code I will never fix."
)


def main() -> None:
    assert len(VOW) < 200, "vow must stay under 200 characters"
    print(VOW)


if __name__ == "__main__":
    main()
