# Report — Decision 029 shared-strand cleanup, Computer Science I (74029)

Campaign: `fall-2026-four-course-cleanup-chain-gun-20260824-v2`. Governing decision: `swosu_cs_curriculum/decisions/029_fall_2026_optional_computing_commons_pivot.md`. Prior art: the same pattern already executed on Computer Architecture (75249) — see `computer_architecture/sidecar/reports/030_architecture_to_optional_commons_end_first_migration.md`.

## Preflight

- Course allowlist restricted to `{74029, 24298}` for the whole pass (verified via `read_canvas_config().allowed_course_ids` before any call).
- Read-only planning pass first (Terra-equivalent): fresh `list_assignments` (161 live at recon — real drift from an earlier partial transcript), `get_all_submissions` pulled for **all** 161 objects (not sampled), live content read for representative objects in every category, and both existing Computing Commons pages (`success-foundations-slash-semester-kickoff`, `professional-pathway-career-artifacts`) read live for destination-adequacy comparison.

## What this pass executed

`scripts/029_shared_strand_cleanup_pass.py`, two categories, each object gated by a fresh `get_assignment` + `get_all_submissions` immediately before its own delete decision, immediate readback (Canvas 404 on re-GET is the confirmed proof of deletion, same finding as the Architecture Pass 2 script), one destructive delete at a time:

1. **`shared-defer`** (70 objects) — Monday Moment Activity (AI Fluency, 14), Professional Minds Wednesday reading+slides (28), Professional Minds Friday reading+slides (28), weeks 3–16 (Friday) / weeks 3–16 (Wednesday). All already have a verified Commons (24298) destination from the Architecture-campaign harvest (weeks 4–16 harvested then; weeks 2–3 pre-existing). 7-day near-term due-date guard.
2. **`retire-noguard`** (42 objects) — A3 Paired Programming Report, A4 Show and Tell Reflection, A7 Friday Feedback Report, all weeks 2–15. Decision 029 says these in-class-only practices get **no Commons migration and no online equivalent at all** — full retirement, not a move. A 24h (not 7-day) near-term guard was used since the decision's own migration posture explicitly wants this removed *before* students submit, not deferred past the due date.

**Result: 112 deleted, 5 deferred** (all 5 are Week 2 shared-strand instances — Monday Moment, Wed reading/slides, Fri reading/slides — caught by the 7-day guard; Terra's recon separately confirmed Week 2's Monday/Wed instances also carry real submissions, so these were correctly out of scope either way). Live count 74029: 161 → 49, exact match with zero collateral change. Module-item sweep across all 21 modules found zero dangling references to any deleted assignment id.

Full receipt: `sidecar/raw/2026-08-25T030638Z__029_shared_strand_cleanup_pass.json`.

## Explicitly out of scope this pass (not touched, not silently dropped)

- **A01–A09** (transcript, progress report, degree plan, resume, dream job paper, gap analysis, advisor meeting, career/degree reflections) — every one already has real 2026 student submissions (18–33 each). Decision 029's gradebook rule keeps already-submitted shared/enrichment work in the home course as bonus credit; these are correctly **preserved untouched**, not eligible for deletion this term. A Commons harvest of this content (for a *future* term's optional home, not this term's live course) is a real, recorded follow-up — see below — but is not a live-course cleanliness blocker.
- **A6 — Professional Pathway** (Week 14/15) — zero activity, has an adequate existing Commons destination (`professional-pathway-career-artifacts`), but that page's wording is Architecture-flavored ("Machine Dossier," "Explain/Defend receipt") since it was written during the Architecture pass. Left live and untouched this pass — a wording-only follow-up, not a safety issue.
- **A10 (Optional/Bonus) Success Foundations Reflection** — already voluntary/0-obligation in the home course; leaving as-is satisfies Decision 029's spirit without any action needed.
- **`Bonus Practice` / `week-NN` (25-pt disciplinary gate)** — confirmed via live content read to be CS1's own Reasoning-Odyssey coursework, not shared/enrichment. Out of Decision 029's scope entirely. `Bonus Practice`'s own description hints it may be a legacy duplicate of `week-NN` ("fulfilled by the Reasoning Odyssey, not a required separate problem set") — an internal CS1 consistency question for Jeremy, unrelated to this campaign.
- **`Friday — Exit ticket`** (and the separate Monday/Wednesday exit tickets) — confirmed via content read to be a logistics check-in tied to the A04–A06 career work, not independent shared/enrichment paperwork; rides with the A01–A09 preserve decision.
- **`W16-farkle-ml-experiment-receipt`** — already 0-points/ungraded structurally; the canonical `Farkle_and_Machine_Learning` repo remains outside this campaign's writable/readable roots, same gap the Architecture pass recorded. No urgency.
- **Orphaned rubric Pages** — several deleted assignments (e.g. Monday Moment, Professional Minds reading/slides) had a separate rubric *Page* module item that is not attached to the Assignment object and is therefore untouched by `delete_assignment`. These are harmless dead weight in busy weekly modules, not a safety issue, but a follow-up pass could clean them for tidiness.

## Follow-up (recorded, not blocking course cleanliness)

1. Commons harvest for A01–A09 (career/degree-planning strand) — nine candidate Commons pages, content drafted during this pass's Terra recon (available in the campaign's working notes) but not yet authored/published, since it affects only future terms, not this term's live course.
2. Genericize the `professional-pathway-career-artifacts` Commons page's Architecture-specific wording now that a second course (CS1) points at it.
3. Optional cleanup of orphaned rubric Pages left behind by this pass's deletions.
4. `Bonus Practice` vs. `week-NN` internal-consistency question — flagged for Jeremy, not a Decision 029 matter.

## Verdict

`CS1 DECISION-029 SHARED-STRAND CLEANUP COMPLETE — 112/117 CANDIDATES REMOVED, 5 CORRECTLY DEFERRED, A01-A09 CORRECTLY PRESERVED (REAL EARNED CREDIT)`

CS1's required grade no longer carries AI Fluency, Professional Minds, or in-class-only pair-programming/show-and-tell paperwork as online graded obligations. Disciplinary coursework (`week-NN`, `Bonus Practice`, `A5-final-reflection`, Attendance, Course Evaluation, Roll Call) is untouched. Real student work (A01–A09, exit tickets, Week 2 shared-strand instances, Roll Call) is untouched. Committed and pushed.
