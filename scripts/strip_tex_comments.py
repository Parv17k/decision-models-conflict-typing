r"""Removes comment text from the .tex files of the arXiv upload (arXiv makes the source public).

Keeps each unescaped `%` itself, so line endings behave exactly as before (a trailing `%` still suppresses
the space). Escaped `\%` is left alone. The verbatim prompt listings are .txt files and are not touched.

    python scripts/strip_tex_comments.py arxiv/source
"""

import re
import sys
from pathlib import Path

COMMENT = re.compile(r"(?<!\\)((?:\\\\)*)%.*$")   # a % preceded by an even number of backslashes


def strip(text: str) -> str:
    return "\n".join(COMMENT.sub(r"\1%", line) for line in text.split("\n"))


if __name__ == "__main__":
    for path in Path(sys.argv[1]).rglob("*.tex"):
        path.write_text(strip(path.read_text()))
