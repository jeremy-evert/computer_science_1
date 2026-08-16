# Raw Work Receipt — CS1 Prompt 100 Farkle hardening

**Date:** 2026-08-16  
**Execution surface:** GitHub connector writes; no local checkout available in this environment  
**Status:** IMPLEMENTED / EXECUTION VALIDATION YELLOW

## Changes landed

- `e44e558c7f27d2e918e13aebbdd1cd31ff45f2e4` — strategy factory/resolver; arbitrary positive `bank_at_N` names.
- `862229a75eb8de6539c5093bac01426a589fdc78` — alternate starting player; player-specific turn counts/Farkle-rate denominators.
- `b16eaafc8d252f604017dd83dbd7c50feebb0009` — displayed learner preference now uses the same comparison as greedy policy.
- `2562658a99d13594c796537c2bef02653ae77bac` — CLI resolves built-ins or `bank_at_N` names.
- `828a6d07ec00740a4c5ccd2cbebdce778e579666` — regression tests for the hardened evidence contract.

## Expected validation command on a real checkout

```bash
PYTHONPATH=lessons/code python3 -m pytest tests/test_farkle_engine.py tests/test_farkle_learner.py -v
```

Then smoke:

```bash
cd lessons/code
python3 -m farkle.cli compare --seed 1 --games 200 --strategy-a bank_at_425 --strategy-b bank_at_800
python3 -m farkle.cli learn-vs-baseline --seed 1 --turns 20000 --games 2000 --baseline bank_at_425
```

## Named yellow

This assistant environment cannot clone GitHub repositories or execute the updated private-repo source locally. The code and tests are committed, but a real checkout must execute the commands above before Prompt 100 is called fully GREEN.
