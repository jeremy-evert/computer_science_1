# Raw Owner Decision — CS1 Week 2 Local AI Launch

Date: 2026-08-22
Status: **OWNER DECISION / CAMPAIGN INPUT**

This file records the curriculum decision that controls the next CS1 Week 2 preparation work. It is durable context, not by itself an executable prompt.

## Decision

Use **Option A**.

The Local AI Lab becomes the spine of CS1 Week 2. The existing Week 2 material is not discarded. Python fundamentals, Learning Science, Professional Minds, and the Coding Odyssey are woven through the Local AI Lab journey so students experience one coherent week rather than two parallel piles of work.

The accepted Local AI package source is the current `jeremy-evert/local_ai_lab_setup` main branch after Piper Mission 004. Its Mission 004 AAR says the source package is ready for the owner Windows dry run and that no further package implementation mission is justified before that empirical test.

## Week 2 teaching story

### Monday — Get the motorcycle running

Student path:

`00 START HERE -> 01 INVENTORY -> 02 READINESS -> 03 OLLAMA -> 04 qwen3:8b -> 05 HELLO OLLAMA`

Teaching goals:

- identify what is already on the machine;
- distinguish FOUND/MISSING from PASS/FAIL;
- run and read small Python code;
- connect `print`, `input`, variables, expressions, and types to real machine context;
- understand that Ollama is a local service and `qwen3:8b` is the approved local model;
- preserve the AI I Lens 2 idea: **Gather Context**.

A machine problem is evidence, not a student failure. A student who reaches a legitimate `NOT READY` condition should preserve the first diagnostic/recovery evidence and can still complete the day's exit ticket.

### Wednesday — Let Aider touch one tiny thing

Student path:

`06 GET/VERIFY AIDER -> 07 PREPARE TINY GIT WORKTREE -> 08 HELLO AIDER -> Toy 1 -> Toy 2`

Teaching goals:

- understand Aider as a program that works on files on disk while using the local Ollama model;
- see `git status` before and after a change;
- make one visible bounded edit;
- repair one tiny failing function/test;
- independently test instead of trusting generated prose;
- connect the experience to *Make It Stick*: prediction, retrieval, generation, feedback, and correction matter more than passive rereading.

Week 2 exposes Git only as visible state. Do not teach add/commit/remotes/SSH/push/pull yet.

### Friday — Use it, verify it, wake your world

Student path:

`Toy 3 -> Coding Odyssey founding charter -> Week 2 Odyssey gate -> verify -> reflect`

Teaching goals:

- make a small student-directed change with Aider;
- explain what changed and why;
- run the code/test and inspect evidence;
- choose one Coding Odyssey genre and write the founding charter;
- implement the existing Week 2 gate with variables plus an arithmetic/comparison expression and a sentence-level printed result;
- connect the experience to *Mindset*: errors and failed tests are useful information when students inspect and respond to them.

Aider may help with a bounded change, but it should not replace the student's genre choice, founding condition, or explanation of the evidence.

## Existing Week 2 objectives that must survive

Preserve these current course commitments while making the Local AI Lab the spine:

- run/read/change Python;
- `print` and `input`;
- variables, expressions, and types;
- Monday Moment / AI I Lens 2: Gather Context;
- Wednesday Professional Minds: *Make It Stick*;
- Friday Professional Minds: *Mindset*;
- Coding Odyssey genre choice;
- one-paragraph founding charter;
- Week 2 Odyssey Quick Check / gate;
- existing standing weekly assignments unless a current source contradiction proves one should move.

Do not create a second unrelated programming problem set merely because the Local AI Lab is being added.

## Week 2 exit tickets

Add three short student-facing exit tickets. Prefer 0-point `online_text_entry` assignments or the repository's equivalent non-denominator mechanism so these checkpoints improve visibility without changing the grading contract.

### Monday Exit Ticket — Is my local AI machine alive?

Student submits:

1. What did the inventory report as FOUND and what, if anything, was MISSING?
2. What was the farthest successful step today: readiness, Ollama, model, or direct Ollama hello?
3. Paste either the successful evidence or the first legitimate diagnostic/recovery result.
4. In one sentence: what does that evidence prove, and what does it **not** prove?

A legitimate `NOT READY` result with preserved evidence counts as a valid completion.

### Wednesday Exit Ticket — What did Aider actually change?

Student submits:

1. One short `git status` observation from before the edit.
2. One short `git status` or diff observation from after the edit.
3. What single change did Aider make?
4. What independent command/test did you run, and what result did it produce?

### Friday Exit Ticket — What did I trust, and what did I verify?

Student submits:

1. Which Coding Odyssey genre did you choose and what is the founding condition of your world?
2. What small change did you ask Aider to help with, if any?
3. What evidence convinced you the code worked or showed you it still needed repair?
4. Name one thing you personally verified instead of accepting the AI's answer on faith.

## Student-facing Week 2 module shape

The implementation may adapt exact Canvas ordering to existing Course Foundry conventions, but a student should perceive this order:

1. Week 2 mission / Start Here.
2. Monday Local AI steps 00-05 plus the existing Monday Python/Lens material.
3. Monday Exit Ticket.
4. Wednesday Aider steps 06-08 plus Toys 1-2 and *Make It Stick*.
5. Wednesday Exit Ticket.
6. Friday Toy 3 plus *Mindset*.
7. Coding Odyssey genre/founding charter and Week 2 gate.
8. Friday Exit Ticket.
9. Existing weekly reflection/report items that remain part of the grading model.

Do not delete useful existing Week 2 items just to make the module shorter. Reconcile and sequence them.

## Public student route

Intended future public route:

`https://jeremy-evert.github.io/swosu-computing/local-ai-lab/cs1/`

The existing `/local-ai-lab/` route currently serves the managed CS2/DSCT lab. The future website should preserve that path for those courses while adding a clear CS1 path for students building/verifying their own local lab.

The website may be staged before the Windows dry run, but **must not be merged/published as the final CS1 launch path until the owner dry run accepts the source package and the exact release artifact exists.**

## Release boundary

The remaining empirical gate is the owner Windows dry run.

Before that gate passes:

- do not create the final student ZIP;
- do not claim Windows acceptance;
- do not publish a final download link;
- do not mutate production Canvas;
- do not restore or use production Canvas credentials;
- do not merge a public website change that implies the package is released.

After the dry run:

1. repair only observed reality defects if any;
2. create the exact student ZIP;
3. test that exact ZIP on the intended Windows path;
4. publish the approved download/public route;
5. reconcile CS1 Canvas from the accepted source when production Canvas credentials are deliberately restored/authorized;
6. separately close the known A10 live assignment-group repair.

## Week 3 boundary

Do not import the Week 3 Work First / Sidecar / motorcycle-vs-garage curriculum into Week 2.

Week 2 makes students comfortable using the motorcycle.

Week 3 teaches them how to build and organize the garage.

## Campaign success

Before the owner dry run, the overnight/source campaign succeeds when:

- CS1 Week 2 source tells one coherent Local-AI-first story;
- the three exit tickets exist in source and do not alter the grading denominator;
- Python fundamentals and the Coding Odyssey survive and are visibly integrated;
- online and face-to-face students can follow the same core path;
- Course Foundry/source compilation tests are green or any genuine seam is precisely reported;
- the public CS1 Local AI route is fully staged on a non-production branch;
- no live Canvas or final-release boundary is crossed;
- a final launch-readiness manifest names the exact branches/commits and the few remaining owner gates.