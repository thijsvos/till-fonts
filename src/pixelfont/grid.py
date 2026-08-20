# -*- coding: utf-8 -*-
"""Cell geometry and naming for a pixel typeface."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Grid:
    """The pixel cell a typeface is drawn on.

    Rows are numbered 0..rows-1 top to bottom. The baseline sits directly under
    ``baseline_row``, so a pixel on that row has its bottom edge at y=0 and
    everything below it descends. All vertical metrics derive from that, which
    keeps ascent + descent == em by construction.

    Row strings may be ``cols``, ``cols-1`` or ``cols-2`` characters wide. The
    narrowest form is inset one column from the left, giving normal glyphs a
    sidebearing on both sides; the full-width form bleeds edge to edge so box
    drawing connects between cells.
    """

    cols: int
    rows: int
    baseline_row: int
    cap_top_row: int
    x_top_row: int
    px: int = 100          # font units per pixel

    @property
    def em(self):
        return self.rows * self.px

    @property
    def advance(self):
        return self.cols * self.px

    @property
    def ascent(self):
        return (self.baseline_row + 1) * self.px

    @property
    def descent(self):
        return (self.rows - self.baseline_row - 1) * self.px

    @property
    def cap_height(self):
        return (self.baseline_row + 1 - self.cap_top_row) * self.px

    @property
    def x_height(self):
        return (self.baseline_row + 1 - self.x_top_row) * self.px

    @property
    def widths(self):
        """Legal row-string widths: inset, wide, and full-bleed."""
        return (self.cols - 2, self.cols - 1, self.cols)

    @property
    def inset_width(self):
        """Row width that gets shifted one column right."""
        return self.cols - 2

    @property
    def wide_width(self):
        """Row width that reaches the right edge but should keep a sidebearing
        when emboldened."""
        return self.cols - 1

    def __post_init__(self):
        if not 0 <= self.baseline_row < self.rows:
            raise ValueError("baseline_row outside the cell")
        if self.ascent + self.descent != self.em:
            raise ValueError("ascent + descent must equal em")


@dataclass(frozen=True)
class Identity:
    """Everything that names a typeface, in the binary and on disk."""

    family: str                # "Till Mono"
    ps_prefix: str             # "TillMono" -- drives psName AND every filename
    slug: str                  # "till-mono" -- directory name
    version: str               # "1.003"
    description: str
    author: str = "Thijs Vos"
    repo: str = "https://github.com/thijsvos/till-fonts"
    vendor_id: str = "TILL"    # 4-char foundry id, shared across the family

    @property
    def copyright(self):
        return f"Copyright 2026 {self.author} ({self.repo})"

    def ps_name(self, style):
        return f"{self.ps_prefix}-{style}"
