# CS1 Week 16 Farkle baseline validation — April

**Date:** 2026-08-16  
**Host:** April  
**Branch start:** `fc5f1a5f5944da344571adf601310d6b219a0f66`  
**Python:** 3.12.3  
**Status:** **GREEN — pre-migration baseline**

This receipt records the working CS1 Week 16 Farkle implementation **before** adopting the canonical shared `jeremy-evert/Farkle_and_Machine_Learning` package.

The purpose is to create an A/B safety rail: if later shared-core adoption changes behavior unexpectedly, we can distinguish a migration regression from a pre-existing CS1 defect.

## Regression suite

Command:

```text
PYTHONPATH=lessons/code python3 -m pytest \
  tests/test_farkle_engine.py \
  tests/test_farkle_learner.py \
  -v
```

Observed result:

```text
32 passed in 0.24s
```

The passing suite includes scoring rules, deterministic seeded behavior, transparent learner behavior, arbitrary `bank_at_N` thresholds, balanced alternating starters, per-player-turn Farkle denominators, and readable comparison output.

## Threshold smoke comparison

Command:

```text
PYTHONPATH=lessons/code python3 -m farkle.cli compare \
  --games 50 \
  --seed 17 \
  --strategy-a bank_at_300 \
  --strategy-b bank_at_425
```

Observed evidence:

```text
50 games, seed=17 (starts A/B=25/25)
  bank_at_300                  win rate 68.0%   avg score 3762   farkle/own-turn 21.2%
  bank_at_425                  win rate 32.0%   avg score 3229   farkle/own-turn 51.5%
  ties: 0.0%   avg turns/game: 18.3
```

## Transparent learner smoke comparison

Command:

```text
PYTHONPATH=lessons/code python3 -m farkle.cli learn-vs-baseline \
  --turns 500 \
  --games 50 \
  --seed 17 \
  --baseline bank_at_425
```

Observed evidence:

```text
Step 1: trained the experience table on 500 solo turns (seed=17).
        68 (situation, action) pairs now have data.

Step 2: comparing the learned strategy to baseline 'bank_at_425' over 50 FRESH games (none of these games were used in training).

50 games, seed=18 (starts A/B=25/25)
  learned_strategy             win rate 68.0%   avg score 3957   farkle/own-turn 8.7%
  bank_at_425                  win rate 32.0%   avg score 3178   farkle/own-turn 50.1%
  ties: 0.0%   avg turns/game: 18.7
```

These bounded smoke results are evidence of reproducible execution, not a claim that either strategy is universally best.

## Migration gate

This GREEN baseline authorizes the next branch-only step:

1. synchronize the canonical shared package into a dedicated generated destination;
2. preserve the CS1-specific lesson/CLI surface;
3. retire duplicated computational ownership only on this branch;
4. rerun the same regression suite and smoke comparisons;
5. compare before/after semantics;
6. merge only after the shared-consumer path is GREEN.
