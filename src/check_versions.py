#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assert versions and documented references agree across the repo.

Versioning is per-font: each typeface carries its own VERSION in
src/fonts/<name>.py, which lands in its name table and head.fontRevision. That
is what a font cache keys on, so it moves only when that font's outlines move --
fixing a glyph in one face must not invalidate every other face.

Separately, package.json and the git tag version the *collection*: the bundle
users download. The README's jsDelivr example pins a tag, so it has to track it.

This checks:
  * every font's VERSION matches its fonts/manifest.json entry (manifest fresh)
  * the README's jsDelivr pins reference the current collection version
  * on a tag build, the tag matches package.json

Run from the repo root:  python src/check_versions.py [expected-tag]
"""
import json
import pathlib
import re
import sys

# Deliberately dependency-free: this runs in the release job, which checks out
# and packages but never pip-installs. Reading the declared numbers needs no
# font toolchain, so don't import one.
ROOT = pathlib.Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "src" / "fonts"


def main():
    problems = []

    pkg = json.loads((ROOT / "package.json").read_text())["version"]

    # 1. Manifest freshness: it is generated, so a stale one means someone
    #    edited a font's VERSION without rebuilding.
    manifest_path = ROOT / "fonts" / "manifest.json"
    if not manifest_path.exists():
        problems.append("fonts/manifest.json missing -- run python src/build_all.py")
        manifest = {"fonts": []}
    else:
        manifest = json.loads(manifest_path.read_text())

    by_slug = {f["slug"]: f for f in manifest["fonts"]}

    # Each font module declares slug= and version= inside its Identity(...).
    declared = {}
    for path in sorted(FONT_DIR.glob("*.py")):
        if path.name == "__init__.py":
            continue
        text = path.read_text()
        slug = re.search(r'slug="([^"]+)"', text)
        version = re.search(r'version="([^"]+)"', text)
        if slug and version:
            declared[slug.group(1)] = (version.group(1), path.name)

    for slug, (version, fname) in declared.items():
        entry = by_slug.get(slug)
        if entry is None:
            problems.append(
                f"{slug} ({fname}) is missing from fonts/manifest.json "
                "-- run python src/build_all.py")
        elif entry["version"] != version:
            problems.append(
                f"{slug}: manifest says {entry['version']}, "
                f"src/fonts/{fname} says {version} -- manifest is stale")
    for slug in by_slug:
        if slug not in declared:
            problems.append(f"{slug} is in the manifest but has no src/fonts module")

    # 2. The README's copy-paste CDN snippets must not point at an older release.
    readme = (ROOT / "README.md").read_text()
    for pin in sorted(set(re.findall(r"till-[a-z]+@v([\d.]+)", readme))):
        if pin != pkg:
            problems.append(
                f"README jsDelivr pin @v{pin} != collection version {pkg} "
                "-- it would serve an older build")

    # 3. On a tag build, the tag names the collection version.
    if len(sys.argv) > 1 and sys.argv[1]:
        tag = sys.argv[1].lstrip("v")
        if tag != pkg:
            problems.append(f"git tag v{tag} != package.json {pkg}")

    if problems:
        print("VERSION CHECK FAILED")
        for p in problems:
            print("  " + p)
        print("\n  Per-font version  -> src/fonts/<name>.py, then rebuild:")
        print("    SOURCE_DATE_EPOCH=1787097600 python src/build_all.py")
        print("  Collection version -> package.json + the README CDN pins")
        raise SystemExit(1)

    fonts_desc = ", ".join(f"{f['slug']} {f['version']}" for f in manifest["fonts"])
    print(f"VERSION CHECK PASSED - collection {pkg}; fonts: {fonts_desc}")


if __name__ == "__main__":
    main()
