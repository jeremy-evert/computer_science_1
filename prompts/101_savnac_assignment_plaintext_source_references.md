# Prompt 101 — Savnac CS1 adjustment: plaintext source references that should be live student links

## Status
Captured during Jeremy's CS1 Savnac dogfood pass on 2026-08-14.

**Executed 2026-08-14.** Assignment 151's citations were literal source-path prose. Fixed 3 of 5: the lesson page (already live, just unlinked) and both Judgment Toolkit section citations (the reference doc itself had never been pushed to Canvas at all — new dedicated Page builder added). The remaining 2 are correctly *not* fabricated: `assignments/A2-coding-odyssey-project.md` (the "World Bible" project) has the identical "never given a dedicated builder" problem but needs a real grading-mechanics decision — filed as `jeremy_task_tracking/questions/003_cs1_a2_reasoning_odyssey_project_never_built.md` — and `planning/coding-odyssey-arc-map.md` is genuinely instructor-only (confirmed by reading it), correctly left unlinked. Verified live (4 real links on assignment 151, idempotent rerun). Read-only inventory for Prompt 102: ~89 similar citations across 24 CS1 files. Full report: `course_foundry/reports/2026-08-14_prompt101_plaintext_source_references.md`.

## Live observation
Jeremy inspected:

`http://localhost:3002/courses/1/assignments/151`

The assignment contains prose that looks like it is trying to point students to real supporting course resources, but the references are rendered as plain text rather than clickable student-facing links.

Examples observed on the live page include:

- `docs/curriculum/judgment_toolkit.md` §2
- `assignments/A2-coding-odyssey-project.md`
- `docs/curriculum/judgment_toolkit.md` §5

and again in the founding-charter paragraph:

- `assignments/A2-coding-odyssey-project.md`
- `docs/curriculum/judgment_toolkit.md` §5

The problem is not that the source path is technically false. The problem is that a repository path survived into student-facing prose without being resolved into the canonical live Canvas/Savnac object students can actually open.

This is a strong canary for a broader class of source-to-LMS rendering defects.

## Desired experience
If student-facing prose names a course resource in a way that clearly functions as a reference, students should receive a usable link to the canonical live object when one exists.

For example, prose should read conceptually like:

- `Judgment Toolkit — §2: Light Build`
- `Reasoning Odyssey project / World Bible instructions`
- `Judgment Toolkit — §5: Judgment Log`

with each label linked to the real Canvas/Savnac page, assignment, file, or other canonical destination.

The repository path may remain available in instructor/source metadata, comments, receipts, or tooling, but should not be the only navigational affordance shown to students.

## Investigation first
Before changing assignment 151:

1. Read the authoritative source that produces assignment 151.
2. Identify exactly how these references entered the rendered assignment body.
3. Determine whether they are:
   - literal source-path prose authored in the assignment,
   - Markdown links whose destinations were lost during rendering,
   - link tokens/placeholders that were never resolved,
   - references produced by a formatter/generator,
   - or another source-owned mechanism.
4. Resolve the intended live destinations from source truth / Harbor / Canvas API rather than guessing URLs.
5. Check whether the referenced resources already have canonical Canvas/Savnac objects. If an intended destination does not exist, report that honestly rather than fabricating a link.

## Bounded repair
Use assignment 151 as the first canary.

Repair the owning source/rendering path so the observed source-like references become real student-facing links to canonical live objects.

Prefer a reusable link-resolution mechanism over hand-writing absolute Canvas URLs into assignment prose.

If the existing Course Foundry / Imprint token or link-resolution machinery already solves this class of problem, reuse/generalize it rather than inventing another syntax.

Do not perform a blind repository-wide search-and-replace in this prompt. Prompt 102 owns the broader quality-control sweep.

## Link-quality contract
For each repaired reference:

- the visible label should make sense to a student without exposing implementation details;
- the target must be a real live object verified through the Canvas/Savnac API or existing resolver;
- the link should remain stable across Savnac regeneration/reconciliation;
- reruns must be idempotent;
- no guessed numeric object IDs or hard-coded ephemeral signed URLs;
- source paths should not leak into student-facing prose unless there is an intentional pedagogical reason to show them.

## Reasoning Odyssey naming
`Coding Odyssey` is retired as the active student-facing name. If the underlying source still says `A2-coding-odyssey-project.md`, preserve the historical/source filename internally but use **Reasoning Odyssey** in current student-facing link labels unless the authoritative course content deliberately requires otherwise.

## Acceptance criteria
Independent Savnac readback of assignment 151 must show:

- the observed `assignments/...` and `docs/...` references are no longer dead-looking/plain-text navigation cues when a canonical live destination exists;
- each rendered link opens the intended live student resource;
- section-specific references such as Judgment Toolkit §2 and §5 land as close to the intended content as the existing Canvas object model reasonably supports;
- no raw unresolved token/placeholder is visible;
- no stale repository path is presented as though students can click it;
- source reruns produce zero duplicate links and zero content thrash;
- tests/readback appropriate to the owning pipeline pass.

## Follow-on
After the canary is repaired, do a read-only inventory of other obvious source-path references in current CS1 student-facing content and hand those findings to Prompt 102. Do not repair the entire corpus in this prompt.

## Scope guardrails
Savnac CS1 course 1 canary first. No production Canvas writes. No broad content rewrite. Fix navigation semantics at the owning source/rendering layer.

## Architectural north star
**Repository paths are useful to builders. Students need navigable course objects. The publishing pipeline should translate between those worlds instead of leaking one into the other.**
