"""CS1 Week 16 doorway into the canonical shared Farkle + ML machine.

Students still run ``python3 -m farkle.cli ...``. The computational truth now
lives in the provenance-pinned sibling package ``farkle_ml`` generated from
``jeremy-evert/Farkle_and_Machine_Learning``.

This package deliberately re-exports the four CS1-facing computational modules
so existing lesson code and regression tests keep their simple imports:

    from farkle import engine, learner, simulate, strategies

CS1 owns the beginner-friendly CLI, lesson, examples, and interpretation. It no
longer owns a second copy of the game/learner/simulation implementation.
"""

from farkle_ml import engine, learner, simulate, strategies

__all__ = ["engine", "learner", "simulate", "strategies"]
