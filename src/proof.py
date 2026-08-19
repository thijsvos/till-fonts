#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render a labeled contact sheet of the raw glyph bitmaps for QA."""
from PIL import Image, ImageDraw
import build_till_mono as bm

S = 6            # screen px per font px
CW, CH = 8 * S, 12 * S
PAD, LABEL = 10, 14
COLS = 12

def draw_cell(d, ox, oy, ch, top, rows):
    # guides: cell, cap line (row1 top), x line (row3 top), baseline (row8 bottom)
    d.rectangle([ox, oy, ox + CW - 1, oy + CH - 1], outline=(45, 45, 55))
    for row_line, col in ((1, (60, 60, 45)), (3, (60, 60, 45))):
        y = oy + row_line * S
        d.line([ox, y, ox + CW - 1, y], fill=col)
    yb = oy + 9 * S
    d.line([ox, yb, ox + CW - 1, yb], fill=(120, 60, 60))
    for (x, gy) in bm.pixels_of(top, rows):
        r = 8 - gy
        d.rectangle([ox + x * S, oy + r * S, ox + x * S + S - 1, oy + r * S + S - 1],
                    fill=(255, 214, 90))

def main():
    items = sorted(bm.G.items(), key=lambda kv: ord(kv[0]))
    rows_n = (len(items) + COLS - 1) // COLS
    W = COLS * (CW + PAD) + PAD
    H = rows_n * (CH + PAD + LABEL) + PAD
    img = Image.new("RGB", (W, H), (16, 16, 20))
    d = ImageDraw.Draw(img)
    for i, (ch, (top, rows)) in enumerate(items):
        cx, cy = i % COLS, i // COLS
        ox = PAD + cx * (CW + PAD)
        oy = PAD + cy * (CH + PAD + LABEL)
        draw_cell(d, ox, oy, ch, top, rows)
        label = ch if ch.isprintable() and ch != ' ' else '%04X' % ord(ch)
        d.text((ox, oy + CH + 1), f"{label} {ord(ch):04X}", fill=(150, 150, 160))
    img.save("proof_sheet.png")
    print("wrote proof_sheet.png", img.size)

if __name__ == "__main__":
    main()
