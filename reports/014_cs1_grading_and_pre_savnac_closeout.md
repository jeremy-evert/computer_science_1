# Report 014 — CS1 grading and pre-Savnac implementation closeout

**Prompt:** `jeremy_task_tracking/prompts/067_cs1_grading_and_pre_savnac_implementation_closeout.md`
**Scope:** Fall 2026 COMSC 1033 (CS1) grading-model closeout + Course
Foundry implementation parity. No Canvas, no Savnac, no synthetic
students, no CS2. Date: 2026-08-12.

## 0. Repo SHAs

| Repo | Starting SHA | Ending SHA |
|---|---|---|
| `computer_science_1` | `e8e125f` | *(recorded at commit time, below)* |
| `course_foundry` | `ae1d330` | *(recorded at commit time, below)* |
| `jeremy_task_tracking` | `49ba67d` | unchanged (read-only this pass) |

## 1. Every previously-open grading decision, and the final decision made

| # | Decision | Final answer |
|---|---|---|
| A1 | Bonus-practice numeric mechanism | Up to 5 flat bonus points/week, 10 weekly-reinforcement weeks (2–5/7–8/10–13), posted as a 0-points-possible Canvas extra-credit object inside the Weekly Reinforcement Assignment group. Capped at 10 counted weeks (50 points) per semester. |
| A2 | Final 100% grade table | See §2 below. A4 gets its own 5% row; Attendance shrinks 10% → 5% to make room. |
| A3 | A4 (Show-and-Tell reflection) disposition | Own 5% "Show-and-Tell reflection" category — structurally identical to A3/A7 (weekly, ~10-pt, rubric-graded), and distinct from Fun Friday reflection (a professional_minds lesson tie-in) and the Friday feedback report (peer feedback given). |
| A4 | Drop-lowest policy | Drop lowest 1 for the six small weekly categories + Weekly Reinforcement Assignment (Canvas's native per-group rule). No drop for Coding Odyssey checkpoints, professional-pathway checkpoints, final reflection, attendance, course evaluation. |
| A5 | Canvas/Savnac submission-location mapping | One authoritative table in `docs/grading-model.md`, mirroring `course_foundry/cs1_desired_course.py`'s actual `_ASSIGNMENT_GROUPS`/per-category grading functions (not a second independently-maintained source of truth). |
| A6 | Automated-feedback/Marker pre-scoring boundary | Formalized: Marker inspects code/text + rubric criteria, runs mechanical pass/fail checks, produces a tentative pre-score with cited evidence, flags (never guesses) missing/ambiguous evidence. Professor enters the final score and retains sole authority over flagged items and qualitative axes (Explanation, Demonstrability). Student sees the pre-score immediately, labeled tentative. |
| A7 | Finals-policy verification | **Verified and closed.** SWOSU's Semester Exam Policies (`bulldog.swosu.edu/publications/handbooks/student/semester-exam.php`) impose no requirement that the final-exam-period activity be a traditional exam — silent on format. A5's reflection-paper-in-finals-slot is compliant as written. **Same search surfaced a real, separate finding**: the "dead days" rule (no graded assignment/activity in the three class days before finals) conflicts with Week 16's previously-graded weekly categories — fixed, see §9. |
| A8 | Attendance language | Syllabus and grading model now say one coherent thing: 5% of the course grade, gradebook-only, instructor-entered, no escalating-penalty/withdrawal-threshold language (that draft language is retired, not adopted). |

## 2. Final 100% grade table

| Category | Weight |
|---|---:|
| Monday Moment quiz | 6% |
| Wacky Wednesday reflection | 6% |
| Fun Friday reflection | 6% |
| Paired-programming report (A3) | 5% |
| Friday feedback report (A7) | 5% |
| Show-and-Tell reflection (A4) | 5% |
| Weekly reinforcement assignment | 25% |
| Coding Odyssey checkpoints | 15% |
| Final reflection paper (A5) | 10% |
| Professional pathway — Week 14 update | 5% |
| Professional pathway — Week 15 submission | 5% |
| Attendance & participation | 5% |
| Course evaluation | 2% |
| **Total** | **100%** |

Programming/technical work (Weekly reinforcement + Checkpoints) = 40% of
the course grade, more than double the next-largest category.

## 3. Bonus mechanism

See §1 (A1). Full rationale, Canvas mechanics, and the bound on the
mechanism's total grade effect (~3 percentage points at the cap):
`docs/grading-model.md`'s "Bonus mechanism" section. Implemented:
`course_foundry/cs1_desired_course.py`'s `_bonus_practice_grading`/
`_weekly_bonus_object`.

## 4. Drop-lowest policy

See §1 (A4) and `docs/grading-model.md`'s "Drop-lowest policy" table for
the full per-category breakdown. Uses Canvas's native "drop lowest N
scores" assignment-group rule — no custom machinery. **Not yet wired into
`course_foundry`'s `DesiredAssignmentGroup`/Imprint schema** — see §14
(remaining yellows).

## 5. A4 disposition

See §1 (A3) and `docs/grading-model.md`'s "A4 disposition" section (a
comparison table against Fun Friday reflection, Friday feedback report,
and Paired-programming report). Implemented: `_a4_grading` now sets
`assignment_group=_SHOW_AND_TELL_GROUP` and a real Friday `due_at`
(previously ungrouped and dateless).

## 6. Automated-feedback boundary

See §1 (A6) and `docs/grading-model.md`'s "Automated-feedback / Marker
pre-scoring boundary" section. This is a **policy document**, not new
code — it formalizes the existing Harbor → Guidepost → Marker → Coach
pipeline (`docs/course-ethos.md`) and the existing mechanical-vs-human
split (`docs/curriculum/judgment_toolkit.md` §1) into one explicit,
auditable workflow. No new Foundry code was needed or written for this
item; it is disclosed here as policy-only, not implied as implemented in
code.

## 7. Finals-policy verification result/source

**Closed, no adjustment needed** for the reflection-in-finals-slot
question. Source: `https://bulldog.swosu.edu/publications/handbooks/student/semester-exam.php`
(SWOSU Student Handbook, Semester Exam Policies) — fetched and quoted
directly 2026-08-12; the policy text covers scheduling, room assignment,
"no early finals," and Incomplete handling, and is silent on assessment
format. Cross-checked against the official Fall 2026 calendar
(`https://www.swosu.edu/calendar/files/2026-27-academic-calendar-unofficial.pdf`).

**New finding from the same search: dead-days compliance.** See §9.

## 8. Active-source drift repaired (Part B sweep)

| File | Stale content | Fix |
|---|---|---|
| `assignments/A1-weekly-coding-practice.md` | "Checkpoint weeks (6, 9, 14, 16)"; "not yet decided" bonus value | Fixed to "(6, 9, 14)" + Week 16 named as no-gate/no-graded-category; bonus mechanism filled in |
| `assignments/A2-coding-odyssey-project.md` | "Point values...not yet finalized" | Now states the final weights |
| `docs/grading-model.md` | "DRAFT PROPOSAL" header; "the textbook chapter supplies that week's concept"; all open-decision checkboxes | Rewritten as FINAL; textbook phrase corrected; every decision closed |
| `docs/course-ethos.md` | "percentages still open" | Marked finalized, dated |
| `planning/fall-2026-course-design.md` | Bonus value and Farkle content listed as open | Marked closed with citations |
| `docs/syllabus.md` | Old 68/10/20/2 weight table presented as current; punitive attendance TODO block | Replaced with final 13-row table; attendance language rewritten coherently |
| `docs/attendance.md` | 10%/10-point framing; "still blocked on university-policy confirmation" | Updated to 5%/5 points; blocker language removed (policy now finalized) |
| `rubrics/odyssey_gates/week-06_rubric.md`, `week-09_rubric.md` | "Weeks 14/16" / "Week 14/16 pair" implying a still-live Week 16 checkpoint | Corrected to Week 14 only, with an explicit Checkpoint-4-retired note |

Verified clean: no remaining `not yet decided` / `still open` / `DRAFT
PROPOSAL` / `not yet finalized` / `Weeks 14/16` hits in active source
(archive/ and historical `reports/*.md` excluded by design).

## 9. Foundry implementation changes (`course_foundry`)

All in `course_foundry/course_foundry/cs1_desired_course.py` unless noted.

1. **`_ASSIGNMENT_GROUPS`**: added `_SHOW_AND_TELL_GROUP` (5%), shrank
   `_ATTENDANCE_GROUP` 10% → 5%. Sum-to-100 assertion still holds (self-checking).
2. **`_a4_grading`**: now takes a `week` argument, sets
   `assignment_group=_SHOW_AND_TELL_GROUP` and `due_at=_fri_due_at(week)`
   (previously ungrouped and dateless by design, per the prompt's own
   still-open flag — now closed).
3. **`_CHECKPOINT_WEEKS`**: `{6, 9, 14, 16}` → `{6, 9, 14}` — the zombie
   Week-16 entry was already unreachable (Week 16's gate file is
   `status="retired"` and never reaches `_odyssey_gate_grading`), but is
   now also correct on its face, per the prompt's explicit "no zombie
   checkpoint" requirement.
4. **`_DEAD_DAYS_WEEKS = {16}`** + `_dead_days_not_graded(week)`: new,
   real institutional-compliance fix (§7's finding). Wired into
   `_odyssey_gate_grading`, `_pm_reading_grading`, `_pm_slides_grading`,
   and `_monday_moment_grading` (content still pushes, forced
   `not_graded`), and into `_weekly_a3_object`, `_weekly_a7_object`,
   `_weekly_a4_object` (skip the instance entirely for Week 16 — no
   separate content exists for those categories that week).
5. **`_bonus_practice_grading`/`_weekly_bonus_object`**: new. One optional
   Bonus Practice object per weekly-reinforcement week (2–5/7–8/10–13),
   `points_possible_override=0`, `assignment_group=_WEEKLY_REINFORCEMENT_GROUP`.
   Wired into `cs1_savnac_desired_course`'s per-week loop.
6. **`cs1_dry_run.py`**: updated the "intentionally omitted" footer —
   removed the two now-stale notes ("no numeric bonus value," "A4
   ungrouped") and replaced with the dead-days note.
7. **Attendance points fixed post-review** (§13a finding 1):
   `_gradebook_only_object(cs1_root, "docs/attendance.md", "Attendance & Participation", 10, ...)`
   → `5`, matching the shrunk 5% group weight. Caught by independent
   review, not by the original implementation pass — a real gap this
   report discloses rather than papers over.

## 10. Retired/no-gate semantics status

**Already correct before this pass** (prompt 019, 2026-08-12, earlier the
same day): `gate_status()` reads a machine-readable `**Gate status:**`
marker (`active`/`optional_no_gate`/`retired`) from each
`assignments/odyssey_gates/week-NN.md` file rather than sniffing file
existence or prose. Verified live: Week 15 = `optional_no_gate`, Week 16 =
`retired`, Week 17 = `active`. No further fix needed. This pass's
`_CHECKPOINT_WEEKS` fix (§9.3) is a separate, smaller correctness item in
the same neighborhood, not a re-fix of this mechanism.

## 11. Dry-run parity status

**Already correct before this pass** (prompt 019): `cs1_dry_run.py`
renders `cs1_savnac_desired_course`'s actual `DesiredCourse` object
verbatim (Section 3 of its output), not a pre-grading approximation. This
pass's only dry-run change was updating the static "intentionally
omitted" footer text (§9.6) to match the new dead-days behavior — the
rendering mechanism itself needed no fix.

## 12. Tests/commands run and results

All from `course_foundry/` using its `.venv` (Python 3.11.13; the
system's bare `python3` is 3.9.21 and cannot import this repo's pydantic
version — not a regression, matches the repo's own `pyproject.toml`
`requires-python = ">=3.11"`).

```
$ .venv/bin/python3 -m pytest -q
460 passed in 3.68s
```
(459 before the post-review attendance fix, §13a finding 1; 460 after
adding its regression test.)

24 tests in `tests/test_cs1_desired_course.py` (8 new, added this pass):
A4 group/due-date placement, bonus-object presence/absence by week type,
full Week-16 dead-days exemption (Monday Moment/PM pushed not_graded, A3/
A4/A7/bonus entirely absent), Week 15 unaffected (control), assignment-
groups sum to 100 with the new Show-and-Tell row, `_CHECKPOINT_WEEKS`
excludes 16, and the attendance-object points-vs-group-weight regression
test added after independent review caught the mismatch.

```
$ .venv/bin/ruff check course_foundry/cs1_desired_course.py course_foundry/cs1_dry_run.py \
    tests/test_cs1_desired_course.py tests/test_cs1_dry_run.py
All checks passed!
```
(Two pre-existing E501 lines this pass's own new/touched code neighbored
were fixed in passing; the repo's other 400+ pre-existing ruff findings in
unrelated files are untouched, out of scope.)

```
$ make task-check
make: *** No rule to make target 'task-check'.  Stop.
$ make check
make: *** No rule to make target 'check'.  Stop.
```
No Makefile in either repo (matches prior reports' findings — not new).

**Real dry run against the actual `computer_science_1` repo:**
```
$ .venv/bin/python3 -m course_foundry.cs1_dry_run --course-repo-path ~/git/computer_science_1
TOTAL: 16 modules, 327 objects -- by kind: {'page': 144, 'assignment': 152, 'file': 31}
```
Manually inspected sentinel weeks:

- **Week 1**: correctly absent from this adapter's output (out of scope
  by design — sourced from `semester_kickoff_week` instead, unrelated to
  this pass).
- **Week 2**: full weekly category set present and graded (Monday Moment
  10pts/6%, Wacky Wed reading+slides 6+4=10pts/6%, Fun Fri 10pts/6%, A3
  10pts/5%, A7 10pts/5%, A4 10pts/5%, Bonus Practice 0pts-possible/25%
  group, Odyssey gate 25pts/25% group) — all with real `due_at` values.
- **Week 6, 9, 14**: Coding Odyssey checkpoint object correctly lands in
  `assignment_group='Coding Odyssey checkpoints'` (15% group); weekly
  categories continue normally.
- **Week 13**: full weekly set + no checkpoint (correct — not a
  checkpoint week).
- **Week 15**: `optional_no_gate` — no Odyssey object; weekly categories
  (Monday Moment/PM/A3/A4/A7) still fully graded (confirms dead-days
  exemption is Week-16-only, not applied a week early).
- **Week 16**: `retired` gate (no Odyssey object, as before this pass);
  **every weekly category pushed `not_graded`** (Monday Moment, PM
  reading/slides) and **A3/A4/A7/Bonus Practice entirely absent** — the
  new dead-days fix, confirmed live against real content.
- **Week 17**: only the final gate/rubric object (`not_graded`,
  pre-existing, out of this pass's scope) — no chapter exam, as before.

Assignment groups (`plan.assignment_groups`) sum to exactly 100, with
`Show-and-Tell reflection: 5%` and `Attendance & participation: 5%` both
present.

```
$ git diff --check   (both repos)
(no output — clean)
```

## 13. Independent review

A fresh subagent with no prior exposure to this work was dispatched to
compare `docs/grading-model.md` against `cs1_desired_course.py`'s actual
behavior line-by-line, specifically hunting for contradictions between the
human-readable grading model and the machine-generated `DesiredCourse` —
not code style. It found real bugs, not style nits.

### 13a. Findings and disposition

| # | Finding | Verdict | Fix |
|---|---|---|---|
| 1 | Attendance object's `points_possible_override` was still hardcoded to `10` at the `_gradebook_only_object(...)` call site in `cs1_savnac_desired_course`, even though `_ASSIGNMENT_GROUPS` and `docs/attendance.md`'s own prose had already been updated to 5% — a real contradiction, live-verified in the dry run (`points_possible=10`) before the fix | **CONFIRMED, real bug** | Fixed: call-site argument `10` → `5`. Added regression test `test_attendance_object_matches_its_5_percent_group_weight`. Re-verified live: dry run now shows `points_possible=5`. |
| 2 | Drop-lowest policy section claimed "Canvas's native... rule — no custom machinery" without disclosing that `imprint.schema.DesiredAssignmentGroup` has no drop-lowest/rules field at all, so nothing pushes this end-to-end yet | **CONFIRMED, real disclosure gap** | `docs/grading-model.md`'s "Drop-lowest policy" section rewritten to state plainly that the mechanism is not yet pushed automatically and must be configured once by hand in Canvas after the initial Savnac push, citing this report's §14 as the tracked implementation yellow. |
| 3 | Both the module docstring and `grading-model.md` cite this report (014) before it existed on disk | **Ordering artifact, not a real issue** | This report exists now, as part of the same commit — resolved by construction. |
| 4 | Bonus cap (10 weeks/50 points) is honestly disclosed as workflow policy, not code-enforced | **Verified correct, no action needed** | Matches §14 item 2 below — already accurately disclosed. |
| 5 | A5 (Final reflection) is placed in the Week 16 Canvas module by the pre-existing canonicalization rule, but the submission-mapping table said "Once, Week 17" with no caveat | **CONFIRMED, real prose/code mismatch** (pre-existing design, newly-inaccurate prose) | Table row corrected to state the actual Week 16 module placement and why (no `due_at` is set, so this creates no Week-16 due-date/dead-days conflict, only a module-location note for a human reviewing the dry run). |
| 6 | Assignment-group weights, A4 disposition, Week 16 dead-days behavior (content pushed not_graded, A3/A4/A7/bonus entirely absent), Week 6 checkpoint mechanics, and the automated-feedback section's cited code (`PmRubricError`, `GateStatusError`, `_MONDAY_MOMENT_CRITERIA_BY_WEEK`) | **Verified correct, no action needed** | Spot-checked live against the real dry run; all matched. |

Findings 1 and 2 were real, and the kind of thing this review was
specifically asked to hunt for — both are now fixed and re-verified
against a fresh dry run and the full test suite (460 passed after the
fix, up from 459 before it).

## 14. Remaining yellows

1. **Drop-lowest is documented policy, not yet Foundry-encoded.** Canvas's
   native "drop lowest N scores" is an assignment-group-level setting;
   `imprint.schema.DesiredAssignmentGroup` (as currently used by this
   module) does not yet carry a drop-lowest field, so this pass's
   drop-lowest table is a **human-implementable Canvas configuration
   policy**, not something `cs1_savnac_desired_course` pushes
   automatically. This is a genuine, disclosed implementation gap — not an
   external-institutional-fact yellow — and is a reasonable candidate for
   a small follow-up prompt if Jeremy wants it auto-applied at push time
   rather than configured once by hand in Canvas after the initial push.
2. **The bonus-practice weekly/semester cap (10 weeks, 50 points) is
   policy, not code-enforced.** `_weekly_bonus_object` creates one
   0-points-possible bonus assignment per weekly-reinforcement week
   (10 total across the semester) — the cap is structurally satisfied by
   there being only 10 such objects to begin with, so a student cannot
   exceed 10 counted weeks by construction. The "up to 5 points" per
   instance is a grading instruction for whoever scores it (professor/
   Marker), not a Canvas-enforced ceiling on a single submission — same
   category of human-scored judgment as every other rubric in this
   course.
3. **The automated-feedback/Marker boundary (§6/A6) is a policy
   document, not new code.** No Marker/Coach code changed in this pass;
   it formalizes an already-real pipeline's intended behavior. Flagged
   explicitly, not silently implied as "implemented."

None of these three are external-institutional-fact or production-
credential blockers — they are implementation follow-ups a future prompt
could pick up if Jeremy wants tighter automation. They do not block a
Savnac candidate deployment: the grading model is coherent, the course
compiler represents it faithfully at push time, and every category that
should carry real points/grading does.

## 15. Readiness statement

CS1's curriculum and grading model are internally coherent, fully
implemented in `course_foundry`'s `DesiredCourse` compiler, and verified
against a real dry run of the actual `computer_science_1` repo content.
Every previously-open grading decision is closed. Every known
pre-Savnac source/adapter contradiction found by this pass (the
Week-16-checkpoint zombie reference, A4's ungrouped/undated placement, and
the newly-discovered dead-days compliance gap) is fixed and tested. No
required-textbook/ZyBooks/Deitel dependency resurfaced. No chapter exam.
No Week 15/16 zombie Odyssey gate. Optional bonus practice is truly
optional/additive and bounded.

**GO for the next step: CS1 Savnac candidate deployment**, with the three
disclosed implementation follow-ups in §14 noted for a future prompt, not
as blockers.

## Boundaries respected

No Savnac writes. No Canvas writes. No synthetic-student runs. No CS2
repo touched. No new curriculum content invented — the only new prose is
grading-policy/mapping documentation and a Foundry bonus-object body reuse
of an already-existing assignment file. No production credentials used.
