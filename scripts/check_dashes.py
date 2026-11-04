"""Fail if published Markdown uses em dashes, en dashes or spaced hyphens.

Code blocks and inline code are ignored. Markdown list bullets ("- item")
and table separators are not flagged.

Usage: python scripts/check_dashes.py [paths...]
"""

import re
import sys
from pathlib import Path

EM_EN = re.compile("[—–]")
SPACED_HYPHEN = re.compile(r"\S \- \S")
INLINE_CODE = re.compile(r"`[^`]*`")
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "dbt_packages", "target"}


def check_file(path: Path) -> list[str]:
    problems = []
    in_fence = False
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        text = INLINE_CODE.sub("", line)
        if EM_EN.search(text):
            problems.append(f"{path}:{n}: em or en dash")
        if SPACED_HYPHEN.search(text):
            problems.append(f"{path}:{n}: spaced hyphen used as a dash")
    return problems


def main(argv: list[str]) -> int:
    roots = [Path(a) for a in argv] or [Path(".")]
    files = []
    for root in roots:
        if root.is_file():
            files.append(root)
        else:
            files += [p for p in root.rglob("*.md") if not SKIP_DIRS & set(p.parts)]
    problems = [p for f in sorted(files) for p in check_file(f)]
    for p in problems:
        print(p)
    print(f"Checked {len(files)} Markdown files, {len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
