# Contributing

Each typeface lives in one module under `src/fonts/`, declaring its grid, its identity
and its glyph bitmaps. The shared machinery — contour tracing, emboldening, TrueType
assembly — is in `src/pixelfont/` and is grid-agnostic, so a new face is data plus a
`Grid`, not new code.

Glyphs are ASCII pixel maps: `X` on, `.` off, rows numbered from the top, with the
baseline sitting under `GRID.baseline_row`. Row strings may be `cols-2` wide (inset one
column, giving a sidebearing on both sides), `cols-1`, or the full `cols` for box and
block characters that must connect edge to edge.

## Editing a glyph

1. `python3 -m venv .venv && . .venv/bin/activate && pip install --require-hashes -r requirements.txt`
2. `export SOURCE_DATE_EPOCH=1787097600` — pins the fonts' internal timestamps so
   rebuilds are byte-identical. CI uses this exact value; without it your rebuilt fonts
   differ from everyone else's and the build fails.
3. Edit the bitmaps, then `python src/build_all.py`. This writes straight into
   `fonts/<name>/` and `docs/fonts/<name>/` — **commit those rebuilt fonts with your
   change**, since CI rebuilds and fails on any drift.
4. `python src/proof.py` and eyeball `proof_sheet_<name>.png`
5. `python src/render_previews.py`, and copy any changed PNGs into `docs/`
6. `python src/compare.py` must still pass — it fails if a glyph becomes byte-identical
   to a reference pixel font outside the documented allow-list
7. Open a pull request that includes the updated proof sheet

## Adding a font

Copy `src/fonts/till_mono.py` as a starting point and give it its own `GRID`,
`IDENTITY`, `G`, `NOTDEF`, `NO_BOLD`, `SPECIMEN` and `COMPARE`. Then add its module name
to `FONTS` in `src/build_all.py` — that list drives the build, the manifest, the
specimen page's switcher, CI attestation and the release assets, so nothing else needs
editing.

Pick references for `COMPARE` that share the new grid's proportions; an 8×8 ROM font is
not a meaningful comparison for a 16-row face. Run `python src/compare.py`, read the
reported identical sets, and record the genuinely single-solution shapes as the
allow-set — with a note explaining why each is unavoidable.

## Bumping the build toolchain

`requirements.txt` pins `fonttools` and `brotli` to exact versions on purpose. The
compiled font bytes are a function of those two libraries — brotli alone is ~98% of every
`.woff2` payload — so a version change rewrites the binaries even when no glyph changed.
Bumping either one therefore **requires rebuilding and committing the fonts in the same
commit**, or CI's drift guard will fail.

`pillow` renders the proof PNGs, which CI does not diff — but it *also* rasterises the
Departure Mono reference in `src/compare.py`, so a bump can move the originality check.
Review a pillow bump against a green `originality` job before merging.

`requirements.txt` is hash-pinned and generated — don't hand-edit the hashes. Change the
versions in `src/gen_requirements.py` and re-run it.

## Versions

Versioning is per-font. Each face carries its own `version` in its `Identity`, which
becomes its name-table version and `head.fontRevision`. That is what OS font caches key
on, so it moves **only when that font's outlines move** — fixing a glyph in one face must
not invalidate every other face for users.

Separately, `package.json` and the git tag version the *collection*: the bundle people
download. The README's jsDelivr examples pin a tag, so they track it.

`python src/check_versions.py` enforces all of this and runs in CI on every push, and
again against the tag on release.

To release the collection as `X.Y.Z`:

1. Bump any font whose outlines changed (`version=` in its `Identity`) and rebuild
2. Set `"version": "X.Y.Z"` in `package.json`
3. Update the jsDelivr pins in `README.md` to `@vX.Y.Z`
4. `python src/check_versions.py` must pass, then tag `vX.Y.Z`

Please keep new glyphs original — don't paste bitmaps from other fonts, even open-source
ones, so the provenance story in the README stays true.
