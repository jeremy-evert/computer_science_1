# Report 005 — Apply Report 002's Pre-Semester Decisions

## Summary

Jeremy answered all six items from `reports/002_pre_semester_readiness_and_literature_audit.md`'s
"Decisions Jeremy Must Make" section (drafted with ChatGPT, pasted into a
Claude session 2026-07-22; explicitly **not final/locked**, but concrete
enough to apply now). This report is the completion record for
`prompts/005_apply_pre_semester_decisions.md`, which applied those six
answers to `planning/`, `assignments/`, `ROADMAP.md`, `START_HERE.md`,
`prompts/README.md`, and one shared method doc in the sibling
`course_foundry` repo. The durable cross-repo decision log entry is
`jeremy_task_tracking/DECISIONS.md`'s 2026-07-22 entry.

Report 002's lower-priority, explicitly-unaddressed item — whether to move
Coding Odyssey checkpoint 1 from Week 9 to Week 10 — was **not** answered in
Jeremy's pasted decisions and was left alone here rather than guessed at.

## Decisions applied

### 1. Weeks 5–6 pacing

Kept the overall sequence. `planning/week-06.md`'s Weekly Focus, Monday
tie-in, and Due-this-week lines were rewritten so functions read as a
brief, ungraded preview only — full functions instruction and grading still
start Week 7 (`planning/week-07.md`, unchanged, already said "chapter 6").
No other unit was compressed, per the decision's explicit instruction.

### 2. Holiday policy — Thanksgiving

`planning/week-15.md`'s Status changed from "Wed+Fri holiday — only Monday
meets" to "fully asynchronous week (instructor travel)" — Jeremy is out of
the country that week, so Monday doesn't meet live either. Added the
Nov-1 load-by date, the "tell students in advance" language, and reframed
Weekly Focus/Due-this-week around independent portfolio completion (see
item 6) plus Coding Odyssey work. The two Wed/Fri Professional Minds "book
of record" entries were kept as record-only (already the pre-existing
pattern) with an explicit note that they're intentionally not force-recorded,
per the "cut the weakest content first" instruction.

Monday-holiday, Friday-holiday, and finals-week policies were **not**
touched, per the decision's explicit "keep the existing policies" language.

Because this is a reusable status type, not a CS1-only one-off, added
**"fully asynchronous week (instructor travel)"** as a new status alongside
the existing four in `course_foundry/planning/course-development-flow.md`
Steps 1, 6, and 7's status enum, generalized (lead-time target, "cut
weakest content first," "stage completion of already-begun work, not new
artifacts") rather than hardcoded to Thanksgiving.

### 3. Content-authoring cadence

This decision is process/sequencing, not a specific week's content, so it
was recorded in `ROADMAP.md`'s "Next step" section rather than edited into
`planning/`: Fall 2026 production is scoped to CS1, CS2, and Discrete
Structures and Critical Thinking only (SE, ML, AI Fluency 2–5 deferred to
spring); CS1 Week 2 is the pipeline test before the rest of CS1 is run
through the same process; CS2 and Discrete Structures follow; one shared AI
Fluency 1 serves all three. Also recorded in
`jeremy_task_tracking/DECISIONS.md` since it governs sibling repos
(`computer_science_2`, `discrete_structures_and_critical_thinking`,
`ai_fluency`) this repo doesn't own.

### 4. AI I doc fidelity

`ROADMAP.md` item 5 (source-availability gap) rewritten: the AI I document
is still not located on disk, but this is now explicitly **not a blocker**
— `ai_fluency` is the authoritative source going forward, scoped to AI
Fluency 1 only. `START_HERE.md` and `prompts/README.md` had stale language
treating the missing document (and the nonexistent
`drive_raw_pull_2026-07-14/` export) as required reading/an open blocker;
both softened to point at `ai_fluency` directly.

**Not done:** no edits to `ai_fluency`'s own docs. That repo's README
already describes AI II–V architecture work (reports 008–010) that predates
this scope decision — reconciling those against "AI Fluency 1 only for
Fall 2026" is flagged as follow-up, not assumed to already match.

### 5. Online section scope

Recorded as a new item 6 in `ROADMAP.md`'s "Real gaps" section: the section
is in scope, sharing CS1's Canvas structure, with the check-in/
disengagement-check system's shape defined (three brief Mon/Wed/Fri
check-ins, piggybacked on existing activities, graded for completion; a
rolling 7-day disengagement check with an auto-reminder then a single
instructor report) but **not built**. This is explicitly a `course_foundry`/
Harbor build (new Canvas items, section-scoped assignments, an automation
layer) — out of scope for a planning-file application pass, per the
prompt's own requirement not to build it here.

### 6. Week 16 redistribution

- `planning/week-01.md` — added an explicit note tying Wednesday/Friday's
  existing degree-check/career content to `assignments/A6-professional-pathway-artifacts.md`'s
  baseline artifacts, and pointing at `semester_kickoff_week`'s A01–A09 set
  as the fuller source (not yet wired as CS1 Week 1's actual content
  source — that's a separate, already-tracked task per
  `jeremy_task_tracking/DECISIONS.md`'s 2026-07-20 entry, not done here).
- `planning/week-14.md` — added a mid-semester update touchpoint (resume,
  GitHub/LinkedIn, dream-job research, skill-gap analysis, degree plan)
  tied to the week's existing GitHub/tools content, explicitly framed as
  "update," not new artifacts.
- `planning/week-15.md` — reframed as the portfolio's completion/submission
  week (see item 2).
- `planning/week-16.md` — removed the 7-artifact professional-pathway set
  from Weekly Focus and Due-this-week; kept Coding Odyssey checkpoint 3,
  full show-and-tell, and the final-reflection kickoff, with an optional
  brief AI Fluency 1 reflection tie-in per the decision text.
- `assignments/A6-professional-pathway-artifacts.md` — added a "Fall 2026
  staging" section documenting the three-stage timeline (Week 1 baseline /
  Week 14 update / Week 15 completion) and stating explicitly that Week 16
  no longer carries this assignment.

## Files changed

- `prompts/005_apply_pre_semester_decisions.md` (new)
- `reports/005_apply_pre_semester_decisions.md` (new, this file)
- `planning/week-01.md`
- `planning/week-06.md`
- `planning/week-14.md`
- `planning/week-15.md`
- `planning/week-16.md`
- `assignments/A6-professional-pathway-artifacts.md`
- `ROADMAP.md`
- `START_HERE.md`
- `prompts/README.md`
- `../course_foundry/planning/course-development-flow.md` (sibling repo,
  own commit)
- `../jeremy_task_tracking/DECISIONS.md` (sibling repo, own commit)

No changes made to `lessons/`, `quizzes/`, `docs/`, `professional_minds/`,
or `ai_fluency/` content — none of the six decisions required them.
`course_foundry/load_adapters.py` and
`course_foundry/semester_kickoff_content_map.py` were left untouched per
the prompt's explicit instruction (pre-existing unrelated uncommitted work
from another session).

## Commands run

Mostly `Read`/`Edit`/`Write` tool calls, plus:

```bash
git status --short --branch          # computer_science_1, course_foundry, jeremy_task_tracking
find /mnt/brandy_nvme/jevert/git -maxdepth 1 -type d
grep -n "^## 20" /mnt/brandy_nvme/jevert/git/jeremy_task_tracking/DECISIONS.md
```

No test suite exists for this repo's markdown content; no `make
task-check`/`make check` targets are defined here (confirmed by their
absence from prior reports and this repo's own file listing — no
`Makefile` present).

## Known limitations

- These are explicitly **not final decisions** — Jeremy's own framing.
  Treat this pass as a real, committed revision that's still open to
  further adjustment, not a closed door.
- Report 002's Week 9 checkpoint-timing question remains unresolved —
  intentionally not answered here.
- The online-section attendance/check-in system (Decision 5) is scoped and
  documented but not built — a distinct, larger `course_foundry` task.
- `ai_fluency`'s own architecture docs (reports 008–010, describing AI
  II–V work) were not reconciled against the "AI Fluency 1 only, three
  fall courses" scope decision — flagged, not fixed.
- CS1's `planning/week-01.md` still doesn't source its content from
  `semester_kickoff_week` directly (a pre-existing, separately tracked
  gap per `jeremy_task_tracking/DECISIONS.md` 2026-07-20) — this pass only
  added a pointer, it didn't do that migration.
- `course_foundry/planning/course-development-flow.md`'s new "fully
  asynchronous week" status type has one real usage so far (CS1 Week 15).
  It hasn't been exercised by a second course yet, so the generalization is
  informed by one data point.

## Ready-for-review status

Ready for Jeremy's review. `reports/006_pre_semester_decisions_recheck.md`
re-audits the planner against these six applied decisions and gives a
readiness verdict for further Canvas/Savnac loading.
