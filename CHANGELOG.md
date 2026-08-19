# Changelog

## Unreleased

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
