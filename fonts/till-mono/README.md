# Till Mono

An original 8×12 pixel monospace for 1980s-style receipts, labels and terminal UIs.
Part of [Till Fonts](https://github.com/thijsvos/till-fonts).

- **148 glyphs** — printable ASCII, slashed zero, `¢ £ € ¥ ° × ÷ • – — … ✓ ☺`, arrows
- **Box drawing**, single and double, that connects seamlessly across lines
- **Block and shade elements** `█ ▀ ▄ ▌ ▐ ░ ▒ ▓ ▪`
- **Regular + Bold**, monospaced at an 8 px advance
- **Pixel-perfect** at font sizes that are multiples of 12 px

## Install

Double-click `ttf/TillMono-Regular.ttf` → Install. On macOS, if it doesn't appear:
`xattr -d com.apple.quarantine ~/Library/Fonts/TillMono-*.ttf`

## Web

```html
<link rel="stylesheet" href="webfonts/till-mono.css">
```

```css
.receipt {
  font-family: "Till Mono", monospace;
  font-size: 24px;   /* multiples of 12px render pixel-perfect */
  line-height: 1;    /* makes │ ║ █ connect vertically */
}
```

## Receipt & label printing

- Label printers (Dymo, Brother, Zebra…) expose a normal font picker — just choose Till
  Mono. Thermal heads are ~203 dpi; **8.7 pt (24 px)** or **13 pt (36 px)** map cleanly
  to printer dots.
- For ESC/POS receipt printers, render text to a 1-bit bitmap with this font (Python +
  Pillow works well) and send it as a raster image.
- Lay out the classic way: pad columns with spaces (58 mm paper ≈ 32 chars, 80 mm ≈ 48
  at 24 px) and rule sections with `─` or `═`.

Licensed under the [SIL Open Font License 1.1](../../OFL.txt).
