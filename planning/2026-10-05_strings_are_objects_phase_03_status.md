# Strings Are Objects — Phase 3 status

- Date: 2026-10-05
- Branch: `codex/strings-phase3`
- Original session starting point: `63ed7a07f890cb8abfad622a808c7591e1d29547`
  (`Build Phase 2 String Laboratory with object discovery and immutability`).
- Resume starting point: `0a4c1c4` (the committed BLOCKED Phase 3 record).
- Lesson implementation starting point after prerequisite incorporation:
  `e0d38569ce771301b94ca658ea41854d92e51f89`.
- Working tree was clean before prerequisite incorporation.
- Status: **COMPLETE**

## Prerequisites and incorporation breadcrumb

The original checkout lacked the Phase 1 Mad Lib and both requested prior-phase
status files. Phase 3 initially stopped and recorded BLOCKED in `0a4c1c4`.
No missing example or prior-phase record was manually recreated.

On the user's explicit prerequisite update, ancestry checks showed both supplied
commits missing. Incorporated them by cherry-pick into this branch:

| Original completed commit | Local cherry-pick | Result |
| --- | --- | --- |
| `b63c980f3a2c136d21a4cdf516172d8aa984b511` | `0ff9626` | Added Phase 1 Mad Lib and status |
| `e02224df1f43a61a88cc63ea053d32af3099bb23` | `e0d3856` | Added Phase 2 status; existing lab already matched its changes |

Cherry-picking preserves the changes under new commit IDs; it does not make the
original commit IDs ancestors of HEAD. Both local cherry-picks are ancestors.
Verified and read all four prerequisite files:

- `lessons/code/strings_mad_lib.py`
- `lessons/code/string_lab.py`
- `planning/2026-10-05_strings_are_objects_phase_01_status.md`
- `planning/2026-10-05_strings_are_objects_phase_02_status.md`

Both prior-phase statuses say COMPLETE, with blockers NONE. The old Phase 2
validation note describes its historical missing-Mad-Lib checkout; the
prerequisite incorporation above resolves that discrepancy for this branch.

## Files changed by Phase 3

- `lessons/06-strings.md` — expanded the placeholder into the canonical lesson.
- `planning/2026-10-05_strings_are_objects_phase_03_status.md` — updated the
  blocked record to this completed handoff.

Prerequisite additions are isolated in the two preceding cherry-pick commits;
Phase 3 did not modify either runnable example or prior-phase status.

## Commands and checks run

- `git status --short --branch`, `git rev-parse HEAD`, and `git log` — identified
  starting points and confirmed a clean initial checkout.
- `git merge-base --is-ancestor b63c980 HEAD` and the corresponding `e02224d`
  check — both initially missing.
- `git show --stat b63c980` and `git show --stat e02224d` — inspected scope.
- `git cherry-pick b63c980` then `git cherry-pick e02224d` — both succeeded.
- `cat` and `rg --files` — read required available context, both completed
  examples, both phase statuses, README, and the shared course design rules.
- `python3` validation heredoc using `ast`, `pathlib`, and `subprocess` — PASS:
  all four prerequisites exist; both relative lesson links resolve; fenced
  Python snippets parse and execute in lesson order with the Mad Lib's raw
  name supplied; indexing/slicing, search positions, result types, and
  immutability agree with the examples; Markdown fences balance and no
  trailing whitespace occurs.
- The validation ran `python3 lessons/code/string_lab.py` — PASS, exit 0;
  checked original and reassigned name output.
- The validation ran `python3 lessons/code/strings_mad_lib.py` with the six
  padded, mixed-case inputs recorded by Phase 1 — PASS, exit 0; checked
  cleaned name, place, and all lowercased story inputs.
- `git diff --check` and `git diff --cached --check` — PASS.
- Editorial review — confirmed all Phase 3 sections, return types, dot lookup
  versus calls, Unicode/index terminology, immutability, and explicitly
  conceptual cross-domain comparisons.

## Decisions made

Used the actual `lessons/code/` artifacts as the source of truth. Kept the
Mad Lib hook, laboratory investigation, and recurring question together as
one teaching arc. Added indexing and slicing without changing the demos.
Explained reassignment as changing a variable's reference rather than a
string's contents; did not promise fresh allocation for every method call.

Distinguished methods from attributes and module functions. Cisco IOS CLI
is explicitly not Python-style dot notation. Network automation method
names must come from actual library documentation. Organizational and policy
hierarchies are labeled analogies; APIs are not all Python object interfaces.

Practice and the exit question are supporting activities, with no added graded
deadline or Object Detective assignment. Any discoveries used in the existing
weekly gate go in its shared graded discussion, visible to classmates.
Preserved the historical-materials note. No unrelated cleanup, Beamer source,
Phase 4 implementation, push, or merge.

## Breadcrumbs for Phase 4

Begin Phase 4 only in a later session. Read the canonical lesson, both examples,
all three phase status files, lesson map, and execution plan. The prerequisite
commit mapping above explains why the original IDs need not be ancestors.

Use the Mad Lib's six-input story and raw/cleaned name transition, the lab's
exact mixed-case padded text, its four return types, the prefix/suffix contrast,
and the two-step immutability example. Keep the recurring question:
“What is this thing, and what can it do?” Preserve the lesson's explicit
boundaries for Cisco, conceptual hierarchies, and APIs.

Inspect existing presentation conventions before choosing a Beamer location;
`presentations/beamer/README.md` exists. Phase 3 did not create presentation
files or settle the deck layout. Follow Phase 4's timing and compilation
requirements in the execution plan. Object Detective remains deferred.

## Blockers

NONE for completed Phase 3 after the user-authorized prerequisite incorporation.
Context limitations remain documented: `../AGENTS.md` and
`planning/2026-10-05_strings_are_objects_breadcrumb_protocol.md` are absent.
They were not invented. Used the available repository instructions, course
ethos, course design rules, execution plan, and the user's explicit handoff
requirements to continue as directed.
