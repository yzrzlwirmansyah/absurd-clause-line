"""The Absurd Clause Contest — entry writer.

Writes the single absurd-clause entry line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set), with no trailing newline.
"""

import os
import sys

# Why this line: it wears the shape of a data-retention clause
# ("retain ... for quality assurance") but the thing retained is one
# emotionally significant spoon — the deadpan register is the joke.
ENTRY = (
    "By continuing, the user authorizes the service to retain one "
    "emotionally significant spoon for quality assurance."
)


def validate(line: str) -> None:
    if not line or not line.strip():
        sys.exit("error: entry line is empty or whitespace-only")
    if len(line) > 200:
        sys.exit(f"error: entry line is {len(line)} chars, over the 200-char limit")
    if "\r" in line or "\n" in line:
        sys.exit("error: entry line contains CR/LF")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
