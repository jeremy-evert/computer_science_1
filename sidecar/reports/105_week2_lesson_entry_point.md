# Prompt 105 — Week 2 lesson entry point

## Scope and summary

- Prompt: `sidecar/prompts/105_week2_lesson_entry_point.md`
- Worksites: `computer_science_1` and the authorized isolated
  `course_foundry.worktrees/103a-production-deploy-tool` worktree only.
- CS1's Week 2 Odyssey Gate, Weekly Focus, and Monday guidance now point to
  the single Week 2 Monday deck through the source-owned
  `{{link:week02_monday_slides}}` token.
- Course Foundry resolves that established token against the existing
  `Slides — Week 02 Monday (PDF)` module File item immediately before both
  adapter and unified-deployer reconciliation. No duplicate File object is
  created.

## Source changes

`computer_science_1`:

- `assignments/odyssey_gates/week-02.md`: replaces the bare Week 2 lesson
  path in the Concept line with a readable Markdown link using the token.
- `planning/week-02.md`: replaces both Weekly Focus lesson-path citations
  and adds the same student-facing Monday link.

`course_foundry` worktree:

- `course_foundry/cs1_reference_links.py`: replaces the prior literal-path
  canary with the reusable `{{link:key}}` resolver and the
  `week02_monday_slides` -> existing deck-title mapping. Missing live links
  become readable plain text, never raw template syntax or a broken href.
- `course_foundry/load_adapters.py`, `sync_adapters.py`, and
  `savnac_deploy.py`: invoke the resolver before reconciliation.
- `tests/test_cs1_reference_links.py`: asserts token resolution, one deck
  module item, and unchanged gate grading metadata.

## Local plan evidence

The course builder already appends `_weekly_monday_deck_object(...)` once
to each ready week's module list. The isolated Week 2 local plan used the
real edited CS1 Markdown plus the actual Week 2 gate grading helper and
the resolver's local URL map. Its resolved excerpts were:

```text
types) — see [the Week 2 Monday technical slides](/courses/1/modules/items/4242).
[the Week 2 Monday technical slides](/courses/1/modules/items/4242) for the
module count: 1
grading unchanged: True
```

There were no literal `{{link:...}}` tokens or backtick lesson paths in the
resolved gate/Week 2 page bodies. The test URL is a local stand-in for the
existing live File module item's `html_url`; no Canvas call was made.

The full production-plan builder also reads `professional_minds` and
`ai_fluency` sibling repositories. Those paths were outside this prompt's
explicit two-worksite authority, so that full build was not run. The focused
tests use synthetic local sibling fixtures and the direct Week 2 local plan
above uses only the authorized CS1 source.

## Grading invariance

The local assertion compared the Week 2 gate's `submission_types`,
`grading_type`, `points_possible`, `assignment_group`, `due_at`, and rubric
criteria before and after substitution. They were identical. The change
does not edit the rubric, 25-point total, 15/10 split, assignment group, due
date, or grading helper.

## Validation

Passing focused suite:

```text
============================= test session starts ==============================
platform linux -- Python 3.11.2, pytest-9.1.1, pluggy-1.6.0
rootdir: /mnt/brandy_nvme/jevert/git/course_foundry.worktrees/103a-production-deploy-tool
configfile: pyproject.toml
plugins: anyio-4.14.2, langsmith-0.11.0
collected 40 items

tests/test_cs1_desired_course.py .................................       [ 82%]
tests/test_cs1_reference_links.py ..                                     [ 87%]
tests/test_cs1_savnac_adapters.py .....                                  [100%]

============================== 40 passed in 0.42s ==============================
```

The requested Week-at-a-Glance test selection was attempted but could not
run from the isolated worktree: its scripts hard-code CSV paths under
`/mnt/brandy_nvme/jevert/git/course_foundry.worktrees/course_foundry/...`,
which does not exist and is outside the authorized worksites. It failed
with `FileNotFoundError` before exercising Week 2. No workaround that would
read another checkout was used.

The required editable install command was attempted. It could not complete
because the dependency `harbor @ git+https://github.com/jeremy-evert/harbor.git`
was unavailable (`fatal: could not read Username for 'https://github.com'`).
The existing local virtual environment still ran the passing focused suite;
`ruff` was not installed, so its check was unavailable.

`git diff --check` passed in both worktrees.

`make task-check` and `make check` were unavailable in both worktrees:

```text
/bin/bash: line 1: make: command not found
```

## Proposed student walk

1. Open the **Week 2: Learning Science** module in Canvas.
2. Click **Slides — Week 02 Monday (PDF)**, the single File item in that
   module, to open the technical walkthrough covering run/read/change
   Python, `print`/`input`, variables, expressions, and types.
3. Return to Week 2 and click the **week-02** Odyssey Gate assignment.
   Its Concept link also opens the same Monday slides if the student needs
   the walkthrough again.
4. Complete and submit the gate's short world-state program.

The Week 2 At-a-Glance/Monday source also links to the same deck after
resolution; no repo path or filesystem hunting is required.

## Commits and status

- Course Foundry implementation/test commit: `c99314d` —
  `Wire Week 2 slides link tokens for CS1`.
- CS1 source and this coordinating report are staged but uncommitted because
  this environment has no configured Git author identity. Per the prompt,
  they are left staged for Foreman review/commit.
- No push was attempted (Foreman pushes after review).
- AGENTS.md: shared instructions followed; Course Foundry repo-local
  instructions reviewed. CS1 has no repo-local `AGENTS.md`.
- Final CS1 status retains the pre-existing untracked `sidecar/raw/`
  untouched, plus the staged source/report files.

## Foreman verification (independent, this session)

Reviewed the full diff in both repos by hand.

- `assignments/odyssey_gates/week-02.md` / `planning/week-02.md`: matches
  spec, readable prose, no grading fields touched — confirmed by diff.
- `cs1_reference_links.py`'s rewrite from the old Prompt-101 literal-string
  `resolve_week02_gate_references` (3 hardcoded citations, including two
  `docs/curriculum/judgment_toolkit.md` §1/§5 links) to the generic
  `{{link:key}}` resolver looked like a possible regression at first read.
  Checked: the old function was never wired into the standing reconcile
  path (`load_adapters.py`/`sync_adapters.py`/`savnac_deploy.py`) on main
  before this unit — its only caller was a completed one-off script,
  `course_foundry/runs/2026-08-14_prompt101_plaintext_source_references/
  live_push.py` (a historical, already-executed live push, not part of any
  standing flow, not pytest-collected). That script's import now breaks
  (the old function name is gone) — a disclosed, low-consequence loose end
  (it will not be rerun), not a functional regression to any live path.
  The Judgment Toolkit §1/§5 citations remain unchanged, literal
  (unresolved) text in `week-02.md` — pre-existing state, outside this
  unit's Week-2-slides scope.
- **Real gap found and fixed as declared Foreman tiny-work**: the golem
  wired `resolve_cs1_link_tokens` into `savnac_deploy.py`,
  `load_adapters.py`, and `sync_adapters.py`, but not into this session's
  own `production_deploy.py` (Prompt 103 Unit A) — a real production push
  today would have shipped the literal `{{link:week02_monday_slides}}`
  token text unresolved to students. Added the identical 5-line pattern
  already reviewed in `savnac_deploy.py`'s `main()`. Re-ran the focused
  suite (`test_cs1_desired_course.py`, `test_cs1_reference_links.py`,
  `test_cs1_savnac_adapters.py`, `test_production_deploy.py`): 47/47 green.
  Full `tests/` suite: 89 failed / 652 passed — same known worktree-
  relative-sibling-path artifact already documented in the 103A report,
  unchanged by this diff (spot-checked one failure directly: still the
  `course_foundry.worktrees/...` vs real `git/...` path mismatch).
- Committed CS1's staged files under the existing configured host Git
  identity (the golem's container lacked one; the host does not).

## Next recommended prompt

Both repos' diffs are reviewed and committed on
`golem/105-week2-lesson-entry-point`
(`computer_science_1` + `course_foundry` worktree, commits `c99314d` +
`22b895a`). Not yet merged to either `main` or pushed — pending this
report's promotion. After merge: run the authorized Savnac review workflow
to confirm the existing Week 2 File item supplies its live URL and the
Week 2 source-derived pages resolve correctly against real Savnac (dry-run
first, matching the standing discipline), then revisit the still-open CS1
online/f2f divergence decision before any production `--confirm-live`.
