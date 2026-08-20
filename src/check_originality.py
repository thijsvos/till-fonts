#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run the originality comparison for every font in the family.

compare.py checks one font; this loops it over FONTS so CI covers the whole
family and fails if any face collides with a reference outside its allow-set.

Run from the repo root:  python src/check_originality.py
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_all import FONTS   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    failed = []
    for name in FONTS:
        print(f"\n{'=' * 62}\n{name}\n{'=' * 62}")
        r = subprocess.run([sys.executable, os.path.join(HERE, "compare.py"), name])
        if r.returncode:
            failed.append(name)
    if failed:
        print(f"\nORIGINALITY FAILED for: {', '.join(failed)}")
        raise SystemExit(1)
    print(f"\nAll {len(FONTS)} font(s) passed the originality check.")


if __name__ == "__main__":
    main()
