# CS1 Week 16 migration to canonical shared Farkle + ML core

**Date:** 2026-08-16  
**Branch:** `farkle/shared-core-cs1-april`  
**Status:** **GREEN — CANONICAL SHARED CONSUMER VALIDATED ON APRIL**

## Why this migration exists

CS1 originally owned the clearest classroom Farkle engine, strategies, transparent learner, and fair simulation. Those semantics were hardened first, then consolidated with reusable experiment/evidence machinery into the canonical repository:

`jeremy-evert/Farkle_and_Machine_Learning`

The shared repository is GREEN and DSCT is already GREEN as its first clean consumer. CS1 now stops maintaining an accidental second computational source while preserving its deliberately simple Week 16 teaching experience.

## Pre-migration April baseline

The migration branch starts from CS1 commit:

`fc5f1a5f5944da344571adf601310d6b219a0f66`

A clean April worktree ran the existing CS1 contract before any ownership change:

```text
PYTHONPATH=lessons/code python3 -m pytest \
  tests/test_farkle_engine.py \
  tests/test_farkle_learner.py -v
```

Observed result:

- **32 passed in 0.24s** on Python 3.12.3;
- threshold smoke: `bank_at_300` 34 wins / 68.0%, `bank_at_425` 16 wins / 32.0%;
- learner smoke after 500 training turns: learned strategy 34 wins / 68.0%, `bank_at_425` 16 wins / 32.0%.

Durable baseline receipt:

`sidecar/runs/cs1_farkle_april_baseline_20260816.md`

The existing tests were deliberately retained as the migration oracle rather than rewritten to fit the shared package.

## Canonical package adoption

The shared synchronization script generated:

`lessons/code/farkle_ml/`

The generated manifest records:

- canonical repository identity;
- source path `src/farkle_ml`;
- source commit `d3a1ed379a652731b0b6237c33b4fe42c518ac9e`;
- synchronization-time repository head;
- SHA-256 hashes for generated source files.

The apply/check cycle completed GREEN on April before the generated package was committed.

## CS1 ownership after migration

### Canonical shared repository owns

- Farkle rules/engine;
- baseline strategies;
- transparent experience-table learner;
- fair deterministic simulation;
- shared contract/evidence/experiment helpers.

### CS1 continues to own

- `lessons/code/farkle/cli.py` as the beginner-facing command surface;
- `lessons/code/farkle/__init__.py` as the compatibility/facade doorway;
- Week 16 lesson voice and examples;
- instructor guide;
- evidence receipt and grading interpretation;
- checked-in classroom sample/fallback material.

The student command stays:

```text
python3 -m farkle.cli ...
```

The lesson now points students at the readable canonical modules under `lessons/code/farkle_ml/` while explicitly telling them that the later-course extension modules are out of scope for CS1.

## Duplicate machinery retired

The following course-local implementations were removed:

- `lessons/code/farkle/engine.py`
- `lessons/code/farkle/strategies.py`
- `lessons/code/farkle/learner.py`
- `lessons/code/farkle/simulate.py`

They are replaced by the provenance-pinned modules under `lessons/code/farkle_ml/`.

## Real April validation

Command:

```text
python3 scripts/validate_week16_shared_farkle.py
```

Observed on April, Python 3.12.3:

- **GREEN — shared provenance manifest**;
- **GREEN — no duplicated computational modules in CS1 facade**;
- **GREEN — CS1 facade resolves canonical module objects**;
- **GREEN — 32/32 regression tests passed in 0.21s**;
- **GREEN — threshold comparison smoke**;
- **GREEN — learner comparison smoke**.

The post-migration bounded smoke results matched the pre-migration baseline exactly:

### Threshold comparison

- `bank_at_300`: 34 wins, 68.0% win rate, avg score 3762, Farkle/own-turn 21.2%;
- `bank_at_425`: 16 wins, 32.0% win rate, avg score 3229, Farkle/own-turn 51.5%;
- starts A/B = 25/25.

### Learner comparison

- learned experience table: 34 wins, 68.0% win rate, avg score 3957, Farkle/own-turn 8.7%;
- `bank_at_425`: 16 wins, 32.0% win rate, avg score 3178, Farkle/own-turn 50.1%;
- starts A/B = 25/25.

Real validator output was written on April as:

`sidecar/runs/cs1_farkle_shared_validation_20260816T234734Z.md`

That real generated receipt should be retained in Git rather than reconstructed by hand.

## Interpretation

This is stronger than a fresh test pass alone. The migration changed computational ownership while the same regression suite and fixed-seed classroom behaviors remained stable.

CS1 now has:

> **canonical shared computational truth + a deliberately simple CS1 teaching lens + real Linux validation**

## Merge state

The branch is technically ready to merge after the real April GREEN receipt is committed. No further runtime validation is required for the documentation-only closure edits in this report and the Week 16 lesson/planning page.
