# -*- coding: utf-8 -*-
"""Turn ASCII bitmaps into a compiled TrueType/WOFF2 font.

Everything here is parameterised by a Grid, so the same code compiles an 8x12
receipt face and an 8x16 text face without special cases.
"""
import os
import shutil

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib.tables.O_S_2f_2 import Panose

from .trace import trace, glyph_name


def shade(grid, keep):
    """Return a full-bleed G entry filled wherever keep(x, y) is true."""
    return (0, ["".join("X" if keep(x, y) else "." for x in range(grid.cols))
                for y in range(grid.rows)])


def validate(grid, glyphs, notdef):
    """Assert every bitmap fits the cell and uses only legal row widths."""
    for ch, (top, rows) in list(glyphs.items()) + [("<notdef>", notdef)]:
        assert 0 <= top and top + len(rows) <= grid.rows, f"{ch!r}: bad row span"
        for r in rows:
            assert len(r) in grid.widths, f"{ch!r}: bad row width {len(r)}"
            assert set(r) <= {'X', '.'}, f"{ch!r}: bad chars"


def pixels_of(grid, top, rows):
    """Return set of (x, gy) pixel coords. gy is y-up: gy = baseline_row - row."""
    pts = set()
    for i, row in enumerate(rows):
        off = 1 if len(row) == grid.inset_width else 0
        r = top + i
        for j, ch in enumerate(row):
            if ch == 'X':
                pts.add((j + off, grid.baseline_row - r))
    return pts


def embolden(grid, pts, wide):
    """Return pts dilated one column right to fake weight.

    wide suppresses the smear into the last column, so glyphs that already
    reach it keep a sliver of right sidebearing instead of touching the next
    character.
    """
    edge = grid.cols - 1
    out = set(pts)
    for (x, y) in pts:
        if x + 1 <= edge:
            out.add((x + 1, y))
    if wide:
        out = {(x, y) for (x, y) in out if not (x == edge and (edge, y) not in pts)}
        out |= {(x, y) for (x, y) in pts}
    return out


def build(font, style="Regular", outdir=None, root=None):
    """Compile one style of one font to TTF + WOFF2; return the TTF path.

    `font` is a module exposing GRID, IDENTITY, G, NOTDEF and NO_BOLD.
    outdir=None writes the tracked repo layout (fonts/<slug>/ttf, .../webfonts
    and docs/fonts/<slug>); any path writes every artifact to that directory.
    """
    grid, ident = font.GRID, font.IDENTITY
    glyphs, notdef, no_bold = font.G, font.NOTDEF, font.NO_BOLD

    validate(grid, glyphs, notdef)
    bold = style == "Bold"
    order = [".notdef"]
    cmap, glyf, metrics = {}, {}, {}

    def compile_glyph(name, top, rows, ch=None):
        """Trace one bitmap into the enclosing glyf/metrics dicts.

        ch=None skips the NO_BOLD lookup, used for .notdef.
        """
        pts = pixels_of(grid, top, rows)
        if bold and pts and (ch is None or ch not in no_bold):
            wide = any(len(r) == grid.wide_width for r in rows)
            pts = embolden(grid, pts, wide)
        pen = TTGlyphPen(None)
        for contour in trace(pts, grid.px):
            pen.moveTo(contour[0])
            for p in contour[1:]:
                pen.lineTo(p)
            pen.closePath()
        glyf[name] = pen.glyph()
        lsb = min((x for x, _ in pts), default=0) * grid.px
        metrics[name] = (grid.advance, lsb)

    compile_glyph(".notdef", *notdef)
    for ch in sorted(glyphs, key=ord):
        name = glyph_name(ch)
        order.append(name)
        cmap[ord(ch)] = name
        compile_glyph(name, *glyphs[ch], ch=ch)
    # render NBSP with the space glyph instead of .notdef
    cmap[0x00A0] = "space"

    fb = FontBuilder(grid.em, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(glyf)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=grid.ascent, descent=-grid.descent)

    ps = ident.ps_name(style)
    fb.setupNameTable({
        "familyName": ident.family,
        "styleName": style,
        "uniqueFontIdentifier": f"{ident.version};{ident.vendor_id};{ps}",
        "fullName": f"{ident.family} {style}",
        "psName": ps,
        "version": f"Version {ident.version}",
        "copyright": ident.copyright,
        "designer": ident.author,
        "designerURL": ident.repo,
        "vendorURL": ident.repo,
        "description": ident.description,
        "licenseDescription": ("This Font Software is licensed under the SIL "
                               "Open Font License, Version 1.1."),
        "licenseInfoURL": "https://openfontlicense.org",
    })

    panose = Panose()
    panose.bFamilyType = 2
    panose.bProportion = 9          # monospaced
    fb.setupOS2(sTypoAscender=grid.ascent, sTypoDescender=-grid.descent,
                sTypoLineGap=0,
                usWinAscent=grid.ascent, usWinDescent=grid.descent,
                sCapHeight=grid.cap_height, sxHeight=grid.x_height,
                usWeightClass=700 if bold else 400,
                achVendID=ident.vendor_id, fsType=0, panose=panose,
                xAvgCharWidth=grid.advance)
    os2 = fb.font["OS/2"]
    os2.fsSelection = 0x20 if bold else 0x40
    fb.font["head"].macStyle = 0x1 if bold else 0x0
    # Machine-readable version; OSes key font-cache invalidation on this,
    # so it has to move whenever the outlines do.
    fb.font["head"].fontRevision = float(ident.version)
    fb.setupPost(isFixedPitch=1, underlinePosition=-150, underlineThickness=100)

    if outdir is None:
        root = root or os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))))
        ttf_dir = os.path.join(root, "fonts", ident.slug, "ttf")
        woff2_dirs = [os.path.join(root, "fonts", ident.slug, "webfonts"),
                      os.path.join(root, "docs", "fonts", ident.slug)]
    else:
        ttf_dir, woff2_dirs = outdir, [outdir]

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
