# -*- coding: utf-8 -*-
"""Till Text -- an original 8x16 pixel-grid monospaced typeface.

Where Till Mono is square and deliberately retro, Till Text is the family's
general-purpose face: a neutral monospace for UI, body copy and code. It takes
its cues from Commit Mono's design thesis -- that a working typeface should be
unremarkable -- and transfers what survives on a pixel grid: a large x-height,
uniform stroke weight and flat terminals. It is a homage, not a transcription;
Commit Mono's optical kerning has no meaning at integer pixel positions.

Grid:
  * cell: 8 px wide x 16 px tall, 100 font units per px, UPM = 1600
  * rows 0..15 top->bottom; baseline sits under row 11
  * rows 0..1  accent zone (acute, grave, circumflex, tilde, umlaut, ring)
  * rows 2..11 caps and ascenders (cap height 1000)
  * rows 4..11 x-height (800) -- x/cap = 0.80, the large-x-height signature
  * rows 12..14 descenders (300); row 15 is underline/breathing room
  * normal glyphs draw in cols 1..6; wide glyphs cols 0..6;
    box/blocks use the full 0..7 so they connect edge-to-edge

Pixel-perfect at multiples of 16px -- which is the web's default body size.

Edit any letter below and rebuild:
  SOURCE_DATE_EPOCH=1787097600 python src/build_all.py
License: SIL Open Font License 1.1
"""
from pixelfont import Grid, Identity, shade

GRID = Grid(cols=8, rows=16, baseline_row=11, cap_top_row=2, x_top_row=4)

IDENTITY = Identity(
    family="Till Text",
    ps_prefix="TillText",
    slug="till-text",
    version="1.000",
    description=("An original 8x16 pixel-grid monospaced typeface for user "
                 "interfaces, body copy and code."),
)

G = {}

# --- uppercase: rows 2..11, 10 rows tall -----------------------------------
G['A'] = (2, ["..XX..", ".X..X.", ".X..X.", "X....X", "X....X",
              "XXXXXX", "X....X", "X....X", "X....X", "X....X"])
G['B'] = (2, ["XXXXX.", "X....X", "X....X", "X....X", "XXXXX.",
              "X....X", "X....X", "X....X", "X....X", "XXXXX."])
G['C'] = (2, ["..XXX.", ".X...X", "X.....", "X.....", "X.....",
              "X.....", "X.....", "X.....", ".X...X", "..XXX."])
G['D'] = (2, ["XXXX..", "X...X.", "X....X", "X....X", "X....X",
              "X....X", "X....X", "X....X", "X...X.", "XXXX.."])
G['E'] = (2, ["XXXXXX", "X.....", "X.....", "X.....", "XXXXX.",
              "X.....", "X.....", "X.....", "X.....", "XXXXXX"])
G['F'] = (2, ["XXXXXX", "X.....", "X.....", "X.....", "XXXXX.",
              "X.....", "X.....", "X.....", "X.....", "X....."])
G['G'] = (2, ["..XXX.", ".X...X", "X.....", "X.....", "X.....",
              "X..XXX", "X....X", "X....X", ".X...X", "..XXX."])
G['H'] = (2, ["X....X", "X....X", "X....X", "X....X", "XXXXXX",
              "X....X", "X....X", "X....X", "X....X", "X....X"])
G['I'] = (2, ["XXXXXX", "..XX..", "..XX..", "..XX..", "..XX..",
              "..XX..", "..XX..", "..XX..", "..XX..", "XXXXXX"])
G['J'] = (2, ["..XXXX", "....X.", "....X.", "....X.", "....X.",
              "....X.", "....X.", "X...X.", "X...X.", ".XXX.."])
G['K'] = (2, ["X....X", "X...X.", "X..X..", "X.X...", "XX....",
              "XX....", "X.X...", "X..X..", "X...X.", "X....X"])
G['L'] = (2, ["X.....", "X.....", "X.....", "X.....", "X.....",
              "X.....", "X.....", "X.....", "X.....", "XXXXXX"])
G['M'] = (2, ["X.....X", "XX...XX", "X.X.X.X", "X.X.X.X", "X..X..X",
              "X..X..X", "X.....X", "X.....X", "X.....X", "X.....X"])
G['N'] = (2, ["X....X", "XX...X", "XX...X", "X.X..X", "X.X..X",
              "X..X.X", "X..X.X", "X...XX", "X...XX", "X....X"])
G['O'] = (2, ["..XX..", ".X..X.", "X....X", "X....X", "X....X",
              "X....X", "X....X", "X....X", ".X..X.", "..XX.."])
G['P'] = (2, ["XXXXX.", "X....X", "X....X", "X....X", "XXXXX.",
              "X.....", "X.....", "X.....", "X.....", "X....."])
G['Q'] = (2, ["..XX..", ".X..X.", "X....X", "X....X", "X....X",
              "X....X", "X.X..X", "X..X.X", ".X..X.", "..XX.X"])
G['R'] = (2, ["XXXXX.", "X....X", "X....X", "X....X", "XXXXX.",
              "X..X..", "X...X.", "X...X.", "X....X", "X....X"])
G['S'] = (2, ["..XXX.", ".X...X", "X.....", "X.....", ".XXX..",
              "...XX.", ".....X", "X....X", ".X...X", "..XXX."])
G['T'] = (2, ["XXXXXX", "..XX..", "..XX..", "..XX..", "..XX..",
              "..XX..", "..XX..", "..XX..", "..XX..", "..XX.."])
G['U'] = (2, ["X....X", "X....X", "X....X", "X....X", "X....X",
              "X....X", "X....X", "X....X", ".X..X.", "..XX.."])
G['V'] = (2, ["X....X", "X....X", "X....X", "X....X", "X....X",
              ".X..X.", ".X..X.", ".X..X.", "..XX..", "..XX.."])
G['W'] = (2, ["X.....X", "X.....X", "X.....X", "X..X..X", "X..X..X",
              "X.X.X.X", "X.X.X.X", "XX...XX", "X.....X", "X.....X"])
G['X'] = (2, ["X....X", "X....X", ".X..X.", ".X..X.", "..XX..",
              "..XX..", ".X..X.", ".X..X.", "X....X", "X....X"])
G['Y'] = (2, ["X....X", "X....X", ".X..X.", ".X..X.", "..XX..",
              "..XX..", "..XX..", "..XX..", "..XX..", "..XX.."])
G['Z'] = (2, ["XXXXXX", ".....X", "....X.", "...X..", "..X...",
              "..X...", ".X....", "X.....", "X.....", "XXXXXX"])

# --- digits: slashed zero, flat terminals -----------------------------------
G['0'] = (2, ["..XX..", ".X..X.", "X....X", "X...XX", "X..X.X",
              "X.X..X", "XX...X", "X....X", ".X..X.", "..XX.."])
G['1'] = (2, ["..XX..", ".XXX..", "X.XX..", "..XX..", "..XX..",
              "..XX..", "..XX..", "..XX..", "..XX..", "XXXXXX"])
G['2'] = (2, ["..XXX.", ".X...X", "X....X", ".....X", "....X.",
              "...X..", "..X...", ".X....", "X.....", "XXXXXX"])
G['3'] = (2, ["..XXX.", ".X...X", "X....X", ".....X", "..XXX.",
              ".....X", ".....X", "X....X", ".X...X", "..XXX."])
G['4'] = (2, ["....XX", "...X.X", "..X..X", ".X...X", "X....X",
              "XXXXXX", ".....X", ".....X", ".....X", ".....X"])
G['5'] = (2, ["XXXXXX", "X.....", "X.....", "X.....", "XXXXX.",
              ".....X", ".....X", "X....X", ".X...X", "..XXX."])
G['6'] = (2, ["..XXX.", ".X...X", "X.....", "X.....", "XXXXX.",
              "X....X", "X....X", "X....X", ".X...X", "..XXX."])
G['7'] = (2, ["XXXXXX", ".....X", "....X.", "....X.", "...X..",
              "...X..", "..X...", "..X...", ".X....", ".X...."])
G['8'] = (2, ["..XXX.", ".X...X", "X....X", ".X...X", "..XXX.",
              ".X...X", "X....X", "X....X", ".X...X", "..XXX."])
G['9'] = (2, ["..XXX.", ".X...X", "X....X", "X....X", "X....X",
              ".XXXXX", ".....X", ".....X", ".X...X", "..XXX."])

# --- lowercase --------------------------------------------------------------
# x-height glyphs: rows 4..11 (8 rows). Ascenders start at row 2 (10 rows).
# Descenders run to row 14.
G['a'] = (4, [".XXXX.", "X....X", ".....X", ".XXXXX", "X....X",
              "X....X", "X...XX", ".XXX.X"])
G['b'] = (2, ["X.....", "X.....", "X.....", "XXXXX.", "X....X",
              "X....X", "X....X", "X....X", "X....X", "XXXXX."])
G['c'] = (4, [".XXXX.", "X....X", "X.....", "X.....", "X.....",
              "X.....", "X....X", ".XXXX."])
G['d'] = (2, [".....X", ".....X", ".....X", ".XXXXX", "X....X",
              "X....X", "X....X", "X....X", "X....X", ".XXXXX"])
G['e'] = (4, [".XXXX.", "X....X", "X....X", "XXXXXX", "X.....",
              "X.....", "X....X", ".XXXX."])
G['f'] = (2, ["..XXX.", ".X....", ".X....", "XXXXX.", ".X....",
              ".X....", ".X....", ".X....", ".X....", ".X...."])
G['g'] = (4, [".XXXXX", "X....X", "X....X", "X....X", "X....X",
              "X....X", ".XXXXX", ".....X", "X....X", ".XXXX."])
G['h'] = (2, ["X.....", "X.....", "X.....", "XXXXX.", "X....X",
              "X....X", "X....X", "X....X", "X....X", "X....X"])
G['i'] = (2, ["..XX..", "..XX..", "......", ".XXX..", "..XX..",
              "..XX..", "..XX..", "..XX..", "..XX..", ".XXXX."])
G['j'] = (2, ["...XX.", "...XX.", "......", "..XXX.", "...XX.",
              "...XX.", "...XX.", "...XX.", "...XX.", "...XX.",
              "X..XX.", ".XXX.."])
G['k'] = (2, ["X.....", "X.....", "X.....", "X...X.", "X..X..",
              "X.X...", "XXX...", "X..X..", "X...X.", "X....X"])
G['l'] = (2, [".XXX..", "..XX..", "..XX..", "..XX..", "..XX..",
              "..XX..", "..XX..", "..XX..", "..XX..", ".XXXX."])
G['m'] = (4, ["XX.XX.", "X.X..X", "X.X..X", "X.X..X", "X.X..X",
              "X.X..X", "X.X..X", "X.X..X"])
G['n'] = (4, ["XXXXX.", "X....X", "X....X", "X....X", "X....X",
              "X....X", "X....X", "X....X"])
G['o'] = (4, [".XXXX.", "X....X", "X....X", "X....X", "X....X",
              "X....X", "X....X", ".XXXX."])
G['p'] = (4, ["XXXXX.", "X....X", "X....X", "X....X", "X....X",
              "X....X", "XXXXX.", "X.....", "X.....", "X....."])
G['q'] = (4, [".XXXXX", "X....X", "X....X", "X....X", "X....X",
              "X....X", ".XXXXX", ".....X", ".....X", ".....X"])
G['r'] = (4, ["X.XXX.", "XX...X", "X.....", "X.....", "X.....",
              "X.....", "X.....", "X....."])
G['s'] = (4, [".XXXXX", "X.....", "X.....", ".XXXX.", ".....X",
              ".....X", "X....X", "XXXXX."])
G['t'] = (2, ["..X...", "..X...", "..X...", "XXXXX.", "..X...",
              "..X...", "..X...", "..X...", "..X..X", "...XX."])
G['u'] = (4, ["X....X", "X....X", "X....X", "X....X", "X....X",
              "X....X", "X...XX", ".XXX.X"])
G['v'] = (4, ["X....X", "X....X", "X....X", "X....X", ".X..X.",
              ".X..X.", "..XX..", "..XX.."])
G['w'] = (4, ["X.....X", "X.....X", "X..X..X", "X..X..X", "X.X.X.X",
              "X.X.X.X", "XX...XX", "X.....X"])
G['x'] = (4, ["X....X", ".X..X.", ".X..X.", "..XX..", "..XX..",
              ".X..X.", ".X..X.", "X....X"])
G['y'] = (4, ["X....X", "X....X", "X....X", "X....X", "X....X",
              "X....X", ".XXXXX", ".....X", "X....X", ".XXXX."])
G['z'] = (4, ["XXXXXX", ".....X", "....X.", "...X..", "..X...",
              ".X....", "X.....", "XXXXXX"])

# --- ASCII punctuation & symbols -------------------------------------------
G[' '] = (11, ["......"])
G['!'] = (2, ["..XX..", "..XX..", "..XX..", "..XX..", "..XX..",
              "..XX..", "..XX..", "......", "..XX..", "..XX.."])
G['"'] = (2, [".X..X.", ".X..X.", ".X..X."])
G['#'] = (3, [".X..X.", ".X..X.", "XXXXXX", ".X..X.", ".X..X.",
              ".X..X.", "XXXXXX", ".X..X.", ".X..X."])
G['$'] = (2, ["..XX..", ".XXXXX", "X.XX..", "X.XX..", ".XXXX.",
              "..XX.X", "..XX.X", "XXXXX.", "..XX..", "..XX.."])
G['%'] = (2, ["XX...X", "XX..X.", "....X.", "...X..", "..X...",
              "..X...", ".X....", ".X..XX", "X...XX", "......"])
G['&'] = (2, [".XXX..", "X...X.", "X...X.", ".X.X..", ".XX...",
              "X..X.X", "X...X.", "X...X.", "X....X", ".XXX.X"])
G["'"] = (2, ["..XX..", "..XX..", "..XX.."])
G['('] = (2, ["...XX.", "..X...", ".X....", ".X....", ".X....",
              ".X....", ".X....", ".X....", "..X...", "...XX."])
G[')'] = (2, [".XX...", "...X..", "....X.", "....X.", "....X.",
              "....X.", "....X.", "....X.", "...X..", ".XX..."])
G['*'] = (3, ["..XX..", "X.XX.X", ".XXXX.", "..XX..", ".XXXX.",
              "X.XX.X", "..XX.."])
G['+'] = (5, ["..XX..", "..XX..", "XXXXXX", "..XX..", "..XX.."])
G[','] = (10, ["..XX..", "..XX..", "..XX..", ".XX..."])
G['-'] = (7, ["XXXXXX", "XXXXXX"])
G['.'] = (10, ["..XX..", "..XX.."])
G['/'] = (2, [".....X", ".....X", "....X.", "...X..", "...X..",
              "..X...", "..X...", ".X....", "X.....", "X....."])
G[':'] = (5, ["..XX..", "..XX..", "......", "......", "..XX..",
              "..XX.."])
G[';'] = (5, ["..XX..", "..XX..", "......", "......", "..XX..",
              "..XX..", "..XX..", ".XX..."])
G['<'] = (4, ["....XX", "..XX..", "XX....", "XX....", "..XX..",
              "....XX"])
G['='] = (5, ["XXXXXX", "XXXXXX", "......", "XXXXXX", "XXXXXX"])
G['>'] = (4, ["XX....", "..XX..", "....XX", "....XX", "..XX..",
              "XX...."])
G['?'] = (2, ["..XXX.", ".X...X", "X....X", ".....X", "....X.",
              "...X..", "..X...", "......", "..XX..", "..XX.."])
G['@'] = (2, ["..XXX.", ".X...X", "X..XXX", "X.X..X", "X.X..X",
              "X.X..X", "X..XXX", "X.....", ".X...X", "..XXX."])
G['['] = (2, [".XXXX.", ".XX...", ".XX...", ".XX...", ".XX...",
              ".XX...", ".XX...", ".XX...", ".XX...", ".XXXX."])
G['\\'] = (2, ["X.....", "X.....", ".X....", "..X...", "..X...",
               "...X..", "...X..", "....X.", ".....X", ".....X"])
G[']'] = (2, [".XXXX.", "...XX.", "...XX.", "...XX.", "...XX.",
              "...XX.", "...XX.", "...XX.", "...XX.", ".XXXX."])
G['^'] = (2, ["..XX..", ".X..X.", "X....X"])
G['_'] = (14, ["XXXXXXXX", "XXXXXXXX"])
G['`'] = (2, [".XX...", "..XX..", "...X.."])
G['{'] = (2, ["...XXX", "..XX..", "..XX..", "..XX..", ".XX...",
              ".XX...", "..XX..", "..XX..", "..XX..", "...XXX"])
G['|'] = (2, ["..XX..", "..XX..", "..XX..", "..XX..", "..XX..",
              "..XX..", "..XX..", "..XX..", "..XX..", "..XX.."])
G['}'] = (2, ["XXX...", "..XX..", "..XX..", "..XX..", "...XX.",
              "...XX.", "..XX..", "..XX..", "..XX..", "XXX..."])
G['~'] = (6, [".XX..X", "X..XX."])

NOTDEF = (2, ["XXXXXX", "X....X", "X....X", "X....X", "X....X",
              "X....X", "X....X", "X....X", "X....X", "XXXXXX"])


# --- typographic marks, currency, math --------------------------------------
G['–'] = (7, ["XXXXXX", "XXXXXX"])                       # en dash
G['—'] = (7, ["XXXXXXXX", "XXXXXXXX"])                   # em dash
G['‘'] = (2, ["...XX.", "..XX..", "..X..."])             # left single quote
G['’'] = (2, ["..XX..", "...XX.", "....X."])             # right single quote
G['“'] = (2, [".XX.XX", "XX.XX.", "X..X.."])             # left double quote
G['”'] = (2, ["XX.XX.", ".XX.XX", "..X..X"])             # right double quote
G['•'] = (6, ["..XX..", ".XXXX.", ".XXXX.", "..XX.."])   # bullet
G['…'] = (10, ["X.X.X.", "X.X.X."])                      # ellipsis
G['¢'] = (3, ["..XX..", ".XXXX.", "X.XX..", "X.XX..", "X.XX..",
                   "X.XX..", ".XXXX.", "..XX.."])             # cent
G['£'] = (2, ["..XXX.", ".X...X", ".X....", ".X....", "XXXX..",
                   ".X....", ".X....", ".X...X", "X.XXX.", "......"])  # pound
G['€'] = (2, ["..XXX.", ".X...X", "X.....", "XXXX..", "X.....",
                   "XXXX..", "X.....", ".X...X", "..XXX.", "......"])  # euro
G['¥'] = (2, ["X....X", ".X..X.", "..XX..", "XXXXXX", "..XX..",
                   "XXXXXX", "..XX..", "..XX..", "..XX..", "......"])  # yen
G['°'] = (2, ["..XX..", ".X..X.", ".X..X.", "..XX.."])   # degree
G['×'] = (5, ["X....X", ".X..X.", "..XX..", ".X..X.", "X....X"])  # multiply
G['÷'] = (5, ["..XX..", "......", "XXXXXX", "......", "..XX.."])  # divide
G['±'] = (4, ["..XX..", "..XX..", "XXXXXX", "..XX..", "..XX..",
                   "......", "XXXXXX"])                       # plus-minus
G['≠'] = (4, ["....X.", "XXXXX.", "...X..", "..X...", ".XXXXX",
                   ".X...."])                                 # not equal
G['≤'] = (4, ["....XX", "..XX..", "XX....", "..XX..", "....XX",
                   "......", "XXXXXX"])                       # <=
G['≥'] = (4, ["XX....", "..XX..", "....XX", "..XX..", "XX....",
                   "......", "XXXXXX"])                       # >=
G['←'] = (5, ["..X...", ".X....", "XXXXXX", ".X....", "..X..."])  # left
G['→'] = (5, ["...X..", "....X.", "XXXXXX", "....X.", "...X.."])  # right
G['↑'] = (3, ["..XX..", ".XXXX.", "X.XX.X", "..XX..", "..XX..",
                   "..XX..", "..XX.."])                       # up
G['↓'] = (3, ["..XX..", "..XX..", "..XX..", "..XX..", "X.XX.X",
                   ".XXXX.", "..XX.."])                       # down
G['✓'] = (3, [".....X", ".....X", "....X.", "....X.", "X...X.",
                   "X...X.", ".X.X..", ".XXX..", "..X..."])        # check


# --- accented Latin-1: composed from a base glyph plus a mark ---------------
# The accent zone is rows 0..1 above caps and rows 2..3 above x-height, so a
# mark never collides with the letter it sits on.
MARKS = {
    "acute":  ["...XX.", "..XX.."],
    "grave":  [".XX...", "..XX.."],
    "circ":   ["..XX..", ".X..X."],
    "tilde":  [".XX..X", "X..XX."],
    "uml":    ["X...X.", "......"],
    "ring":   ["..XX..", "..XX.."],
    "caron":  [".X..X.", "..XX.."],
}


def accented(base, mark, cap):
    """Return a G entry: `base`'s bitmap with `mark` floated above it.

    cap=True places the mark in the cap accent zone (rows 0..1), otherwise in
    the x-height accent zone (rows 2..3).
    """
    top, rows = G[base]
    mark_top = 0 if cap else 2
    pad = top - (mark_top + len(MARKS[mark]))
    return (mark_top, MARKS[mark] + ["......"] * pad + list(rows))


for _ch, _base, _mark in [
    ('À', 'A', 'grave'), ('Á', 'A', 'acute'), ('Â', 'A', 'circ'),
    ('Ã', 'A', 'tilde'), ('Ä', 'A', 'uml'),   ('Å', 'A', 'ring'),
    ('È', 'E', 'grave'), ('É', 'E', 'acute'), ('Ê', 'E', 'circ'),
    ('Ë', 'E', 'uml'),   ('Ì', 'I', 'grave'), ('Í', 'I', 'acute'),
    ('Î', 'I', 'circ'),  ('Ï', 'I', 'uml'),   ('Ñ', 'N', 'tilde'),
    ('Ò', 'O', 'grave'), ('Ó', 'O', 'acute'), ('Ô', 'O', 'circ'),
    ('Õ', 'O', 'tilde'), ('Ö', 'O', 'uml'),   ('Ù', 'U', 'grave'),
    ('Ú', 'U', 'acute'), ('Û', 'U', 'circ'),  ('Ü', 'U', 'uml'),
    ('Ý', 'Y', 'acute'),
]:
    G[_ch] = accented(_base, _mark, cap=True)

for _ch, _base, _mark in [
    ('à', 'a', 'grave'), ('á', 'a', 'acute'), ('â', 'a', 'circ'),
    ('ã', 'a', 'tilde'), ('ä', 'a', 'uml'),   ('å', 'a', 'ring'),
    ('è', 'e', 'grave'), ('é', 'e', 'acute'), ('ê', 'e', 'circ'),
    ('ë', 'e', 'uml'),   ('ñ', 'n', 'tilde'),
    ('ò', 'o', 'grave'), ('ó', 'o', 'acute'), ('ô', 'o', 'circ'),
    ('õ', 'o', 'tilde'), ('ö', 'o', 'uml'),   ('ù', 'u', 'grave'),
    ('ú', 'u', 'acute'), ('û', 'u', 'circ'),  ('ü', 'u', 'uml'),
    ('ý', 'y', 'acute'), ('ÿ', 'y', 'uml'),
]:
    G[_ch] = accented(_base, _mark, cap=False)

# Dotless i takes the accent instead of a tittle.
G['ı'] = (4, ["..XX..", "..XX..", "..XX..", "..XX..", "..XX..",
                   "..XX..", "..XX..", ".XXXX."])
for _ch, _mark in [('ì', 'grave'), ('í', 'acute'),
                   ('î', 'circ'), ('ï', 'uml')]:
    G[_ch] = accented('ı', _mark, cap=False)

# Cedilla hangs below the baseline rather than floating above.
G['Ç'] = (2, ["..XXX.", ".X...X", "X.....", "X.....", "X.....",
                   "X.....", "X.....", "X.....", ".X...X", "..XXX.",
                   "...X..", "..XX.."])
G['ç'] = (4, [".XXXX.", "X....X", "X.....", "X.....", "X.....",
                   "X.....", "X....X", ".XXXX.", "...X..", "..XX.."])
G['Ø'] = (2, ["..XXX.", ".X..XX", "X...XX", "X..X.X", "X..X.X",
                   "X.X..X", "X.X..X", "XX...X", ".XX..X", "..XXX."])
G['ø'] = (4, [".XXXXX", "X...XX", "X..X.X", "X..X.X", "X.X..X",
                   "X.X..X", "XX...X", "XXXXX."])
G['ß'] = (2, [".XXXX.", "X....X", "X....X", "X.XXX.", "X....X",
                   "X....X", "X....X", "X....X", "X...X.", "X.XX.."])

# --- box drawing ------------------------------------------------------------
# Full-bleed 8-wide rows so segments meet exactly at cell edges. The vertical
# rule sits at cols 3..4 and the horizontal at rows 7..8, so single and double
# forms share a centre and can be mixed in one frame.
VROW = "...XX..."          # single vertical
DROW = "..X..X.."          # double vertical
BLANK = "........"
HBAR = "XXXXXXXX"
LEFT_H = "XXXX...."
RIGHT_H = "....XXXX"


def _box(rows_spec):
    """Build a full-bleed 16-row box glyph from a {row: pattern} mapping."""
    return (0, [rows_spec.get(r, BLANK) for r in range(16)])


def _vert(rows_spec, bar):
    """As _box, but fill every unspecified row with a vertical bar."""
    return (0, [rows_spec.get(r, bar) for r in range(16)])


# single
G['─'] = _box({7: HBAR, 8: HBAR})
G['│'] = _vert({}, VROW)
G['┌'] = _vert({**{r: BLANK for r in range(7)}, 7: RIGHT_H, 8: RIGHT_H}, VROW)
G['┐'] = _vert({**{r: BLANK for r in range(7)}, 7: LEFT_H, 8: LEFT_H}, VROW)
G['└'] = _vert({**{r: BLANK for r in range(9, 16)}, 7: RIGHT_H, 8: RIGHT_H}, VROW)
G['┘'] = _vert({**{r: BLANK for r in range(9, 16)}, 7: LEFT_H, 8: LEFT_H}, VROW)
G['├'] = _vert({7: RIGHT_H, 8: RIGHT_H}, VROW)
G['┤'] = _vert({7: LEFT_H, 8: LEFT_H}, VROW)
G['┬'] = _vert({**{r: BLANK for r in range(7)}, 7: HBAR, 8: HBAR}, VROW)
G['┴'] = _vert({**{r: BLANK for r in range(9, 16)}, 7: HBAR, 8: HBAR}, VROW)
G['┼'] = _vert({7: HBAR, 8: HBAR}, VROW)

# double
# Bars sit at cols 2 and 5 and rows 6 and 9, so the two strokes of a double
# line pass through each other's interior at a junction.
_DV = "..X..X.."          # both verticals
_DH = "XXXXXXXX"          # both horizontals (full bleed)
_DH_GAP = "XXX..XXX"      # horizontal interrupted where the verticals pass
_R_OUT = "..XXXXXX"       # from the left vertical rightward
_R_IN = "..X..XXX"        # left vertical + inner run rightward
_L_OUT = "XXXXXX.."       # from the right vertical leftward
_L_IN = "XXX..X.."        # inner run leftward + right vertical
_V_L = "..X....."         # left vertical only
_V_R = ".....X.."         # right vertical only

G['═'] = _box({6: _DH, 9: _DH})
G['║'] = _vert({}, _DV)
G['╔'] = (0, [BLANK]*6 + [_R_OUT, _V_L, _V_L, _R_IN] + [_DV]*6)
G['╗'] = (0, [BLANK]*6 + [_L_OUT, _V_R, _V_R, _L_IN] + [_DV]*6)
G['╚'] = (0, [_DV]*6 + [_R_IN, _V_L, _V_L, _R_OUT] + [BLANK]*6)
G['╝'] = (0, [_DV]*6 + [_L_IN, _V_R, _V_R, _L_OUT] + [BLANK]*6)
G['╠'] = (0, [_DV]*6 + [_R_IN, _V_L, _V_L, _R_IN] + [_DV]*6)
G['╣'] = (0, [_DV]*6 + [_L_IN, _V_R, _V_R, _L_IN] + [_DV]*6)
G['╦'] = (0, [BLANK]*6 + [_DH, _DV, _DV, _DH_GAP] + [_DV]*6)
G['╩'] = (0, [_DV]*6 + [_DH_GAP, _DV, _DV, _DH] + [BLANK]*6)
G['╬'] = (0, [_DV]*6 + [_DH_GAP, _DV, _DV, _DH_GAP] + [_DV]*6)

# --- block elements ---------------------------------------------------------
G['█'] = (0, [HBAR] * 16)
G['▀'] = (0, [HBAR] * 8)
G['▄'] = (8, [HBAR] * 8)
G['▌'] = (0, ["XXXX...."] * 16)
G['▐'] = (0, ["....XXXX"] * 16)
G['▪'] = (6, [".XXXX...", ".XXXX...", ".XXXX...", ".XXXX..."])
G['░'] = shade(GRID, lambda x, y: x % 2 == 0 and y % 2 == 0)
G['▒'] = shade(GRID, lambda x, y: (x + y) % 2 == 0)
G['▓'] = shade(GRID, lambda x, y: not (x % 2 == 0 and y % 2 == 0))

# Box and block characters must keep exact cell geometry, so they are never
# emboldened -- a smear would break the connections between cells.
NO_BOLD = set("─│┌┐└┘├┤┬┴┼═║╔╗╚╝╠╣╦╩╬█▀▄▌▐░▒▓—_")

# ------------------------------------------------------------- originality --
# Only Departure Mono is compared: font8x8 is an 8x8 ROM face, and cropping an
# 8-row glyph against a 16-row one produces a similarity number that means
# nothing. Departure Mono is a genuine pixel monospace and the closest relative.
# The allow-set below is what a run actually reports -- shapes with essentially
# one solution on a pixel grid. Anything outside it fails CI.
COMPARE = {
    "refs": {
        "departure.otf":
            "https://raw.githubusercontent.com/rektdeckard/departure-mono/main/"
            "public/assets/DepartureMono-Regular.otf",
    },
    # The ellipsis is three dots on a baseline -- there is no other way to
    # draw it on a pixel grid, so a match there is unavoidable, not derivative.
    "allowed": {"Departure Mono": set("\u2026")},
}

# ---------------------------------------------------------------- specimen --
SPECIMEN = {
    "tagline": "AN OPEN-SOURCE 8×16 PIXEL MONOSPACE • SIL OFL 1.1",
    "lines": [
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "abcdefghijklmnopqrstuvwxyz",
        "0123456789 ¢$€£¥ #%&@*+=<>/\\",
        "Grüße aus Zürich — café naïve piñata",
        "Sphinx of black quartz, judge my vow.",
    ],
    "bold_line": "Bold for emphasis: 240 items · €1,284.00",
    "sample": """┌─ register ───────────────────┐
│ [b]inbox[/b]        12 unread       │
│ notes         4 drafts       │
│ archive     318 items        │
├──────────────────────────────┤
│ def parse(line: str) -> int: │
│     x = line.split("=")[1]   │
│     return int(x) ≠ 0        │
└──────────────────────────────┘""",
    "tester": "The quick brown fox jumps over the lazy dog ✓",
}
