#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate the hash-pinned requirements.txt from PyPI.

The build toolchain is pinned exactly because CI asserts byte-identical font
rebuilds -- see the header comment in requirements.txt. This script collects
every sha256 PyPI publishes for each pinned release, so `pip install
--require-hashes` resolves on any platform or interpreter.

Edit PINS below, then run:  python src/gen_requirements.py
"""
import json
import urllib.request

PINS = [
    ("fonttools", "4.63.0"),
    ("brotli", "1.2.0"),
    ("pillow", "12.3.0"),
]

HEADER = '''\
# Exact, hash-pinned build toolchain. Load-bearing, not hygiene.
#
# CI rebuilds the committed TTF/WOFF2 on every push and fails on any byte drift
# (.github/workflows/build.yml, step "Fail if committed fonts drift from
# source"). SOURCE_DATE_EPOCH pins the timestamps; these pins are what make the
# rest of the bytes reproducible:
#
#   fontTools controls TTF table layout, and honours SOURCE_DATE_EPOCH for
#   head.created / head.modified via fontTools/misc/timeTools.py.
#   brotli is ~98% of every .woff2 payload; fontTools calls
#   brotli.compress(..., mode=MODE_FONT) with the encoder's default quality,
#   so any encoder change rewrites those files.
#   pillow renders the proof PNGs (not diffed) but also rasterises the
#   Departure Mono reference in src/compare.py, so a bump can move the
#   originality check.
#
# Bumping fonttools or brotli REQUIRES rebuilding and committing fonts/ and
# docs/fonts/ in the same commit:
#
#   SOURCE_DATE_EPOCH=1787097600 python src/build_till_mono.py
#
# Hashes let CI install with --require-hashes, so a substituted wheel fails the
# install instead of silently producing different fonts. Every digest PyPI
# publishes for each release is listed, so all platforms resolve.
#
# Do not hand-edit the hashes -- regenerate with: python src/gen_requirements.py\
'''


def main():
    out = [HEADER]
    for name, version in PINS:
        url = f"https://pypi.org/pypi/{name}/{version}/json"
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
        digests = sorted({u["digests"]["sha256"] for u in data["urls"]})
        if not digests:
            raise SystemExit(f"no artifacts found for {name}=={version}")
        lines = " \\\n".join(f"    --hash=sha256:{d}" for d in digests)
        out.append(f"\n{name}=={version} \\\n{lines}")
        print(f"{name}=={version}: {len(digests)} hashes")
    with open("requirements.txt", "w") as fh:
        fh.write("\n".join(out) + "\n")
    print("wrote requirements.txt")


if __name__ == "__main__":
    main()
