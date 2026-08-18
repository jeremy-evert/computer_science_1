# Prompt 105 — CS1 Week 2 technical-path incident: source-owned lesson entry point

**Status:** READY
**Owner:** assigned Golem (Codex), reviewed/accepted by Foreman
**Worksites (cross-repo, both explicitly authorized by this prompt, mirroring
Prompt 103's "shared Course Foundry repairs are allowed when necessary to
complete CS1 correctly" precedent):**
- `computer_science_1`, main checkout, already on branch
  `golem/105-week2-lesson-entry-point` — **operate directly here, do not
  create another branch.**
- `course_foundry`, via the isolated worktree at
  `/mnt/brandy_nvme/jevert/git/course_foundry.worktrees/103a-production-deploy-tool`
  (reused directory from a prior unit — already on a fresh branch
  `golem/105-week2-lesson-entry-point` off current `main`, tip `b074a6a`).

**Critical: never touch `/mnt/brandy_nvme/jevert/git/course_foundry` itself
(the bare path, no `.worktrees` in it).** A live `submission-listener.service`
runs against that exact directory with its own uncommitted in-flight state.
Confirm `pwd` shows the `.worktrees/103a-production-deploy-tool` path before
any write there. This mount also exposes sibling repositories
(`discrete_structures_and_critical_thinking`, `computer_architecture`,
`computer_science_2`, `professional_minds`, `jeremy_task_tracking`, etc.) —
**do not read or write any of them.** Your authority is exactly the two
worksites named above.

**Mode:** Work (mutating), isolated branches in both worksites, no live
Canvas credentials, no network calls of any kind.

## Why this matters

Jeremy reported a real launch-blocking incident (JTT `TASKS.md` §3, restated
here in full so you don't have to trust a summary):

> Week 2's active Odyssey Gate is live (Savnac course 1, assignment 151),
> but students have no visible starting point for the variables/expressions/
> types technical content — the gate cites `lessons/02-variables-expressions-
> types.md` only as a non-clickable source path, and neither the Week 2
> At-a-Glance page nor the Week 2 Monday page link to a student-facing
> lesson/presentation.

Foreman investigated first (read-only, no mutation) and confirmed the exact
shape of the gap directly in source, not by guessing:

1. `computer_science_1/assignments/odyssey_gates/week-02.md`'s own body
   contains the literal line `**Concept:** variables, expressions, types
   (\`lessons/02-variables-expressions-types.md\`).` — a bare backtick-quoted
   repo-relative path, not a link. This file's content becomes the gate
   assignment's live Canvas body verbatim (no code-side wrapping) — so this
   bare path is exactly what a student sees today.
2. `computer_science_1/planning/week-02.md` (the source `week_at_a_glance`/
   Monday-page content compiles from) also only cites
   `lessons/01-foundations-print-input.md` and
   `lessons/02-variables-expressions-types.md` as bare backtick paths in its
   "Weekly Focus" and "Monday" sections — same defect, same root cause.
3. A real, already-compiled, already-source-controlled entry point for this
   exact content already exists and is close to wired:
   `computer_science_1/presentations/beamer/week_02_mon/week02_mon.pdf`
   (the Week 2 Monday lecture deck). `course_foundry/course_foundry/
   cs1_desired_course.py`'s `_weekly_monday_deck_object(cs1_root, week)`
   (around line 1101) already turns this exact PDF into a Canvas File object
   titled `"Slides — Week 02 Monday (PDF)"` in Canvas Files folder
   `slides/week_02_mon` — **this function and its object already exist and
   are correct; do not duplicate them or create a second Canvas object for
   the same deck.** What's missing is (a) confirming this File object is
   actually wired into the Week 2 module's item order (not just floating in
   Canvas Files unreferenced), and (b) that nothing anywhere actually links
   *to* it — the gate and the day pages just cite a raw filesystem path.
4. This codebase already has a working, established mechanism for exactly
   this class of problem — a stable cross-reference token resolved at push
   time, not a hardcoded Canvas URL authored before the object exists.
   Read `course_foundry/course_foundry/load_adapters.py` around line 328
   (the `{{link:some_key}}` token substitution function) and
   `course_foundry/course_foundry/semester_kickoff_content_map.py` around
   line 584 for a real working example of a `{{link:...}}` token pointing at
   a deck object. `course_foundry/course_foundry/architecture_desired_course.py`
   around line 259-267 shows the accepted fallback behavior when a
   `{{link:...}}` token can't resolve (strip to plain text rather than ship
   a permanently-broken `<a href="{{link:...}}">` — Canvas strips unresolved
   `{{...}}` template syntax raw otherwise). Reuse this exact pattern; do not
   invent a second cross-reference mechanism.

This is deliberately scoped as a **Week 2 fix**, not a 17-week content-
authoring project: `_weekly_monday_deck_object`'s own docstring states only
Week 2 has a compiled deck on disk today — the other 13 weeks' decks are a
separate, not-yet-greenlit authoring effort, correctly out of scope here.

## Task

1. In `computer_science_1` (already on branch
   `golem/105-week2-lesson-entry-point`): edit
   `assignments/odyssey_gates/week-02.md`'s `**Concept:**` line and
   `planning/week-02.md`'s "Weekly Focus" and "Monday" sections to replace
   the bare `lessons/02-variables-expressions-types.md` (and, in
   `planning/week-02.md`'s Weekly Focus line only, the co-cited
   `lessons/01-foundations-print-input.md`) backtick-path citations with a
   real, clickable `{{link:...}}` token pointing at the Week 2 Monday slides
   deck object, choosing a token key consistent with whatever key naming
   convention `semester_kickoff_content_map.py`'s existing `{{link:
   monday_slides}}`-style examples use. Keep the surrounding prose readable
   — a student should see something like "this week's technical concept
   (variables, expressions, types) — see {{link:week02_monday_slides}}",
   not a raw token dropped mid-sentence with no framing.
2. In the `course_foundry` worktree: confirm (read the relevant module-
   assembly code, likely near where `_weekly_monday_deck_object`'s return
   value is folded into the Week 2 module's item list) that this File
   object is actually included in Week 2's live module item order, not only
   theoretically returned by the function. If it is already correctly wired
   into the module, say so explicitly and change nothing there. If it's
   missing from the module assembly, wire it in following the exact pattern
   A3/A4/A7's weekly objects already use in that same module list.
3. Confirm (read the resolution code, likely in `load_adapters.py` or
   wherever `push_course`/`imprint.reconcile` calls the substitution
   function) that a `{{link:...}}` token placed in `body_markdown` sourced
   from `assignments/odyssey_gates/week-02.md` and `planning/week-02.md`
   actually gets resolved against the right object's real key/slug at
   `cs1_savnac_desired_course` build time — i.e., that the gate object and
   the Week 2 day-page objects are built in an order (or two-pass process)
   where the deck's resolvable key exists before/when their `body_markdown`
   is substituted. If the existing token-resolution pass is a single global
   pass over the whole built course (as the kickoff/Architecture precedent
   suggests), this should just work with no code change beyond adding the
   token in the source markdown files from step 1 — confirm this by
   building the plan and reading the object's resolved `body_markdown`
   directly, don't assume.
4. Do not touch the gate's rubric, points (25 total, two-axis 15/10 split),
   `assignment_group`, `due_at`, or grading mechanics in any way — this unit
   is entry-point wiring only.
5. Do not create a second Canvas object for the same deck, and do not touch
   any week other than Week 2.

## Validation (acceptance test — the actual falsifiable check)

Build CS1's local plan (whatever CLI entrypoint `cs1_desired_course.py`
exposes for a local, no-network plan build — check its own `if __name__ ==
"__main__"`/CLI section or existing tests for the exact invocation, e.g.
something resembling `python -m course_foundry.cs1_desired_course plan` or a
direct Python call in a small script) and inspect the resulting Week 2
objects directly (no live Canvas call — this stays local/dry, exactly like
103A):

- The Odyssey Gate (Week 2) assignment's resolved `body_markdown` contains
  no literal `{{link:...}}` token text and no bare
  `lessons/02-variables-expressions-types.md` backtick path — it contains a
  real resolved reference (a Canvas-relative URL or equivalent resolved
  form) to the Week 2 Monday slides File object.
- The same is true for whatever object(s) `planning/week-02.md` compiles
  into (the Monday page / At-a-Glance content) for its
  `lessons/01-...`/`lessons/02-...` citations.
- The Week 2 module's item list (from the same local plan) includes the
  Monday slides File object exactly once — confirm no duplicate object was
  created.
- The gate's own rubric/points/grading fields are byte-identical to the
  pre-change plan for Week 2 (diff the plan JSON/repr before and after your
  change for just this field set) — proves you didn't touch grading while
  fixing wiring.

Run the existing course_foundry test suite scoped to
`tests/test_cs1_desired_course.py` and any `tests/test_week_at_a_glance.py`
cases touching Week 2/CS1 (`pytest tests/test_cs1_desired_course.py
tests/test_week_at_a_glance.py -k "week02 or week_02 or cs1"` or the
equivalent — use your own judgment on the exact `-k` filter after reading
the test file, do not guess a filter that silently matches nothing). If no
existing test actually exercises this new link-resolution behavior, add one
(a real assertion, not a change-detector) — this is required per
`spells/dispatch.md`'s "building one when none already exists is part of
the smallest correct change."

You will need to build a Python venv in the course_foundry worktree
(`python3 -m venv .venv && .venv/bin/pip install -e '.[dev]'`) exactly like
Prompt 103 Unit A did — the disposable/isolated worktree has no deps
pre-installed. This is expected, not a blocker; do it as part of the unit.

## Report / student walk (deliverable, not optional)

Write a plain-language **proposed student walk** in your final report: as a
Week 2 student who has never seen the repo, describe exactly what you would
click, in order, starting from the Week 2 module in Canvas, to reach the
technical lesson content and then the gate — using only the resolved
`body_markdown`/module structure you just verified locally, not
speculation. If the walk still requires knowing a repo path or hunting, say
so explicitly rather than declaring success.

## Evidence destination

`computer_science_1/sidecar/reports/105_week2_lesson_entry_point.md`:
source diff summary (both repos), the resolved `body_markdown` excerpts
proving the token resolved, the module item-order confirmation, the
rubric/points-unchanged diff, full test output, and the proposed student
walk. Do not write a second report in `course_foundry` — one coordinating
report in `computer_science_1` covering both repos' commits is correct,
matching Prompt 103's own precedent (`FOREMAN.md`'s "one coordinating
worksite... may point to all resulting commits").

## Forbidden

- Any live Canvas call, mocked-as-live or real, anywhere.
- Any change to the gate's rubric, points, `assignment_group`, `due_at`, or
  `_ODYSSEY_TWO_AXIS_CRITERIA`.
- Touching any week other than Week 2.
- Touching `/mnt/brandy_nvme/jevert/git/course_foundry` (the bare, live
  checkout) or any sibling repository other than `computer_science_1` and
  the named `course_foundry` worktree.
- Creating a second Canvas object/deck for the same content.
- `git add -A`/`git add .` in either repo — stage only the files this unit
  actually needs to change.
- Inventing a new `{{...}}`-style token syntax instead of reusing the
  existing `{{link:...}}` mechanism.

## On blocker

If the `{{link:...}}` resolution pass turns out not to already cover
`cs1_savnac_desired_course`'s gate/day-page objects (i.e. it's wired for
kickoff/Architecture but genuinely not for CS1's weekly content), that is a
real, reportable finding — implement the minimal wiring needed (reusing the
existing substitution function, not a new one) if it's a small, obviously
correct addition; if it looks larger than "call the existing function in
one more place," stop and report the exact gap instead of guessing at a
bigger redesign.

## Done when

- Both repos' diffs reviewed, tests passing (existing + any new assertion),
  local plan build shows a resolved (non-token, non-bare-path) reference in
  both the gate and the day-page content for Week 2 only;
- rubric/points/grading fields provably unchanged;
- report written with the proposed student walk;
- committed to `golem/105-week2-lesson-entry-point` in both repos (if `git
  commit` fails with "Author identity unknown", leave staged and say so
  explicitly, same as Prompt 103's precedent — Foreman will complete the
  commit after independent review). Do not push — Foreman pushes after
  review.
