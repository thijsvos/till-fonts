# Contributing

Glyphs are ASCII pixel maps in `src/build_till_mono.py` — `X` on, `.` off,
rows 0–11 top to bottom with the baseline under row 8. Standard glyphs draw
in columns 1–6; box/block characters bleed across the full 0–7 cell so they
connect between lines.

To propose a change:

1. `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt`
2. `export SOURCE_DATE_EPOCH=1787097600` — pins the font's internal timestamp
   so rebuilds are byte-identical. CI uses this exact value; without it your
   rebuilt fonts differ from everyone else's and the build fails.
3. Edit the bitmaps, then `python src/build_till_mono.py`. This writes straight
   into `fonts/ttf/`, `fonts/webfonts/` and `docs/fonts/` — **commit those
   rebuilt fonts with your change**, since CI rebuilds and fails on any drift.
4. `python src/proof.py` and eyeball `proof_sheet.png`
5. Regenerate the docs images with `python src/render_previews.py` and copy
   the PNGs into `docs/` if they changed
6. Open a pull request that includes the updated proof sheet

Please keep new glyphs original — don't paste bitmaps from other fonts, even
open-source ones, so the provenance story in the README stays true.
