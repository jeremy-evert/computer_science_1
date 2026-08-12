# Week 16 instructor guide — Farkle / Machine Learning fun week

**Companion to:** `lessons/10-farkle-ml.md` (student-facing lesson),
`lessons/code/farkle/` (runnable code), `planning/week-16.md` (weekly
schedule), `assignments/W16-farkle-ml-experiment-receipt.md` (the light
evidence artifact due this week).

**Framing for yourself before class:** this is a payoff week, not a new
unit. Every piece of Python a student needs to read this week — dice
rolls, an `if`/`else` decision, a loop, a function, a dictionary — they
already have. Your job is to make the *idea* (a machine's behavior
changes because of repeated feedback) land intuitively, not to teach
reinforcement learning.

---

## Setup before class

- Confirm Python 3.9+ is available (no third-party packages required —
  the whole package uses only the standard library).
- From `computer_science_1/lessons/code/`, run once to confirm the
  environment works:
  ```
  python3 -m farkle.cli compare --seed 1 --games 1000
  ```
  If that prints a report in under a second, you're ready.
- Optional: run `PYTHONPATH=lessons/code python3 -m pytest tests/ -v`
  from the repo root once before class — if any test fails, do not
  demo live until it's fixed (see "Fallback" below).

---

## Wednesday — "Can a machine learn to play a dice game?"

**Goal of the day:** students understand the rules well enough to have
an opinion, and can name state/action/reward in their own decision.

**Suggested flow (≈50 min):**

1. **(10 min) Play, don't lecture.** Have students roll real dice (or
   use any dice roller) in pairs and play a couple of rounds by hand
   using the rules in `lessons/10-farkle-ml.md` §1. Let a few Farkle on
   purpose by being greedy. This is the most important ten minutes of
   the week — do not skip it for more code time.
2. **(5 min) Collect strategies out loud.** Ask 3-4 students what turn
   score made them stop. Write their numbers on the board. You now have
   real human baselines before any code runs.
3. **(10 min) Vocabulary.** Introduce state/action/reward using
   `lessons/10-farkle-ml.md` §2's table. Point at the board strategies
   students just gave and translate one into the `bank_at_300`-style
   function live.
4. **(15 min) Live demo.** Run, projected:
   ```
   python3 -m farkle.cli play --seed 1 --strategy bank_at_300
   python3 -m farkle.cli compare --seed 1 --games 5000 --strategy-a bank_at_300 --strategy-b bank_at_800
   ```
   Ask for a prediction before running the second command. Most classes
   predict the aggressive (800) strategy wins more — it usually loses
   badly to the Farkle rate. That surprise is the hook for Friday.
5. **(10 min) Students run it themselves** with their own strategy
   parameters (pick their own threshold from step 2) and compare against
   a classmate's.

**Likely confusions:**
- Students expect "aggressive wins" and need to see the Farkle-rate
  column to understand why it usually doesn't.
- "Hot dice" is confusing on first read — demo it live if a `play` trace
  happens to show one (a `--seed` that produces one within a few tries
  works fine, or just narrate the code path in `engine.py`).
- Some students conflate the *state dictionary* with the *learner's
  table*. They are different: the state dictionary describes one moment;
  the table (Friday) is the machine's *accumulated memory* across many
  moments.

**Where to stop and ask questions:** right after the `compare` demo,
before moving on. "Why did the number come out that way?" is the
question that turns this into a lesson instead of a magic trick.

---

## Friday — "Teach it something, then test it"

**Goal of the day:** students watch a table of numbers change with
practice, evaluate it honestly, and compare it to their own strategy.

**Suggested flow (≈50 min):**

1. **(5 min) Recap** Wednesday's surprising result.
2. **(15 min) Live demo — train and inspect.**
   ```
   python3 -m farkle.cli train --seed 1 --turns 20000 --show-table
   ```
   Scroll to rows with `dice_remaining` = 1 or 2 and rows with
   `dice_remaining` = 6. Ask students to predict the preference before
   you scroll to it. This is the "tiny visible learner" moment — there
   is nothing else to it, and that's the point.
3. **(15 min) Live demo — test on fresh games.**
   ```
   python3 -m farkle.cli learn-vs-baseline --seed 1 --turns 20000 --games 5000 --baseline bank_at_300
   ```
   Ask: is this a fair test? (Yes — the evaluation games are a different
   seed than training, so the learner hasn't "seen" them.)
4. **(10 min) Human vs. machine, out loud.** Put a student-chosen
   threshold strategy from Wednesday's board list up against the learned
   strategy (`compare`-style, or eyeball the two `learn-vs-baseline`/
   `compare` reports side by side). Ask: where do they agree? Where does
   the machine surprise you?
5. **(5 min) Close with judgment, not math.** Ask directly: *"What
   evidence would convince you the machine actually learned something
   useful?"* Let a few answers land before pointing at the receipt
   template's interpretation questions.

**Likely confusions:**
- "Different behavior" read as automatically "better" — press on this;
  it's explicitly the closing judgment move the lesson wants.
- Randomness anxiety — a student's own `--seed` run may show the learner
  losing to a baseline in a single small comparison. That's expected and
  useful: ask *how many games would you want to run before believing
  that*, which is the "ten lucky games is weak evidence" point.
- Some students want to know if this is "real AI." Be honest per
  `lessons/10-farkle-ml.md`'s closing note: it's a real, simplified
  instance of the same idea, not a toy pretending to be something else,
  and not the full sophistication of production reinforcement learning
  either.

**Where to stop and ask questions:** right before showing the
`learn-vs-baseline` numbers — get a prediction on record first.

---

## Fallback if the live learner behaves oddly due to randomness

The learner is trained live with real randomness; on a bad `--seed` it
can occasionally look worse than a baseline in one small demo run, or the
printed table can look sparse from too few training turns. If that
happens in front of the class:

1. **Don't panic-debug live.** This is itself teachable: "the table
   hasn't seen enough examples of this situation yet — how would we find
   out?" is a legitimate answer, not a failure.
2. Fall back to the checked-in reference run:
   `lessons/code/farkle/sample_output/trained_table_seed1.json` was
   generated with `--seed 1 --turns 20000` and is the exact table quoted
   in `reports/013_week16_farkle_ml_capstone.md`'s sample results. Load
   and show it instead:
   ```python
   from farkle import learner
   table = learner.load_table("farkle/sample_output/trained_table_seed1.json")
   for row in table.table_rows():
       print(row)
   ```
3. If time is short, `--turns 20000` finishes in well under a second on
   any modern laptop — increasing it live to "prove it keeps learning"
   is a safe, fast recovery, not a real time cost.
4. There is no "magic exact win rate" this demo owes you. If a single
   `compare`/`learn-vs-baseline` run looks unconvincing, running it again
   with `--games 5000` or higher and a couple of different `--seed`
   values is the correct response, in class or as a talking point about
   evidence quality — not something to be defensive about.

---

## Classroom flow at a glance

| Day | Time | Focus |
|---|---|---|
| Wednesday | ~50 min | Play the game, name state/action/reward, run baseline comparisons |
| Friday | ~50 min | Train and inspect the learner, test on fresh games, human-vs-machine discussion, close with judgment questions |

## What NOT to do this week

- Do not derive or name the Bellman equation, discount factor/gamma, or
  a formal Markov decision process, even informally as "the real version
  of what this table is doing." Save that for students who ask and are
  headed to CS2 — point them at
  `docs/curriculum/cs2-farkle-ml-handoff.md`.
- Do not require students to write the Farkle engine from scratch. They
  read and run it; they do not rebuild it under finals-week pressure.
- Do not grade this week on a specific win rate. Grade on whether the
  receipt shows real evidence and real interpretation (see the rubric
  note in `assignments/W16-farkle-ml-experiment-receipt.md`).
