# -*- coding: utf-8 -*-
"""Shared machinery for building pixel-grid typefaces.

A font is a Grid (cell geometry), an Identity (naming) and a dict of ASCII
bitmaps. Everything else -- contour tracing, emboldening, TrueType assembly --
lives here and is font-agnostic.
"""
from .grid import Grid, Identity
from .trace import trace, glyph_name
from .compile import build, validate, pixels_of, embolden, shade

__all__ = ["Grid", "Identity", "trace", "glyph_name",
           "build", "validate", "pixels_of", "embolden", "shade"]
