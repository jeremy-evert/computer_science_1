# CS1 Week 16 migration to canonical shared Farkle + ML core

**Date:** 2026-08-16  
**Branch:** `farkle/shared-core-cs1-april`  
**Status:** MIGRATION AUTHORED — REAL APRIL VALIDATION REQUIRED

## Why this migration exists

CS1 originally owned the clearest classroom Farkle engine, strategies, transparent learner, and fair simulation. Those semantics were hardened first, then consolidated with reusable experiment/evidence machinery into the canonical repository:

`jeremy-evert/Farkle_and_Machine_Learning`

The shared repository is now GREEN and DSCT is already GREEN as its first clean consumer. CS1 should therefore stop maintaining an accidental second computational source while preserving its deliberately simple Week 16 teaching experience.

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
- balanced 50-game threshold smoke completed;
- 500-turn learner / 50-game fresh-evaluation smoke completed.

Durable receipt:

`sidecar/runs/cs1_farkle_april_baseline_20260816.md`

This baseline is the migration oracle. The existing tests are not rewritten merely to make the shared package appear compatible.

## Canonical package adoption

The shared synchronization script generated:

`lessons/code/farkle_ml/`

The generated manifest records:

- canonical repository identity;
- source path `src/farkle_ml`;
- source commit;
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
- Week 16 lesson voice and examples;
- instructor guide;
- evidence receipt and grading interpretation;
- checked-in classroom sample/fallback material.

The student command stays:

```text
python3 -m farkle.cli ...
```

`lessons/code/farkle/__init__.py` re-exports the canonical CS1-facing modules so existing lesson/test imports remain simple.

## Duplicate machinery retired on this branch

The following course-local implementations were removed after the canonical snapshot was generated:

- `lessons/code/farkle/engine.py`
- `lessons/code/farkle/strategies.py`
- `lessons/code/farkle/learner.py`
- `lessons/code/farkle/simulate.py`

They are replaced by the provenance-pinned modules under `lessons/code/farkle_ml/`.

## Validation contract

Run from the CS1 repository root:

```text
python3 scripts/validate_week16_shared_farkle.py
```

The validator must:

1. verify the shared provenance manifest;
2. verify the old duplicate computational modules are absent;
3. verify the CS1 facade resolves the canonical module objects;
4. rerun the same two pre-migration regression files;
5. rerun the bounded threshold comparison smoke;
6. rerun the bounded learner-vs-baseline smoke;
7. write a timestamped `sidecar/runs/cs1_farkle_shared_validation_<timestamp>.md` receipt;
8. exit nonzero on any required failure.

## What remains before GREEN

- execute the one-command validator on April;
- retain the resulting GREEN receipt;
- reconcile Week 16 lesson/guide/planning prose from old local-code ownership to canonical shared ownership;
- promote the Week 16 status/postmortem;
- keep this work isolated from `main` until merge timing is deliberately chosen.

No merge to `main` is authorized by this report.
