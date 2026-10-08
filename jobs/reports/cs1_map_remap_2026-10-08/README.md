# CS1 Weeks 9–16 re-map under the objects-first sequence — plan for Jeremy's yes/no

Seat: Anna (april). Date: 2026-10-08. Deadline: Mon 2026-10-12 9:00 AM CDT.
Branch `anna/cs1-map-remap-2026-10-08` (from `origin/main` 83cd646). **Docs only. Nothing in the course was changed and nothing was written to Canvas.**

Circuit note: the mission names Terra (plan) / Sol (check). Anna drafted this plan directly from the repo files; the Sol-style dependency check is recorded in "Check" at the end.

## 1. Decision being re-mapped
Jeremy, 2026-10-07: Week 9 = OOP intro (use others' objects, then first custom classes; Checkpoint 2 stays in Week 9). Week 10 = dictionaries. Week 11 = OOP again.
Source map (`planning/week-09..16.md`, `coding-odyssey-arc-map.md`, `fall-2026-course-design.md`): W9 strings+CP2, W10 lists, W11 dicts + Decide/Compare #1, W12 classes R1, W13 classes R2 + D/C #2, W14 Git + CP3, W15 async, W16 Farkle/ML, W17 finals.

Calendar facts (from `planning/block-map.md`): W9 Oct 12–16, **Mon+Wed only** (Fall Break from Wed 10 PM, no Friday). W10 Oct 19–23, W11 Oct 26–30, W12 Nov 2–6, W13 Nov 9–13, W14 Nov 16–20 are full weeks. W15 Nov 23–27 is **fully async** (instructor travel; Thanksgiving). W16 Nov 30–Dec 4. W17 Dec 7–11 finals.

## 2. Proposed sequence (recommended: Option A)

| Wk | Dates | Technical focus (new) | Odyssey gate / instrument | Change vs August map |
|---|---|---|---|---|
| 9 | Oct 12–16 (Mon, Wed) | Objects you use (`str`, `list` as objects with methods) → first custom `class`: `__init__`, state, one method. List basics enter here only as "an object you use". | **Checkpoint 2** (stays). Class use is *encouraged, not required* (see Risk 1). | Was "strings continued". Focus replaced; CP2 unchanged. |
| 10 | Oct 19–23 | Lists consolidated, then **dictionaries**: key/value, lookup, dict of records, list-of-dicts. Instances can be dict values. | Merged Quick Check: world tracks a growing collection of named entities **and** looks one up by key. Pair programming (A3) stays. | Old W10 (lists) + W11 (dicts) gates merge here. |
| 11 | Oct 26–30 | **OOP round 2 / refactor**: turn a dict/list-entry noun into a class; collections of objects; methods that read/change state. | Quick Check: major noun is now a class with `__init__` and ≥1 method, replacing the dict-entry form. **Decide/Compare #1** moves here (dict vs class vs list for your noun — a better trade-off than "dict vs list"). | Old W12 gate lands here. D/C #1 moves W11→W11 (same week, new question). |
| 12 | Nov 2–6 | Objects interact: object-to-object method calls; composition; modules (split a world across files). | Quick Check: ≥2 classes interact (old W13 gate). | Old W13 gate lands here. Old W12 "R1" content absorbed into W9/W11. |
| 13 | Nov 9–13 | Build culmination week. Light new concept: **files/persistence** (save/load world state, e.g. JSON or text). Pair programming (A3) stays. | Quick Check: world saves and reloads state. **Decide/Compare #2 (capstone)** stays here. | New W13 concept (fills the unplaced persistence outcome — Finding 1). |
| 14 | Nov 16–20 | Git/GitHub/pair/AI-aware coding. | **Checkpoint 3 + Full Trail Debrief** (stays). Debrief question 1 reworded (Risk 3). | No sequence change; wording only. |
| 15 | Nov 23–27 | Async, no new technical concept; portfolio. | none | Unchanged. |
| 16 | Nov 30–Dec 4 | Farkle/ML. | none | Unchanged. Consumes dict + classes + files: all earlier now. |
| 17 | Dec 7–11 | Finals. | Final Debrief + Judgment Log | Unchanged. |

Holidays: Fall Break stays in W9 (no Fri), Thanksgiving stays in W15 (async). Monday Moments lenses, Wacky Wednesday, Fun Friday books are untouched (they follow the calendar, not the technical topic); only the "technical tie-in" sentences are retargeted (Section 3).

### What moves / merges / drops
- **Moves:** classes R1 from W12 → W9 (intro) + W11 (refactor of the world's noun). Interacting classes W13 → W12. Strings-continued content: gone from W9 (taught in W8 "Strings Are Objects" — already delivered).
- **Merges:** W10 lists + W11 dicts → one W10 (lists briefly seen in W9, reviewed at the top of W10). Their two Quick Checks → one.
- **Drops:** nothing from course outcomes. The only "drop" is the standalone W10 list-only gate and the W9 "no new concept / consolidate strings" framing.
- **Adds:** persistence week (W13) — optional, see Decision C.
- **Course outcomes check (`fall-2026-course-design.md`)**: trace/test/improve (all weeks); decompose into functions/data (W7, W10); collections (W9–W10); basic classes (W9, W11, W12); files/persistence (**W13 under Option A; unplaced today**); disclose/validate AI work (Monday Moments, all weeks). All retained.
- **Odyssey gates retained:** CP1 W6 (unchanged), CP2 W9, CP3 W14, D/C #1 W11, D/C #2 W13, capstone W13, final W17.

### Alternative (Option B, smaller change)
W9 OOP intro, W10 lists+dicts, W11 classes R1, W12 classes R2 (interact), W13 build + D/C #2 with **no new concept**, persistence dropped as a required topic. Fewer new files to author; leaves the "saves/loads state" genre promise (`coding-odyssey-arc-map.md`) unmet. Option A recommended because that promise and the outcome both exist today with no home.

## 3. Files that must change (not changed here)

Repo `computer_science_1`:
| File | Change |
|---|---|
| `planning/week-09.md` | Focus → OOP intro; supersession note; keep Monday/WW/Friday/holiday lines. (Also in the Week 9 build mission.) |
| `planning/week-10.md`, `-11.md`, `-12.md`, `-13.md` | Focus + "Due this week" per table; retarget Monday-Moment tie-ins: W10 Critique (list/dict review — still fits), W11 Verify (collection edge cases → class/state edge cases), W12 Revise ("refactor first-pass class" now fits W11→W12 instead), W13 Decide (composition vs inheritance — inheritance remains optional per A2). Friday show-and-tell lines in W11–W13 follow. |
| `planning/week-14.md` | Debrief wording only (Risk 3); no sequence change. |
| `planning/coding-odyssey-arc-map.md` | Arc 2/3 boundaries, "Real focus" column and gate table rows W9–W13, the Wk12 "noun tracked in Wk10-11 collection" gate text, "What didn't survive" paragraph (names Wk9 strings / Wk11 collections), and the reconciliation note. Arc 2 (W7–9) is no longer "First Real Choices" through strings; arc 3 length unchanged (W10–W14). |
| `planning/fall-2026-course-design.md` | Semester spine table rows 9–13 and the "classes/files" outcome sentence. |
| `planning/block-map.md` | Monday lecture rows L08–L12 and the "Reconciled 2026-08-12" note naming Wk9 strings / collections starting Wk10. |
| `assignments/odyssey_gates/week-09.md` | Concept line ("no new concept… through strings") and CP2 scope sentence. Build mission item 5 already covers description text. |
| `assignments/odyssey_gates/week-10.md`, `-11.md`, `-12.md`, `-13.md` | W10 = merged list+dict gate; W11 = class-refactor gate + D/C #1 rewritten (dict vs class); W12 = interaction gate (old W13 text); W13 = persistence gate + D/C #2 (existing capstone text retained). |
| `rubrics/odyssey_gates/week-09_rubric.md` … `week-13_rubric.md` | Mirror the new gate checklists. |
| `assignments/odyssey_gates/week-14.md` | Debrief intro ("Weeks 12-13 were the deliberate refactor crisis"), Q1 and Q2 ("design choice made back in Week 10-11") — all three (Risk 3). |
| `assignments/odyssey_gates/week-08.md:56`, `planning/zybooks-assignment-map.md:47` | Look-ahead "Week 9 (strings continued) is Checkpoint 2". |
| `NAMING.md:23`, `templates/T5-start-here.md:81`, `planning/week-10.md`/`week-13.md` A3 lines | A3 pair programming pinned to "Week 10" / weekly gate; stays valid, verify only. |
| `assignments/odyssey_gates/week-13.md`, `rubrics/.../week-13_rubric.md:41` | "A bigger version of Week 11's move" — D/C #1 is now dict vs class; reword. |
| `docs/curriculum/judgment_toolkit.md` (also 108–114, 146–151) | D/C rationale "real Week 11 topic is collections"; Checkpoint 3 Debrief rationale "Weeks 12-13 (OOP Rounds 1-2)… not Week 10". |
| `docs/curriculum/recommended-resources.md` rows 24–30 and C09 note (~56) | Spine rows 9–13 and persistence row. |
| `planning/coding-odyssey-arc-map.md` lines 35–37, 104–105, 113–114 | Also "both OOP rounds… Weeks 12-13", "real Wk9 is strings". |
| `assignments/A2-coding-odyssey-project.md` lines 51, 64 | "Week 13–17 capstone" / "Week 13 D/C composition vs inheritance": still valid, check. |
| `reports/010`, `012`, `002` | Historical restatements of the old sequence: leave as history. |
| `assignments/A2-coding-odyssey-project.md` | Checkpoint table / D/C placement lines (~116–117: "Week 11 — data-structure choice", "Week 13 capstone"). |
| `docs/curriculum/judgment_toolkit.md` | D/C #1 description ("Wk 10-11, collections-era design choice") and the lines that explain why Wk11 is collections. |
| `lessons/07-collections.md`, `lessons/08-classes-and-modules.md` | Both are ~15-line stubs today (objectives + historical pointers). New sequence needs real lesson text: split 08 into intro (W9), refactor (W11), interaction/modules (W12); add a persistence section (W13, likely in 09 or a new lesson). Highest authoring cost. |
| `rubrics/odyssey_gates/week-14_rubric.md` | Debrief rows cite "Week 10-13 design decision", "Week 10-11 design choice" and "Week 13's gate" interaction; retarget to the new weeks (Risk 3). |
| `assignments/odyssey_gates/week-16.md`, `week-17.md`, `rubrics/.../week-16_rubric.md`, `week-17_rubric.md` | Cross-references to "Week 11 or Week 13" D/C moments and "moved to Week 13": still true under Option A (D/C #1 stays W11, #2 stays W13); verify wording only. |
| `planning/zybooks-assignment-map.md` (lines 48–51, 126–129), `docs/curriculum/recommended-resources.md` (line 26 spine row) | Week mapping for Ch 8 lists/dicts (W10–11 → W9–10) and Ch 9/11 classes/modules (W12–13 → W9, W11–12); legacy/optional references only. |
| `ROADMAP.md`, `docs/curriculum/course-sequence.md`, `docs/curriculum/unit-map.md` | Reference mentions of week order; refresh only where they cite Week 9–13 explicitly (ROADMAP line 46 is historical; leave). |
| `sidecar/canvas_pages/week-10…13-*.html` | Page titles carry the old topic ("lists and dictionaries begin", "classes and objects I/II"); regenerate from updated planning files. Also `week-9-strings-continued-and-checkpoint-2-evolution-week.html` (stale W9 page; the Week 9 build mission supersedes it) and `week-8-strings-and-text-processing-...html:16` ("Week 9 (strings continued)" look-ahead). |

Canvas weeks affected (CS1 74029; verify id and name at write time): **Weeks 9, 10, 11, 12, 13** modules (overview page, gate assignment description, rubric); **Week 14** gate description (Debrief wording only). Weeks 15–17 unaffected. Weekly rollover discovery needs a Page item whose title names the week — keep "Week N" in titles; renaming topic subtitles is not a rollover risk. No gradebook columns or due dates change (every gate stays due Friday 11:59 PM Central; W9 Fri Oct 16 despite the break, per the build mission).

## 4. Dependency problems and findings

1. **Finding 1 — files/persistence has no week today.** `fall-2026-course-design.md` lists it as an outcome, `coding-odyssey-arc-map.md` guarantees genres support "save/load state", and Week 16 consumes "files/data where useful"; no week 2–15 teaches it. Option A gives it W13. Decision C below.
2. **Risk 1 — Checkpoint 2 vs 1.5 weeks of OOP.** CP2 is due Fri Oct 16, but only Mon+Wed meet and the week introduces classes. Requiring classes in CP2 would grade a concept after two sessions. Recommend: CP2 *scope stays "consolidate what's taught"*; a first class is an optional extension credit-wise neutral. Gate text must say so.
3. **Risk 2 — "noun tracked in Wk10–11 collection becomes a class" (old W12 gate).** Still true, now at W11 against the W10 dict/list. But students who build their noun as a class in W9 skip the dict→class refactor. Recommend the W9 class be a small starter (any simple noun, not necessarily the world's), and W10 collections store plain dict records, so the W11 conversion is genuine.
4. **Risk 3 — Full Trail Debrief (W14) Q1** asks "what broke when you moved from dict/list entries to classes". Premise survives for students following the plan; reword to "when your design changed (dict→class, or one class→several)" so class-first students can answer honestly.
5. **Risk 4 — Decide/Compare #1 and W10 load.** Merging list+dict gates in W10 is heavy for a single week. D/C #1 is moved off W10 into W11 (dict vs class) to keep W10 to the Quick Check + pair-programming session.
6. **Risk 5 — Week 9 delivered content already built.** The Week 9 build mission (`anna_cs1_week9_oop_intro_build_2026-10-08.md`) publishes W9 Canvas content under the new focus before this plan is approved. W9 content is consistent with all options here; W10+ are not yet touched, so no rework if Jeremy says no to anything past W9.
7. **Risk 6 — thin lesson sources.** `lessons/07` and `lessons/08` are stubs; W10–W13 Canvas pages (sidecar) were generated against the old map and must be regenerated, not edited.
8. **Risk 7 — Wk16 Farkle.** Consumes dicts (learner) and classes "where useful"; both now arrive earlier. No change needed; verify `week-16.md` prerequisites text still true (it cites "objects where useful").
9. **Not affected:** Checkpoint 1 (W6), Checkpoint 3 (W14, Git-backed receipt on W13 code), A6 portfolio (W1/14/15), A5 final reflection (W16–17), pair-programming sessions W10/W13 (keep), AI Fluency lens order (calendar-driven).

10. **Review finding — persistence conflicts with a standing choice.** `docs/curriculum/recommended-resources.md:30` says persistence is "integrated where authentic, **not one isolated week**". A dedicated W13 persistence week reverses that. Lower-cost variant of Option A: integrate save/load into the W12/W13 gates (a small load/save step on the world) rather than a teaching week. `A2:51-55` already requires save/load "by the Week 13–17 capstone" with no teaching week, and the Farkle learner (`lessons/code/farkle_ml/learner.py:85,94`) uses JSON save/load, so the gap is real either way.
11. **Review finding — W13 load.** Persistence + D/C #2 + build culmination in W13 squeezes the "Week 14 uses W13 code as-is" pin (`planning/week-14.md`). Integrated persistence (item 10) eases this.
12. **Review finding — W10 load.** Moving D/C #1 off W10 does not reduce the content load of lists-review + dicts + merged gate. If Jeremy wants a lighter W10, put the list review in W9 and keep W10 dict-only.

## 5. Decisions needed from Jeremy (yes/no)
- **A. Adopt Option A sequence** (table in Section 2)? Or Option B?
- **B. D/C #1 moves to W11 with the question "dict vs class vs list for your noun"?** (Recommended yes.)
- **C. Persistence: integrated into W12/W13 gates (recommended, matches `recommended-resources.md:30`), a dedicated W13 teaching week (Option A as drawn), or dropped as a required outcome?** If drop, remove it from `fall-2026-course-design.md` and the genre "save/load" promise.
- **D. Checkpoint 2: classes optional (recommended) or required?**
- If A is yes, the next missions are in order: W10 package (due before Mon Oct 19), W11, W12, W13, then the file edits in Section 3. Anna does not author the course content; Ivy/Terra-Luna-Sol circuit builds each week.

## 6. Check
Dependency sweep ran with `grep` across `planning/`, `assignments/`, `rubrics/`, `docs/curriculum/` for Week 9–13 topic references and "Wk10-11"-style cross-references; the file list above comes from that. Independent read-only review (subagent) found 3 factual errors, 5 missed files, 4 unflagged dependencies; all folded into Sections 3–4 (items 10–12). Sol golem circuit itself was not run.
