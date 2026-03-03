"""
NSM Core - Natural Semantic Metalanguage + Glyph81567
======================================================
Universal semantic primitives integrated with base-144k computational language.

Main exports:
- NSM_PRIMES: Dictionary of 65 semantic primitives
- GLYPH_NSM_MAPPING: 10 fundamental glyphs
- FSOU: Semantic composition engine
- FSOUComposer: Factory for creating FSOUs
"""

from nsm_core.nsm_primitives import NSM_PRIMES, NSMCategory, NSMPrimitive
from nsm_core.glyph_nsm_mapping import GLYPH_NSM_MAPPING, get_nsm_primes_for_glyph
from nsm_core.nsm_expansion_phase2 import EXTENDED_GLYPH_SET, get_all_glyphs
from nsm_core.fsou_composer import FSOU, FSOUComposer, EXAMPLE_FSOOUS

__version__ = "2.0.0"
__all__ = [
    "NSM_PRIMES",
    "NSMCategory",
    "NSMPrimitive",
    "GLYPH_NSM_MAPPING",
    "EXTENDED_GLYPH_SET",
    "get_all_glyphs",
    "get_nsm_primes_for_glyph",
    "FSOU",
    "FSOUComposer",
    "EXAMPLE_FSOOUS",
]
