<p align="center">
  <img src="docs/receipt_demo.png" alt="A 1986-style video store receipt set in Till Mono" width="560">
</p>

<h1 align="center">Till Fonts</h1>

<p align="center">
  <em>A family of original open-source pixel typefaces.</em><br><br>
  <img alt="License: OFL-1.1" src="https://img.shields.io/badge/license-OFL--1.1-blue">
  <img alt="Fonts" src="https://img.shields.io/badge/fonts-2-orange"><br><br>
  <a href="https://thijsvos.github.io/till-fonts/"><strong>Live specimen &amp; type tester &rarr;</strong></a>
</p>

Every glyph in every face is drawn by hand on a pixel grid as ASCII art in a Python
source file, then traced to TrueType outlines by code in this repo. No font was ever
opened, traced or converted.

## The fonts

| Font | Grid | Glyphs | Styles | For |
|---|---|---|---|---|
| **[Till Mono](fonts/till-mono/)** | 8×12 | 148 | Regular + Bold | Receipts, labels, terminal UIs. Square and deliberately retro; box drawing that connects seamlessly. Pixel-perfect at multiples of 12px. |
| **[Till Text](fonts/till-text/)** | 10×16 | 208 | Regular + Bold | UI, body copy and code. Neutral, with a large x-height and full Latin-1 accents. Pixel-perfect at multiples of 16px — the web's default body size. |

*A till is a cash register — the family is named for where the first face belongs.*

## Install

Grab the TTFs from the **[latest release](https://github.com/thijsvos/till-fonts/releases/latest)**
— or from `fonts/<name>/ttf/` — and install them like any other font: double-click →
Install.

**macOS: if the font doesn't appear after installing**, the download is quarantined.
Safari/Chrome tag downloaded files with `com.apple.quarantine`, and Font Book copies
the tag into `~/Library/Fonts/` — the font installs, reports `valid=yes`, and is still
skipped by the font registry, so it never shows up in any font picker. Clear it:

```sh
xattr -d com.apple.quarantine ~/Library/Fonts/Till*.ttf
```

The font appears within a few seconds; no logout or cache reset needed. This is a macOS
download-security behaviour, not a problem with the font.

Release assets carry [build provenance](https://docs.github.com/actions/security-guides/using-artifact-attestations),
so you can verify a download really came from this repo's CI:

```sh
gh attestation verify TillMono-Regular.ttf --repo thijsvos/till-fonts
```

## Use on the web

Each font ships a drop-in stylesheet next to its WOFF2s:

```html
<link rel="stylesheet" href="fonts/till-mono/webfonts/till-mono.css">
```

Or hotlink via jsDelivr, pinned to a release tag — no install, no build step:

```css
src: url("https://cdn.jsdelivr.net/gh/thijsvos/till-fonts@v2.1.1/fonts/till-mono/webfonts/TillMono-Regular.woff2") format("woff2");
```

You can also depend on the whole family from another project:

```sh
npm install github:thijsvos/till-fonts   # fonts land in node_modules/till-fonts/fonts
git submodule add https://github.com/thijsvos/till-fonts vendor/till-fonts
```

## Build from source

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install --require-hashes -r requirements.txt   # CI builds on Python 3.14

# Pins the fonts' internal timestamps so rebuilds are byte-identical.
# CI uses this exact value — build without it and your fonts will look "changed".
export SOURCE_DATE_EPOCH=1787097600

python src/build_all.py         # every font -> fonts/<name>/, docs/fonts/<name>/
python src/proof.py             # contact sheet of every glyph, per font
python src/render_previews.py   # specimen + receipt images
python src/compare.py           # originality check (downloads reference fonts)
```

The built fonts are committed, and CI rebuilds on every push and fails if they differ
from source — so a glyph edit must be committed together with its rebuilt fonts.

## How a font is put together

Each typeface is one module under [`src/fonts/`](src/fonts) declaring its grid, its
identity and its glyph bitmaps. Everything else — contour tracing, emboldening,
TrueType assembly — is shared machinery in [`src/pixelfont/`](src/pixelfont).

A glyph is an ASCII bitmap; `X` is a pixel, `.` is empty, and the number is the top row:

```python
G['A'] = (1, ["..XX..",
              ".X..X.",
              "X....X",
              "X....X",
              "XXXXXX",
              "X....X",
              "X....X",
              "X....X"])
```

Flip some pixels, rebuild, done. Bold is generated automatically by thickening strokes
one pixel. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Originality

Every outline is original. Because pixel grids force convergent solutions,
[`src/compare.py`](src/compare.py) diffs every glyph against reference pixel fonts on
every push, and **fails CI** if any glyph becomes byte-identical to a reference outside a
small allow-list of single-solution shapes (a rule for underscore, a cross for plus, the
obvious box corners). Current results for Till Mono:

**Till Mono** (8×12, compared against an 8×8 ROM font and Departure Mono):

| Reference | Shared glyphs | Identical bitmaps |
|---|---|---|
| font8x8 (IBM-style 8×8 ROM) | 94 | 1 — `_` |
| Departure Mono | 144 | 12 — ``! * + , = T ` × ÷ – ┌ ╔`` |

**Till Text** (10×16, compared against Departure Mono only — an 8×8 ROM font is
not a meaningful comparison for a 16-row face):

| Reference | Shared glyphs | Identical bitmaps | Mean IoU |
|---|---|---|---|
| Departure Mono | 205 | **0** | 0.36 |

**No letter or digit matches any reference in either face.** Every collision is a
shape with essentially one solution on a pixel grid — a rule for underscore, a
cross for plus, the obvious box corners. Till Text has no collisions at all.

## License

Till Fonts is licensed under the [SIL Open Font License 1.1](OFL.txt) — free for
commercial use, embedding, bundling, modification and redistribution. No Reserved Font
Name is declared, but if you fork a face into something new, picking a new name keeps
things unconfusing.
