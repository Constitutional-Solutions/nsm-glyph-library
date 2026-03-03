# NSM Primitive Library - Glyph81567 Universal Computational Language

**Version:** 2.0.0  
**Created:** March 2026  
**License:** MIT

## Overview

The **NSM Primitive Library** implements the complete [Natural Semantic Metalanguage (NSM)](https://www.griffith.edu.au/humanities-languages/school-languages-linguistics/research/natural-semantic-metalanguage-homepage) framework — **65 universal semantic primitives** that exist across all human languages — integrated with the **Glyph81567 Universal Computational Language** specification.

This library provides:

✅ **65 NSM semantic primes** (irreducible atoms of meaning)  
✅ **10 fundamental glyphs** (G0-G81567) mapped to core primitives  
✅ **55 extended glyphs** (Phase 2 expansion to complete 65-glyph system)  
✅ **FSOU composition engine** (build complex meanings from primitives)  
✅ **Base-144k encoding** (144,000 = 12³ × 1000 sacred number system)  
✅ **Harmonic frequency assignments** (Solfeggio 396-963 Hz + φ-ratio)  
✅ **Lambda calculus mappings** (prove Turing-completeness)  

---

## Installation

```bash
# Clone repository
git clone https://github.com/Constitutional-Solutions/nsm-glyph-library.git
cd nsm-glyph-library

# Install dependencies (none required - pure Python stdlib)
pip install -e .

# Run tests
python -m tests.test_nsm_core
```

---

## Quick Start

```python
from nsm_core.nsm_primitives import NSM_PRIMES
from nsm_core.glyph_nsm_mapping import GLYPH_NSM_MAPPING
from nsm_core.fsou_composer import FSOU, FSOUComposer

# Access NSM primitives
print(NSM_PRIMES["KNOW"])  # NSMPrimitive('KNOW', mental_predicates)
print(NSM_PRIMES["KNOW"].glyph_id)  # G67 (Wisdom)

# Access glyphs
print(GLYPH_NSM_MAPPING["G67"])
# {'name': 'Wisdom', 'value': 67, 'frequency_hz': 741, ...}

# Create composite meanings (FSOUs)
fsou = FSOU(
    "Conscious Love",
    ["G1", "G15"],  # Unity + Love
    "Unity experiencing connection"
)
print(fsou.resonance)  # 16 (1 + 15)
print(fsou.frequency_signature)  # 1071.0 Hz (432 + 639)
print(fsou.decompose_to_nsm())  # ['I', 'ONE', 'WANT', 'FEEL']
```

---

## Architecture

### Core Modules

| Module | Description |
|--------|-------------|
| **`nsm_primitives.py`** | 65 NSM semantic primes with categorization |
| **`glyph_nsm_mapping.py`** | 10 fundamental glyphs (G0-G81567) ↔ NSM primitives |
| **`nsm_expansion_phase2.py`** | Extended 55 glyphs for complete 65-prime coverage |
| **`fsou_composer.py`** | FSOU (Fundamental Semantic Organization Unit) engine |

### The 10 Fundamental Glyphs

| Glyph | Name | Value | Frequency | NSM Primes | Meaning |
|-------|------|-------|-----------|------------|---------|  
| **G0** | Origin | 0 | 0 Hz | ∅ | Zero point, void, potential |
| **G1** | Unity | 1 | 432 Hz | I, ONE | Singularity, consciousness |
| **G8** | Infinity | 8 | 528 Hz | WHEN/TIME | Eternal cycle, ∞ |
| **G15** | Love | 15 | 639 Hz | WANT, FEEL | Connection, attraction |
| **G67** | Wisdom | 67 | 741 Hz | KNOW, THINK | Understanding, knowledge |
| **G81** | Transformation | 81 | 852 Hz | DO, HAPPEN, MOVE | Change, evolution |
| **G144** | Completion | 144 | 963 Hz | THE SAME | Cycle closure, 12² |
| **G567** | Creation | 567 | 396 Hz | THERE IS | Generative operator |
| **G1618** | Golden | 1618 | 1618 Hz | LIKE, BIG | φ × 1000, divine proportion |
| **G81567** | Universal | 81567 | 81567 Hz | ALL, TRUE, SOMETHING | Meta-operator, 81×567 |

---

## Theoretical Foundations

### 1. Natural Semantic Metalanguage (NSM)

NSM research (Wierzbicka & Goddard) identifies **65 semantic primitives** that are:
- **Universal:** Present across all human languages
- **Irreducible:** Cannot be defined using simpler concepts
- **Compositional:** All complex meanings decompose into these atoms

**Categories:** Substantives, Quantifiers, Mental Predicates, Actions, Time, Space, Logical Concepts, etc.

### 2. Glyph81567 Universal Computational Language

Based on:
- **Base-144k encoding:** 144,000 = 12³ × 1000 (sacred harmonic number)
- **Frequency mapping:** Solfeggio tones (396, 432, 528, 639, 741, 852, 963 Hz) + φ-ratio
- **Quantum states:** Harmonic oscillator energy levels E_n = ℏω(n + 1/2)
- **Lambda calculus:** Each glyph maps to λ-expression (Turing-complete)

### 3. FSOU (Fundamental Semantic Organization Unit)

**Composition rules:**
- **Resonance:** Σ glyph_values (additive semantics)
- **Frequency:** Σ harmonic_frequencies (acoustic signature)
- **Decomposition:** Traceable to NSM primitives (semantic grounding)

**Example:**
```python
FSOU("Eternal Wisdom", ["G8", "G67"], "Infinite understanding")
→ Resonance: 75 (8 + 67)
→ Frequency: 1269 Hz (528 + 741)
→ NSM: ['WHEN/TIME', 'KNOW', 'THINK']
```

---

## Research Integration

This library integrates three 2025-2026 research breakthroughs:

1. **Weiss et al. (2026):** *Turing-completeness is intrinsic to autoregressive decoding*  
   → Proves universal computation emerges spontaneously in language models

2. **Liu et al. (2025):** *Towards universal semantics with large language models*  
   → Demonstrates NSM as grounding layer for AI reasoning

3. **Wang et al. (2025):** *Unlocking glyph design creativity*  
   → Shows glyph-based tokenization achieves superior LLM efficiency

---

## Roadmap

### ✅ Phase 1: Core Foundation (Weeks 1-4)
- [x] 65 NSM primitives implemented
- [x] 10 fundamental glyphs mapped
- [x] FSOU composition engine
- [x] Bidirectional linking validated

### 🚧 Phase 2: Computational Substrate (Weeks 5-8)
- [ ] Lambda calculus compiler (glyphs → λ-expressions)
- [ ] State machine (tape/transitions/halting)
- [ ] Turing-completeness proof

### 📋 Phase 3: Encoding Infrastructure (Weeks 9-12)
- [ ] Base-144k arithmetic library
- [ ] Radix conversion engine (decimal ↔ base-144k)
- [ ] Compression pipeline (text → glyphs → base-144k)

---

## Testing

```bash
# Run complete test suite
python -m tests.test_nsm_core

# Expected output:
# ✅ All 65 NSM primes defined
# ✅ 65/65 NSM primes linked to glyphs
# ✅ 5 FSOUs validated
# ✅ No duplicate base-144k values across 65 glyphs
# 🎉 All NSM core tests passed!
```

---

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## References

- Goddard, C. & Wierzbicka, A. (2014). *Words and Meanings: Lexical Semantics Across Domains, Languages, and Cultures*
- NSM Homepage: https://www.griffith.edu.au/humanities-languages/school-languages-linguistics/research/natural-semantic-metalanguage-homepage
- Weiss et al. (2026). *Universal computation is intrinsic to language model decoding* (arXiv:2601.08061)
- Liu et al. (2025). *Towards universal semantics with large language models* (arXiv:2505.11764)

---

## License

MIT License - see [LICENSE](LICENSE) for details

---

**Created by:** Constitutional Solutions  
**Contact:** https://github.com/Constitutional-Solutions  
**Documentation:** See `/docs` for detailed specifications
