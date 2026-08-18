# Sidecar Report 102 — CS1 Online launch recon and target lock

**Date:** 2026-08-17/18
**Prompt:** `sidecar/prompts/102_cs1_online_launch_recon_and_target_lock.md`
**Scope:** read-only recon against real SWOSU Canvas, local dry-run compilation. No production Canvas writes were made by this prompt.

## Verdict: GREEN

Exact real Fall 2026 CS1 Online Canvas course is locked by evidence, the current desired state compiles cleanly, no unresolved source-of-truth contradiction exists, shared Week 1 is represented correctly, grading groups sum to 100%, drop-lowest is representable, sentinel weeks behave correctly, the production diff is understood, no unrelated destructive action is required, and Prompt 103 can perform a bounded reconcile against one exact course id (`74033`).

---

## 1. Repo/branch/SHA table

| Repo | Branch | HEAD SHA | Working tree | Notes |
|---|---|---|---|---|
| `computer_science_1` | main | `a0d0a48b1964b0861783fb80738c5dda6f21f485` | clean | source of truth for content |
| `course_foundry` | main | `11a2a2c742b0b1a4f33494c04c2cb0a9f964b981` | **dirty (672 paths)** | live, running `submission_listener` daemon (PID 379684, started 00:53, `--live --nrp-enabled`) is writing to `runs/submission_listener/state.sqlite3*`, receipts, and `runs/zero_submission_queue.jsonl`, plus ~600 untracked `reports/127_cs1_zero_submission_roundtrip_experiment_*.md` files from an in-progress experiment. This is intentional, unrelated, currently-running local work — preserved untouched, not committed, not discarded, per prompt instruction #4. |
| `harbor` | main | `5d69e3ede4b6f1ab4cb32cf003faea79f7df8cc0` | clean | fast-forwarded to `origin/main` (was 1 commit behind; no conflicts) |
| `semester_kickoff_week` | main | `94d8591369c350996f6984b05d0a9d50cee764a8` | clean | up to date |
| `professional_minds` | main | `af54438aeb4bddbbceed4524bc10379b0b9d5a3c` | clean | up to date |
| `ai_fluency` | main | `022262cf207c28a9504425779a24247ddcf66884` | clean | up to date |

No repo was reset, stashed, or force-updated. No repair commits were required (see §6).

---

## 2. Savnac reference state (Canvas course id 1, `COMSC-1033-SAVNAC`)

Read live via `~/.config/canvas/savnac.env` against `http://192.168.122.172:3000`:

| Object | Count |
|---|---:|
| Modules | 21 |
| Assignments | 161 |
| Pages | 216 |
| Files | 37 |
| Assignment groups | 15 (14 CS1-weighted + Canvas's default 0%-weight "Assignments") |

Savnac carries more objects (414 non-group objects) than the current Git-compiled desired state for Weeks 2–17 (324 objects) plus Week 1 kickoff (~39 objects, per the live 74033 Week-1 modules, §3). The extra ~50 objects are consistent with Savnac's role as an accumulating proving ground (superseded experiment artifacts, prior-iteration objects from the many `course_foundry/runs/*cs1*` passes) rather than evidence of missing Git content — per the prompt's governing rule, Git is authoritative and this delta is not being forced backward.

The most recent full-semester dry-run/push evidence, `course_foundry/runs/2026-08-13_cs1_launch_readiness_079/REPORT.md`:

- Verdict: GO-WITH-YELLOWS.
- Imprint dry run against Savnac: **`0 to create, 0 to update, 336 unchanged, 0 to delete`** — i.e. Savnac's live state and the then-current Git-compiled desired state were already byte-for-byte reconciled (proven idempotency/read-back).
- Desired-state snapshot that pass: 16 modules, 322 objects (144 pages, 147 assignments, 31 files), 14 weighted assignment groups. Today's dry run (§4) is 16 modules / 324 objects — a 2-object drift over 4 days of ordinary content evolution, not a regression (see §4 for today's own baseline comparison).
- Week 1 confirmed owned by the shared kickoff adapter, audited live rather than duplicated into the Weeks 2–17 adapter — same pattern observed live on `74033` (§3).
- AI Fluency and Professional Minds strands confirmed present in Savnac through Week 16.

Drop-lowest, Week 15 async, Week 16 dead-days, and Week 17 finals behavior are all covered by the automated `docs/grading-model.md`-documented mechanics (prompts 067/068) and were re-confirmed directly against the current compiler in §4, not solely inferred from the Savnac archive.

---

## 3. Production Canvas target discovery and lock

Live, read-only `GET`s against `https://swosu.instructure.com` (real SWOSU token, confirmed live and resolving to Jeremy Paul Evert, id 24406) on both candidates named in the dispatch:

| Field | Course 74033 | Course 74029 |
|---|---|---|
| `name` | Fall 2026 Computer Science I (COMSC-1033-1414) | Fall 2026 Computer Science I (COMSC-1033-1415) |
| `course_code` | `COMSC-1033-1414.2026FA` | `COMSC-1033-1415.2026FA` |
| `sis_course_id` | 49300 | 49301 |
| `term` | Fall 2026 (id 290, active) | Fall 2026 (id 290, active) |
| `section` | id 76388, "Fall 2026 Computer Science I (COMSC-1033-1414)", 2026-08-17 → 2026-12-12 | id 76384, "...1415", 2026-08-17 → 2026-12-12 |
| `workflow_state` | **unpublished** | **available** (published) |
| Jeremy's role | TeacherEnrollment, active | TeacherEnrollment, active |
| `total_students` | 21 | 20 |
| `apply_assignment_group_weights` | true | false |
| Modules / Assignments / Pages / Files (live) | 6 / 17 / 9 / 5 | 5 / 13 / 7 / (not queried further) |

### Target-lock evidence (converging, not assumed)

The Canvas API alone does not disambiguate "online" vs. "traditional" — section numbers only. `computer_science_1`'s own git source of truth does, unambiguously, across five independent files, all consistent with each other and pre-dating tonight's task:

- `course_metadata.yaml` (populated 2026-08-11): `section_number: "COMSC-1033-1415"`, `official.modality: "Traditional (in-person)"`, `catalog_offering_note: "Traditional, in-person section (a separate online section, 1414, also exists but is not this offering)"`.
- `docs/syllabus.md` (sourced from Self-Service, confirmed 2026-07-14): `Section: COMSC-1033-1415 (traditional); note: a separate online section 1414 also exists`; `Modality: Face-to-face (traditional per Self-Service)`.
- `ROADMAP.md` (2026-07-22 decision record): "the online section (`COMSC-1033-1414`) is in scope, sharing CS1's Canvas structure" and (separately) "`COMSC-1033-1414` shares CS1's Canvas structure (no separate authoring)."
- `planning/block-map.md`: "Online section 1414 runs on the same content but has no MWF periods."
- `course_foundry/reports/003_canvas_capability_planning.md` (2026-07-16 live Canvas catalog pull): explicitly tabulates `74033 → section 1414` and `74029 → section 1415`, stating "`1415` is the in-person MWF section the planner is written for... `1414` is the parallel online section."

Live Canvas course names/codes match this mapping exactly: `74033` = `...1414`, `74029` = `...1415`. There is no contradiction between git and live Canvas, and no second plausible online candidate exists — no ambiguity condition is triggered.

**Target lock: Canvas course id `74033`** (`COMSC-1033-1414.2026FA`, "Fall 2026 Computer Science I", the online section), currently unpublished, 21 students already enrolled, Jeremy as active teacher.

`74029` (`COMSC-1033-1415`) is the traditional in-person section per this same evidence and is correctly **excluded** as a production target — it falls under the prompt's explicit "face-to-face CS1" rejection rule, independent of its published state.

### Live content already on 74033 (sanity check, not this prompt's write)

`74033` is not an empty shell: it already carries the shared Week 1 kickoff modules (`Monday: Survive This Semester`, `Wednesday: Thrive In Your Degree`, `Friday: Entering Your Career`, `A07 — Advisor (Later)`, `Success Foundations (Optional/Bonus)`) plus a partial Week 2 module (`professional_minds` Wednesday/Friday reading+slides only — no lesson pages, no Monday Moment, no Week 2 Coding Odyssey gate yet). All 15 assignment groups already exist on `74033` with the correct names and weights (matching the compiler's 14 CS1 groups + Canvas's default 0%-weight "Assignments" group, verified against §4's dry run). This is consistent with an earlier, narrower kickoff-only push having already landed here — not contamination from the wrong course, and not evidence that a full semester push has happened.

---

## 4. Current dry-run compilation (zero production writes)

Ran the live compiler (not a static export):

```
cd course_foundry && ./.venv/bin/python3 -m course_foundry.cs1_dry_run \
  --course-repo-path /mnt/brandy_nvme/jevert/git/computer_science_1
```

(Note: system `python3` is 3.9 and cannot import `course_foundry` — its Pydantic models use `X | None` syntax requiring 3.10+. The repo's own `.venv` (Python 3.11.13) is required and was used. This is worth flagging to Prompt 103 as an environment prerequisite, not a code defect.)

**Result: 16 modules, 324 objects — 145 pages, 147 assignments, 32 files.** (Weeks 2–17; Week 1 is owned separately by `semester_kickoff_week` and correctly not duplicated into this count — confirmed live on `74033`, §3.)

- Previously documented 2026-08-12 baseline was 16 modules / 327 objects. **Explained, not a regression:** today's Week 17 content-readiness scan flags Week 17 as "not ready" because `ai_fluency` has no `week_17_*` Monday Moments folder and `professional_minds` has no Week 17 Wednesday/Friday reading or compiled deck. `planning/week-17-finals.md` states explicitly: *"Status: Finals week. No new Monday Moments or Professional Minds content."* This is by design — Week 17 is deliberately content-light (only the final Odyssey gate assignment + rubric page, plus A5 which canonically lands in the Week 16 module per `docs/grading-model.md`). The 3-object gap between 327 and 324 is fully accounted for by this intentional, documented absence, not a compiler or content regression.
- **Assignment groups sum to exactly 100%**: kickoff 5 + Monday Moment 5 + Wacky Wed 5 + Fun Fri 5 + paired-programming 5 + Friday feedback 5 + Show-and-Tell 5 + weekly reinforcement 25 + Coding Odyssey checkpoints 15 + final reflection 8 + pathway Wk14 5 + pathway Wk15 5 + attendance 5 + course eval 2 = **100%**.
- **Sentinel weeks**, machine-verified from the compiler's own gate-status output:
  - Week 2: ACTIVE required gate.
  - Week 6: ACTIVE required gate (checkpoint 1).
  - Week 9: ACTIVE required gate (checkpoint 2).
  - Week 14: ACTIVE required gate (checkpoint 3, plus Professional Pathway Wk14 update).
  - Week 15: no mandatory gate (optional enrichment only) — correct async/Thanksgiving behavior.
  - Week 16: RETIRED, produces no Canvas gate object — correct dead-days/no-new-graded-work behavior (module still renders lesson/PM/Monday-Moment content, not_graded).
  - Week 17: ACTIVE required gate (final Odyssey gate + rubric), reflection paper (A5) canonically placed in the Week 16 module per documented rule.
- **Odyssey-gate semantics** for all other weeks (3, 4, 5, 7, 8, 10, 11, 12, 13): ACTIVE required gate — no unexpected optional/retired weeks outside the three sentinel exceptions above.
- **External-link/file objects**: 32 files rendered (Week-16 PDF decks, Week-1-adjacent slide decks, etc.), each with `source_path` resolved to a real file on disk under the sibling repos — no missing/dangling file source paths observed in the render.
- **Compiler warnings/skipped objects**: none raised by the run itself; the only "missing" markers are the intentional Week 17 Monday-Moment/PM omission above (Section 1 of the render, informational-only — it does not gate what `cs1_savnac_desired_course` actually renders).

---

## 5. Desired-vs-production semantic diff (read-only)

Compared the rendered `DesiredCourse` (§4) against live `74033` (§3):

| Category | Finding |
|---|---|
| Missing modules | 16 of 16 Weeks-2–17 modules are missing from `74033` (only the separately-owned Week 1 kickoff modules + a partial Week 2 shell exist live). Expected — full deploy has not happened yet; this is exactly what Prompt 103 exists to do. |
| Missing pages/assignments/files | All ~324 Weeks-2–17 objects are missing live, plus Week 2's lesson pages, Monday Moment page/assignment/rubric, and Coding Odyssey Week-2 gate (present in the desired plan, absent live). |
| Stale/obsolete objects | None found. Everything live on `74033` matches named objects in the desired plan (Week 1 kickoff set, Week 2 PM Wed/Fri set) — no unrecognized/foreign content. |
| Assignment groups/weights | **Names and weights already match exactly** — all 14 CS1 groups plus the default "Assignments" group are present live with the correct percentages, matching §4's rendered plan verbatim. |
| Drop-lowest rules | **Mismatched.** All 15 live assignment groups on `74033` currently show `rules: {}` — no `drop_lowest` rule applied yet, even though the desired plan calls for `drop_lowest: 1` on 7 categories. This is expected pre-reconcile state (prompt 068's automated drop-lowest push runs as part of the real Imprint reconcile, not something that happens by merely creating groups) — a legitimate, understood item for Prompt 103, not a compiler defect. |
| Due dates | Not yet comparable at object level — no Weeks 2–17 assignments exist live to compare due dates against. |
| Publish state | `74033` is `unpublished`. Desired plan does not itself dictate course-level publish state (that is Prompt 104's student-view closeout concern per the three-prompt chain). No contradiction. |
| Missing Week 1 shared kickoff objects | **None — Week 1 is fully present and correct live**, matching the shared-kickoff-ownership contract exactly (5 kickoff modules + advisor module, same titles/structure as the desired plan expects `semester_kickoff_week` to own). |
| Duplicate objects | None observed. |
| Dangling module items | None observed in the 6 live modules inspected. |
| Broken internal links | Not exercisable without deeper page-body inspection; out of scope for a course with 96% of its content not yet pushed. Flagged as a Prompt 103 in-flight check, not a 102 blocker. |
| Missing files/assets | All 32 desired file objects resolve to real source paths on disk (§4); none pushed live yet (expected). |
| Objects present in Canvas but not represented by Git | None found — `74033`'s only live content (Week 1 kickoff, partial Week 2 PM) is fully accounted for by the shared-kickoff-adapter and PM-content pipeline that this repo's own docs describe. |

**Summary:** `74033` is a correctly-identified, mostly-empty real target that already has its Week 1 shared kickoff content and matching assignment-group scaffolding in place — i.e., prior narrower work already landed there safely — and is now ready for Prompt 103's full Weeks 2–17 reconcile plus the drop-lowest rule push. No contamination, no wrong-course content, no destructive cleanup required.

---

## 6. Launch-blocking compiler defects: none found, no repairs made

The dry run compiled cleanly with zero exceptions, zero warnings beyond the documented/expected Week 17 content omission (§4), assignment groups sum to exactly 100%, drop-lowest is representable (already implemented and proven idempotent against Savnac per prompt 068/079), and no course-specific compiler code assumes the wrong Canvas structure. No test/repair cycle was triggered in `course_foundry` or `harbor`; no commits were made to either repo.

Two **non-blocking** readiness notes for Prompt 103, not treated as gate failures for 102:

1. **No pipeline adapter is registered for course id `74033`.** `course_foundry/course_foundry/run.py` only registers `register_load_adapter`/`register_sync_adapter` for course ids `1` (Savnac) and `24298` (Harbor sandbox). `cs1_savnac_load_adapter`/`cs1_savnac_sync_adapter` themselves take `course_id` as a plain parameter (default `1`) and are not Savnac-specific in implementation — they can be called directly with `course_id=74033` against the real `CANVAS_API_BASE_URL`/`CANVAS_API_TOKEN`, or registered in `run.py` first. Prompt 103 needs to decide which path it uses; this is a wiring/registration gap, not a code defect.
2. **The online section's own differentiated rhythm is explicitly out of scope for tonight's content.** `ROADMAP.md` (2026-07-22 decision, still open as of today): "online-section attendance system — decided in scope, not yet built... three brief Mon/Wed/Fri check-ins for online students... a rolling disengagement check... not started." `planning/block-map.md` separately notes 1414's own delivery rhythm ("async digests + podcasts may *be* the delivery") is still an open design question. Per `block-map.md`, "Online section 1414 runs on the same content" as the traditional section for now, which is consistent with deploying the same Weeks 2–17 desired course into `74033` tonight. The online-specific attendance/check-in build remains a real, separately tracked gap — not something this prompt is authorized to design or build (the mission explicitly forbids redesigning the course), and not something that blocks getting the existing, decided curriculum into the correct shell.

Given no defect required repair, `course_foundry` and `harbor` were left exactly as pulled (§1); no repair commits exist to report.

---

## 7. Tests run

No code was changed, so no test suite was run beyond the dry-run compilation itself (§4), which is the load-bearing "does this even compile" check for this prompt. `course_foundry`'s existing `tests/test_load_adapters.py`, `tests/test_sync_adapters.py`, `tests/test_graph.py` were read (not re-run) to confirm the adapter-registry mechanics described in §6 finding 1.

## 8. Commits created

None. No repair was required in `course_foundry` or `harbor` (§6). `harbor` was fast-forwarded from `origin/main` (no new local commit — a pull, not a repair). No file in `computer_science_1` other than this report was touched; this report itself will be committed and pushed to `computer_science_1`'s `main`.

## 9. Final verdict: GREEN

All Section 7 launch-gate conditions are met:

- Exact real Fall 2026 CS1 Online Canvas course locked by evidence: **`74033`**.
- Current desired state compiles cleanly (16 modules / 324 objects, zero errors, one fully-explained intentional content omission).
- No unresolved source-of-truth contradiction (git and live Canvas agree on section identity).
- Shared Week 1 is represented correctly (live-verified on `74033`).
- Grading groups sum to exactly 100%.
- Drop-lowest is representable and proven idempotent against Savnac (§2); not yet applied to `74033` — understood, expected pre-reconcile state, not a defect.
- Sentinel weeks (2, 6, 9, 14, 15, 16, 17) all behave correctly.
- Production diff is understood (§5) — a mostly-empty target ready for a full, non-destructive reconcile.
- No unrelated destructive action is required.
- Prompt 103 can perform a bounded reconcile against exactly one course id, `74033`, using either a direct `cs1_savnac_load_adapter(course_repo_path, course_id=74033)` call or a new `run.py` registry entry (§6).

**I know exactly which Fall 2026 online shell is ours (`74033`), I know exactly what Git says should be there (16 modules / 324 objects, 100%-summing grading model, drop-lowest and dead-days rules included), I know the current delta (Week 1 kickoff + partial Week 2 PM content already correctly present; Weeks 2–17's remaining ~300 objects and the drop-lowest rule push are the entire Prompt 103 job), and the deployment machinery is ready to reconcile it.**
