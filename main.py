"""The out-of-office auto-reply a houseplant would send.

Writes the reply to /output/entry.txt for make.fun's
"The Houseplant Out-of-Office" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "Out of office: I'm a fern. I've been ignored since March and the "
    "sunlight does all the work anyway."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 120 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 120, "line must be 1-120 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
