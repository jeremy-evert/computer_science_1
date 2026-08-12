# Report 011 — CS1 core coverage matrix and open-resource slurp

**Prompt:** `jeremy_task_tracking/codex_prompts/017_cs1_core_coverage_matrix_and_open_resource_slurp.md`
**Scope:** Fall 2026 COMSC 1033 (CS1) only. Research, quantified coverage matrix, and a bounded rights-aware capture. No Canvas, Savnac, production ZyBooks, or student data touched; no course weeks or assignments rewritten.
**Research/access date:** 2026-08-12.
**Prior evidence read first:** `reports/010_cs1_evidence_review_and_free_alternatives.md` (treated as background; Jeremy's pinned decisions in prompt 017 are authoritative where they conflict with anything older).

## Read this first

CS50P (Harvard's *Introduction to Programming with Python*) is the strongest single no-cost starting source against the pinned C01–C13 core: it is the only evaluated resource with both a dedicated Unit Tests week (C10) and a dedicated Object-Oriented Programming week (C08), it has the strongest built-in autograded practice loop (`check50`/`style50`) of anything reviewed, and its CC BY-NC-SA 4.0 license explicitly permits noncommercial adaptation and redistribution with attribution — compatible with a public, noncommercial university course. It does **not** cover Git/GitHub (C12) or AI-aware programming (C13); those are filled by GitHub Skills' "Introduction to GitHub" (MIT-licensed) and GitHub Docs' "Review AI-generated code" tutorial (CC BY 4.0) respectively. Two remaining soft holes — C09 (files/CSV/JSON/persistence, currently a "2") and C11 (technical judgment/explanation, currently a "1–2") — get a light supplemental read each rather than a full second textbook.

Also found and flagged, not fixed: `assignments/A2-coding-odyssey-project.md` (line 50) and `planning/coding-odyssey-arc-map.md` (line 80) both still require every genre to support "at least one class hierarchy" by the Week 16–17 capstone. Prompt 017 pins inheritance/class hierarchies as explicitly **not** required core (C08). This is a real conflict between shipped assignment text and Jeremy's newer pinned decision — see Section A and Section H.

## A — Pinned CS1 core and Odyssey fit

Fit check against the four current genres: Frontier Settlement, Investigation Bureau, Starship Log, Small Business. Source files reviewed: `assignments/A2-coding-odyssey-project.md`, all 16 files in `assignments/odyssey_gates/`, all 16 files in `rubrics/odyssey_gates/`, `planning/coding-odyssey-arc-map.md`.

| Core ID | Capability | Why CS1 needs it | Frontier | Investigation | Starship | Small Business | Existing Odyssey evidence | Conflict/stale requirement |
|---|---|---|---|---|---|---|---|---|
| C01 | Run, read, and change Python | Entry skill; needed before anything else | Natural | Natural | Natural | Natural | Week 1 universal foundations (no Odyssey gate yet) | None |
| C02 | Values, variables, expressions, I/O | Powers first world state | Natural (resources, colonist counts) | Natural (case numbers, evidence tallies) | Natural (crew counts, fuel) | Natural (inventory counts, prices) | Week 2 gate: computed-value requirement | None |
| C03 | Decisions | State-dependent behavior | Natural (event branches) | Natural (suspect logic) | Natural (system status branches) | Natural (stock/reorder logic) | Week 3–4 gates | None |
| C04 | Repetition | Variable/unknown amounts of work | Natural (seasons, colonist processing) | Natural (case list processing) | Natural (log entries, crew roster loop) | Natural (transaction batches) | Week 5 gate | None |
| C05 | Functions and decomposition | Breaks the world into actions | Natural (`found_settlement()`, `harvest()`) | Natural (`open_case()`, `interview()`) | Natural (`log_entry()`, `jump()`) | Natural (`sell_item()`, `restock()`) | Week 7 gate: refactor into parameter/return function | None |
| C06 | Strings and text | Real text in the world | Natural (event narration) | Natural (case notes — strongest genre fit; text-analysis side-quest) | Natural (log narration) | Natural (receipts, item descriptions) | Week 8 gate | None |
| C07 | Collections | Model a growing world | Natural (colonist list, resource dict) | Natural (evidence list, suspect dict) | Natural (crew list, systems dict) | Natural (inventory list, customer dict) | Week 10–11 gates | None |
| C08 | Classes and objects (no inheritance requirement) | Turn a real noun into a class with state/behavior | Natural (`Colonist`, `Settlement`) | Natural (`Case`, `Suspect`) | Natural (`CrewMember`, `Ship`) | Natural (`Product`, `Customer`) | Week 12–13 gates: "Introductory OOP only" per Report 010 | **Stale requirement found** — see below |
| C09 | Files and persistence (CSV/JSON/Markdown) | Save/reload a persistent world; CSV/JSON/Markdown specifically named as important formats | Natural (save colonist roster to CSV/JSON) | Natural (case files as Markdown reports, evidence as JSON) | Natural (flight log as Markdown, telemetry as CSV/JSON) | Natural (inventory as CSV, receipts as Markdown) | "save/load state" is explicit in the genre menu (A2 line 50-51) | None — this is correctly pinned and already required |
| C10 | Testing and debugging | Evidence code works | Natural (test a harvest edge case) | Natural (test a false-lead edge case) | Natural (test a fuel-empty edge case) | Natural (test a zero-stock edge case) | Week 7 gate requires a passing test; checkpoints require demonstrate/explain | None |
| C11 | Technical judgment and explanation | Explain/compare/defend choices | Natural | Natural | Natural | Natural | Decide/Compare instrument, Weeks 11 and 16; Judgment Log/World Bible | None |
| C12 | Git and GitHub | Meaningful commits, collaboration | Genre-neutral (tooling, not world content) | Genre-neutral | Genre-neutral | Genre-neutral | Week 14: dedicated Git/GitHub professional-workflow week | None |
| C13 | AI-aware programming | Use AI while remaining accountable | Genre-neutral | Genre-neutral | Genre-neutral | Genre-neutral | Monday Moments AI Fluency lenses run in parallel every week; Full Trail Debrief (Wk14) requires disclosure of tool use | None |

**Stale requirement, flagged not fixed (per prompt boundary):** `assignments/A2-coding-odyssey-project.md` line 50–51 and `planning/coding-odyssey-arc-map.md` line 80 both state every genre must support, by the Week 16–17 capstone, "a collection of things, text data, a save/load state, **at least one class hierarchy**, and a numeric feature." Persistence ("save/load state") correctly matches pinned C09. **"At least one class hierarchy" does not match pinned C08**, which explicitly states "Inheritance/class hierarchies are not required core." This is the same wording in two files (the assignment's own genre-menu paragraph and the arc-map's genre-menu restatement), so it is one stale decision propagated to two places, not two independent errors. Recommend a narrow follow-up prompt that either (a) drops "at least one class hierarchy" from the capstone requirement entirely, or (b) demotes it to an *optional* enrichment note, consistent with C08's non-required status. Do not repair in this prompt.

One additional non-blocking observation: `planning/week-13.md` line 11 frames "composition vs. inheritance" as a Decide/Compare *comparison* option, not a requirement to implement inheritance — that phrasing is consistent with C08 and needs no change.

## B — Candidate resource scorecard

Full machine-readable version: `reports/011_cs1_resource_coverage_matrix.csv` and `reports/011_cs1_resource_coverage_matrix.json`. Scoring method: 0 = absent, 1 = mentions/weak support, 2 = teachable coverage but incomplete or weak practice, 3 = strong beginner-appropriate treatment with usable examples/practice/evidence. Dimension columns (Beginner clarity, Practice, Link granularity, Accessibility, Currency, Friction) use the same 0–3 scale. Rights category is categorical evidence, not a score.

| Resource | Cost/account | Rights category | C01 | C02 | C03 | C04 | C05 | C06 | C07 | C08 | C09 | C10 | C11 | C12 | C13 | Beginner clarity | Practice | Link gran. | Accessibility | Currency | Friction | Weighted/summary judgment |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CS50P** | Free, no account to read/watch; free CS50 ID/GitHub only for autograder/certificate | OPEN-REUSE (CC BY-NC-SA 4.0) | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 0 | 1 | 3 | 3 | 3 | 3 | 2 | 2 | **Selected starting source** — see Section C |
| Python official docs/tutorial | Free, no account | OPEN-REUSE (PSF License v2; code 0BSD) | 2 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 1 | 1 | 0 | 0 | 2 | 1 | 3 | 2 | 3 | 3 | Best reference layer; kept under CS50P, not as the spine (assumes background, no practice loop) |
| Python for Everybody (PY4E) | Free, no account (book); optional free account (interactive edition) | OPEN-REUSE (CC BY 4.0) | 2 | 3 | 2 | 3 | 3 | 2 | 3 | 1 | 2 | 1 | 2 | 0 | 0 | 3 | 2 | 2 | 2 | 2 | 2 | Best true-novice clarity and most permissive license; weak on OOP (C08) and testing (C10) |
| Runestone FOPP | Free, no account to read | OPEN-REUSE (GNU FDL 1.3+) | 2 | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 0 | 0 | 3 | 3 | 3 | 2 | 2 | 2 | Closest runner-up to CS50P; strongest embedded interactive practice of the text-first candidates |
| Automate the Boring Stuff, 2e | Free, no account | OPEN-REUSE (CC BY-NC-SA 3.0) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 3 | 2 | 1 | 0 | 0 | 3 | 1 | 2 | 2 | 2 | 3 | Not backbone-strength, but the strongest reviewed C09 (CSV/JSON/file) treatment — used as a hole filler |
| Software Carpentry (python-novice-gapminder) | Free, no account | OPEN-REUSE (CC BY 4.0 lessons; MIT code) | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 2 | 2 | 2 | 2 | 2 | 2 | Data/plotting workshop framing; weak genre fit; not recommended (Section G) |
| Exercism Python Track | Free; account for mentoring/progress | PERMISSION-UNCLEAR (bundle-level; per-repo license not individually reverified) | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 0 | 2 | 1 | 0 | 0 | 2 | 3 | 1 | 2 | 3 | 2 | Best practice/mentoring loop reviewed; held at metadata-only pending explicit license confirmation |
| GitHub Skills — Introduction to GitHub | Free; GitHub account required | OPEN-REUSE (MIT) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 3 | 2 | 2 | 3 | 2 | **Selected C12 hole filler** |
| GitHub Docs — Review AI-generated code | Free, no account | OPEN-REUSE (CC BY 4.0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 2 | 1 | 3 | 2 | 3 | 3 | **Selected C13 hole filler** (partial — written for working developers, needs instructor framing for CS1 novices) |

Evidence trail for nontrivial ratings: CS50P's C10/C08 = 3 and syllabus structure were confirmed by direct capture of the weekly landing pages (`cs50.harvard.edu/python/weeks/0/`–`/9/`, 200 OK each; Week 5 = "Unit Tests," Week 8 = "Object-Oriented Programming," Week 6 = "File I/O" with on-page "CSV. dict" concept tags). CS50P's license was confirmed on-page (`/python/license/`, CC BY-NC-SA 4.0 text captured verbatim). PY4E's CC BY 4.0 (rather than the older CC BY-NC-SA the book once used) was confirmed via `py4e.com/materials` and the `py4e` GitHub repo. Runestone FOPP's GNU FDL was confirmed via its own copyright page and cross-referenced against Runestone's general open-source posture. Automate the Boring Stuff's CC BY-NC-SA 3.0 was confirmed via direct fetch of `automatetheboringstuff.com`. Software Carpentry's CC BY 4.0/MIT split was confirmed via its own `LICENSE.html`. GitHub Skills' MIT license and GitHub Docs' CC BY 4.0 were each confirmed by fetching the primary-source `LICENSE` file directly (`raw.githubusercontent.com/skills/introduction-to-github/main/LICENSE`; `github.com/github/docs/blob/main/LICENSE`).

## C — Starting-source selection

| Candidate | Strengths | Weaknesses | Strong-core count (score=3) | Clear-hole count (score 0–1) | Rights/slurp status | Why selected/not selected |
|---|---|---|---|---|---|---|
| **CS50P** | Dedicated Unit Tests + OOP weeks; best autograded practice loop; strong accessibility (captions/transcripts); current, actively maintained | No Git/GitHub or AI-aware content; NC-SA license constrains any adapted republishing to noncommercial/share-alike (acceptable for this noncommercial public course, but worth flagging) | 7 (C01, C02, C03, C04, C05, C08, C10) | 2 (C12=0, C13=1) | OPEN-REUSE; captured (bounded) | **Selected.** Highest strong-core count of any single general-Python resource, best practice loop, acceptable license for our use case. |
| Runestone FOPP | Most permissive license (GFDL); best embedded practice among pure-text books | No dedicated unit-testing pedagogy; weaker OOP treatment than CS50P | 5 | 2 (C12, C13) | OPEN-REUSE; metadata-only | Strong runner-up; not selected because CS10/C08 depth loses to CS50P and it lacks CS50P's grading loop. Worth keeping as a linked alternative for students who prefer a pure-text/interactive-exercise format over video lectures. |
| PY4E | Best true-novice clarity; most permissive simple license (CC BY, no SA) | Very weak OOP (C08=1); weak testing (C10=1) | 3 | 2 (C08, C10 near-hole; C12, C13 absent) | OPEN-REUSE; metadata-only | Not selected as spine because C08/C10 are both pinned core and PY4E under-serves both; kept as a supplemental link for Weeks 2–3 and Weeks 10–11 if CS50P's pace needs a gentler on-ramp. |
| Automate the Boring Stuff | Strongest practical C09 (files/CSV/JSON) content of anything reviewed | No autograding; uneven OOP/testing depth | 1 | 4 | OPEN-REUSE; metadata-only | Not a backbone; selected narrowly as the C09 hole-filling supplement (Section E/F). |
| Python official docs | Most authoritative and most permissively licensed (PSF/0BSD); best link granularity | No built-in practice/feedback; assumes background | 5 | 3 (C10, C11, plus C12/C13 absent) | OPEN-REUSE; metadata-only | Kept as the reference layer underneath CS50P (students who want the primary-source doc for any concept), not the primary teaching text. |
| Software Carpentry | CC BY 4.0, workshop-tested | Data/plotting framing, no OOP, weak genre fit | 0 | 6 | OPEN-REUSE; metadata-only | Not recommended — see Section G. |
| Exercism | Best practice/mentoring loop reviewed | License unclear at bundle level; not a teaching text | 0 | 5 | PERMISSION-UNCLEAR; metadata-only | Not selected as backbone (not a text); considered for C10 hole-filling but held back pending a license check (Section E). |

## D — Capture/slurp receipt

Durable corpus root: `/mnt/brandy_nvme/jevert/durable/cs1_open_resources/` (non-Git, matches the `zybooks_captures/` pattern: `raw/`, `normalized/`, `manifest.jsonl`, plus a `course_manifest.json` summary and a `metadata_only_sources.jsonl` for evaluated-but-not-captured candidates).

| Source | Attempted | Captured | Metadata-only | Skipped-rights/terms | Failed | Bytes | Manifest path |
|---|---:|---:|---:|---:|---:|---:|---|
| CS50P (home, license, weeks 0–9) | 12 | 12 | 0 | 0 | 0 | 219,914 | `/mnt/brandy_nvme/jevert/durable/cs1_open_resources/manifest.jsonl` |
| GitHub Docs — Review AI-generated code | 1 | 1 | 0 | 0 | 0 | 601,620 | same |
| GitHub Skills — intro-to-github README+LICENSE | 2 | 2 | 0 | 0 | 0 | 3,450 | same |
| Python official docs/tutorial | — | 0 | 1 | 0 | 0 | 0 | `metadata_only_sources.jsonl` |
| PY4E | — | 0 | 1 | 0 | 0 | 0 | same |
| Runestone FOPP | — | 0 | 1 | 0 | 0 | 0 | same |
| Automate the Boring Stuff | — | 0 | 1 | 0 | 0 | 0 | same |
| Software Carpentry | — | 0 | 1 | 0 | 0 | 0 | same |
| Exercism Python Track | — | 0 | 1 | 0 | 0 | 0 | same |
| **Totals** | **15** | **15** | **6** | **0** | **0** | **820,984** | — |

Capture boundaries (recorded in `course_manifest.json`):

- **CS50P capture is intentionally bounded to landing/index pages** (title, nav, headline concept list, on-page license block) for the home page, the license page, and each of the 10 weekly pages (12 pages total). Full lecture notes, video transcripts, slides, "Shorts," and problem-set specs were **not** mirrored — they remain link-only. This keeps the corpus lean per the prompt's "lean and sufficient" instruction, while the license (CC BY-NC-SA 4.0) would in fact permit a fuller mirror if a later prompt decides one is worth the storage/upkeep cost.
- `cs50.harvard.edu/robots.txt` returned HTTP 404 (no robots.txt published, no explicit crawl restriction found). Capture volume was kept small regardless, and a descriptive User-Agent identifying the request as noncommercial course-build research was used throughout.
- Six other evaluated candidates (Python docs, PY4E, Runestone FOPP, Automate the Boring Stuff, Software Carpentry, Exercism) were deliberately held to **metadata-only** (URL, license, access-date, core tags, capture decision recorded) per the prompt's explicit instruction not to slurp multiple general textbooks automatically.
- Every captured raw file has a SHA-256 hash recorded in `manifest.jsonl`; normalized plain-text extracts of the 12 CS50P pages are stored alongside under `normalized/`.
- Nothing in this durable corpus was or will be committed to Git.

## E — Hole matrix after starting source (CS50P)

| Core ID | Target | CS50P score | Exact missing piece | Hole severity | Best hole-specific candidates | Recommended filler |
|---|---|---:|---|---|---|---|
| C12 | Git and GitHub | 0 | No Git/GitHub content anywhere in CS50P | Clear hole | GitHub Skills "Introduction to GitHub" (MIT, hands-on, free); GitHub Docs "Git and GitHub learning resources" index | **GitHub Skills — Introduction to GitHub** (captured, Section D) |
| C13 | AI-aware programming | 1 | CS50.ai exists as a study aid but there is no instruction on *evaluating/testing/disclosing* AI-generated code | Clear hole (score 1) | GitHub Docs "Review AI-generated code" (CC BY 4.0, primary source, current); various commercial 2026 blog posts (ContextQA, Skyramp, Momentic — reputable-looking but license/reuse status unclear, not OER) | **GitHub Docs — Review AI-generated code**, with instructor framing to make it CS1-novice-appropriate (partial fill, not full — flagged, not silently treated as solved) |
| C09 | Files and persistence (CSV/JSON/Markdown) | 2 | CS50P's File I/O week explicitly covers `open`, `list`, `sorted`, `with`, and CSV via `dict`; JSON and Markdown-specific handling were not confirmed present on the captured landing page | Possible hole (judgment call) | Automate the Boring Stuff's file/CSV/JSON chapters (CC BY-NC-SA 3.0); Python docs `json`/`csv` module pages (PSF/0BSD) | **Automate the Boring Stuff (file/CSV/JSON chapters, link-only)** as a light supplemental read, plus a direct link to the Python docs `json` module page. Do not add a second full textbook. |
| C11 | Technical judgment and explanation | 2 | CS50P's "Libraries" and "Et Cetera" weeks build some judgment/comparison habits but there is no dedicated compare-and-defend instrument comparable to Odyssey's own Decide/Compare | Possible hole (judgment call) | None found that beats the course's own instrument | **No external filler recommended** — Odyssey's own Decide/Compare (Weeks 11 and 16) and Judgment Log already carry this outcome; treat CS50P as reinforcement only, not primary evidence source for C11. |
| C06 | Strings and text | 2 | Present via Week 7 Regular Expressions, but no single dedicated "strings" week the way branching/loops/functions each get one | Possible hole (judgment call) | PY4E's dedicated strings chapter (CC BY 4.0) | Optional link to PY4E's strings chapter if a student wants more; not required — Odyssey's Week 8 gate already supplies the authentic practice. |
| C07 | Collections | 2 | Lists/dicts used throughout CS50P but no single dedicated "collections" week | Possible hole (judgment call) | Python docs data-structures chapter; PY4E Chapters 8–10 | Optional links only; Odyssey Weeks 10–11 gates already supply authentic practice. |

All other core IDs (C01–C05, C08, C10) scored 3 on CS50P and need no filler.

## F — Proposed zero-cost learning package

| Core ID | Primary learning source | Supplemental source if needed | Practice/feedback source | Direct link(s) | Account | License/access | Why this is enough |
|---|---|---|---|---|---|---|---|
| C01–C05, C10 | CS50P Weeks 0–3, 5 | Python docs tutorial (reference) | CS50P `check50`/`style50` | `cs50.harvard.edu/python/weeks/{0,1,2,3,5}/` | None to read; free CS50 ID for autograder | CC BY-NC-SA 4.0 | Highest-scoring, best-practiced source for these IDs; already captured |
| C06 | CS50P Week 7 | PY4E strings chapter (optional) | CS50P problem sets | `cs50.harvard.edu/python/weeks/7/` | None | CC BY-NC-SA 4.0 / CC BY 4.0 | Sufficient; Odyssey Week 8 gate supplies authentic practice |
| C07 | CS50P (throughout) | Python docs data structures chapter | CS50P problem sets; Odyssey Weeks 10–11 gates | `docs.python.org/3/tutorial/datastructures.html` | None | PSF/0BSD | Sufficient given authentic gate practice |
| C08 | CS50P Week 8 | — | CS50P problem sets | `cs50.harvard.edu/python/weeks/8/` | None | CC BY-NC-SA 4.0 | Dedicated OOP week; no inheritance requirement to satisfy per C08 |
| C09 | CS50P Week 6 | Automate the Boring Stuff (file/CSV/JSON chapters); Python docs `json` module | CS50P problem sets | `cs50.harvard.edu/python/weeks/6/`; `automatetheboringstuff.com`; `docs.python.org/3/library/json.html` | None | CC BY-NC-SA 4.0 / 3.0; PSF/0BSD | Confirmed CSV coverage plus a light, license-clean supplement closes the JSON/Markdown gap without a second textbook |
| C11 | Odyssey's own Decide/Compare + Judgment Log | CS50P Weeks 4/9 (light reinforcement) | Odyssey gate rubrics | `docs/curriculum/judgment_toolkit.md` | None | Course-owned | The authentic instrument already exceeds anything found externally |
| C12 | GitHub Skills — Introduction to GitHub | GitHub Docs learning-resources index | GitHub Skills' own automated exercise checks | `github.com/skills/introduction-to-github` | Free GitHub account | MIT | Official, hands-on, real repo/PR practice; matches Week 14's existing Git/GitHub focus |
| C13 | GitHub Docs — Review AI-generated code | Monday Moments AI Fluency lenses (course-owned) | Full Trail Debrief disclosure requirement (Wk14) | `docs.github.com/en/copilot/tutorials/review-ai-generated-code` | None | CC BY 4.0 | Best free primary-source reading found; the course's own Monday Moments/Debrief carry most of the actual assessed C13 outcome |

## G — What not to pull

- **Software Carpentry / Data Carpentry "Plotting and Programming in Python"** — openly licensed (CC BY 4.0) and well-built, but its data/plotting-for-researchers framing has no natural genre fit inside any of the four Coding Odyssey worlds and it has zero OOP content (C08 = 0). Redundant with CS50P/PY4E for everything it does cover.
- **A second full general-Python textbook alongside CS50P** (e.g., adding Runestone FOPP or PY4E as a co-equal required text) — both are strong resources and are kept as *optional* linked supplements, but adding either as a second required spine would violate the prompt's "lean and sufficient" instruction and duplicate authentic Odyssey practice that already covers C06/C07.
- **Exercism's exercise bodies (copied/rehosted)** — the practice/mentoring loop is excellent, but the per-repo license for the Python track specifically was not individually reverified in this pass (only a sibling repo's MIT license was confirmed). Link to Exercism; do not copy or embed its exercise text until a named future prompt confirms the Python track's own license.
- **Commercial 2026 "how to review AI-generated code" blog posts** (ContextQA, Skyramp, Momentic, etc.) surfaced during the C13 hole search — plausible-looking and current, but none stated a clear reuse license, and their audience is professional engineering teams, not CS1 novices. GitHub Docs' own tutorial was chosen instead specifically because its license and provenance are unambiguous.
- **A full-course mirror of every CS50P page** (video transcripts, slides, full problem-set specs) — the license would permit it, but it is unnecessary for this task's purpose (coverage judgment + a small anchor capture) and would meaningfully grow an unreviewed non-Git corpus. If a later prompt decides to actually build Canvas-facing links/embeds from CS50P, that prompt should do its own bounded, purpose-built capture rather than assuming this one is exhaustive.

## H — Decisions / next bounded prompts

Kept narrow and separated by kind, per the prompt's instruction:

**Mechanical course-source reconciliation (small, low-risk, do next if picking one):**
1. Fix the stale "at least one class hierarchy" capstone requirement in `assignments/A2-coding-odyssey-project.md` (line 50–51) and `planning/coding-odyssey-arc-map.md` (line 80) to match pinned C08 (inheritance not required). Recommend simply dropping the clause or rewording to "at least one class with meaningful state/behavior" — a two-file, few-word fix, but it is a real drift from Jeremy's newer pinned decision and should not be silently carried forward into Fall 2026 materials.
2. No other stale wording was found in the Odyssey gate/rubric files reviewed for this prompt (all 16 gate files and all 16 rubric files were scanned for `class hierarchy`, `save/load`, and `inheritance`; only the two occurrences above and one unrelated Decide/Compare mention in `planning/week-13.md` — which is fine as written — turned up).

**Resource publication/deployment (separate, larger, do only after a decision meeting with Jeremy):**
3. A decision prompt that confirms whether CS50P becomes the *linked* backbone in student-facing materials (Canvas/Savnac week pages), and if so, drafts the actual link map (per-week CS50P URL + GitHub Skills + the two hole-filler links) into the course's existing week files — this is publication work, explicitly out of scope for this research-only prompt.
4. If Jeremy wants a fuller CS50P mirror for offline/durability reasons (e.g., against future URL rot), a follow-up capture prompt scoped specifically to "mirror CS50P's full lecture notes for weeks 0–9" — bounded, rights-checked (license already confirmed permissive), and separate from this prompt's small anchor capture.
5. A short prompt to individually confirm the Exercism Python track's own repository license before any of its exercise text is used beyond linking.

## Boundaries respected

No Canvas or Savnac writes. No production ZyBooks writes. No student data. No course weeks or assignments rewritten (the stale "class hierarchy" wording was flagged, not repaired). No third-party copyrighted bodies committed to Git — all raw captures live under `/mnt/brandy_nvme/jevert/durable/cs1_open_resources/`, outside any Git repository. No authentication, paywall, robots, or access-restriction bypass attempted; `cs50.harvard.edu/robots.txt` was checked (404 = none published) before the bounded capture.

## Commands run

```
git status --short --branch
git pull --ff-only  (implicit: repo was already clean and up to date with origin/main)
WebFetch / WebSearch: license and syllabus verification for CS50P, Python docs, PY4E,
  Runestone FOPP, Automate the Boring Stuff, Software Carpentry, Exercism,
  GitHub Skills, GitHub Docs
curl (bounded capture): CS50P home/license/weeks-0-9 (12 pages, 200 OK each);
  GitHub Docs AI-code-review page; GitHub Skills intro-to-github README+LICENSE
python3: manifest/course_manifest/metadata_only JSON builders; CSV/JSON matrix builder;
  HTML-to-text normalization for the 12 captured CS50P pages
sha256sum: content-hash verification for all captured raw files
```

## Validation / test results

This is a research-and-capture task with no application code changed. `make task-check` / `make check` were checked for applicability:

```
$ make task-check
make: *** No rule to make target 'task-check'.  Stop.
$ make check
make: *** No rule to make target 'check'.  Stop.
```

No `Makefile` exists in this repository (confirmed: `ls Makefile` → not found). Both targets are unavailable, not skipped; this matches the repo's existing pattern (no other CS1 report records a working `make` target).

`git diff --check` was run before the final commit (see below) and reported no whitespace errors.

## Limitations

- The CS50P capture is bounded to landing/index pages, not full lecture content; C06/C07/C09/C11 scores for CS50P are therefore judgment calls informed by the syllabus structure and the captured landing-page concept tags, not a line-by-line read of every lecture transcript.
- Exercism's Python-track-specific license was not individually reverified (only a sibling-language repo's MIT license was confirmed); it is held at metadata-only/PERMISSION-UNCLEAR pending that check.
- No accessibility audit beyond published evidence (captions/transcripts existing for CS50P; general web accessibility of the other sites was not independently tested with assistive technology).
- No student pilot of any resource was run; this report is evidence and recommendation only, not a validated classroom outcome.
- The "friction" and "currency" dimension scores are single-agent judgment calls informed by the evidence gathered, not a formal rubric independently cross-checked by a second reviewer.

## AGENTS.md status

Repository-local `AGENTS.md` was not separately re-read in full for this task (top-level `~/git/AGENTS.md` was read and followed; it states repo-local files may add stricter rules). No conflicts were observed between the top-level constitution and this prompt's instructions.

## Changed files

- `reports/011_cs1_core_resource_coverage_and_slurp.md` (new)
- `reports/011_cs1_resource_coverage_matrix.csv` (new)
- `reports/011_cs1_resource_coverage_matrix.json` (new)

Durable, non-Git artifacts (not part of any commit):
- `/mnt/brandy_nvme/jevert/durable/cs1_open_resources/course_manifest.json`
- `/mnt/brandy_nvme/jevert/durable/cs1_open_resources/manifest.jsonl`
- `/mnt/brandy_nvme/jevert/durable/cs1_open_resources/metadata_only_sources.jsonl`
- `/mnt/brandy_nvme/jevert/durable/cs1_open_resources/raw/cs50p/*.html` (12 files)
- `/mnt/brandy_nvme/jevert/durable/cs1_open_resources/raw/github_hole_fillers/*` (3 files)
- `/mnt/brandy_nvme/jevert/durable/cs1_open_resources/normalized/*.txt` (12 files)

## Next recommended prompt

`jeremy_task_tracking/codex_prompts/018_odyssey_class_hierarchy_wording_fix.md` (proposed, not written) — the narrow mechanical fix identified in Section H item 1. Larger resource-publication work (Section H items 3–5) should wait for an explicit decision from Jeremy given this is deliberately research-only.
