# Report 100 — Harden Week 16 Farkle / ML evidence

**Date:** 2026-08-16  
**Status:** IMPLEMENTED WITH EXECUTION-VALIDATION YELLOW

## What changed

The existing CS1 Week 16 design was preserved. Four narrow evidence-contract seams were repaired:

1. repeated strategy comparisons now alternate starting player;
2. Farkle rate is calculated over each strategy's own turns;
3. displayed experience-table preference uses the same rule as the actual greedy policy;
4. the CLI now truthfully supports arbitrary positive human thresholds via `bank_at_N`, such as `bank_at_425`.

Regression tests were added for these guarantees.

## Implementation commits

- `e44e558c7f27d2e918e13aebbdd1cd31ff45f2e4`
- `862229a75eb8de6539c5093bac01426a589fdc78`
- `b16eaafc8d252f604017dd83dbd7c50feebb0009`
- `2562658a99d13594c796537c2bef02653ae77bac`
- `828a6d07ec00740a4c5ccd2cbebdce778e579666`

Raw connector receipt:

- `sidecar/runs/100_cs1_farkle_hardening_connector_receipt.md`

## What did not change

- Farkle rule variant;
- scoring engine;
- transparent running-average learner concept;
- no formal RL mathematics;
- no third-party ML dependency;
- no new Week 16 checkpoint;
- no Architecture tournament infrastructure.

## Validation yellow

This assistant environment could write through the connected GitHub app but could not clone/execute the private repository locally. A real checkout must run:

```bash
PYTHONPATH=lessons/code python3 -m pytest tests/test_farkle_engine.py tests/test_farkle_learner.py -v
```

and the documented CLI smoke commands before this report is promoted to fully GREEN.

CS2 may consume this corrected source state for implementation, but its own release should retain the same named validation yellow until its one-command validator runs on a real checkout.
