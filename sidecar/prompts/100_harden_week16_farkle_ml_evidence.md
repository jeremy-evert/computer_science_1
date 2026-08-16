# Sidecar Prompt 100 - Harden Week 16 Farkle / ML evidence without turning it into a new project

**Status:** READY WHEN DELIBERATELY STARTED  
**Scope:** CS1 Week 16 Farkle / Machine Learning package only  
**Owner:** Foreman  
**Mode:** inspect -> reproduce -> make surgical repairs -> test -> reconcile student/instructor prose -> report -> stop

## Mission

The existing CS1 Week 16 Farkle / ML package is already good and should be preserved.

Do **not** redesign it because a broader cross-course Farkle conversation exists elsewhere. Do not import Computer Architecture tournament infrastructure, Kubernetes, containers, GPUs, cloud benchmarking, cost accounting, leaderboards, or a larger ML stack into CS1.

This prompt exists because inspection found a few concrete seams where the current implementation can make the evidence students are asked to trust less honest than the lesson intends.

The governing rule is:

> Fix the evidence contract. Preserve the fun week.

If the findings below turn out not to reproduce on the current branch, document that and leave the corresponding code alone.

---

## Read first

Read the current source before changing anything:

- `planning/week-16.md`
- `lessons/10-farkle-ml.md`
- `docs/curriculum/week-16-instructor-guide.md`
- `assignments/W16-farkle-ml-experiment-receipt.md`
- `assignments/odyssey_gates/week-16.md`
- `rubrics/odyssey_gates/week-16_rubric.md`
- `lessons/code/farkle/engine.py`
- `lessons/code/farkle/strategies.py`
- `lessons/code/farkle/learner.py`
- `lessons/code/farkle/simulate.py`
- `lessons/code/farkle/cli.py`
- `tests/test_farkle_engine.py`
- `tests/test_farkle_learner.py`
- `reports/013_week16_farkle_ml_capstone.md`

Also inspect the current grading model only far enough to confirm that this prompt does not invent a new Week 16 category or point value.

---

## What is already strong and should stay strong

Preserve these choices unless a real bug forces a local change:

- Python standard library only for the student experience;
- no third-party ML dependency;
- deterministic seeds;
- real runnable Farkle engine;
- simple human-readable strategies;
- transparent experience-table learner;
- no formal reinforcement-learning mathematics;
- fresh-game evaluation after training;
- play/predict before showing machine results;
- evidence and interpretation instead of a magic required win rate;
- checked-in fallback table for instructor recovery;
- short Week 16 receipt;
- no Odyssey Checkpoint 4;
- no giant final project;
- no requirement to write the Farkle engine from scratch.

This is a payoff week. Keep it one.

---

# Required investigation and repairs

## 1. Remove first-player contamination from strategy comparisons

### Current concern

`simulate.play_game()` always starts with `strategy_a`, and the documented course variant ends immediately when the first player reaches the target.

That means a reported A-vs-B win rate may contain a first-move advantage in addition to the strategy difference.

The lesson asks students to use win rate as evidence that one strategy is better. The comparison runner therefore needs to make starting position fair or explicitly neutralized.

### Required outcome

Implement the smallest understandable solution that balances starting position across a comparison.

Preferred shape:

- preserve strategy A and strategy B identities in the output;
- over an even-sized comparison, each strategy starts the same number of games;
- define/document sensible behavior for an odd game count;
- remain deterministic under a fixed seed;
- do not complicate the student CLI unnecessarily.

A simple alternating starter is acceptable if tests demonstrate the contract. A more elaborate paired-seed tournament is unnecessary unless there is a compelling reason.

### Tests

Add tests proving:

- starting position is balanced for an even comparison;
- fixed-seed results remain reproducible;
- A/B labels and accumulated statistics stay attached to the correct strategy when B starts;
- existing comparison behavior still runs end to end.

Do **not** add inferential-statistics machinery just to solve this.

---

## 2. Make `farkle_rate` mean what the label says

### Current concern

`run_many_games()` accumulates each player's Farkles separately but divides each by `total_turns`, where `total_turns` includes both players' turns.

That is not a per-strategy Farkle rate. It approximately halves the intuitive quantity students think they are reading.

### Required outcome

Track the number of turns actually taken by each player/strategy and calculate:

> Farkle rate = that strategy's Farkles / that strategy's turns

Keep the output vocabulary understandable to a CS1 student.

### Tests

Add a deterministic test that would fail under the old denominator and pass under the corrected per-player denominator.

If useful, include per-player turn counts in the internal summary dictionary. Do not clutter the student-facing report unless the extra number genuinely helps interpretation.

---

## 3. Make the learner's printed preference match the action it will actually take

### Current concern

`ExperienceTable.choose_action(..., explore=False)` and `ExperienceTable.table_rows()` do not derive preference through exactly the same rule.

In particular, when evidence exists for only one action, the printed `current_preference` can disagree with the action the trained strategy would actually choose.

This matters because the student lesson explicitly asks students to inspect a row, read what the table prefers, and explain why.

### Required outcome

Establish one source of truth for greedy action selection and reuse it for both:

- actual learned-strategy decisions; and
- the human-readable `current_preference` field.

Do not hide unexplored actions. Counts (`roll_seen`, `bank_seen`) should remain visible so students can notice weak evidence.

### Tests

For every row in a trained table fixture/test surface, verify that `current_preference` agrees with the non-exploring action the table would take for the corresponding state.

Also test a deliberately sparse/one-action-observed situation so this seam cannot silently return.

---

## 4. Reconcile the "your human strategy" experience with what students can actually run

### Current concern

The lesson and instructor guide correctly want students to begin with their own human intuition. The source even says human strategies are what students write before meeting the learner.

But the CLI accepts only the fixed names in `BUILT_IN_STRATEGIES`, and the lesson mostly demonstrates `bank_at_300` versus `bank_at_800`.

Do not turn Week 16 into a new programming assignment merely to fix this wording mismatch.

### Required outcome

Choose the smallest CS1-appropriate solution. Good options include one of these:

1. add a CLI parameter for an arbitrary bank threshold, backed by the existing strategy factory pattern; or
2. give students one tiny, explicit, safe place to change/add a threshold strategy and show exactly how to run it; or
3. if neither is pedagogically worth the friction, revise the prose so students are clearly choosing among supplied human strategies rather than pretending they authored runnable code.

Preference: preserve a tiny act of student authorship if it can be done with almost no setup burden.

Acceptance test:

> A student who says "my rule is bank at 425" should have a truthful, obvious path to test that rule without learning new Week 16 machinery.

Keep this bounded to the concepts they already know.

---

# Light evidence-quality improvement

The current lesson already tells students to rerun with another seed when interpreting a learned strategy. Preserve that instinct.

If a tiny CLI/documentation improvement can make the evidence stronger without adding conceptual load, consider a small fixed **seed bundle** comparison, for example three documented seeds, so the student can see whether the same story survives more than one random stream.

This is **optional**. Do not build a statistics package, confidence-interval lesson, tournament scheduler, or leaderboard. If the existing "run another seed" flow is clearer for CS1, keep it.

---

# Student/instructor reconciliation

After code repairs, update only the prose that is actually affected.

At minimum inspect:

- `lessons/10-farkle-ml.md`
- `docs/curriculum/week-16-instructor-guide.md`
- `assignments/W16-farkle-ml-experiment-receipt.md`
- `planning/week-16.md`

Make sure they now accurately describe:

- fair/balanced strategy comparison;
- the meaning of Farkle rate;
- the learner's visible preference;
- how the student's human strategy is represented/run;
- the fact that randomness still requires repeated evidence rather than one magic result.

Do not inflate the receipt. Two to four sentences per requested reflection item should remain normal.

Do not resurrect a Week 16 Odyssey gate or invent numeric grading weight.

---

# Explicit non-goals

Do **not** add any of the following in this prompt:

- Computer Architecture cost/performance tournament;
- hardware categories;
- Raspberry Pi/Desktop/NRP lanes;
- Kubernetes or pod runners;
- containers as a Week 16 student requirement;
- GPU support;
- cloud deployment;
- leaderboards;
- round-robin infrastructure;
- scikit-learn, NumPy, PyTorch, pandas, matplotlib, or another dependency just because it is available;
- Q-learning/Bellman equations/discount factors;
- a larger state space using total score/opponent score unless a concrete CS1 bug requires it;
- a new Farkle rules variant;
- a new major assignment;
- production Canvas or Savnac work;
- unrelated CS1 cleanup.

The broader Farkle ecosystem can reuse this engine later. That is not this prompt's job.

---

# Validation

Run the full existing Farkle test surface plus the new tests.

At minimum:

```bash
PYTHONPATH=lessons/code python3 -m pytest tests/test_farkle_engine.py tests/test_farkle_learner.py -v
```

Also execute the student-facing command path from the lesson, including:

- one traced turn;
- baseline-vs-baseline comparison;
- learner training/table inspection;
- learned-vs-baseline fresh-game comparison;
- the chosen student-authored/arbitrary-threshold path if implemented.

Use fixed seeds and record representative outputs.

Do not require exact stochastic win percentages in tests unless the test is deliberately about fixed-seed reproducibility. Prefer contract/invariant tests.

---

# Required report

Create:

`sidecar/reports/100_harden_week16_farkle_ml_evidence.md`

Report:

- whether each suspected issue reproduced;
- exact repair made, if any;
- tests added/changed;
- final test count and result;
- representative fair comparison output;
- corrected Farkle-rate interpretation;
- proof printed learner preference matches actual greedy action;
- final human-strategy workflow;
- files changed;
- final commit SHA(s);
- any remaining yellow that actually matters to Week 16.

If investigation shows a proposed repair is unnecessary, say so explicitly instead of manufacturing work.

---

# Done when

This prompt is done when the existing Week 16 package is **more trustworthy but not materially larger**.

A good completion should feel like:

> We fixed three evidence seams, made the student's human strategy path honest, strengthened the tests, and then left the damn thing alone.

If the implementation starts growing into a shared tournament platform or a new ML unit, stop. That is scope failure, not progress.
