# Changelog

## 1.0.2 — 2026-08-19

Bold fix. Regular is unchanged and byte-identical to 1.0.0.

- **Fixed:** the 9 glyphs with 7-px-wide rows (`M W m w # % & @ ☺`) had no right
  sidebearing in Bold, so they touched the following character — `MMM` and `WWW`
  rendered as a fused mass. `embolden()`'s guard against this was dead code.
- Corrected documentation: the build command in `build_till_mono.py`'s module
  docstring omitted `SOURCE_DATE_EPOCH`; the claim that pillow is safe to bump
  alone was wrong (it rasterises the originality check's reference font)
- Added docstrings to the functions that warrant them; dropped an unused parameter

## 1.0.1 — 2026-08-19

No font changes — the binaries are byte-identical to 1.0.0.

- Build toolchain pinned exactly and hash-verified (`pip --require-hashes`), so
  reproducibility covers the compiler, not just the timestamp
- GitHub Actions moved to Node 24 runtimes ahead of the runner deprecation, and
  all five actions pinned to commit SHAs
- Release assets carry build provenance attestation
- Originality comparison (`src/compare.py`) now asserts and runs in CI
- CI builds on Python 3.14 (verified to produce byte-identical fonts)
- Dependabot configured for Actions and pip; security alerts enabled

## 1.0.0 — 2026-08-19

Initial release.

- Regular + Bold, 148 glyphs each
- Printable ASCII, slashed zero, currency (¢ £ € ¥), math (° × ÷),
  typographic marks (– — ' ' " " • …), arrows, ✓ ☺
- Single + double box drawing, block and shade elements
- TTF + WOFF2 builds, Python build pipeline (fontTools)
- Verification tooling (`src/compare.py`) and glyph proof sheet
