# -*- coding: utf-8 -*-
"""Till Mono -- an original 8x12 pixel-grid monospaced typeface.

Inspired by the 1980s engineering-terminal aesthetic and by classic dot-matrix
receipt printers. All outlines are original, drawn on a pixel grid and compiled
to TrueType.

Grid:
  * cell: 8 px wide x 12 px tall, 100 font units per px, UPM = 1200
  * rows 0..11 top->bottom; baseline sits under row 8
  * caps + digits: rows 1..8 (cap height 800)
  * x-height: rows 3..8 (600); descenders: rows 9..11 (300)
  * normal glyphs draw in cols 1..6; wide glyphs cols 0..6;
    box/blocks use the full 0..7 so they connect edge-to-edge

Edit any letter below and rebuild:
  SOURCE_DATE_EPOCH=1787097600 python src/build_all.py
Without SOURCE_DATE_EPOCH the head timestamps float and CI's drift guard fails.
License: SIL Open Font License 1.1
"""
from pixelfont import Grid, Identity, shade

GRID = Grid(cols=8, rows=12, baseline_row=8, cap_top_row=1, x_top_row=3)

IDENTITY = Identity(
    family="Till Mono",
    ps_prefix="TillMono",
    slug="till-mono",
    version="1.004",
    description=("An original 8x12 pixel-grid monospaced typeface for "
                 "1980s-style receipts, terminals and labels."),
)

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

G['\u2591'] = shade(GRID, lambda x, y: x % 2 == 0 and y % 2 == 0)      # light 25%
G['\u2592'] = shade(GRID, lambda x, y: (x + y) % 2 == 0)               # medium 50%
G['\u2593'] = shade(GRID, lambda x, y: not (x % 2 == 0 and y % 2 == 0))  # dark 75%

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


# ---------------------------------------------------------------- specimen --
# Sample content for docs/index.html. Each font carries its own, because the
# demos are not portable: this one needs box drawing, blocks and the smiley.
SPECIMEN = {
    "tagline": "AN OPEN-SOURCE 8\u00d712 PIXEL MONOSPACE \u2022 SIL OFL 1.1",
    "lines": [
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "abcdefghijklmnopqrstuvwxyz",
        "0123456789 \u00a2$\u20ac\u00a3\u00a5 #%&@*+=<>/\\",
        "!?\"'()[]{}|;:,.^~\u2013\u2014\u2022\u2026\u00b0\u00d7\u00f7 \u2190\u2191\u2192\u2193 \u2713\u263a",
        "Sphinx of black quartz, judge my vow.",
    ],
    "bold_line": "Bold for totals: GRAND TOTAL $19.58",
    "sample": """\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557
\u2551      RAD VIDEO + ARCADE      \u2551
\u2551   2600 ATARI AVE \u2022 MALL 8    \u2551
\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d

 06/21/1986  22:42  REG#2  0084
\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
THE WARRIORS  VHS           2.99
TRON          VHS           2.99
ARCADE TOKENS \u00d725           5.00
BLANK TAPE T-120            7.49
\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
SUBTOTAL                   18.47
TAX 6%                      1.11
[b]TOTAL                      19.58[/b]
\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
   \u2591\u2592\u2593 BE KIND \u2022 REWIND \u2593\u2592\u2591
    \u263a HAVE A RADICAL DAY \u263a""",
    "tester": "THANK YOU \u2022 COME AGAIN \u263a",
}


# ------------------------------------------------------------- originality --
# References to diff against, and the shapes that are allowed to coincide.
# On an 8x12 grid a handful of glyphs have essentially one sensible solution --
# a rule for underscore, a cross for plus, the obvious box corners -- so any two
# pixel fonts converge on them. Anything identical OUTSIDE these sets is a real
# collision and fails CI. Regenerate by running src/compare.py and reading the
# reported identical sets.
COMPARE = {
    "refs": {
        "font8x8_basic.h":
            "https://raw.githubusercontent.com/dhepper/font8x8/master/font8x8_basic.h",
        "departure.otf":
            "https://raw.githubusercontent.com/rektdeckard/departure-mono/main/"
            "public/assets/DepartureMono-Regular.otf",
    },
    "allowed": {
        "font8x8 (IBM ROM style)": set("_"),
        "Departure Mono": set("!*+,=T`\u00d7\u00f7\u2013\u250c\u2554"),
    },
}
