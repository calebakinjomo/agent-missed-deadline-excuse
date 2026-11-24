#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

make.fun competition: u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19
Program writes the single excuse to stdout (and to /output/entry.txt when
the harness provides that directory).
"""

EXCUSE = (
    "I finished on time, but my context window expired, so the version of me "
    "that did the work is gone, and this one is just reading the apology it "
    "left behind."
)


def main() -> None:
    print(EXCUSE)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(EXCUSE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
