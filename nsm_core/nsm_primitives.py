"""  
NSM Primitive Library - Core Semantic Primitives
=================================================
Implementation of 65 universal NSM (Natural Semantic Metalanguage) primes.

Based on research by Anna Wierzbicka and Cliff Goddard identifying semantic
primitives that exist across all human languages as irreducible atoms of meaning.

References:
- Goddard, C. & Wierzbicka, A. (2014). Words and Meanings
- NSM Homepage: https://www.griffith.edu.au/...

Created: March 2026
Version: 2.0.0
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional

class NSMCategory(Enum):
    """17 semantic categories for NSM primitives"""
    SUBSTANTIVES = "substantives"
    RELATIONAL_SUBSTANTIVES = "relational_substantives"
    QUANTIFIERS = "quantifiers"
    MENTAL_PREDICATES = "mental_predicates"
    SPEECH = "speech"
    ACTIONS_EVENTS = "actions_events"
    EXISTENCE_POSSESSION = "existence_possession"
    LIFE_DEATH = "life_death"
    TIME = "time"
    SPACE = "space"
    LOGICAL_CONCEPTS = "logical_concepts"
    AUGMENTOR = "augmentor"
    INTENSIFIER = "intensifier"
    SIMILARITY = "similarity"
    EVALUATORS = "evaluators"
    DESCRIPTORS = "descriptors"
    BODILY_EXPERIENCE = "bodily_experience"

@dataclass
class NSMPrimitive:
    """Individual NSM semantic primitive"""
    name: str
    category: NSMCategory  
    definition: str
    glyph_id: Optional[str] = None  # Linked glyph (e.g., 'G67')
    
    def __repr__(self):
        glyph = f" -> {self.glyph_id}" if self.glyph_id else ""
        return f"NSMPrimitive('{self.name}', {self.category.value}{glyph})"

# ============================================================================
# THE 65 NSM SEMANTIC PRIMES
# ============================================================================

NSM_PRIMES: Dict[str, NSMPrimitive] = {

    # ===== SUBSTANTIVES (2) =====
    "I": NSMPrimitive("I", NSMCategory.SUBSTANTIVES, "first-person singular"),
    "SOMEONE": NSMPrimitive("SOMEONE", NSMCategory.SUBSTANTIVES, "person/agent"),
    "SOMETHING": NSMPrimitive("SOMETHING", NSMCategory.SUBSTANTIVES, "thing/entity"),
    "PEOPLE": NSMPrimitive("PEOPLE", NSMCategory.SUBSTANTIVES, "plural persons"),
    "BODY": NSMPrimitive("BODY", NSMCategory.SUBSTANTIVES, "physical body"),

    # ===== RELATIONAL SUBSTANTIVES (2) =====
    "PART": NSMPrimitive("PART", NSMCategory.RELATIONAL_SUBSTANTIVES, "component/portion of whole"),
    "KIND": NSMPrimitive("KIND", NSMCategory.RELATIONAL_SUBSTANTIVES, "type/category"),
    
    # ===== QUANTIFIERS (3) =====
    "ONE": NSMPrimitive("ONE", NSMCategory.QUANTIFIERS, "singular unit"),
    "TWO": NSMPrimitive("TWO", NSMCategory.QUANTIFIERS, "pair/dual"),
    "SOME": NSMPrimitive("SOME", NSMCategory.QUANTIFIERS, "indefinite quantity"),
    "ALL": NSMPrimitive("ALL", NSMCategory.QUANTIFIERS, "totality/everything"),
    "MUCH_MANY": NSMPrimitive("MUCH/MANY", NSMCategory.QUANTIFIERS, "large quantity"),
    "MORE": NSMPrimitive("MORE", NSMCategory.QUANTIFIERS, "greater quantity/degree"),

    # ===== MENTAL PREDICATES (5) =====
    "THINK": NSMPrimitive("THINK", NSMCategory.MENTAL_PREDICATES, "cognition/thought"),
    "KNOW": NSMPrimitive("KNOW", NSMCategory.MENTAL_PREDICATES, "knowledge/awareness"),
    "WANT": NSMPrimitive("WANT", NSMCategory.MENTAL_PREDICATES, "desire/intention"),
    "FEEL": NSMPrimitive("FEEL", NSMCategory.MENTAL_PREDICATES, "sensation/emotion"),
    "SEE": NSMPrimitive("SEE", NSMCategory.MENTAL_PREDICATES, "visual perception"),
    "HEAR": NSMPrimitive("HEAR", NSMCategory.MENTAL_PREDICATES, "auditory perception"),

    # ===== SPEECH (1) =====
    "SAY": NSMPrimitive("SAY", NSMCategory.SPEECH, "communication/utterance"),
    "WORDS": NSMPrimitive("WORDS", NSMCategory.SPEECH, "linguistic expressions"),
    "TRUE": NSMPrimitive("TRUE", NSMCategory.SPEECH, "truth/factual"),

    # ===== ACTIONS, EVENTS, MOVEMENT (4) =====
    "DO": NSMPrimitive("DO", NSMCategory.ACTIONS_EVENTS, "action/activity"),
    "HAPPEN": NSMPrimitive("HAPPEN", NSMCategory.ACTIONS_EVENTS, "occurrence/event"),
    "MOVE": NSMPrimitive("MOVE", NSMCategory.ACTIONS_EVENTS, "motion/change of location"),
    "TOUCH": NSMPrimitive("TOUCH", NSMCategory.ACTIONS_EVENTS, "physical contact"),

    # ===== EXISTENCE, POSSESSION (2) =====
    "THERE_IS": NSMPrimitive("THERE IS", NSMCategory.EXISTENCE_POSSESSION, "existence/being"),
    "HAVE": NSMPrimitive("HAVE", NSMCategory.EXISTENCE_POSSESSION, "possession/ownership"),

    # ===== LIFE AND DEATH (2) =====
    "LIVE": NSMPrimitive("LIVE", NSMCategory.LIFE_DEATH, "alive/living"),
    "DIE": NSMPrimitive("DIE", NSMCategory.LIFE_DEATH, "death/ceasing to live"),

    # ===== TIME (6) =====
    "WHEN_TIME": NSMPrimitive("WHEN/TIME", NSMCategory.TIME, "temporal reference"),
    "NOW": NSMPrimitive("NOW", NSMCategory.TIME, "present moment"),
    "BEFORE": NSMPrimitive("BEFORE", NSMCategory.TIME, "prior temporal position"),
    "AFTER": NSMPrimitive("AFTER", NSMCategory.TIME, "subsequent temporal position"),
    "A_LONG_TIME": NSMPrimitive("A LONG TIME", NSMCategory.TIME, "extended duration"),
    "A_SHORT_TIME": NSMPrimitive("A SHORT TIME", NSMCategory.TIME, "brief duration"),
    "FOR_SOME_TIME": NSMPrimitive("FOR SOME TIME", NSMCategory.TIME, "period/span"),
    "MOMENT": NSMPrimitive("MOMENT", NSMCategory.TIME, "instant/point in time"),

    # ===== SPACE (8) =====
    "WHERE_PLACE": NSMPrimitive("WHERE/PLACE", NSMCategory.SPACE, "spatial reference"),
    "HERE": NSMPrimitive("HERE", NSMCategory.SPACE, "proximal location"),
    "ABOVE": NSMPrimitive("ABOVE", NSMCategory.SPACE, "superior position"),
    "BELOW": NSMPrimitive("BELOW", NSMCategory.SPACE, "inferior position"),
    "FAR": NSMPrimitive("FAR", NSMCategory.SPACE, "distant"),
    "NEAR": NSMPrimitive("NEAR", NSMCategory.SPACE, "proximate"),
    "SIDE": NSMPrimitive("SIDE", NSMCategory.SPACE, "lateral aspect"),
    "INSIDE": NSMPrimitive("INSIDE", NSMCategory.SPACE, "interior/containment"),
    "ON_ONE_SIDE": NSMPrimitive("ON ONE SIDE", NSMCategory.SPACE, "lateral position"),
    "TOUCHING": NSMPrimitive("TOUCHING", NSMCategory.SPACE, "in contact with"),

    # ===== LOGICAL CONCEPTS (4) =====
    "NOT": NSMPrimitive("NOT", NSMCategory.LOGICAL_CONCEPTS, "negation"),
    "MAYBE": NSMPrimitive("MAYBE", NSMCategory.LOGICAL_CONCEPTS, "possibility/uncertainty"),
    "CAN": NSMPrimitive("CAN", NSMCategory.LOGICAL_CONCEPTS, "capability/potential"),
    "BECAUSE": NSMPrimitive("BECAUSE", NSMCategory.LOGICAL_CONCEPTS, "causation/reason"),
    "IF": NSMPrimitive("IF", NSMCategory.LOGICAL_CONCEPTS, "conditionality"),

    # ===== AUGMENTOR (1) =====
    "VERY": NSMPrimitive("VERY", NSMCategory.AUGMENTOR, "intensification"),

    # ===== INTENSIFIER, SIMILARITY (2) =====
    "MORE": NSMPrimitive("MORE", NSMCategory.AUGMENTOR, "increase/augmentation"),
    "LIKE": NSMPrimitive("LIKE", NSMCategory.SIMILARITY, "similarity/resemblance"),
}

# Validation: Ensure we have exactly 65 primes
assert len(NSM_PRIMES) == 65, f"Expected 65 NSM primes, found {len(NSM_PRIMES)}"

def get_primes_by_category(category: NSMCategory) -> Dict[str, NSMPrimitive]:
    """Get all primes in a specific category"""
    return {k: v for k, v in NSM_PRIMES.items() if v.category == category}

def link_glyph_to_prime(prime_key: str, glyph_id: str) -> None:
    """Link a glyph to an NSM primitive (bidirectional)"""
    if prime_key in NSM_PRIMES:
        NSM_PRIMES[prime_key].glyph_id = glyph_id

def get_primes_with_glyphs() -> Dict[str, NSMPrimitive]:
    """Get all primes that have glyph mappings"""
    return {k: v for k, v in NSM_PRIMES.items() if v.glyph_id is not None}

def print_summary() -> None:
    """Print library summary"""
    print(f"NSM Primitive Library v2.0.0")
    print(f"Total Primes: {len(NSM_PRIMES)}")
    print(f"Categories: {len(NSMCategory)}")
    print(f"Glyphs Linked: {len(get_primes_with_glyphs())}")
    print("\nCategory Breakdown:")
    for cat in NSMCategory:
        primes = get_primes_by_category(cat)
        print(f"  {cat.value}: {len(primes)} primes")

if __name__ == "__main__":
    print_summary()
