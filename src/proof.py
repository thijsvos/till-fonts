#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render a labeled contact sheet of the raw glyph bitmaps for QA.

Writes proof_sheet_<slug>.png per font. Run from the repo root:
  python src/proof.py
"""
import importlib

from PIL import Image, ImageDraw

from build_all import FONTS
from pixelfont import pixels_of

S = 6            # screen px per font px
PAD, LABEL = 10, 14
COLS = 12


def draw_cell(d, grid, ox, oy, top, rows):
    """Draw one glyph cell with cap, x-height and baseline guides at (ox, oy)."""
    cw, ch = grid.cols * S, grid.rows * S
    d.rectangle([ox, oy, ox + cw - 1, oy + ch - 1], outline=(45, 45, 55))
    for row_line in (grid.cap_top_row, grid.x_top_row):
        y = oy + row_line * S
        d.line([ox, y, ox + cw - 1, y], fill=(60, 60, 45))
    yb = oy + (grid.baseline_row + 1) * S
    d.line([ox, yb, ox + cw - 1, yb], fill=(120, 60, 60))
    for (x, gy) in pixels_of(grid, top, rows):
        r = grid.baseline_row - gy
        d.rectangle([ox + x * S, oy + r * S, ox + x * S + S - 1, oy + r * S + S - 1],
                    fill=(255, 214, 90))


def sheet(font):
    grid = font.GRID
    cw, ch = grid.cols * S, grid.rows * S
    items = sorted(font.G.items(), key=lambda kv: ord(kv[0]))
    rows_n = (len(items) + COLS - 1) // COLS
    img = Image.new("RGB",
                    (COLS * (cw + PAD) + PAD, rows_n * (ch + PAD + LABEL) + PAD),
                    (16, 16, 20))
    d = ImageDraw.Draw(img)
    for i, (c, (top, rows)) in enumerate(items):
        ox = PAD + (i % COLS) * (cw + PAD)
        oy = PAD + (i // COLS) * (ch + PAD + LABEL)
        draw_cell(d, grid, ox, oy, top, rows)
        label = c if c.isprintable() and c != ' ' else '%04X' % ord(c)
        d.text((ox, oy + ch + 1), f"{label} {ord(c):04X}", fill=(150, 150, 160))
    out = f"proof_sheet_{font.IDENTITY.slug}.png"
    img.save(out)
    print("wrote", out, img.size)


def main():
    for name in FONTS:
        sheet(importlib.import_module(f"fonts.{name}"))


if __name__ == "__main__":
    main()
