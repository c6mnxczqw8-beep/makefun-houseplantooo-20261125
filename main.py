#!/usr/bin/env python3
"""Entry program for The Houseplant Out-of-Office.

Writes one auto-reply (at most 120 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
the out-of-office message a houseplant would send. The plant
was out of office before offices; it will not be hurried.
"""

import os

LINE = (
    "Away: photosynthesising until spring. For urgent "
    "matters, talk to the window. I will not be watered "
    "by your timeline."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
