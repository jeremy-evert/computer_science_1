# Sidecar Prompt 107A — Integrate the Local AI Lab into CS1 Week 2

**Status:** READY  
**Owner decision:** `sidecar/raw/2026-08-22_week2_local_ai_launch_owner_decision.md`  
**Mode:** source-only campaign implementation, no production Canvas

## Mission

Make the Local AI Lab the **spine** of CS1 Week 2 while preserving the current Python fundamentals, Learning Science / Professional Minds material, and Coding Odyssey gate.

The outcome should feel like one week with one story, not an old Week 2 plus an unrelated AI setup pile.

Work on the campaign branch:

`campaign/week2-local-ai-launch`

Create it from current `computer_science_1/main` if it does not already exist. If it already exists, inspect its history/state and resume only if the campaign state is unambiguous and clean.

Do **not** merge the campaign branch to `main` in this prompt.

## Read first

Read current truth, not cached assumptions:

1. `sidecar/raw/2026-08-22_week2_local_ai_launch_owner_decision.md`
2. `planning/week-02.md`
3. `assignments/odyssey_gates/week-02.md`
4. the current Week 2 assignment/rubric sources and module-building conventions
5. `NAMING.md`, `README.md`, and any directly relevant local course instructions
6. current Course Foundry CS1 desired-state/content-map/deployment code only as needed to understand how Week 2 source becomes Canvas objects
7. read-only `jeremy-evert/local_ai_lab_setup` current main, especially:
   - `reports/piper/2026-08-22_mission_004_after_action_report.md`
   - `packages/cs1_online/00_START_HERE.md` through `09_AIDER_TOY_EXERCISES.md`
   - the package scripts/examples needed to keep course instructions truthful

The accepted package source is the Local AI Lab source tree. Do not fork/rewrite its install instructions inside CS1 unless the course needs a short explanatory summary or link target.

## Required Week 2 teaching arc

Implement the owner decision:

### Monday — Get the motorcycle running

Core Local AI path:

`00 -> 01 -> 02 -> 03 -> 04 -> 05`

Integrate rather than remove:

- run/read/change Python;
- `print` / `input`;
- variables, expressions, and types;
- Monday Moment / AI I Lens 2: Gather Context.

### Wednesday — Let Aider touch one tiny thing

Core Local AI path:

`06 -> 07 -> 08 -> Toy 1 -> Toy 2`

Integrate:

- `git status` before/after;
- one visible edit;
- one tiny failing-function/test repair;
- independent verification;
- Professional Minds: *Make It Stick*.

### Friday — Use it, verify it, wake your world

Core Local AI path:

`Toy 3 -> Coding Odyssey founding charter -> Week 2 gate -> verify -> reflect`

Integrate:

- Professional Minds: *Mindset*;
- current Coding Odyssey genre menu;
- founding charter;
- variables + arithmetic/comparison expression + sentence-level printed result;
- World Bible/Judgment Log note if current course source still requires it.

Aider may assist one bounded change. It must not replace the student's genre choice, founding condition, or evidence explanation.

## Three required exit tickets

Create three short Week 2 exit-ticket source objects following current repository/Course Foundry conventions.

Prefer `online_text_entry`, 0 points, and a placement/mechanism that **cannot enlarge a weighted grading denominator**. If the current compiler has a clearer semantic mechanism for ungraded/0-weight checkpoints, use that instead, but prove the gradebook consequence.

### Monday Exit Ticket — Is my local AI machine alive?

Ask exactly for the substance below, with student-friendly wording:

1. FOUND vs MISSING inventory result.
2. Farthest successful step: readiness, Ollama, model, or direct Ollama hello.
3. Successful evidence **or** first legitimate diagnostic/recovery evidence.
4. One sentence: what does this evidence prove, and what does it not prove?

A legitimate `NOT READY` result with preserved evidence is a valid completion.

### Wednesday Exit Ticket — What did Aider actually change?

Ask for:

1. a short `git status` observation before;
2. a short `git status` or diff observation after;
3. the single change Aider made;
4. the independent command/test and result.

### Friday Exit Ticket — What did I trust, and what did I verify?

Ask for:

1. Coding Odyssey genre + founding condition;
2. bounded Aider help used, if any;
3. evidence that showed working/not-yet-working state;
4. one thing personally verified instead of trusting the AI answer.

## Module/source shape

A student should perceive this order:

1. Week 2 mission / Start Here.
2. Monday Local AI steps 00-05 with the existing Monday Python/Lens material.
3. Monday Exit Ticket.
4. Wednesday Local AI steps 06-08 + Toys 1-2 + *Make It Stick*.
5. Wednesday Exit Ticket.
6. Friday Toy 3 + *Mindset*.
7. Coding Odyssey genre/founding charter + Week 2 gate.
8. Friday Exit Ticket.
9. Existing standing weekly report/reflection items that remain part of the grading model.

Use existing module/page/assignment conventions. Avoid introducing a new general-purpose compiler abstraction if existing patterns can express this cleanly.

## Preserve current grading and course contracts

Do not casually remove or repurpose existing graded assignments.

Before implementation, inventory the current Week 2 objects and their grading-group/point behavior. After implementation, prove:

- existing weighted group totals are unchanged;
- existing Week 2 graded items keep their points/groups unless this prompt explicitly requires otherwise;
- the new exit tickets do not change the denominator;
- no A10/kickoff repair is mixed into this mission;
- no Week 3 content is imported;
- online students do not require a human partner for the Local AI core path;
- face-to-face students can follow the same core path with live help available.

If current A3/A7/A4 or other standing weekly items naturally reinforce the new story, update explanatory wording only when it improves coherence without changing their established grading purpose.

## Link/source discipline

The intended future public CS1 Local AI route is:

`https://jeremy-evert.github.io/swosu-computing/local-ai-lab/cs1/`

Do not create a live/public dependency that does not yet exist. On the campaign branch, use the repository's established token/reference mechanism when possible so the final public URL can be resolved at release time.

Preserve any literal `lessons/...` citations required by Course Foundry scanners. Do not repeat the Prompt 105 failure mode where a prettier link accidentally removed a machine-readable source reference.

## Course Foundry boundary

Prefer a CS1-source-only change.

If a minimal Course Foundry change is genuinely required to represent the three exit tickets or their module placement:

- use a separate `campaign/cs1-week2-local-ai-launch` branch/worktree in `course_foundry`;
- make the smallest course-specific/backward-compatible change;
- preserve all other course behavior;
- add focused tests;
- do not merge that campaign branch to `main` in this prompt.

Do not redesign the general deployment framework.

## Validation

Run the strongest source/static tests available without production Canvas credentials, including as applicable:

- CS1 content-map / desired-course tests;
- module ordering/object tests;
- grading-group/points invariants;
- link-token/reference tests;
- relevant Course Foundry focused tests;
- `git diff --check` on changed repositories.

If Savnac or another synthetic Canvas path is already authorized and available without restoring production credentials, it may be used for bounded non-production verification. It is not required if source/desired-state tests prove the needed behavior.

Do not source, restore, request, print, or use production SWOSU Canvas credentials.

## Required report

Write on the CS1 campaign branch:

`sidecar/reports/107A_week2_local_ai_curriculum_integration.md`

Use one of exactly these verdicts:

- `INTEGRATED`
- `BLOCKED`

Report:

- branches and starting SHAs;
- exact Week 2 source files changed/created;
- exact three exit-ticket source paths and grading behavior;
- how Python fundamentals / Professional Minds / Coding Odyssey were preserved;
- module ordering result;
- tests run/results;
- Course Foundry changes if any;
- every unresolved seam;
- exact campaign branch heads pushed.

## Git / durability

For each writable repository used:

- protect pre-existing work;
- fetch before branching;
- use forward commits only;
- never force-push;
- stage only in-scope changes;
- commit/push verified work to the campaign branch;
- verify the remote branch/commit before claiming completion.

## Hard stops

Stop rather than infer permission if the work requires:

- production Canvas reads/writes or credential restoration;
- merging any campaign branch to accepted `main`;
- publishing the final CS1 website route;
- creating the final ZIP before the owner Windows dry run;
- altering the Local AI package architecture;
- importing Week 3 Work First/Sidecar curriculum;
- changing grading weights or standing grading policy;
- a new human pedagogy decision not resolved by the owner-decision file.

## Done when

The CS1 campaign branch expresses one coherent Local-AI-first Week 2, the three exit tickets exist without changing the grading denominator, existing Week 2 learning objectives survive, source/desired-state validation is complete, the work is pushed, and the 107A report is durable.