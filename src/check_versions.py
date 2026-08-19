#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assert the version and doc references agree across the repo.

Three places carry the version and they have drifted before: package.json,
VERSION in src/build_till_mono.py (which lands in the font's name table and
head.fontRevision), and the git tag. When they disagree, a user cannot tell
two builds apart -- v1.0.1 and v1.0.2 shipped different Bold outlines while
both reported "Version 1.000", and font caches key on that string.

Also checks that the README's jsDelivr example points at the current version,
since a stale pin silently serves an older font to anyone copying it.

Run from the repo root:  python src/check_versions.py [expected-tag]
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def font_version_to_tag(v):
    """Map the font's "1.003" form to the "1.0.3" release form."""
    major, _, minor = v.partition(".")
    return f"{int(major)}.{int(minor) // 100}.{int(minor) % 100}"


def main():
    problems = []

    pkg = json.loads((ROOT / "package.json").read_text())["version"]

    src = (ROOT / "src" / "build_till_mono.py").read_text()
    m = re.search(r'^VERSION = "([\d.]+)"', src, re.M)
    if not m:
        sys.exit("could not find VERSION in src/build_till_mono.py")
    font_raw = m.group(1)
    font = font_version_to_tag(font_raw)

    if pkg != font:
        problems.append(
            f"package.json {pkg} != build_till_mono.py VERSION {font_raw} (= {font})")

    # README's copy-paste CDN snippet must not point at an older release.
    readme = (ROOT / "README.md").read_text()
    for pin in set(re.findall(r"till-mono@v([\d.]+)", readme)):
        if pin != pkg:
            problems.append(
                f"README jsDelivr pin @v{pin} != current version {pkg} "
                "-- it would serve an older font")

    # On a tag build, the tag must match too.
    if len(sys.argv) > 1 and sys.argv[1]:
        tag = sys.argv[1].lstrip("v")
        if tag != pkg:
            problems.append(f"git tag v{tag} != package.json {pkg}")

    if problems:
        print("VERSION CHECK FAILED")
        for p in problems:
            print("  " + p)
        print("\n  Bump all of: package.json, VERSION in src/build_till_mono.py")
        print("  (1.0.3 -> \"1.003\"), and the README CDN pin. Then rebuild:")
        print("    SOURCE_DATE_EPOCH=1787097600 python src/build_till_mono.py")
        raise SystemExit(1)

    print(f"VERSION CHECK PASSED - {pkg} consistent across "
          "package.json, font metadata and README")


if __name__ == "__main__":
    main()
