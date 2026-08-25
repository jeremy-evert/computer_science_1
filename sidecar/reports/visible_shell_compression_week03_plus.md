# Report — CS1 student-visible module shell compression, Week 03+

Follow-on to `sidecar/reports/029_shared_strand_cleanup.md`, applying the same visible-shell doctrine used on Computer Architecture (Prompt 030C) to CS1 (74029), at the owner's direct request in this session.

## Hard boundary respected

**Week 2 is active student territory** (Monday Moment week 2 due the day of this pass, other Week 2 items due through 2026-08-31) and was never touched. Verified before and after: module 218504 held 25 items both times.

## What was done

For each substantive week (3–16), the module shell was compressed to just the objects with real, current value:

- the week's disciplinary "week-NN" Reasoning-Odyssey-style gate assignment (where one exists — weeks 3–14 only; weeks 15/16 have no such gate) plus its rubric page;
- "Bonus Practice (Week NN)" where it exists (weeks 3–5, 7–8, 10–13; several weeks never had one);
- the week's own lesson/topic page, **only for the week that actually introduces that lesson chapter** (see bug note below) — weeks 3, 5, 7, 8, 10, 12, 14;
- Week 16 additionally keeps its Farkle/ML topic page and its `W16-farkle-ml-experiment-receipt` assignment.

Removed from the module path (unlinked, not deleted — objects remain live and reachable, matching the Architecture pass's fallback since `delete_page`/`delete_file` were unreliable under this session's safety classifier): Monday Moment Activity pages and their now-orphaned rubric pages (the graded Assignment versions were already deleted in the earlier Decision 029 pass), Professional Minds Wednesday/Friday reading pages, slide Files, and their orphaned rubric pages.

## Bug found and fixed before this report was written

The first automated pass (a single loop across all 14 weeks, done for speed at the owner's request to move faster) guessed that each week's lesson-topic page follows the pattern `NN-topic` for week `NN`. That is wrong: CS1's lesson chapters (`lessons/01-foundations...md` through `lessons/10-farkle-ml.md`) are introduced only on the weeks that actually cover new material — confirmed by reading each week's own assignment description, which cites its `Concept: lessons/0N-x.md` explicitly. Weeks 4, 6, 9, 11, 13 deliberately reuse a previous week's chapter (or are pure checkpoint/synthesis weeks) and never had their own topic page in the module at all.

The wrong pattern caused two real problems, caught before reporting:

1. Weeks 5, 7, 8, 10, 12, 14 had their real topic page (`04-loops`, `05-functions`, `06-strings`, `07-collections`, `08-classes-and-modules`, `09-projects-tools-and-reflection` respectively) wrongly unlinked.
2. Weeks 15 and 16 — which have no `week-NN` gate assignment at all — matched nothing in the guessed keep-set and were emptied to **0 module items**.

Fixed via `create_module_item` (confirmed not blocked by the session classifier, unlike content-edit calls) after determining the correct owning week for each page from its own content and each assignment's `Concept:` citation:

- re-linked the six wrongly-removed topic pages to their correct weeks;
- re-linked Week 16's `10-farkle-ml` page (its own body says "Week 16") and `W16-farkle-ml-experiment-receipt` assignment;
- re-linked Week 15's Monday Moment page as a minimal anchor (see gap below).

Independently re-verified every week's final module contents after the fix — see receipt.

## Content gap flagged, not invented

**Week 15 ("Modern AI") has no dedicated disciplinary object live** — no `week-15` gate assignment, no topic page of its own. Its only content is the standard Monday Moment/Professional Minds shared strand (which happens to be thematically about AI evaluation this week — `week-15-wed-evaluating-llms`, `week-15-fri-evaluating-ai-harms` — but these are the same templated Professional Minds reading format used every week, not CS1-authored disciplinary content). A Monday Moment page was restored as a minimal anchor so the module isn't empty; this is flagged for Jeremy's awareness, not resolved — building Week 15's actual disciplinary content (if intended) is out of this cleanup mission's scope.

## Result

| Week | Kept items |
|---|---|
| 3 | 03-branching, Bonus Practice, week-03, week-03_rubric |
| 4 | Bonus Practice, week-04, week-04_rubric |
| 5 | 04-loops, Bonus Practice, week-05, week-05_rubric |
| 6 | week-06, week-06_rubric |
| 7 | 05-functions, Bonus Practice, week-07, week-07_rubric |
| 8 | 06-strings, Bonus Practice, week-08, week-08_rubric |
| 9 | week-09, week-09_rubric |
| 10 | 07-collections, Bonus Practice, week-10, week-10_rubric |
| 11 | Bonus Practice, week-11, week-11_rubric |
| 12 | 08-classes-and-modules, Bonus Practice, week-12, week-12_rubric |
| 13 | Bonus Practice, week-13, week-13_rubric |
| 14 | 09-projects-tools-and-reflection, week-14, week-14_rubric |
| 15 | Monday Moment (flagged content gap) |
| 16 | 10-farkle-ml, W16-farkle-ml-experiment-receipt |

No assignment content, points, due dates, submissions, grades, comments, or rubrics were modified. No underlying object was deleted this pass — only module-item links were removed or restored. Full machine receipt: `sidecar/raw/2026-08-25T201807Z__visible_shell_compression_week03_plus.json`.

## Verdict

`CS1 VISIBLE SHELL COMPRESSION COMPLETE — WEEK 02 PROTECTED, WEEKS 03-16 COMPACT, WEEK 15 CONTENT GAP FLAGGED FOR JEREMY`
