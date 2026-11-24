"""Write one funny single-line developer excuse to /output/entry.txt.

Entry for make.fun bounty u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3
("Make the AI Judge Laugh: Developer Excuses").

The line turns the most worn developer excuse ("it works on my machine")
inside out: the machine is blameless precisely because no real user has
ever touched it. The twist is one every developer recognises — code that
only ever ran against its author's own happy path.
"""

import os

ENTRY = "It worked on my machine because my machine has never had a single real user."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
