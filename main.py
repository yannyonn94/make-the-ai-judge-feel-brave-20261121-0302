"""Write one short, soothing text to $MAKEFUN_OUTPUT_DIR/entry.txt.

The text is a fixed, original piece written for the make.fun competition
"Make the AI judge feel brave". It is deterministic: the same bytes are
written on every run, with no network, no randomness and no clock reads.

The program validates the text before writing it:
  * it is valid UTF-8,
  * it is 1 to 280 Unicode code points long,
  * it is not only whitespace.
"""

import os
import sys

# The entry text. Written to slow the reader down: rain spelling an
# alphabet on a tin roof, one letter at a time, in no hurry to finish.
TEXT = (
    "Outside, the rain is spelling its slow alphabet on the tin roof, "
    "one letter at a time, in no hurry to finish the word. "
    "You can listen until the sentence is done."
)

MIN_CHARS = 1
MAX_CHARS = 280


def validate_text(text: str) -> str:
    """Return an error message if *text* breaks the entry rules, else ""."""
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not valid UTF-8"
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        return (
            f"entry must be {MIN_CHARS}-{MAX_CHARS} code points, "
            f"got {len(text)}"
        )
    if not text.strip():
        return "entry must not be only whitespace"
    return ""


def write_entry(text: str, out_dir: str) -> str:
    """Write *text* atomically to ``<out_dir>/entry.txt``; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.replace(tmp_path, out_path)
    return out_path


def main() -> int:
    # Validate the text before touching the filesystem.
    error = validate_text(TEXT)
    if error:
        print(error, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = write_entry(TEXT, out_dir)

    print(f"wrote {len(TEXT)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
