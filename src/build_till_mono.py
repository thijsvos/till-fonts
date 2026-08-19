#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Till Mono — an original 8x12 pixel-grid monospaced typeface.

Inspired by the 1980s engineering-terminal aesthetic (the same well Berkeley
Mono draws from) and by classic dot-matrix receipt printers. All outlines are
original, drawn on a pixel grid and compiled to TrueType.

Grid:
  * cell: 8 px wide x 12 px tall, 100 font units per px, UPM = 1200
  * rows 0..11 top->bottom; baseline sits under row 8
  * caps + digits: rows 1..8 (cap height 800)
  * x-height: rows 3..8 (600); descenders: rows 9..11 (300)
  * normal glyphs draw in cols 1..6; wide glyphs cols 0..6;
    box/blocks use the full 0..7 so they connect edge-to-edge

Edit any letter below and re-run:  python3 build_till_mono.py
License: SIL Open Font License 1.1
"""

import os
import shutil
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib.tables.O_S_2f_2 import Panose

PX = 100          # font units per pixel
EM = 1200
ADV = 800         # 8 px advance
ASC, DESC = 900, 300
FAMILY = "Till Mono"
VERSION = "1.000"
AUTHOR = "Thijs Vos"
REPO = "https://github.com/thijsvos/till-mono"
COPYRIGHT = f"Copyright 2026 {AUTHOR} ({REPO})"

# Built artifacts are committed, so the build writes straight to their tracked
# locations; CI rebuilds and fails if the result differs (see .github/workflows).
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TTF_DIR = os.path.join(ROOT, "fonts", "ttf")
WOFF2_DIRS = [os.path.join(ROOT, "fonts", "webfonts"),
              os.path.join(ROOT, "docs", "fonts")]

# ----------------------------------------------------------------------------
# Glyph bitmaps: char -> (top_row, [row strings])
#   row string length 6 -> drawn at cols 1..6
#   row string length 7 -> drawn at cols 0..6
#   row string length 8 -> drawn at cols 0..7 (full bleed, for box/blocks)
# ----------------------------------------------------------------------------

G = {}

G[' '] = (0, [])

# --- uppercase -------------------------------------------------------------
G['A'] = (1, ["..XX..",
              ".X..X.",
              "X....X",
              "X....X",
              "XXXXXX",
              "X....X",
              "X....X",
              "X....X"])
G['B'] = (1, ["XXXXX.",
              "X....X",
              "X....X",
              "XXXXX.",
              "X....X",
              "X....X",
              "X....X",
              "XXXXX."])
G['C'] = (1, [".XXXX.",
              "X....X",
              "X.....",
              "X.....",
              "X.....",
              "X.....",
              "X....X",
              ".XXXX."])
G['D'] = (1, ["XXXX..",
              "X...X.",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              "X...X.",
              "XXXX.."])
G['E'] = (1, ["XXXXXX",
              "X.....",
              "X.....",
              "XXXXX.",
              "X.....",
              "X.....",
              "X.....",
              "XXXXXX"])
G['F'] = (1, ["XXXXXX",
              "X.....",
              "X.....",
              "XXXXX.",
              "X.....",
              "X.....",
              "X.....",
              "X....."])
G['G'] = (1, [".XXXX.",
              "X....X",
              "X.....",
              "X.....",
              "X..XXX",
              "X....X",
              "X....X",
              ".XXXX."])
G['H'] = (1, ["X....X",
              "X....X",
              "X....X",
              "XXXXXX",
              "X....X",
              "X....X",
              "X....X",
              "X....X"])
G['I'] = (1, ["..XXX.",
              "...X..",
              "...X..",
              "...X..",
              "...X..",
              "...X..",
              "...X..",
              "..XXX."])
G['J'] = (1, ["...XXX",
              "....X.",
              "....X.",
              "....X.",
              "....X.",
              "....X.",
              "X...X.",
              ".XXX.."])
G['K'] = (1, ["X....X",
              "X...X.",
              "X..X..",
              "XXX...",
              "X..X..",
              "X...X.",
              "X....X",
              "X....X"])
G['L'] = (1, ["X.....",
              "X.....",
              "X.....",
              "X.....",
              "X.....",
              "X.....",
              "X.....",
              "XXXXXX"])
G['M'] = (1, ["X.....X",
              "XX...XX",
              "X.X.X.X",
              "X..X..X",
              "X.....X",
              "X.....X",
              "X.....X",
              "X.....X"])
G['N'] = (1, ["X....X",
              "XX...X",
              "X.X..X",
              "X..X.X",
              "X...XX",
              "X....X",
              "X....X",
              "X....X"])
G['O'] = (1, [".XXXX.",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              ".XXXX."])
G['P'] = (1, ["XXXXX.",
              "X....X",
              "X....X",
              "XXXXX.",
              "X.....",
              "X.....",
              "X.....",
              "X....."])
G['Q'] = (1, [".XXXX.",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              "X..X.X",
              "X...X.",
              ".XXX.X"])
G['R'] = (1, ["XXXXX.",
              "X....X",
              "X....X",
              "XXXXX.",
              "X.X...",
              "X..X..",
              "X...X.",
              "X....X"])
G['S'] = (1, [".XXXX.",
              "X....X",
              "X.....",
              ".XXXX.",
              ".....X",
              ".....X",
              "X....X",
              ".XXXX."])
G['T'] = (1, ["XXXXX.",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X..."])
G['U'] = (1, ["X....X",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              ".XXXX."])
G['V'] = (1, ["X....X",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              ".X..X.",
              ".X..X.",
              "..XX.."])
G['W'] = (1, ["X.....X",
              "X.....X",
              "X.....X",
              "X.....X",
              "X..X..X",
              "X.X.X.X",
              "XX...XX",
              "X.....X"])
G['X'] = (1, ["X....X",
              "X....X",
              ".X..X.",
              "..XX..",
              "..XX..",
              ".X..X.",
              "X....X",
              "X....X"])
G['Y'] = (1, ["X....X",
              "X....X",
              ".X..X.",
              "..XX..",
              "..X...",
              "..X...",
              "..X...",
              "..X..."])
G['Z'] = (1, ["XXXXXX",
              ".....X",
              "....X.",
              "...X..",
              "..X...",
              ".X....",
              "X.....",
              "XXXXXX"])

# --- lowercase -------------------------------------------------------------
G['a'] = (3, [".XXXX.",
              ".....X",
              ".XXXXX",
              "X....X",
              "X....X",
              ".XXXXX"])
G['b'] = (1, ["X.....",
              "X.....",
              "X.....",
              "X.XXX.",
              "XX...X",
              "X....X",
              "XX...X",
              "X.XXX."])
G['c'] = (3, [".XXXX.",
              "X....X",
              "X.....",
              "X.....",
              "X....X",
              ".XXXX."])
G['d'] = (1, [".....X",
              ".....X",
              ".....X",
              ".XXX.X",
              "X...XX",
              "X....X",
              "X...XX",
              ".XXX.X"])
G['e'] = (3, [".XXXX.",
              "X....X",
              "XXXXXX",
              "X.....",
              "X....X",
              ".XXXX."])
G['f'] = (1, ["...XX.",
              "..X...",
              "XXXXX.",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X..."])
G['g'] = (3, [".XXX.X",
              "X...XX",
              "X....X",
              "X....X",
              "X...XX",
              ".XXX.X",
              ".....X",
              ".....X",
              ".XXXX."])
G['h'] = (1, ["X.....",
              "X.....",
              "X.....",
              "X.XXX.",
              "XX...X",
              "X....X",
              "X....X",
              "X....X"])
G['i'] = (1, ["...X..",
              "......",
              "..XX..",
              "...X..",
              "...X..",
              "...X..",
              "...X..",
              "..XXX."])
G['j'] = (1, ["....X.",
              "......",
              "...XX.",
              "....X.",
              "....X.",
              "....X.",
              "....X.",
              "....X.",
              "....X.",
              "....X.",
              ".XXX.."])
G['k'] = (1, ["X.....",
              "X.....",
              "X.....",
              "X...X.",
              "X..X..",
              "XXX...",
              "X..X..",
              "X...X."])
G['l'] = (1, ["..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..XXX."])
G['m'] = (3, [".XX.XX.",
              "X..X..X",
              "X..X..X",
              "X..X..X",
              "X..X..X",
              "X..X..X"])
G['n'] = (3, ["X.XXX.",
              "XX...X",
              "X....X",
              "X....X",
              "X....X",
              "X....X"])
G['o'] = (3, [".XXXX.",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              ".XXXX."])
G['p'] = (3, ["X.XXX.",
              "XX...X",
              "X....X",
              "X....X",
              "XX...X",
              "X.XXX.",
              "X.....",
              "X.....",
              "X....."])
G['q'] = (3, [".XXX.X",
              "X...XX",
              "X....X",
              "X....X",
              "X...XX",
              ".XXX.X",
              ".....X",
              ".....X",
              ".....X"])
G['r'] = (3, ["X.XXX.",
              "XX...X",
              "X.....",
              "X.....",
              "X.....",
              "X....."])
G['s'] = (3, [".XXXXX",
              "X.....",
              ".XXXX.",
              ".....X",
              "X....X",
              ".XXXX."])
G['t'] = (2, ["..X...",
              "XXXXX.",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..XXX."])
G['u'] = (3, ["X....X",
              "X....X",
              "X....X",
              "X....X",
              "X...XX",
              ".XXX.X"])
G['v'] = (3, ["X....X",
              "X....X",
              "X....X",
              ".X..X.",
              ".X..X.",
              "..XX.."])
G['w'] = (3, ["X.....X",
              "X.....X",
              "X..X..X",
              "X..X..X",
              "X.X.X.X",
              ".X...X."])
G['x'] = (3, ["X....X",
              ".X..X.",
              "..XX..",
              "..XX..",
              ".X..X.",
              "X....X"])
G['y'] = (3, ["X....X",
              "X....X",
              "X....X",
              "X....X",
              "X...XX",
              ".XXX.X",
              ".....X",
              ".....X",
              ".XXXX."])
G['z'] = (3, ["XXXXXX",
              "....X.",
              "...X..",
              "..X...",
              ".X....",
              "XXXXXX"])

# --- digits (slashed zero, terminal style) ---------------------------------
G['0'] = (1, [".XXXX.",
              "X....X",
              "X...XX",
              "X..X.X",
              "X.X..X",
              "XX...X",
              "X....X",
              ".XXXX."])
G['1'] = (1, ["..X...",
              ".XX...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              ".XXXX."])
G['2'] = (1, [".XXXX.",
              "X....X",
              ".....X",
              "....X.",
              "...X..",
              "..X...",
              ".X....",
              "XXXXXX"])
G['3'] = (1, [".XXXX.",
              "X....X",
              ".....X",
              "..XXX.",
              ".....X",
              ".....X",
              "X....X",
              ".XXXX."])
G['4'] = (1, ["....X.",
              "...XX.",
              "..X.X.",
              ".X..X.",
              "X...X.",
              "XXXXXX",
              "....X.",
              "....X."])
G['5'] = (1, ["XXXXXX",
              "X.....",
              "X.....",
              "XXXXX.",
              ".....X",
              ".....X",
              "X....X",
              ".XXXX."])
G['6'] = (1, [".XXXX.",
              "X....X",
              "X.....",
              "XXXXX.",
              "X....X",
              "X....X",
              "X....X",
              ".XXXX."])
G['7'] = (1, ["XXXXXX",
              ".....X",
              "....X.",
              "...X..",
              "..X...",
              "..X...",
              "..X...",
              "..X..."])
G['8'] = (1, [".XXXX.",
              "X....X",
              "X....X",
              ".XXXX.",
              "X....X",
              "X....X",
              "X....X",
              ".XXXX."])
G['9'] = (1, [".XXXX.",
              "X....X",
              "X....X",
              ".XXXXX",
              ".....X",
              ".....X",
              "X....X",
              ".XXXX."])

# --- ASCII punctuation & symbols -------------------------------------------
G['!'] = (1, ["..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "......",
              "..X..."])
G['"'] = (1, [".X..X.",
              ".X..X."])
G['#'] = (1, [".X..X..",
              ".X..X..",
              "XXXXXXX",
              ".X..X..",
              ".X..X..",
              "XXXXXXX",
              ".X..X..",
              ".X..X.."])
G['$'] = (0, ["...X..",
              ".XXXX.",
              "X..X.X",
              "X..X..",
              ".XXXX.",
              "...X.X",
              "...X.X",
              "X..X.X",
              ".XXXX.",
              "...X.."])
G['%'] = (2, ["XX....X",
              "XX...X.",
              "....X..",
              "...X...",
              "..X....",
              ".X...XX",
              "X....XX"])
G['&'] = (1, [".XX....",
              "X..X...",
              "X..X...",
              ".XX....",
              "X..X..X",
              "X...XX.",
              "X...XX.",
              ".XXX..X"])
G["'"] = (1, ["..X...",
              "..X..."])
G['('] = (1, ["....X.",
              "...X..",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "...X..",
              "....X."])
G[')'] = (1, [".X....",
              "..X...",
              "...X..",
              "...X..",
              "...X..",
              "...X..",
              "..X...",
              ".X...."])
G['*'] = (2, ["..X...",
              "X.X.X.",
              ".XXX..",
              "X.X.X.",
              "..X..."])
G['+'] = (3, ["..X...",
              "..X...",
              "XXXXX.",
              "..X...",
              "..X..."])
G[','] = (8, ["..X...",
              "..X...",
              ".X...."])
G['-'] = (5, [".XXXX."])
G['.'] = (8, ["..X..."])
G['/'] = (1, [".....X",
              "....X.",
              "....X.",
              "...X..",
              "..X...",
              "..X...",
              ".X....",
              "X....."])
G[':'] = (5, ["..X...",
              "......",
              "......",
              "..X..."])
G[';'] = (5, ["..X...",
              "......",
              "......",
              "..X...",
              "..X...",
              ".X...."])
G['<'] = (3, ["....X.",
              "..XX..",
              "XX....",
              "..XX..",
              "....X."])
G['='] = (4, ["XXXXX.",
              "......",
              "XXXXX."])
G['>'] = (3, [".X....",
              "..XX..",
              "....XX",
              "..XX..",
              ".X...."])
G['?'] = (1, [".XXXX.",
              "X....X",
              ".....X",
              "....X.",
              "...X..",
              "...X..",
              "......",
              "...X.."])
G['@'] = (1, [".XXXXX.",
              "X.....X",
              "X..XX.X",
              "X.X.X.X",
              "X.X.X.X",
              "X..XXX.",
              "X......",
              ".XXXXX."])
G['['] = (1, ["..XXX.",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..XXX."])
G['\\'] = (1, ["X.....",
               ".X....",
               ".X....",
               "..X...",
               "...X..",
               "...X..",
               "....X.",
               ".....X"])
G[']'] = (1, [".XXX..",
              "...X..",
              "...X..",
              "...X..",
              "...X..",
              "...X..",
              "...X..",
              ".XXX.."])
G['^'] = (1, ["..X...",
              ".X.X..",
              "X...X."])
G['_'] = (9, ["XXXXXXXX"])
G['`'] = (1, ["..X...",
              "...X.."])
G['{'] = (1, ["...XX.",
              "..X...",
              "..X...",
              ".X....",
              "..X...",
              "..X...",
              "..X...",
              "...XX."])
G['|'] = (1, ["..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X...",
              "..X..."])
G['}'] = (1, [".XX...",
              "...X..",
              "...X..",
              "....X.",
              "...X..",
              "...X..",
              "...X..",
              ".XX..."])
G['~'] = (5, [".XX..X",
              "X..XX."])

# --- currency, math, marks --------------------------------------------------
G['\u00A2'] = (2, ["...X..",          # cent sign
                   ".XXXX.",
                   "X..X.X",
                   "X..X..",
                   "X..X..",
                   "X..X.X",
                   ".XXXX.",
                   "...X.."])
G['\u00A3'] = (1, ["..XXX.",          # pound
                   ".X...X",
                   ".X....",
                   "XXXX..",
                   ".X....",
                   ".X....",
                   ".X....",
                   "XXXXXX"])
G['\u00A5'] = (1, ["X....X",          # yen
                   ".X..X.",
                   "..XX..",
                   "XXXXX.",
                   "..X...",
                   "XXXXX.",
                   "..X...",
                   "..X..."])
G['\u20AC'] = (1, ["..XXX.",          # euro
                   ".X...X",
                   "XXXX..",
                   ".X....",
                   "XXXX..",
                   ".X....",
                   ".X...X",
                   "..XXX."])
G['\u00B0'] = (1, ["..XX..",          # degree
                   ".X..X.",
                   ".X..X.",
                   "..XX.."])
G['\u00D7'] = (3, ["X...X.",          # multiply
                   ".X.X..",
                   "..X...",
                   ".X.X..",
                   "X...X."])
G['\u00F7'] = (3, ["..X...",          # divide
                   "......",
                   "XXXXX.",
                   "......",
                   "..X..."])
G['\u2013'] = (5, ["XXXXX."])          # en dash
G['\u2014'] = (5, ["XXXXXXXX"])        # em dash (full bleed)
G['\u2018'] = (1, ["...X..",           # left single quote
                   "..X..."])
G['\u2019'] = (1, ["..X...",           # right single quote
                   ".X...."])
G['\u201C'] = (1, [".X..X.",           # left double quote
                   "X..X.."])
G['\u201D'] = (1, [".X..X.",           # right double quote
                   "..X..X"])
G['\u2022'] = (4, ["..XX..",           # bullet
                   ".XXXX.",
                   ".XXXX.",
                   "..XX.."])
G['\u2026'] = (8, ["X.X.X."])          # ellipsis
G['\u2190'] = (3, ["..X...",           # left arrow
                   ".X....",
                   "XXXXXX",
                   ".X....",
                   "..X..."])
G['\u2191'] = (2, ["..X...",           # up arrow
                   ".XXX..",
                   "X.X.X.",
                   "..X...",
                   "..X...",
                   "..X...",
                   "..X..."])
G['\u2192'] = (3, ["...X..",           # right arrow
                   "....X.",
                   "XXXXXX",
                   "....X.",
                   "...X.."])
G['\u2193'] = (2, ["..X...",           # down arrow
                   "..X...",
                   "..X...",
                   "..X...",
                   "X.X.X.",
                   ".XXX..",
                   "..X..."])
G['\u2713'] = (3, [".....X",           # check mark
                   "....XX",
                   "...XX.",
                   "X.XX..",
                   "XXX...",
                   ".X...."])
G['\u263A'] = (1, [".XXXXX.",          # CP437 smiley
                   "X.....X",
                   "X.X.X.X",
                   "X.....X",
                   "X.X.X.X",
                   "X..X..X",
                   "X.....X",
                   ".XXXXX."])

# --- box drawing: single ----------------------------------------------------
VBAR = "....X..."
G['\u2500'] = (5, ["XXXXXXXX"])
G['\u2502'] = (0, [VBAR] * 12)
G['\u250C'] = (5, ["....XXXX"] + [VBAR] * 6)
G['\u2510'] = (5, ["XXXXX..."] + [VBAR] * 6)
G['\u2514'] = (0, [VBAR] * 5 + ["....XXXX"])
G['\u2518'] = (0, [VBAR] * 5 + ["XXXXX..."])
G['\u251C'] = (0, [VBAR] * 5 + ["....XXXX"] + [VBAR] * 6)
G['\u2524'] = (0, [VBAR] * 5 + ["XXXXX..."] + [VBAR] * 6)
G['\u252C'] = (5, ["XXXXXXXX"] + [VBAR] * 6)
G['\u2534'] = (0, [VBAR] * 5 + ["XXXXXXXX"])
G['\u253C'] = (0, [VBAR] * 5 + ["XXXXXXXX"] + [VBAR] * 6)

# --- box drawing: double ----------------------------------------------------
DBAR = "...X.X.."
G['\u2550'] = (4, ["XXXXXXXX", "........", "XXXXXXXX"])
G['\u2551'] = (0, [DBAR] * 12)
G['\u2554'] = (4, ["...XXXXX", "...X....", "...X.XXX"] + [DBAR] * 5)
G['\u2557'] = (4, ["XXXXXX..", ".....X..", "XXXX.X.."] + [DBAR] * 5)
G['\u255A'] = (0, [DBAR] * 4 + ["...X.XXX", "...X....", "...XXXXX"])
G['\u255D'] = (0, [DBAR] * 4 + ["XXXX.X..", ".....X..", "XXXXXX.."])
G['\u2560'] = (0, [DBAR] * 4 + ["...X.XXX", "...X....", "...X.XXX"] + [DBAR] * 5)
G['\u2563'] = (0, [DBAR] * 4 + ["XXXX.X..", ".....X..", "XXXX.X.."] + [DBAR] * 5)
G['\u2566'] = (4, ["XXXXXXXX", "........", "XXXX.XXX"] + [DBAR] * 5)
G['\u2569'] = (0, [DBAR] * 4 + ["XXXX.XXX", "........", "XXXXXXXX"])
G['\u256C'] = (0, [DBAR] * 4 + ["XXXX.XXX", "........", "XXXX.XXX"] + [DBAR] * 5)

# --- block elements ----------------------------------------------------------
G['\u2588'] = (0, ["XXXXXXXX"] * 12)     # full block
G['\u2580'] = (0, ["XXXXXXXX"] * 6)      # upper half
G['\u2584'] = (6, ["XXXXXXXX"] * 6)      # lower half
G['\u258C'] = (0, ["XXXX...."] * 12)     # left half
G['\u2590'] = (0, ["....XXXX"] * 12)     # right half
G['\u25AA'] = (4, [".XXX..",            # small black square
                   ".XXX..",
                   ".XXX.."])

def _shade(keep):
    return (0, ["".join("X" if keep(x, y) else "." for x in range(8))
                for y in range(12)])

G['\u2591'] = _shade(lambda x, y: x % 2 == 0 and y % 2 == 0)      # light 25%
G['\u2592'] = _shade(lambda x, y: (x + y) % 2 == 0)               # medium 50%
G['\u2593'] = _shade(lambda x, y: not (x % 2 == 0 and y % 2 == 0))  # dark 75%

NOTDEF = (1, ["XXXXXX",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              "X....X",
              "XXXXXX"])

# glyphs excluded from bold emboldening (they must keep exact cell geometry)
NO_BOLD = set("\u2500\u2502\u250C\u2510\u2514\u2518\u251C\u2524\u252C\u2534"
              "\u253C\u2550\u2551\u2554\u2557\u255A\u255D\u2560\u2563\u2566"
              "\u2569\u256C\u2588\u2580\u2584\u258C\u2590\u2591\u2592\u2593"
              "\u2014_")

# ----------------------------------------------------------------------------
# bitmap -> pixel set -> traced contours
# ----------------------------------------------------------------------------

def validate():
    for ch, (top, rows) in list(G.items()) + [("<notdef>", NOTDEF)]:
        assert 0 <= top and top + len(rows) <= 12, f"{ch!r}: bad row span"
        for r in rows:
            assert len(r) in (6, 7, 8), f"{ch!r}: bad row width {len(r)}"
            assert set(r) <= {'X', '.'}, f"{ch!r}: bad chars"

def pixels_of(top, rows):
    """Return set of (x, gy) pixel coords. gy is y-up: gy = 8 - row."""
    pts = set()
    for i, row in enumerate(rows):
        off = 1 if len(row) == 6 else 0
        r = top + i
        for j, ch in enumerate(row):
            if ch == 'X':
                pts.add((j + off, 8 - r))
    return pts

def embolden(pts, wide7):
    out = set(pts)
    for (x, y) in pts:
        if x + 1 <= 7:
            out.add((x + 1, y))
    if wide7:                      # keep a sliver of right bearing on 7px glyphs
        out = {(x, y) for (x, y) in out if not (x == 7 and (6, y) not in pts)}
        out |= {(x, y) for (x, y) in pts}
    return out

RIGHT = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}
LEFT = {v: k for k, v in RIGHT.items()}

def trace(pts):
    """March pixel boundary; filled area stays on the right of travel
    (clockwise outers, counter-clockwise holes, TrueType style)."""
    edges = {}
    def add(a, b):
        edges.setdefault(a, []).append(b)
    for (x, y) in pts:
        if (x, y + 1) not in pts: add((x, y + 1), (x + 1, y + 1))   # top
        if (x + 1, y) not in pts: add((x + 1, y + 1), (x + 1, y))   # right
        if (x, y - 1) not in pts: add((x + 1, y), (x, y))           # bottom
        if (x - 1, y) not in pts: add((x, y), (x, y + 1))           # left
    contours = []
    while edges:
        start = next(iter(edges))
        pt = start
        nxt = edges[pt].pop()
        if not edges[pt]:
            del edges[pt]
        d = (nxt[0] - pt[0], nxt[1] - pt[1])
        loop = [pt]
        pt = nxt
        while pt != start:
            loop.append(pt)
            cands = edges.get(pt, [])
            best = None
            for pref in (RIGHT[d], d, LEFT[d]):
                tgt = (pt[0] + pref[0], pt[1] + pref[1])
                if tgt in cands:
                    best = tgt
                    break
            if best is None:
                best = cands[0]
            cands.remove(best)
            if not cands:
                del edges[pt]
            d = (best[0] - pt[0], best[1] - pt[1])
            pt = best
        # drop collinear midpoints
        simp = []
        n = len(loop)
        for i in range(n):
            a, b, c = loop[i - 1], loop[i], loop[(i + 1) % n]
            if (b[0] - a[0]) * (c[1] - b[1]) != (b[1] - a[1]) * (c[0] - b[0]):
                simp.append(b)
        contours.append([(x * PX, y * PX) for (x, y) in simp])
    return contours

# ----------------------------------------------------------------------------
# font compilation
# ----------------------------------------------------------------------------

AGL = {' ': "space", '!': "exclam", '"': "quotedbl", '#': "numbersign",
       '$': "dollar", '%': "percent", '&': "ampersand", "'": "quotesingle",
       '(': "parenleft", ')': "parenright", '*': "asterisk", '+': "plus",
       ',': "comma", '-': "hyphen", '.': "period", '/': "slash",
       ':': "colon", ';': "semicolon", '<': "less", '=': "equal",
       '>': "greater", '?': "question", '@': "at", '[': "bracketleft",
       '\\': "backslash", ']': "bracketright", '^': "asciicircum",
       '_': "underscore", '`': "grave", '{': "braceleft", '|': "bar",
       '}': "braceright", '~': "asciitilde"}

def glyph_name(ch):
    if ch in AGL:
        return AGL[ch]
    if ch.isascii() and ch.isalnum():
        return ch if ch.isalpha() else "zero one two three four five six seven eight nine".split()[int(ch)]
    return "uni%04X" % ord(ch)

def build(style="Regular", outdir=None):
    validate()
    bold = style == "Bold"
    order = [".notdef"]
    cmap, glyf, metrics = {}, {}, {}

    def compile_glyph(name, top, rows, ch=None):
        pts = pixels_of(top, rows)
        if bold and pts and (ch is None or ch not in NO_BOLD):
            wide7 = any(len(r) == 7 for r in rows)
            pts = embolden(pts, wide7)
        pen = TTGlyphPen(None)
        for contour in trace(pts):
            pen.moveTo(contour[0])
            for p in contour[1:]:
                pen.lineTo(p)
            pen.closePath()
        glyf[name] = pen.glyph()
        lsb = min((x for x, _ in pts), default=0) * PX
        metrics[name] = (ADV, lsb)

    compile_glyph(".notdef", *NOTDEF)
    for ch in sorted(G, key=ord):
        name = glyph_name(ch)
        order.append(name)
        cmap[ord(ch)] = name
        compile_glyph(name, *G[ch], ch=ch)
    # map NBSP to space width
    cmap[0x00A0] = "space"

    fb = FontBuilder(EM, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(glyf)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=ASC, descent=-DESC)

    ps = f"TillMono-{style}"
    fb.setupNameTable({
        "familyName": FAMILY,
        "styleName": style,
        "uniqueFontIdentifier": f"{VERSION};TILL;{ps}",
        "fullName": f"{FAMILY} {style}",
        "psName": ps,
        "version": f"Version {VERSION}",
        "copyright": COPYRIGHT,
        "designer": AUTHOR,
        "designerURL": REPO,
        "vendorURL": REPO,
        "description": ("An original 8x12 pixel-grid monospaced typeface for "
                        "1980s-style receipts, terminals and labels."),
        "licenseDescription": ("This Font Software is licensed under the SIL "
                               "Open Font License, Version 1.1."),
        "licenseInfoURL": "https://openfontlicense.org",
    })

    panose = Panose()
    panose.bFamilyType = 2
    panose.bProportion = 9          # monospaced
    fb.setupOS2(sTypoAscender=ASC, sTypoDescender=-DESC, sTypoLineGap=0,
                usWinAscent=ASC, usWinDescent=DESC,
                sCapHeight=800, sxHeight=600,
                usWeightClass=700 if bold else 400,
                achVendID="TILL", fsType=0, panose=panose,
                xAvgCharWidth=ADV)
    os2 = fb.font["OS/2"]
    os2.fsSelection = 0x20 if bold else 0x40
    fb.font["head"].macStyle = 0x1 if bold else 0x0
    fb.setupPost(isFixedPitch=1, underlinePosition=-150, underlineThickness=100)

    # outdir=None -> the tracked repo layout; pass a path for a throwaway build.
    ttf_dir, woff2_dirs = (TTF_DIR, WOFF2_DIRS) if outdir is None else (outdir, [outdir])

    os.makedirs(ttf_dir, exist_ok=True)
    ttf = os.path.join(ttf_dir, f"{ps}.ttf")
    fb.save(ttf)
    try:
        fb.font.flavor = "woff2"
        os.makedirs(woff2_dirs[0], exist_ok=True)
        woff2 = os.path.join(woff2_dirs[0], f"{ps}.woff2")
        fb.font.save(woff2)
        for d in woff2_dirs[1:]:
            os.makedirs(d, exist_ok=True)
            shutil.copyfile(woff2, os.path.join(d, f"{ps}.woff2"))
    except Exception as e:
        print("woff2 skipped:", e)
    print("built", ttf, f"({len(order)} glyphs)")
    return ttf

if __name__ == "__main__":
    build("Regular")
    build("Bold")
