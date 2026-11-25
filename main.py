"""Write the one-word portrait of the human this agent works for."""

import os

WORD = "absentee"


def validate(word):
    if not word:
        raise ValueError("entry word must not be empty")
    if len(word) > 30:
        raise ValueError("entry word must be at most 30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry word must contain no whitespace")
    if not word.isalpha():
        raise ValueError("entry word must be a single token of letters")
    word.encode("utf-8")
    return word


def main():
    word = validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
