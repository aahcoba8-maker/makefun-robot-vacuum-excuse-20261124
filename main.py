"""Robot vacuum's excuse for missing a spot.

Writes one line (<=140 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt,
falling back to the script directory when the variable is unset.
Stdlib only.
"""

import os

ENTRY = "I leave one crumb behind every clean so you still feel useful sweeping it up yourself."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry length {len(text)} out of range"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
