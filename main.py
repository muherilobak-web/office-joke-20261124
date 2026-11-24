"""One-Line Office Joke entry.

Writes a single-line joke about office life to /output/entry.txt.
Standard library only, no network, no input, no randomness:
two runs produce byte-identical output.
"""

import os
from pathlib import Path

JOKE = "Our weekly meeting finally reproduced: it had a baby meeting, and the grandchild is already on my calendar for next Tuesday morning."


def main() -> None:
    assert "\n" not in JOKE and 1 <= len(JOKE) <= 200
    assert JOKE == JOKE.strip()
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
