#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render specimen + receipt previews from Till Mono's compiled TTFs.

Writes specimen.png and receipt_demo.png. Run from the repo root -- the
TTF input paths are relative.
"""
import random
from PIL import Image, ImageDraw, ImageFont

import fonts.till_mono as bm

FONT_DIR = f"fonts/{bm.IDENTITY.slug}/ttf"
REG = f"{FONT_DIR}/{bm.IDENTITY.ps_name('Regular')}.ttf"
BOLD = f"{FONT_DIR}/{bm.IDENTITY.ps_name('Bold')}.ttf"


def adv(size):
    """Monospace advance in px at a given ppem, derived from the grid."""
    return size * bm.GRID.advance // bm.GRID.em

# ---------------------------------------------------------------- specimen --
def specimen():
    """Render the type specimen sheet to specimen.png."""
    BG, AMBER, DIM = (13, 13, 16), (255, 176, 0), (150, 105, 25)
    W = 1060
    img = Image.new("RGB", (W, 1210), BG)
    d = ImageDraw.Draw(img)
    y = 44

    def line(text, size=36, color=AMBER, font=REG, x=44, dy=None):
        nonlocal y
        f = ImageFont.truetype(font, size)
        d.text((x, y), text, font=f, fill=color)
        y += dy if dy is not None else size + size // 3

    line("TILL MONO", 72, AMBER, BOLD, dy=88)
    line("AN OPEN-SOURCE 8×12 PIXEL MONOSPACE • SIL OFL 1.1", 24, DIM, REG, dy=52)

    line("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    line("abcdefghijklmnopqrstuvwxyz")
    line("0123456789 ¢$€£¥ #%&@*+=<>/\\")
    line("!?\"'()[]{}|;:,.^~–—•…°×÷ ←↑→↓ ✓☺", dy=64)

    line("Sphinx of black quartz, judge my vow.")
    line("Pack my box with five dozen jugs — £4.20", dy=64)
    line("Bold for totals: GRAND TOTAL $19.58", 36, AMBER, BOLD, dy=64)

    def box(width, txt, dbl=True):
        tl, tr, bl, br, h, v = ("╔","╗","╚","╝","═","║") if dbl else ("┌","┐","└","┘","─","│")
        return [tl + h * width + tr,
                v + txt.center(width) + v,
                bl + h * width + br]
    left = box(16, "TOTAL    19.58", True)
    right = box(16, "░▒▓█▓▒░ ▌▐▪•", False)
    for a, b in zip(left, right):
        line(a + "  " + b, 36, AMBER, REG, dy=40)
    y += 24

    line("PIXEL-PERFECT AT MULTIPLES OF 12PX:", 24, DIM, REG, dy=40)
    x = 44
    for s in (12, 24, 36, 48):
        f = ImageFont.truetype(REG, s)
        d.text((x, y + 48 - s), f"RECEIPT{s}", font=f, fill=AMBER)
        x += adv(s) * 9 + 24
    y += 84

    # subtle CRT scanlines
    px = img.load()
    for yy in range(0, img.height, 3):
        for xx in range(img.width):
            r, g, b = px[xx, yy]
            px[xx, yy] = (r * 82 // 100, g * 82 // 100, b * 82 // 100)
    img = img.crop((0, 0, W, min(img.height, y + 20)))
    img.save("specimen.png")
    print("wrote specimen.png", img.size)

# ----------------------------------------------------------------- receipt --
def receipt():
    """Render the mock till receipt to receipt_demo.png."""
    SIZE = 24                      # 2 screen px per font px
    CW = adv(SIZE)                 # char width
    COLS = 32
    LH = SIZE + 2
    PAPER, INK, FAINT = (248, 243, 231), (26, 24, 21), (120, 114, 102)
    BGTOP, BGBOT = (166, 162, 154), (128, 124, 116)

    def row(label, amount):
        return (label + amount.rjust(COLS - len(label)))

    rule = "─" * COLS
    rng = random.Random(84)
    bar = "".join(rng.choice("▌▐█││ ") for _ in range(26))

    lines = [
        ("╔" + "═" * 30 + "╗", REG),
        ("║" + "RAD VIDEO + ARCADE".center(30) + "║", BOLD),
        ("║" + "2600 ATARI AVE • MALL 8".center(30) + "║", REG),
        ("╚" + "═" * 30 + "╝", REG),
        ("", REG),
        (" 06/21/1986  22:42  REG#2  0084", REG),
        (rule, REG),
        (row("THE WARRIORS  VHS", "2.99"), REG),
        (row("TRON          VHS", "2.99"), REG),
        (row("ARCADE TOKENS ×25", "5.00"), REG),
        (row("BLANK TAPE T-120", "7.49"), REG),
        (rule, REG),
        (row("SUBTOTAL", "18.47"), REG),
        (row("TAX 6%", "1.11"), REG),
        (row("TOTAL", "19.58"), BOLD),
        (row("CASH", "20.00"), REG),
        (row("CHANGE", "0.42"), REG),
        (rule, REG),
        ("░▒▓ BE KIND • REWIND ▓▒░".center(COLS), REG),
        ("☺ HAVE A RADICAL DAY ☺".center(COLS), REG),
        ("", REG),
        (bar.center(COLS), REG),
        ("0 084221 98675".center(COLS), REG),
    ]

    margin, pad_y = 20, 26
    pw = COLS * CW + margin * 2
    ph = len(lines) * LH + pad_y * 2
    W, H = pw + 120, ph + 130
    img = Image.new("RGB", (W, H))
    for yy in range(H):                       # soft background gradient
        t = yy / H
        c = tuple(int(a + (b - a) * t) for a, b in zip(BGTOP, BGBOT))
        ImageDraw.Draw(img).line([(0, yy), (W, yy)], fill=c)
    d = ImageDraw.Draw(img)

    x0, y0 = (W - pw) // 2, (H - ph) // 2
    d.rectangle([x0 + 7, y0 + 9, x0 + pw + 7, y0 + ph + 9], fill=(96, 92, 86))
    d.rectangle([x0, y0, x0 + pw, y0 + ph], fill=PAPER)
    for edge_y, up in ((y0, True), (y0 + ph, False)):   # perforated tear edges
        step = 14
        for xx in range(x0, x0 + pw, step):
            tri = [(xx, edge_y), (xx + step, edge_y),
                   (xx + step // 2, edge_y + (7 if up else -7))]
            d.polygon(tri, fill=img.getpixel((max(xx, 0), max(edge_y - (12 if up else -12), 0))))

    fr = ImageFont.truetype(REG, SIZE)
    fb = ImageFont.truetype(BOLD, SIZE)
    ty = y0 + pad_y
    for text, fontpath in lines:
        f = fb if fontpath == BOLD else fr
        d.text((x0 + margin, ty), text, font=f, fill=INK)
        ty += LH
    img.save("receipt_demo.png")
    print("wrote receipt_demo.png", img.size)

if __name__ == "__main__":
    specimen()
    receipt()
