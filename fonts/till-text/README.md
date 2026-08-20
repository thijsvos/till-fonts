# Till Text

An original 8×16 pixel monospace for user interfaces, body copy and code.
Part of [Till Fonts](https://github.com/thijsvos/till-fonts).

Where [Till Mono](../till-mono/) is square and deliberately retro, Till Text is the
general-purpose face. It takes its cues from Commit Mono's thesis — that a working
typeface should be unremarkable — and transfers what survives on a pixel grid: a large
x-height, uniform stroke weight and flat terminals.

- **208 glyphs** — printable ASCII, Latin-1 accents (`é à ü ñ ç ø ß …`), typographic
  marks, currency, maths (`± ≤ ≥ ≠ × ÷`), arrows, box drawing and blocks
- **Large x-height** — 800 of a 1000 cap height, the ratio that keeps small text legible
- **Regular + Bold**, monospaced at an 8 px advance
- **Pixel-perfect at multiples of 16 px**, which is the web's default body size

## Install

Double-click `ttf/TillText-Regular.ttf` → Install. On macOS, if it doesn't appear:
`xattr -d com.apple.quarantine ~/Library/Fonts/TillText-*.ttf`

## Web

```html
<link rel="stylesheet" href="webfonts/till-text.css">
```

```css
body {
  font-family: "Till Text", monospace;
  font-size: 16px;   /* multiples of 16px render pixel-perfect */
  line-height: 1.5;
}
```

Licensed under the [SIL Open Font License 1.1](../../OFL.txt).
