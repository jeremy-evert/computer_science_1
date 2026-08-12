# Report 012 — CS1 pre-Savnac source reconciliation

**Prompt:** `jeremy_task_tracking/codex_prompts/018_cs1_pre_savnac_source_reconciliation.md`
**Scope:** Fall 2026 COMSC 1033 (CS1) source-of-truth reconciliation only.
No Canvas, Savnac, production ZyBooks, or student-data writes.
**Date:** 2026-08-12.

## Context this pass executed against

Prompt 018 was written 2026-08-06-ish, before a same-day 2026-08-11
reversal that briefly made ZyBooks the required/primary graded-practice
track (prompt 049). That reversal was itself superseded 2026-08-12: after
slurping ZyBooks content and digging into course design, real gaps were
found and open-source CS50P was found to cover the ground better. CS1 is
now built around an open-source core — not ZyBooks, not Deitel. Jeremy
confirmed directly: "continue with 018." This report executes 018's §4
("no required textbook or external course") as written, and additionally
walks back the 2026-08-11 ZyBooks-first drift that landed in
`course_metadata.yaml` and `planning/zybooks-assignment-map.md` between
018 being written and being executed.

## A — Decision implementation receipt

| Pinned decision | Active files changed | What changed | Remaining caveat |
|---|---|---|---|
| 1. Week 1 = no programming; C01 moves to Week 2 | `planning/week-01.md`, `planning/week-02.md`, `planning/block-map.md`, `docs/syllabus.md`, `planning/fall-2026-course-design.md`, `lessons/01-foundations-print-input.md` | Removed all `print`/`input`/first-program/paired-programming/Hello-World/Odyssey content from Week 1; moved the on-ramp (C01 + basic I/O) into Week 2 alongside variables/expressions/types | None — clean |
| 2. Odyssey remains required spine, no parallel required textbook track | `assignments/A1-weekly-coding-practice.md` | Already true pre-pass (2026-07-27 reconciliation); tightened wording to remove textbook-chapter framing | None |
| 3. Standalone problems become optional bonus | `assignments/A1-weekly-coding-practice.md`, `assignments/A2-coding-odyssey-project.md`, `docs/grading-model.md`, `docs/syllabus.md` | Added explicit optional-bonus-practice policy: never required, never reduces base grade, earned bonus is kept even after satisfying the Odyssey gate | **No numeric point value invented** — flagged as an open decision in `docs/grading-model.md` and `planning/fall-2026-course-design.md`, per the prompt's explicit instruction not to guess a number |
| 4. No required textbook/external course; ZyBooks/Deitel optional; CS50P recommended | `docs/syllabus.md`, `course_metadata.yaml`, `planning/fall-2026-course-design.md`, `planning/zybooks-assignment-map.md`, `lessons/02-variables-expressions-types.md`, new `docs/curriculum/recommended-resources.md` | Removed Deitel-as-required-text and the zyBooks-chapter-numbering-convention blocks from the syllabus; walked back `course_metadata.yaml`'s 2026-08-11 ZyBooks-required textbook block to `required: false`/historical-optional with full provenance kept; marked `planning/zybooks-assignment-map.md` superseded (not deleted — nothing in it was ever created live); created the week-level CS50P resource map the prompt asked for | Historical `lessons/03`–`lessons/09` "Before class" sections were not individually audited line-by-line for residual Deitel-required phrasing beyond the confirmed `lessons/02` instance (grep found no other `Read Deitel`/`assigned text` matches, so this is believed complete, not merely assumed) |
| 5. Files/persistence (CSV/JSON/Markdown) stays CS1 core | *(no change needed)* | Already correctly pinned per Report 011 Section A (C09); confirmed still intact, added to the new resource map as an integrated-not-isolated capability | None |
| 6. Kill mandatory inheritance/class hierarchy | `assignments/A2-coding-odyssey-project.md`, `planning/coding-odyssey-arc-map.md` | Removed "at least one class hierarchy" from both files (Report 011's flagged, not-yet-fixed item); replaced with the prompt's suggested C08 wording: meaningful classes/objects with state/behavior and at least one meaningful interaction | None — clean |
| 7. Week 14 = Git week, not a new build sprint | `planning/week-14.md`, `assignments/odyssey_gates/week-14.md` (already compliant), `docs/curriculum/judgment_toolkit.md` | Added explicit "building is done by Week 13" framing to Week 14; Checkpoint 3 was already framed as a Full Trail Debrief on existing code, not a new deadline — light reinforcement only | None |
| 8. Week 15 = Thanksgiving, fully async | *(no change needed)* | Already correctly pinned; confirmed no drift | None |
| 9. Week 16 = Farkle/ML fun week | `planning/week-16.md`, `assignments/odyssey_gates/week-16.md`, `rubrics/odyssey_gates/week-16_rubric.md`, `assignments/A2-coding-odyssey-project.md`, `docs/curriculum/judgment_toolkit.md`, `planning/coding-odyssey-arc-map.md`, `docs/syllabus.md`, `planning/block-map.md`, `docs/curriculum/recommended-resources.md` | Retired the old Checkpoint 4 ("final creative pass") and Decide/Compare #2 (capstone) from Week 16; moved Decide/Compare #2 to Week 13 alongside the real build culmination; rewrote Week 16's planning file, gate, and rubric to describe the Farkle/ML applied fun week with no Odyssey coding gate | Full Farkle/ML lesson content itself was **not authored** in this pass — flagged as a follow-up authoring task in every file that references it, consistent with "this pass exists to make the source coherent, not to add another design layer" |
| 10. Week 17 = reflection, no chapter exam | `planning/week-17-finals.md` | Removed the "chapter exam if used" line; noted `quizzes/Q2-chapter-exam.md` is retained as a historical reusable template, not an active requirement | None |
| 11. Report 011 six/seven fix | `reports/011_cs1_resource_coverage_matrix.csv`, `reports/011_cs1_resource_coverage_matrix.json` | Both "six C-ids at 3" → "seven C-ids at 3" (the Markdown report already said seven; only the CSV/JSON summary prose had the typo) | None — verified both files now say seven consistently |
| 12a. Week 9 collections drift | `planning/block-map.md` | Found and fixed: the Monday-lecture-package table (L08) said "Collections: lists and dictionaries" at Week 9 — contradicted the pinned Week 9 = strings-continued / Week 10 = collections-begin sequence, which every `planning/week-NN.md` file already had correct. Fixed L08/L09/L10 topic labels to match | None — `planning/week-NN.md` files needed no change here, only `block-map.md` |
| 12b. Week 3/chapter citations | `planning/week-02.md` through `planning/week-13.md` (10 files) | Removed all "chapter N" citations from active weekly `Due this week` sections, replaced with topic/capability language, per "now that no textbook/chapter numbering system is required, prefer topic/capability language" | None — the Week 3 "chapter 3 vs chapter 4" mismatch that reports 008/011/zybooks-assignment-map documented is now moot, since no chapter citation remains in `week-03.md` at all |

## B — Final semester spine

| Week | Human/course purpose | Technical capability | Odyssey role | Resource role | Required/optional evidence |
|---|---|---|---|---|---|
| 1 | Success Foundations (class/semester, degree, career) | **None — no programming** | None | None | Getting-to-know-you quiz only |
| 2 | Technical on-ramp begins | Run/read/change Python; `print`/`input`; variables, expressions, types | Genre pick, founding charter, first gate | CS50P Weeks 0-1 (recommended) | Odyssey gate (required) |
| 3 | — | Conversion/formatting; branching intro | Gate | CS50P Weeks 1-2 (recommended) | Odyssey gate (required) |
| 4 | — | Branching / decisions | Gate | CS50P Week 2 (recommended) | Odyssey gate (required) |
| 5 | — | Loops / repetition | Gate | CS50P Week 3 (recommended) | Odyssey gate (required) |
| 6 | — | Loops consolidation | Checkpoint 1 (baby project, light) | — | Checkpoint (required) |
| 7 | — | Functions / decomposition | Gate + passing unit test | CS50P Weeks 4-5 (recommended) | Odyssey gate (required) |
| 8 | — | Strings / text | Gate | CS50P Week 7 (recommended) | Odyssey gate (required) |
| 9 | — | Strings continued | Checkpoint 2 (first real pass) | — | Checkpoint (required) |
| 10 | — | Lists / collections begin | Gate + pair session | Python docs/PY4E (recommended) | Odyssey gate (required) |
| 11 | Technical judgment | Dictionaries / organized data | Gate + Decide/Compare #1 | Python docs/PY4E (recommended) | Odyssey gate (required) |
| 12 | — | Classes / objects round 1 | Gate | CS50P Week 8 (recommended) | Odyssey gate (required) |
| 13 | Build culminates | Classes / objects round 2, modules, interactions | Gate + capstone Decide/Compare #2 | CS50P Week 8 (recommended) | Odyssey gate (required) |
| 14 | Professional-pathway mid-update | Git/GitHub/collaboration/AI-aware workflow | Checkpoint 3 (Full Trail Debrief, Git receipt on existing code — not new build) | GitHub Skills + GitHub Docs (recommended) | Checkpoint (required) |
| 15 | Thanksgiving, fully async | No new technical concept | Optional cleanup only | — | Professional-pathway portfolio submission (required) |
| 16 | Applied fun | Farkle/ML — consumes CS1 core, no RL math required | No gate (retired) | Historical archive reuse (follow-up authoring) | None new required |
| 17 | Reflection / closure | No new technical material | Final Debrief + Judgment Log checkpoint 3 | — | Final reflection + final portfolio (evidence/receipt) |

## C — Resource policy

| Resource | Required? | Student cost | Use in course | Bonus-practice role | Publication/reuse note |
|---|---|---|---|---|---|
| Jeremy's own lectures/Odyssey gates | Yes | $0 | Required course-owned spine | N/A | Original content |
| CS50P | No — recommended | $0 to read/watch; free CS50 ID only for autograder | Concept/notes support, mapped to our weeks | Selected problems, week-aligned only, never a whole problem set | CC BY-NC-SA 4.0; link only, no body content rehosted |
| Python official docs | No — recommended | $0 | Reference layer | N/A | PSF License/0BSD; link only |
| GitHub Skills / GitHub Docs | No — recommended for Week 14 | $0 (free GitHub account for the hands-on exercise) | Git/AI-aware-coding hole-fillers | N/A | MIT / CC BY 4.0 |
| Deitel *Intro to Python...* | No — optional suggested reading only | Student cost if purchased | None required | N/A | Historical citations preserved in `lessons/02`, `docs/syllabus.md`; not deleted |
| ZyBooks (`SWOSUCOMSC1033Fall2026`) | No — historical/optional/legacy only | N/A (not adopted for grading) | None required | N/A | Adoption metadata preserved in `course_metadata.yaml` with `required: false` and full provenance; `planning/zybooks-assignment-map.md` marked superseded, not deleted |
| Standalone practice problems (instructor/CS50P/vetted open) | No — optional | $0 | Optional bonus-credit practice | Additive, kept even after Odyssey requirement is met | No exercise text copied; link only. Point value not yet decided (flagged) |

## D — Stale-reference scan

| Search/claim | Remaining active occurrences | Why acceptable or what was fixed |
|---|---|---|
| `Deitel` | `docs/syllabus.md` (optional-reading historical note), `lessons/02-variables-expressions-types.md` (now explicitly optional), `course_metadata.yaml` note (superseded framing) | Fixed to optional/historical everywhere found in active files; no remaining "Deitel is required/assigned" claims |
| `ZyBooks`/`zyBooks`/`zybook` | `course_metadata.yaml` (now `required: false`, marked superseded), `planning/zybooks-assignment-map.md` (marked superseded header), `docs/curriculum/course-sequence.md` (explicitly self-described historical archive map), `planning/coding-odyssey-arc-map.md` (historical "what didn't survive the merge" note) | All remaining occurrences are either historical/provenance or explicitly marked non-required |
| `chapter exam` | `planning/week-17-finals.md` (now says "No chapter exam"), `quizzes/Q2-chapter-exam.md` (historical reusable template, self-described as such), `docs/curriculum/course-sequence.md`/`docs/reports/curriculum-history-synthesis.md` (historical) | Fixed the one active claim (Week 17); rest is provenance |
| `class hierarchy` | `assignments/A2-coding-odyssey-project.md` and `planning/coding-odyssey-arc-map.md` (both now say inheritance/hierarchy is explicitly *not* required, referencing the fix) | Fixed — no remaining requirement language |
| `Week 1` near `print`/`input`/`program`/`pair`/`show-and-tell` | None in `planning/week-01.md` | Fixed — Week 1 now has zero programming content |
| `Checkpoint 4` | `planning/week-16.md`, `assignments/odyssey_gates/week-16.md`, `rubrics/odyssey_gates/week-16_rubric.md`, `assignments/A2-coding-odyssey-project.md`, `docs/curriculum/judgment_toolkit.md`, `planning/coding-odyssey-arc-map.md` | All remaining mentions are explicit retirement notices ("Checkpoint 4 is retired..."), not active requirements. Two report files (`reports/010`, `reports/007`) retain it as unmodified historical text |
| `final creative pass` / `full show-and-tell` (Week 16) | None describing Week 16 as required in any active file | Fixed — Week 16 is now the Farkle/ML week everywhere it's described |
| `Week 9` / collections | `planning/block-map.md` fixed (L08/L09/L10); every `planning/week-NN.md` file was already correct | Fixed the one real drift found |
| `chapter N` citations in weekly "Due this week" sections | None remaining in `planning/week-02.md` through `planning/week-13.md` | Fixed — replaced with topic/capability language throughout |
| `chapter N` in `lessons/*.md` "Historical materials" sections and `docs/curriculum/course-sequence.md`/`unit-map.md`/`curriculum-history-synthesis.md` | Present, unchanged | Acceptable — these are explicitly self-described historical/archive-derived summaries, not active per-week requirements; edited only the one active-requirement instance found (`lessons/02`'s "Before class" reading) |

## E — Savnac readiness blockers

Genuine open items that need Jeremy's decision before a Savnac build, not manufactured caution:

1. **Optional standalone bonus-practice point value/mechanism is not decided.** The policy is now explicit everywhere (A1, A2, grading-model, syllabus), but the exact number/weighting is a real remaining call — flagged in `docs/grading-model.md`'s open items, not invented.
2. **Farkle/ML Week 16 lesson content does not exist yet.** The planning/gate/rubric shape is reconciled (no competing Odyssey deadline, no RL math requirement), but the actual lesson material is a follow-up authoring task.
3. **CS50P link map is metadata/URL-level only** (`docs/curriculum/recommended-resources.md`), not yet published into Canvas/Savnac week pages — that's explicitly publication work for a later prompt, per Report 011 Section H.
4. **Grading weights in `docs/grading-model.md` remain a DRAFT PROPOSAL** with several pre-existing open checkboxes (A4 weight, drop-lowest policy, Canvas submission locations) — none of these are new from this pass, but they still block a fully wired Savnac gradebook.

## F — Exact validation receipt

```
$ git pull --ff-only
Already up to date.

$ git status --short
(clean before edits; confirmed)

$ find . -iname "AGENTS.md"
(no output — no repo-local AGENTS.md exists in computer_science_1)

$ git diff --check
(no output — no whitespace errors)

$ ls Makefile
ls: cannot access 'Makefile': No such file or directory

$ make check
make: *** No rule to make target 'check'.  Stop.

$ make task-check
make: *** No rule to make target 'task-check'.  Stop.

$ ls -la tests/
(only .gitkeep present — no test suite exists in this repo)

$ python3 -c "import yaml; d=yaml.safe_load(open('course_metadata.yaml')); print('OK', d['textbook']['required'])"
OK False

$ grep -n "six\|seven" reports/011_cs1_resource_coverage_matrix.csv reports/011_cs1_resource_coverage_matrix.json
(both files now say "seven" only)
```

No repository-native validation target exists (matches Report 011's prior finding — this repo has no `Makefile` and an empty `tests/` directory). All checks performed were manual: targeted `grep` sweeps (Section D), a YAML parse check on `course_metadata.yaml`, `git diff --check`, and file-existence checks on every newly created or cross-referenced file (`docs/curriculum/recommended-resources.md`, the moved Week 13 Decide/Compare content, the retired Week 16 gate/rubric).

## Boundaries respected

No Savnac writes. No Canvas writes. No production ZyBooks writes. No student data. No private/durable ZyBooks or Deitel evidence deleted — `course_metadata.yaml`'s ZyBooks product metadata and `lessons/02`'s Deitel citation are both preserved, just correctly marked optional/historical rather than required. No licensed textbook body content published or copied — the new `docs/curriculum/recommended-resources.md` links to CS50P/GitHub Skills/GitHub Docs pages only, reproducing no body text. No CS50P week order imposed on the semester — the resource map maps CS50P material to our pinned sequence. No mandatory CS50P enrollment/certificate/problem-set sequence. No mandatory inheritance/class hierarchy (removed). No programming in Week 1 (removed). No giant Odyssey deadline competing with Week 16's Farkle/ML week (Checkpoint 4 and capstone Decide/Compare moved to Week 13). No invented numerical bonus-point value (flagged as an open decision instead).
