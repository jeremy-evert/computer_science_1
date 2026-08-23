# Prompt 107A — CS1 Week 2 Local AI curriculum integration

## Verdict

`INTEGRATED`

## Campaign state

- CS1 campaign: `campaign/week2-local-ai-launch`
- CS1 starting accepted base: `a80cfc1cbd4c2385d676a78234c7a74379e24a47`
- CS1 implementation commit: `c8e63b4f88dadda757b73cf042de57c0c6836744`
- Course Foundry campaign: `campaign/cs1-week2-local-ai-launch`
- Course Foundry starting accepted base: `969b50aa7f07dedb96049103f52b8bcc9fa0ac5c`
- Course Foundry compiler seam commit: `f292c18`
- Local AI package source: `5843352c97ca0e16cb237963687dc5d83003df6c`

Both campaign commits were present locally and were pushed/verified before this
round advanced. No production Canvas credential or live Canvas operation was
used.

## CS1 source changes

The Week 2 source now presents one Local-AI-first path:

- `lessons/week02-local-ai-00-start-here.md` through
  `lessons/week02-local-ai-09-aider-toy-exercises.md`
- `planning/week-02.md`
- `assignments/week02-local-ai-exit-ticket-monday.md`
- `assignments/week02-local-ai-exit-ticket-wednesday.md`
- `assignments/week02-local-ai-exit-ticket-friday.md`

Monday carries the inventory/readiness/Ollama/model/hello route while retaining
the Python run/read/change, `print`/`input`, variables, expressions, types, and
Gather Context material. Wednesday carries Aider, visible Git state, bounded
edits, independent checks, and *Make It Stick*. Friday carries Toy 3, *Mindset*,
the existing Coding Odyssey genre/founding-charter/Week 2 gate, and reflection.
Aider is explicitly bounded away from the student's genre choice, founding
condition, and evidence explanation.

## Exit tickets and grading behavior

The three source paths are:

1. `assignments/week02-local-ai-exit-ticket-monday.md`
2. `assignments/week02-local-ai-exit-ticket-wednesday.md`
3. `assignments/week02-local-ai-exit-ticket-friday.md`

Each is a short `online_text_entry` checkpoint with `0` points in the existing
Weekly Reinforcement Assignment group. The Course Foundry campaign change
preserves interleaved source order and encodes these assignments as ungraded
zero-point submissions; it does not alter standing assignment groups, weights,
or drop rules. Monday explicitly accepts a legitimate `NOT READY` diagnostic
as evidence.

## Course Foundry change

The smallest required compiler change was used on the separate campaign branch:
preserve textual source order when extracting interleaved CS1 lesson and
assignment references, and give the three named exit tickets their explicit
zero-point online-text-entry desired behavior. A focused regression test covers
both behaviors.

## Validation

- CS1 source-reference and exit-ticket static assertions: PASS.
- `python3 -m compileall` on the Course Foundry package/tests: PASS.
- `git diff --check` in both campaign repositories: PASS.
- The Course Foundry focused pytest suite could not run on this host because
  the checkout has no `.venv`, system Python lacks `pytest`, and importing the
  package also requires unavailable `pydantic`. This is recorded as a local
  validation seam for adversarial review; no dependency was installed and no
  production access was attempted.

## Unresolved seams

- The final public CS1 Local AI route is staged later in `swosu-computing`; it
  is not published by this round.
- The owner Windows dry run remains the empirical package/release gate.
- The known live A10 repair remains outside this chain.

## Durable heads

- CS1: `campaign/week2-local-ai-launch` at `c8e63b4f88dadda757b73cf042de57c0c6836744`
- Course Foundry: `campaign/cs1-week2-local-ai-launch` at `f292c18`
