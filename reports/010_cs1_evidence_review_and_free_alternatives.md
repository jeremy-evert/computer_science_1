# Report 010 — CS1 evidence review and free alternatives

**Prompt:** `jeremy_task_tracking/codex_prompts/012_cs1_evidence_review_and_free_alternatives.md`  
**Scope:** Fall 2026 COMSC 1033 only; evidence and discussion recommendations, not a semester-plan change.  
**Research/access date:** 2026-08-12.  
**Licensed-material boundary:** the durable capture was used only as a TOC/inventory check. Its `course_manifest.json` identifies the course as CS1 and its `manifest.jsonl` has 476 entries; no licensed body text is reproduced here.

## Read this first

The current course is not a sequence of generic weekly homework sets. Its technical backbone is the Coding Odyssey: gates in Weeks 2–5, 7–8, and 10–13; four project checkpoints (6, 9, 14, 16); pair work in Weeks 10 and 13; and a final show-and-tell/debrief. Monday Moments (AI Fluency) and Professional Minds are separate, parallel strands. Therefore the relevant question is not “how do we replace 120 `KEEP` sections with 120 free sections?” It is which concepts students need to do the next gate and enter CS2, and what small amount of additional feedback is missing after the authentic work.

The current `KEEP` count is **120**, but it contains both core outcomes and breadth that the published Odyssey gates neither require nor assess (for example binary numbers, tuples/sets in Week 3, nested loops/loop-else, arbitrary arguments, operator overloading, and much of the modules chapter). The present evidence supports a **zero-cost outcome-equivalent path** for the actual technical spine, provided instructor-authored gates, feedback, and a lightweight local/autograder check remain available. ZyBooks' distinctive value is its integrated, immediately graded practice and consistent commercial UX—not irreplaceable reading content or the course's authentic assessment.

## A — Existing course architecture

| Week/block | Existing course focus | Existing project/gate/assessment | Special strand/module | Current source files | Notes/conflicts |
|---|---|---|---|---|---|
| 1 | Universal survival/degree/career launch; environment, `print`, `input`, first program | Setup + first submission; no Odyssey gate | Monday Moment + degree/career kickoff; show-and-tell | `planning/week-01.md`, `lessons/01-foundations-print-input.md` | Must remain universal; Odyssey genre pick was deliberately moved out. |
| 2 | Variables, expressions, types | Genre/charter + computed-value gate | AI Lens: context; Professional Minds | `week-02.md`, `odyssey_gates/week-02.md` | First CS1-specific Odyssey work. |
| 3 | Types/conversion/formatting; branching intro | Conditional changes world output | AI Lens: plan; Professional Minds | `week-03.md`, `week-03` gate | **Citation conflict:** plan calls branching “chapter 3”; current adoption is Types ch. 3 and Branching ch. 4. |
| 4 | Branching/decision making (two meetings) | Meaningful ≥2-branch decision | Lens: decompose; Professional Minds | `week-04.md`, `week-04` gate | Labor Day compression; no extra practice should be added casually. |
| 5 | Loops/repetition | Variable/unknown-event loop gate | Lens: select model; Professional Minds | `week-05.md`, `week-05` gate | Authentic loop is already required. |
| 6 | Loop consolidation; functions preview only | Checkpoint 1 baby project/dry run | Lens: prompt engineering; Professional Minds | `week-06.md`, `A2`, `week-06` gate | No graded functions yet by explicit decision. |
| 7 | Functions/decomposition + unit-test thinking | Refactor an action into parameter/return function; passing test | Lens: RAG; Professional Minds | `week-07.md`, `week-07` gate | High-value feedback point. |
| 8 | Strings/text processing | Parse/format actual world text | Lens: reason; Professional Minds | `week-08.md`, `week-08` gate | Optional text/NLP enrichment later, not a required outcome. |
| 9 | Strings continued | Checkpoint 2: first real project pass, collections state | Lens: generate; Professional Minds (Friday absent) | `week-09.md`, `A2`, `week-09` gate | Fall Break removes Friday. |
| 10 | Lists/dictionaries, lists first | Growing list gate; pair session | Lens: critique; Professional Minds | `week-10.md`, `week-10` gate, `A3` | Project supplies deliberate list use. |
| 11 | Dictionaries/reliability | Dict lookup + Decide/Compare #1 | Lens: verify; Professional Minds | `week-11.md`, `week-11` gate | Project supplies data-structure choice and edge-case explanation. |
| 12 | Classes/objects/modules round 1 | Turn a real noun into a class | Lens: revise; Professional Minds | `week-12.md`, `week-12` gate | Introductory OOP only. |
| 13 | Classes/modules round 2 | Interacting objects; pair session | Lens: decide; Professional Minds | `week-13.md`, `week-13` gate, `A3` | No need to force inheritance/operator overloading. |
| 14 | GitHub, pair programming, AI-aware coding | Checkpoint 3 + mandatory Full Trail Debrief | Lens: automate; Professional Minds | `week-14.md`, `A2`, `week-14` gate | Optional LLM API side quest, not graded. |
| 15 | Async consolidation/portfolio | Professional-pathway portfolio; no technical gate | Lens: measure (recorded) | `week-15.md`, `A6`, `week-15` gate | No new technical material; optional NLP/dataset side quests only. |
| 16 | Final creative pass/show-and-tell | Checkpoint 4 + Decide/Compare #2 | Lens: reflect; Professional Minds | `week-16.md`, `A2`, `week-16` gate | Consolidation, not ML/Farkle content. |
| 17/finals | Final portfolio/reflection | Final Odyssey debrief/Judgment Log; possible chapter exam | No new strands | `week-17-finals.md`, `week-17` gate | No new technical material. |

## B — Technical spine vs. ZyBooks vs. free alternatives

Exact section identifiers are retained as clusters from `planning/zybooks-section-decisions.csv`; “all” means every current `KEEP` in that stated range, not a claim that each is mandatory.

| Concept/topic | Why the course needs it | Current ZyBooks sections | Current Prompt-010 classification | Free reading/background candidate(s) | Free interactive/practice candidate(s) | License/access notes | Already practiced by project/gate? | Preliminary recommendation | Confidence/open question |
|---|---|---|---|---|---|---|---|---|---|
| Run code, I/O, errors, environment | Needed to begin and demonstrate a program | 1.1–1.10; 1.12–1.14; 1.19–1.21 | KEEP (16) | Python docs: tutorial/interpreter; PY4E Chs. 1–2 | Python Tutor for tracing; local interpreter | Python docs PSF/0BSD examples; PY4E CC BY-NC-SA; Python Tutor free web service. Accounts: none apparent. RAG: unclear for all. | Week 1 submission | CORE; ZyLabs are replaceable as practice, not as convenience | High; need accessibility review with actual students. |
| Variables, arithmetic, conversion, formatting | Directly powers Wk2 world state and later gates | 2.1–2.12; 3.1, 3.6, 3.8, 3.10 | KEEP (16) | Python tutorial (numbers, strings, control flow); PY4E Chs. 2–3 | Python Tutor; instructor tests/terminal | Python docs freely redistributable under PSF license; PY4E adaptation is NC-SA only. | Wk2 gate | CORE; `random`, module basics, and deep object framing are OPTIONAL SUPPORT | High. |
| Early survey of list/tuple/set/dict and binary | Useful vocabulary, but premature for this sequence | 3.2–3.5, 3.9 | KEEP (5) | Python tutorial data structures, deferred to Wk10–11 | Python Tutor later; no standalone task now | Same as above | No (until Wk9–11 for lists/dicts) | REPLACEABLE BY FREE; defer lists/dicts, make tuples/sets/binary REFERENCE | High: current gates do not need these in Wk3. |
| Branching and Boolean reasoning | Required for Wk3–4 meaningful choices | 4.1–4.12 | KEEP (12) | Python tutorial `if`; Python docs expressions | Python Tutor trace cases; one instructor-created boundary test | PSF license; no account. | Wk3/4 gates | CORE for if/elif/else, comparisons, Boolean operators, indentation; conditional expressions/identity are OPTIONAL SUPPORT | High. |
| Loops | Required to process recurring/unknown events | 5.1–5.12 | KEEP (12) | Python tutorial `for`, `range`, `break`/`continue`; PY4E Ch. 5 | Python Tutor + the gate's own run transcript | PSF / CC BY-NC-SA respectively. | Wk5 gate + Wk6 checkpoint | CORE for `for`/`while`, range, accumulation, sentinel, debugging; nested loops, loop-else, `enumerate` OPTIONAL SUPPORT | High. |
| Functions and tests | Required for Wk7 decomposition and CS2 readiness | 6.1–6.18 | KEEP (18) | Python tutorial functions; `unittest` docs as instructor reference | Local `unittest`/pytest-style single test; Python Tutor | Python docs reusable under PSF; no account. | Wk7 gate | CORE for definition, parameters, return, scope basics, tests; arbitrary args/multiple outputs/docstrings/engineering examples OPTIONAL SUPPORT | High; choose the exact no-cost test runner. |
| String manipulation | Required for Wk8 real text and later data input | 7.1–7.4 | KEEP (4) | Python tutorial text/data structures | Gate itself + Python Tutor | PSF license; no account. | Wk8 gate, Wk9 checkpoint | CORE | High. |
| Lists/dicts and reliability | Needed to model a growing world and defend a choice | 8.1–8.10, 8.12–8.15 | KEEP (14) | Python tutorial lists/dicts; PY4E Ch. 8 | Gate plus a small instructor edge-case fixture | PSF / CC BY-NC-SA. | Wk9–11 gates/checkpoint | CORE for append/iterate/dict lookup/mutation/edge cases; nesting, comprehensions, sorting, CLI args OPTIONAL SUPPORT/REFERENCE | High. |
| Classes and simple modules | Needed for planned Wk12–13 refactor and modest CS2 preparation | 9.1–9.10; 11.1–11.13 | KEEP (23) | Python tutorial classes/modules | Project refactor plus instructor-created constructor/method smoke test | PSF license; no account. | Wk12/13 gates, Wk14 checkpoint | CORE for `__init__`, state, methods, import/simple module; REFERENCE for operator overloading, GC, reloading/packages/most labs | High; define whether CS2 actually assumes modules beyond import. |
| Tooling, GitHub, collaboration, AI verification | Course-specific professional outcome | No essential ZyBooks cluster | Instructor path | GitHub Skills/docs; course handouts | Existing pair sessions, commits, checkpoint debriefs | GitHub account required for GitHub lane; rights/tool policies must be checked at adoption. | Wk10/13 pair work, Wk14 checkpoint | CORE but instructor-created; ZyBooks cannot replace it | High. |
| Files, exceptions, inheritance, recursion, algorithms/data science | Useful Python knowledge, not presently an outcome | Current CSV marks later material OPTIONAL/UNUSED | OPTIONAL/UNUSED | Python docs, later OER reading | Optional self-directed exercises only | Do not copy commercial exercises; free access alone is not redistribution permission. | No | REFERENCE / OPTIONAL SUPPORT, not a CS1 requirement | High: current design explicitly keeps these optional. |

### What ZyBooks adds, and what it does not

| ZyBooks contribution | Evidence-based value | Replaceable without purchase? | Caveat |
|---|---|---|---|
| Sequenced exposition and a single navigation surface | Reduces instructor curation and learner navigation burden | Yes, with linked Python docs/PY4E/Runestone-style material | Python tutorial says it assumes prior programming knowledge, so it needs instructor framing or beginner OER alongside it. |
| Embedded/automated zyLabs | Fast, standardized formative feedback | Yes, with Odyssey gates plus small instructor-owned tests/tracing exercises | Replacing it shifts some grading/feedback setup to instructor; do not treat free sites' exercises as copyable. |
| Large exercise bank and coverage breadth | Easy optional/remedial practice | Yes for concept access; not necessarily like-for-like UX | The current 120 KEEP inventory is not evidence that all 120 need grading. |
| Commercial accessibility/support/integration | Potentially lower friction when institution support is active | Partly | Must be tested with actual accessibility needs and LMS workflow; no price/accessibility conclusion was inferred from the capture. |

## C — Weekly practice load

| Week/topic | Existing authentic/project evidence | What skill still needs repetition? | Suggested required standalone problems | Suggested optional practice | Why this amount is enough | Free equivalent if no ZyBooks |
|---|---|---|---|---|---|---|
| 1 foundations | First program/submission and show-and-tell | Run, edit, observe error/output | 0 beyond first program | Python Tutor trace of a tiny I/O program | Launch already produces executable evidence; avoid double assignment | Local Python + Python Tutor. |
| 2 variables/expressions | Computed-value Odyssey gate | Conversion/formatting errors | 0; gate must include one computed value and sentence | 1–2 short conversion traces | Gate is the deliberate practice; traces target common misconception | Python docs/PY4E + Python Tutor. |
| 3–4 branching | Conditional gate then meaningful ≥2-branch gate | Boundary/invalid testing | 0; require 2 named test cases in gate evidence | 2 decision-table traces | Two escalating gates plus test evidence outclass detached problems | Python Tutorial `if`; Python Tutor. |
| 5–6 loops | Variable-event loop, then baby-project checkpoint | Trace termination/off-by-one | 0; checkpoint run transcript | 2 short loop traces | Gate requires nontrivial repetition; Wk6 is intentionally not overloaded | Python tutorial loop pages; Python Tutor. |
| 7 functions | Refactor plus passing unit test | Parameters/returns/scope | 0; the required test is the focused feedback | One additional test case | Gate and test make transfer visible without a second set | Python tutorial + local `unittest`. |
| 8–9 strings | Text gate then real project checkpoint | Index/slice/method selection | 0 | 1 text-cleaning trace | Direct application plus checkpoint gives feedback | Python tutorial + Python Tutor. |
| 10 lists | Growing-list gate plus pair programming | Mutation/traversal/empty collection | 0; require one empty/small case in gate evidence | 1 list trace | `append` plus traversal is already explicit and observable | Python tutorial lists + local test. |
| 11 dictionaries | Lookup gate + defended structure choice | Missing key/duplicate-key behavior | 0; require one edge case in evidence | 1 dict trace | Gate combines code, testable lookup, and judgment | Python tutorial dictionaries + local test. |
| 12–13 classes | Class refactor then interacting objects, with pair work | Constructor/state/method interaction | 0; require a constructor/method smoke run | 1 object-state trace | Two sequential gates deliberately supply repetition and feedback | Python tutorial classes + local smoke test. |
| 14 | Checkpoint 3 + Full Trail Debrief | Revision/ownership/tool use | 0 | Optional GitHub Skills module | Checkpoint is the assessment; extra problems would displace reflection | GitHub docs/Skills + project. |
| 15–17 | Portfolio, final build/debrief | Consolidation and explanation | 0 | Optional text/dataset enrichment | Explicitly no new technical content; Farkle/ML would violate current load | Free references only, self-directed. |

## D — Student access/cost paths

| Lane | Student cost | Required accounts/tools | Reading/background source | Practice source | Graded-work equivalence | Student friction | Instructor friction | Risks |
|---|---:|---|---|---|---|---|---|---|
| Lean ZyBooks | Unknown—request current institutional price | ZyBooks + Python environment; GitHub if required | Narrow, instructor-selected ZyBooks sections | Selected zyLabs plus Odyssey | Strong convenience; Odyssey still supplies authentic grading | One paid login and platform navigation | Lowest formative-feedback setup | Paying for breadth not actually required; price not verified. |
| Zero-cost equivalent | $0 for materials | Browser + local Python; GitHub only if the course keeps GitHub requirement | Python docs + PY4E/Runestone-style beginner OER links | Odyssey gates/checkpoints, Python Tutor traces, instructor-owned local tests | Equivalent for stated course outcomes if gates/rubrics/feedback remain identical | Multiple links; docs tutorial is not novice-first | Must curate links, publish small tests, and provide feedback | Free web access does not grant copying/RAG; availability and accessibility need a pre-semester check. |
| Hybrid recommended for discussion | ZyBooks only for students/institution choosing it; free lane available | Same as above, ZyBooks optional/additive | Free canonical links; ZyBooks as structured optional support | Same graded Odyssey work for all; zyLabs optional/remedial | Best preserves equal outcomes and lets ZyBooks add convenience | Some choice/navigation | Must state one canonical graded lane and avoid two inequivalent standards | Licensing/account/accessibility review; avoid accidental pressure to buy. |

## Resource audit (current public research)

“Automation/RAG policy” is conservative: it describes a visible policy signal, not legal advice. `Unclear` means do not ingest/copy until a rights holder gives specific permission.

| Resource | Direct URL; accessed | Free access / open license | Account; linking/adapting/redistributing; exercise reuse | Automation/RAG | Accessibility/usability and currency |
|---|---|---|---|---|---|
| Python Tutorial and reference | https://docs.python.org/3/tutorial/ ; 2026-08-12 | Free; Python Software Foundation License; documentation examples additionally 0BSD | No account. Link freely; PSF license permits reproduce/derive/distribute with notice; code examples reusable under 0BSD. | Permitted for docs/examples subject to licenses; still keep attribution/notice | Official and current (3.14.7 page dated 2026-08-12); tutorial explicitly expects some programming background, so not sufficient as the sole novice text. |
| Python for Everybody (PY4E) | https://www.py4e.com/book.php ; https://www.py4e.com/lessons ; 2026-08-12 | Free web/book access; site identifies CC BY-NC-SA | No account apparent for book. Link/adapt under CC BY-NC-SA terms; noncommercial/share-alike constrain course redistribution; do not assume exercises can be relicensed. | Unclear—CC license governs copyright, not a RAG permission statement | Beginner-oriented, established university courseware; web delivery; verify current accessibility before adoption. |
| Runestone, *Foundations of Python Programming* | https://runestone.academy/ns/books/published/fopp/index.html ; 2026-08-12 | Free public text; license must be checked per book/version before copying | Public reading; account may be needed to save interactive progress. Link; do not adapt/redistribute exercises until the book-specific license is verified. | Unclear | Purpose-built interactive textbook; navigation was publicly reachable; test keyboard/screen-reader workflow. |
| Python Tutor | https://pythontutor.com/ ; 2026-08-12 | Free web visualizer; no open-license conclusion found | No account apparent for basic use. Link; do not copy/rehost interface or exercises absent explicit permission. | Unclear | Very good novice trace visualization; browser/service dependency and accessibility need review. |
| GitHub Skills/docs | https://skills.github.com/ ; https://docs.github.com/ ; 2026-08-12 | Free access; GitHub account required for interactive repository work | Link freely; licensing/reuse and automation policy must be confirmed from the specific repo/docs terms before copying | Unclear | Relevant to existing GitHub outcome; account creation and institutional policy are friction. |

## E — Decisions for Jeremy

| Decision | Why it matters | Evidence for option A | Evidence for option B | Recommendation, if any | Can work continue without decision? |
|---|---|---|---|---|---|
| Is ZyBooks required, optional, or replaced? | Cost and equitable access | Required: integrated commercial labs and one guided surface | Free/hybrid: all actual outcomes are assessed in instructor-owned Odyssey gates; free primary/OER sources cover spine | Hybrid is the strongest discussion starting point; verify price and accessibility first | Yes; derive materials against a free canonical spine, without changing publication. |
| What is the minimum technical core before CS2? | Stops 120 KEEP entries becoming an unexamined quota | Broad core: current CSV’s Chapters 1–9/11 | Narrow core: gates require I/O, variables/types, branch/loops, functions/tests, strings, list/dict, simple classes/modules | Use the narrow gate-aligned core; label advanced subtopics support/reference | Yes; table B is enough to author a later decision prompt. |
| Are any standalone chapter problems graded? | Avoids duplicated workload | Add problems for standardized micro-feedback | A1 explicitly says Odyssey fulfills weekly coding practice; gates have concrete criteria and checkpoints | Default to zero required standalone problems; add only a named micro-check where evidence shows a feedback gap | Yes. |
| Resolve Week 3 chapter citation | Avoids a student-facing factual error | Preserve existing phrase | Current adoption: Ch. 3 Types, Ch. 4 Branching; prior Report 008 already flags it | Correct the citation in a narrow later metadata pass | Yes. |
| Farkle/Q-learning/ML status | Prevents old experiments from silently becoming curriculum | Retain as required: historical Spring 2026 experiment | Current plan explicitly reserves Wk15/16 for consolidation; history labels Farkle/Q-learning promising extensions, not backbone; AI V is separate ML course | Keep Farkle/Q-learning and ML out of required CS1; at most optional, ungraded enrichment after scope/rights review | Yes; no implementation should proceed without an explicit future decision. |
| Which free practice service, if any, becomes canonical? | Determines account/accessibility/support burden | Python Tutor: low-friction visual tracing | Runestone: richer interactive experience, possibly account/progress dependency | Start with no external graded service: local instructor tests + optional Python Tutor; pilot accessibility before committing | Yes. |

## Evidence trail, limitations, and next step

Reviewed: `planning/block-map.md`, `planning/coding-odyssey-arc-map.md`, every `planning/week-*.md`, A1/A2, every `assignments/odyssey_gates/` file, lessons/course sequence maps, `planning/zybooks-section-decisions.csv`, `planning/fall-2026-course-design.md`, Reports 002/007/008/009, historical synthesis, and durable CS1 capture metadata. No Canvas, Savnac, ZyBooks, student data, grading dates, or licensed body text were written or copied.

Limitations: no current ZyBooks price was available in the reviewed evidence; no accessibility audit or student pilot was run; terms and automation/RAG rules that were not explicit were marked `unclear`, not inferred. This report intentionally does not select a final lane or rewrite the semester.

**Recommended next prompt:** a discussion-driven decision prompt that selects the access lane and confirms the narrow CS2-prerequisite spine, followed only then by a small implementation prompt for links/metadata and the Week-3 citation correction.
