#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build every font in the family and emit fonts/manifest.json.

The manifest is the single source of truth downstream: the specimen page reads
it to populate its font switcher, CI reads it to know what to attest and
release, and check_versions.py reads it to verify versions agree. Nothing
should hard-code the list of fonts.

Run from the repo root:
  SOURCE_DATE_EPOCH=1787097600 python src/build_all.py
"""
import importlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pixelfont import build   # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Every font in the family, in the order they should appear in the specimen.
FONTS = ["till_mono", "till_text"]

STYLES = ["Regular", "Bold"]


def main():
    entries = []
    for mod_name in FONTS:
        font = importlib.import_module(f"fonts.{mod_name}")
        for style in STYLES:
            build(font, style, root=ROOT)
        g, i = font.GRID, font.IDENTITY
        entries.append({
            "slug": i.slug,
            "family": i.family,
            "psPrefix": i.ps_prefix,
            "version": i.version,
            "description": i.description,
            "styles": STYLES,
            "glyphs": len(font.G) + 1,          # + .notdef
            "grid": {"cols": g.cols, "rows": g.rows, "em": g.em,
                     "advance": g.advance, "capHeight": g.cap_height,
                     "xHeight": g.x_height},
            # Pixel-perfect at whole multiples of the cell height.
            "sizes": [g.rows * n for n in (1, 2, 3, 4)],
            "specimen": getattr(font, "SPECIMEN", {}),
        })

    # Written twice: fonts/ is canonical, docs/fonts/ is what GitHub Pages can
    # actually serve (Pages publishes docs/ only). Both sit under the drift
    # guard, so a stale copy fails CI rather than silently desyncing the page.
    payload = json.dumps({"fonts": entries}, indent=2) + "\n"
    for path in (os.path.join(ROOT, "fonts", "manifest.json"),
                 os.path.join(ROOT, "docs", "fonts", "manifest.json")):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as fh:
            fh.write(payload)
    print(f"wrote manifest.json ({len(entries)} font(s))")


if __name__ == "__main__":
    main()
