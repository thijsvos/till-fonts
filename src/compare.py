#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare Till Mono glyph bitmaps against reference pixel fonts.

For every shared character we crop each glyph to its ink bounding box and
check (a) exact bitmap identity and (b) best-alignment intersection-over-
union similarity. References:
  * font8x8 (IBM PC ROM-style 8x8 font, public domain)
  * Departure Mono (Helena Zhang, OFL) rendered at its native pixel size

Fetches both references into the CWD on first run, writes compare_sheet.png,
and exits 1 on any identical bitmap outside the allow-sets below (CI gate).
Run from the repo root: python src/compare.py
"""
import re
import os
import sys
import importlib
import urllib.request
from math import gcd
from functools import reduce
from PIL import Image, ImageDraw, ImageFont
from pixelfont import pixels_of

# Which font to check; defaults to Till Mono so bare `python src/compare.py`
# keeps working. src/check_all.py loops over the family.
_MOD = sys.argv[1] if len(sys.argv) > 1 else "till_mono"
bm = importlib.import_module(f"fonts.{_MOD}")

REFS = bm.COMPARE["refs"]
for fname, url in REFS.items():
    if not os.path.exists(fname):
        print("downloading reference:", fname)
        urllib.request.urlretrieve(url, fname)

# ---------------------------------------------------------------- helpers --
def crop(pixset):
    """Return pixset as a hashable tuple-of-tuples bitmap cropped to its ink
    bounding box, or None if the set is empty.
    """
    if not pixset:
        return None
    xs = [p[0] for p in pixset]; ys = [p[1] for p in pixset]
    x0, y0 = min(xs), min(ys)
    w, h = max(xs) - x0 + 1, max(ys) - y0 + 1
    grid = [[False] * w for _ in range(h)]
    for (x, y) in pixset:
        grid[y - y0][x - x0] = True
    return tuple(tuple(r) for r in grid)

def iou(a, b):
    """Best IoU over the offsets tried; each axis slides only where ``a`` is longer."""
    ha, wa = len(a), len(a[0]); hb, wb = len(b), len(b[0])
    if (ha, wa) < (hb, wb) or (ha * wa) < (hb * wb):
        a, b, ha, wa, hb, wb = b, a, hb, wb, ha, wa
    A = {(x, y) for y in range(ha) for x in range(wa) if a[y][x]}
    B0 = {(x, y) for y in range(hb) for x in range(wb) if b[y][x]}
    best = 0.0
    for dy in range(ha - hb + 1) if ha >= hb else [0]:
        for dx in range(wa - wb + 1) if wa >= wb else [0]:
            B = {(x + dx, y + dy) for (x, y) in B0}
            i = len(A & B); u = len(A | B)
            best = max(best, i / u if u else 0.0)
    return best

# ------------------------------------------------------------- till mono --
till = {}
for ch, (top, rows) in bm.G.items():
    c = crop({(x, -gy) for (x, gy) in pixels_of(bm.GRID, top, rows)})
    if c:
        till[ch] = c

# ---------------------------------------------------------------- font8x8 --
rom = {}
if "font8x8_basic.h" in REFS:
    src = open("font8x8_basic.h").read()
    groups = re.findall(r"\{([^}]*)\}", src)
    for code, grp in enumerate(groups[:128]):
        vals = [int(v, 16) for v in re.findall(r"0x[0-9A-Fa-f]{2}", grp)]
        if len(vals) != 8 or code < 32 or code > 126:
            continue
        pix = {(x, y) for y, byte in enumerate(vals) for x in range(8)
               if byte >> x & 1}                  # LSB = leftmost pixel
        c = crop(pix)
        if c:
            rom[chr(code)] = c

# ---------------------------------------------------------- departure mono --
from fontTools.ttLib import TTFont
tf = TTFont("departure.otf")
upm = tf["head"].unitsPerEm
gs = tf.getGlyphSet()
from fontTools.pens.recordingPen import RecordingPen
coords = []
cmap = tf.getBestCmap()
for ch in "HAB8misc":
    gname = cmap.get(ord(ch))
    if not gname:
        continue
    pen = RecordingPen(); gs[gname].draw(pen)
    for op, pts in pen.value:
        for pt in pts:
            if pt:
                coords += [int(pt[0]), int(pt[1])]
px_unit = reduce(gcd, [abs(c) for c in coords if c] or [100])
ppem = upm // px_unit
print(f"departure: upm={upm} pixel-unit={px_unit} -> native ppem={ppem}")

dep = {}
f = ImageFont.truetype("departure.otf", ppem)
for ch in till:
    if ord(ch) not in cmap:
        continue
    img = Image.new("L", (ppem * 3, ppem * 3), 0)
    ImageDraw.Draw(img).text((ppem, ppem), ch, font=f, fill=255)
    w, h = img.size
    pix = {(x, y) for y in range(h) for x in range(w) if img.getpixel((x, y)) > 127}
    c = crop(pix)
    if c:
        dep[ch] = c

# ----------------------------------------------------------------- report --
def compare(name, ref):
    """Print the similarity report for one reference and return the chars
    whose bitmaps are identical -- the input to the originality gate below.
    """
    shared = [ch for ch in sorted(till, key=ord) if ch in ref]
    exact, sims = [], []
    for ch in shared:
        a, b = till[ch], ref[ch]
        if a == b:
            exact.append(ch)
        sims.append((iou(a, b), ch))
    sims.sort(reverse=True)
    mean = sum(s for s, _ in sims) / len(sims)
    print(f"\n=== vs {name}: {len(shared)} shared glyphs ===")
    print(f"identical bitmaps: {len(exact)}  {''.join(exact) if exact else ''}")
    print(f"mean best-alignment IoU: {mean:.2f}")
    print("closest non-identical:",
          "  ".join(f"{ch}:{s:.2f}" for s, ch in sims[:8] if ch not in exact))
    return exact

RESULTS = {}
if rom:
    RESULTS["font8x8 (IBM ROM style)"] = compare("font8x8 (IBM ROM style)", rom)
RESULTS["Departure Mono"] = compare("Departure Mono", dep)

# ------------------------------------------------------------ visual sheet --
CHARS = [c for c in "AGKMQRS0aegsy&@#?$%" if c in till]
S, PAD, LBL = 7, 14, 18
fonts = [(bm.IDENTITY.family.upper(), till, (255, 176, 0))]
if rom:
    fonts.append(("IBM-STYLE 8x8 ROM", rom, (120, 190, 255)))
fonts.append(("DEPARTURE MONO", dep, (170, 255, 140)))
cellw = 10 * S
W = PAD + len(CHARS) * (cellw + PAD)
H = PAD + len(fonts) * (13 * S + PAD + LBL) + 8
img = Image.new("RGB", (max(W, 640), H), (15, 15, 19))
d = ImageDraw.Draw(img)
for fi, (label, table, col) in enumerate(fonts):
    oy = PAD + fi * (13 * S + PAD + LBL)
    d.text((PAD, oy), label, fill=(160, 160, 170))
    for ci, ch in enumerate(CHARS):
        ox = PAD + ci * (cellw + PAD)
        bmc = table.get(ch)
        if not bmc:
            d.text((ox, oy + LBL + 20), "-", fill=(90, 90, 95)); continue
        for y, row in enumerate(bmc):
            for x, on in enumerate(row):
                if on:
                    d.rectangle([ox + x * S, oy + LBL + y * S,
                                 ox + x * S + S - 1, oy + LBL + y * S + S - 1],
                                fill=col)
OUT = f"compare_sheet_{bm.IDENTITY.slug}.png"
img.save(OUT)
print("\nwrote", OUT, img.size)

# ----------------------------------------------------------------- verdict --
# On a pixel grid a handful of shapes have essentially one sensible
# solution, so any two pixel fonts converge on them -- a horizontal rule for
# underscore, a cross for plus, the obvious box corners. Those are listed here
# as expected. An identical bitmap for anything *outside* these sets would be a
# real collision worth investigating, so CI fails on it.
ALLOWED = bm.COMPARE["allowed"]

problems = []
for label, exact in RESULTS.items():
    allowed = ALLOWED.get(label, set())
    unexpected = sorted(set(exact) - allowed)
    if unexpected:
        problems.append(f"{label}: unexpected identical glyphs {''.join(unexpected)!r}")

print()
if problems:
    print("ORIGINALITY CHECK FAILED")
    for p in problems:
        print("  " + p)
    print("  A glyph now matches a reference font exactly. Either redraw it, or")
    print("  if it is genuinely a single-solution shape, add it to the allow-set")
    print("  in src/compare.py with a note explaining why.")
    raise SystemExit(1)
print("ORIGINALITY CHECK PASSED - identical bitmaps are canonical shapes only")
