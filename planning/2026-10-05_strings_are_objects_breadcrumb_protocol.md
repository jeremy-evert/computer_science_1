# Strings Are Objects — Codex Breadcrumb Protocol

**Course:** COMSC-1033 Computer Science I  
**Created:** 2026-10-05  
**Purpose:** Make every Codex phase recoverable from GitHub without relying on chat history.

## Rule

Every Codex phase must leave a small, phase-specific status file in the repository.

Use:

`planning/2026-10-05_strings_are_objects_phase_0N_status.md`

Examples:

- Phase 1: `planning/2026-10-05_strings_are_objects_phase_01_status.md`
- Phase 2: `planning/2026-10-05_strings_are_objects_phase_02_status.md`
- Phase 3: `planning/2026-10-05_strings_are_objects_phase_03_status.md`

Each phase gets its own file so parallel or sequential Codex branches do not fight over one shared progress log.

## When to write it

Create the phase status file near the beginning of the session and update it before the final commit.

If the phase becomes blocked, update the status file **before stopping** if possible.

The status file is part of the phase deliverable and should be committed with the phase work.

## Required contents

```markdown
# Strings Are Objects — Phase N Status

**Phase:** N — short name
**Branch:** branch-name
**Status:** IN_PROGRESS | COMPLETE | BLOCKED
**Started from:** branch or commit
**Last updated:** YYYY-MM-DD

## Goal

One or two sentences describing exactly what this phase is supposed to produce.

## Files changed

- path
- path

## Commands / validation

- command
- result

## Decisions made

- brief decision and why

## Breadcrumbs for the next phase

- what the next session should know
- important paths
- assumptions worth preserving

## Blockers

- `NONE`

or, if blocked:

- exact command that failed
- exact error or concise excerpt
- what was tried
- what remains unresolved
- safest next action
```

## Status meanings

### IN_PROGRESS

The phase has begun but has not passed acceptance checks.

### COMPLETE

The phase's acceptance checks passed. Include validation evidence and the commit-ready result.

### BLOCKED

The phase cannot safely continue without a decision, missing dependency, failing toolchain, repository conflict, or other unresolved issue.

A BLOCKED phase should not improvise around the problem. Record the evidence and stop.

## Commit convention

Prefer a phase commit message that makes the breadcrumb obvious, for example:

```
Phase 1: add strings Mad Lib demo
Phase 2: add string laboratory
Phase 3: expand canonical strings lesson
```

The status file should normally be included in the same commit.

## Handoff rule

The next Codex session should read, in this order:

1. `AGENTS.md`
2. `NAMING.md`
3. `planning/2026-10-05_strings_are_objects_lesson_map.md`
4. `planning/2026-10-05_strings_are_objects_codex_execution_plan.md`
5. `planning/2026-10-05_strings_are_objects_breadcrumb_protocol.md`
6. all completed prior phase status files
7. the artifacts produced by prior phases that matter to the new phase

The repository is the durable memory.

If a previous phase status says **BLOCKED**, do not silently continue past it. Resolve or explicitly supersede the blocker first.
