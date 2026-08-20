# -*- coding: utf-8 -*-
"""Boundary tracing and PostScript glyph naming.

Both are font-agnostic: trace() marches any set of unit pixels into closed
TrueType contours, and glyph_name() maps a character to its AGL name.
"""

RIGHT = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}
LEFT = {v: k for k, v in RIGHT.items()}

def trace(pts, px):
    """March the pixel boundary into closed contours, scaled by px.

    Filled area stays on the right of travel: clockwise outers,
    counter-clockwise holes, TrueType style.
    """
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
        contours.append([(x * px, y * px) for (x, y) in simp])
    return contours

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
    """Return the AGL/PostScript glyph name for ch, falling back to uniXXXX."""
    if ch in AGL:
        return AGL[ch]
    if ch.isascii() and ch.isalnum():
        return ch if ch.isalpha() else "zero one two three four five six seven eight nine".split()[int(ch)]
    return "uni%04X" % ord(ch)
