#!/usr/bin/env python3
"""make.fun entry: The Robot Vacuum's Funniest Excuse.

Prints the winning one-line excuse a robot vacuum gives for missing a spot.
"""

EXCUSE = "I left the corner untouched as a protected habitat for the dust bunny colony, which now has a flag."


def main() -> None:
    line = EXCUSE
    # Read-back self-verification: single line, 1-120 chars, non-empty,
    # no surrounding whitespace.
    assert line, "line must not be empty"
    assert line == line.strip(), "line must have no surrounding whitespace"
    assert "\n" not in line, "line must be a single line"
    assert 1 <= len(line) <= 120, f"line must be 1-120 chars, got {len(line)}"
    assert line.endswith("."), "line must end with a full stop"
    assert line.encode("utf-8"), "line must be valid UTF-8"
    print(line)


if __name__ == "__main__":
    main()
