# COMSC 1033 — Grading Model (DRAFT PROPOSAL)

**Status: reviewed, 2026-07-31.** Direction is decided
(see `course-ethos.md`): no traditional tests, points attach to every weekly
artifact, the old single "homework" bucket splits into named categories, the
final is worth points. The *percentages* below are a first proposal that sums
to 100 — adjust freely.

**Reconciled 2026-07-27:** the "weekly reinforcement assignment" row and the
"Coding Odyssey checkpoints" row below are two grains of the *same* project,
not two separate assignments. Every technical week is a Coding Odyssey week
(`assignments/A2-coding-odyssey-project.md`) — the textbook chapter supplies
that week's concept, applied inside the student's own world; the weekly
gate/checkpoint that results *is* the weekly reinforcement assignment. See
`assignments/A1-weekly-coding-practice.md` and
`docs/curriculum/judgment_toolkit.md`.

> **Final decided (2026-07-15):** the final is a **reflection paper**, built
> from the existing template (`assignments/A5-final-reflection.md`). One small
> residual: confirm at syllabus finalization that university policy is
> satisfied by a reflection paper in the finals slot.

## Proposed weights

| Category | Weight | Cadence | Notes |
|---|---:|---|---|
| Monday Moment quiz | 6% | weekly | Short; checks the AI-fluency principle of the week |
| Wacky Wednesday reflection | 6% | weekly | Tie-in to the week |
| Fun Friday reflection | 6% | weekly | Tie-in to the week |
| Paired-programming report | 5% | weekly | Student's own contribution, honestly assessed |
| Friday feedback report | 5% | weekly | Quality of feedback the student *gave* |
| Weekly reinforcement assignment | 25% | weekly | Two axes: result 15% + process 10% (rubric below). Result = that week's Coding Odyssey gate + Light Build continuation, weeks 2–5/7–8/10–13. Optional standalone bonus practice (`assignments/A1-weekly-coding-practice.md`) is additive on top of this row, not part of its 25% — exact point value not yet decided, see Open decisions. |
| Coding Odyssey checkpoints | 15% | 3 checkpoints (Wk 6/9/14) | The bigger, periodic grading pass on the same project — full four-axis Build rubric, not the weekly gate's pass/fail. Keeps the historical effort ladder in spirit (70/80/90/100 → now the Functions/Concept-use/Explanation/Demonstrability axes, `judgment_toolkit.md` §2). **Reconciled 2026-08-12 (prompt 055):** the table previously said "4 checkpoints (Wk 6/9/14/16)" — stale from before Checkpoint 4 was retired at Week 16 (`reports/012_pre_savnac_source_reconciliation.md`). Week 16 is the Farkle/ML fun week, not a checkpoint; see `planning/week-16.md` and `reports/013_week16_farkle_ml_capstone.md`. |
| Final reflection paper | 10% | finals week | Template basis: `assignments/A5-final-reflection.md`; sanity-check against university finals policy |
| Professional pathway — Week 14 update | 5% | Week 14 | Reasoning-graded update pass + new changelog/diff artifact (`assignments/A6-professional-pathway-artifacts.md`, `rubrics/A6-week-14-update_rubric.md`). Decided 2026-08-06, reshaped from an ungraded prep checkpoint into its own graded row. |
| Professional pathway — Week 15 submission | 5% | Week 15 | Completion + submission of the full artifact set + next-steps reflection (`rubrics/A6-week-15-submission_rubric.md`). Decided 2026-08-06 — previously had no rubric or weight row at all despite carrying real work. |
| Attendance & participation | 10% | daily | Historical policy; shrunk from 20% on 2026-08-06 to absorb the professional-pathway rows below without over-summing the table — confirm language at syllabus finalization |
| Course evaluation | 2% | end of term | Carried from current model |
| **Total** | **100%** | | Reconciled 2026-08-06 — see "What this replaces" history and "Open decisions" below for the attendance trim that made this balance. |

**Week 16 (Farkle/ML) grading, reconciled 2026-08-12 (prompt 055):** Week
16 carries no Coding Odyssey checkpoint/gate (see above) and this task
does not invent one. The week's light evidence artifact
(`assignments/W16-farkle-ml-experiment-receipt.md`) is participation/
reflection evidence of the same shape as the existing weekly
Wacky-Wednesday-reflection / Fun-Friday-reflection / attendance rows
above — Week 16 already has both a Wacky Wednesday and Fun Friday slot
(`planning/week-16.md`). No new percentage row is added for it; it is
covered by those existing categories. If a future pass wants a distinct
graded weight specifically for the Farkle/ML receipt, that is a new
decision for Jeremy to make, not one made here.

**Not in the table above: A4 (Show and Tell reflection).** Decided
2026-08-08 (Jeremy: "I want to see a PPR and SnTR for every week that we
have them") — A4 now pushes a real, gradable, rubric-scored instance every
ready week in Canvas (`course_foundry`'s `_weekly_a4_object`, same weekly
pattern as the paired-programming report and Friday feedback report rows
above). It earns real points today (10 pts/week, Canvas's default
0%-weighted "Assignments" group) but has **no row and no percentage in this
table** — unlike "Fun Friday reflection" above (professional_minds' own
Friday slides reflection, a distinct artifact), A4 was never in this weight
model at all, on-disk or live, before today. Cadence is decided; weight is
not — see "Open decisions" below.

Weekly categories drop-lowest or late-work handling: inherit the standing
two-week late window (see syllabus) — decide drop-lowest at finalization.

## The two-axis rubric for the weekly reinforcement assignment

**Axis 1 — the working result (15 points of the 25).** For gate weeks
(2–5, 7–8, 10–13), this is that week's Odyssey Quick Check (pass/fail floor)
plus the Light Build continuation band, mapped onto the historical
effort-based ladder: gate not yet passed sits around 25% of the axis, gate
passed with minimal continuation 50–75%, gate passed with a solid-to-strong
continuation 100%. For checkpoint weeks (6, 9, 14), the four-axis Full
Build rubric (`docs/curriculum/judgment_toolkit.md` §2) stands in for this
axis directly instead of the ladder.

**Axis 2 — process (10 points of the 25).** Knowledge management and
resource tracking are part of the ethos, even in CS1. Four dimensions,
graded from what the student submits:

| Dimension | What earns points | Evidence submitted |
|---|---|---|
| **Rhetoric** | Interrogated the question — restated it, challenged an assumption, or justified taking it as written — rather than silently answering the prompt as-is | 2–3 sentences at the top of the submission |
| **Planning** | A plan existed before code: outline, pseudocode, flowchart, or steps — and the submission notes where reality diverged from it | The plan artifact, however rough |
| **Resource budgeting** | Tracks every service/model/tier used (free or paid), the limits hit (hourly/weekly/trial/free caps), and why that tool fit the problem — different models hit different. This is budget management as a skill. **Graded on the tracking and reasoning, never on how much was spent — a student running only free/local tools can earn full marks** | Tool-and-limits ledger, a few lines |
| **Knowledge management** | Prompts and chats are tracked: links, exports, or pasted excerpts, organized enough that the student could find and reuse them next week | Prompt/chat log attached or linked |

Scoring per dimension: 0 (absent) / 1 (present) / 2 (present and thoughtful),
× 4 dimensions = 8, plus 2 points for the whole package being organized and
reusable = 10.

## What this replaces

The prior working model (`docs/syllabus.md`): homework/practice/project 68%,
reflection 10%, attendance 20%, evaluation 2%. The 68% bucket is what splits
into the named weekly categories above; the 10% end-of-semester reflection
folds into the final.

## Pair-work grading rule (2026-07-15)

Pairs may share one repository. Each student documents their own
contributions, and the pair's git log must show a lines-of-code split no
more lopsided than 80/20. The paired-programming report is where each
student narrates their side.

## Open decisions

- [ ] **Optional standalone bonus-practice point value/mechanism**
      (flagged 2026-08-12, `reports/012_pre_savnac_source_reconciliation.md`):
      Jeremy wants students who do optional standalone problems (see
      `assignments/A1-weekly-coding-practice.md`) to earn additive bonus
      credit and keep it even after satisfying the normal Odyssey
      requirement. This repo has no pre-existing standalone-problem point
      convention to preserve, so no number is invented here — a small
      remaining implementation decision, not a blocker to using the policy
      as written.
- [ ] Confirm university finals policy accepts a reflection paper (small
      residual; decision itself is made).
- [ ] Confirm or adjust every percentage above.
- [x] **Reconcile the table's 110% total** (2026-08-06): the professional
      pathway's two new rows (5% + 5%, decided and confirmed by Jeremy the
      same day) had been added without shrinking any existing row, over-summing
      the table by 10 points. Resolved by shrinking Attendance & participation
      20% → 10% (Jeremy's call, 2026-08-06) — the row already marked
      "confirm at finalization" and least tied to specific rubric math. Table
      now sums to 100%.
- [ ] Drop-lowest policy per weekly category.
- [ ] Where each artifact is submitted in Canvas (one assignment group per
      category keeps the gradebook legible).
- [ ] How the automated-feedback reply scores or pre-scores the process
      rubric (Marker names gaps; the professor keeps final authority).
- [ ] **A4 (Show and Tell reflection) weight/category** (flagged
      2026-08-08, exit-ticket grading audit; cadence decided same day, weight
      still open): A4 now pushes weekly to Canvas with real points and a real
      rubric, ungrouped in the 0%-weighted default "Assignments" group. Giving
      it a real percentage means shrinking some other row to keep the table at
      100% — the same class of call Jeremy made explicitly for the two
      professional-pathway rows above. Not decided; do not guess a number.
