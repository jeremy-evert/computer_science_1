# Prompt 015 — Reconcile CS1 source to the Reasoning Odyssey doctrine (Prompt 126 slice 1 of 4)

## Status

READY. Dispatched by the Foreman as the first course-specific slice of
`jeremy_task_tracking/prompts/126_cross_course_reasoning_odyssey_fabric.md`,
per its own execution rule: prove a small slice first, one course at a time.
CS1 goes first per Jeremy's 2026-08-15 standing priority.

Precedent this must follow exactly:
`jeremy_task_tracking/questions/answered_questions/003_cs1_a2_reasoning_odyssey_project_never_built.md`.

## Why

CS1 already has the real machinery the doctrine needs — `assignments/A2-coding-odyssey-project.md`
and sixteen weekly gates + rubrics in `assignments/odyssey_gates/` and
`rubrics/odyssey_gates/` (weeks 2–17). What it does not yet have is
reconciliation to the doctrine Jeremy actually decided:

- student-facing name is **Reasoning Odyssey**, not Coding Odyssey (source
  still says "Coding Odyssey / Choose Your Own Adventure" in A2's own title);
- A2 becomes the **Week-2 kickoff/home base** — orientation into the
  persistent project, not a single giant graded artifact;
- the **World Bible** must read as the living record integrated into the
  weekly gates, not a side concept;
- Weeks 6, 9, and 14 are the larger synthesis/checkpoint weeks (confirm the
  weekly gates for those three weeks already reflect that, or fix them);
- no second gradebook category — the existing weekly-reinforcement /
  checkpoint grading structure stays as-is; do not invent new point buckets.

## Scope — this leaf only

1. Read `assignments/A2-coding-odyssey-project.md` in full and reconcile its
   language/title to Reasoning Odyssey framing per the precedent above. Keep
   its role as Week-2 kickoff/home base explicit.
2. Read all sixteen files in `assignments/odyssey_gates/` (weeks 2–17) and
   their matching rubrics in `rubrics/odyssey_gates/`. For each week, verify
   it already has: guidance, a real assignment task, a rubric, a submission
   path, and points. Where "Coding Odyssey" language survives and should read
   "Reasoning Odyssey" per the precedent, fix it. Do not invent new weeks or
   remove existing ones.
3. Confirm (or correct) that Weeks 6, 9, 14 read as synthesis/checkpoint
   weeks per the precedent's description, without dropping their weekly
   points/rubric/submission contract.
4. Grep the rest of the repo (`lessons/`, `docs/`, `planning/`, other
   `assignments/`) for "Coding Odyssey" and reconcile *only* clear
   student-facing/doctrine references to Reasoning Odyssey — leave historical
   citations, provenance notes, and internal planning docs that are
   deliberately archival (e.g. `planning/coding-odyssey-arc-map.md`, already
   confirmed instructor-only by Prompt 101) alone unless the precedent
   clearly calls for the change there too. If genuinely unsure whether a hit
   is student-facing, list it in the report rather than guessing.
5. Do **not** touch the CS1 grading model / weights, do not create a new
   assignment category, do not touch Canvas/Savnac directly (source only —
   deployment is a separate later step), do not touch other courses.

## Do not

- Do not build a new Odyssey homework track alongside the real weekly gates.
- Do not rename "World Bible" itself — it is correct as-is per doctrine.
- Do not change point values or grading weights.
- Do not touch `course_metadata.yaml`'s grading block.
- Do not touch any other repo (course_foundry, computer_science_2, etc.).

## Deliverable

Write `reports/015_reasoning_odyssey_fabric_reconciliation.md` in this repo
(`computer_science_1`) listing: every file changed and why, every "Coding
Odyssey" hit found and whether it was changed or deliberately left (with
reason), confirmation that Weeks 6/9/14 read as checkpoint weeks, and
confirmation that grading weights were not touched.
