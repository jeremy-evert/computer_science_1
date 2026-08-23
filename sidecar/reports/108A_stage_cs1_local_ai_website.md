# Prompt 108A — Stage CS1 Local AI student website

## Verdict

`STAGED`

## Durable state

- Repository: `jeremy-evert/swosu-computing`
- Campaign branch: `campaign/week2-local-ai-launch`
- Base: `0c242e8aaa6a6c670a647091e420693e787bf7cc`
- Pushed head: `11dcbe10f941544cfdaae5913ba17e1a8046e563`
- Intended future URL: `https://jeremy-evert.github.io/swosu-computing/local-ai-lab/cs1/`

The campaign was built in an isolated worktree from accepted `origin/main`.
The pre-existing dirty `swosu-computing` main checkout was not changed.

## Pages changed

- `local-ai-lab/index.html` — adds a clear chooser distinguishing CS1's
  build-your-own path from the existing CS2/DSCT managed classroom path while
  retaining the managed content and routes.
- `local-ai-lab/cs1/index.html` — new CS1 Week 2 page with the exact accepted
  `00` through `09` sequence, evidence doctrine, local/safety boundary, and
  Canvas route.
- `cs1/index.html` — adds the Week 2 Local AI entry point.

The CS1 page does not duplicate the package's long command instructions. It
points students to the Canvas module for authoritative lessons, due dates,
exit tickets, and submissions. It names the approved `qwen3:8b` model and
keeps CS1's own-lab model separate from the managed CS2/DSCT model.

## Release boundary

The page contains no clickable ZIP/download URL. A maintainer-only HTML comment
marks the insertion point:

`FINAL DOWNLOAD INSERTED AFTER OWNER WINDOWS DRY RUN`

No Windows acceptance, checksum, release tag, or final artifact is claimed.

## Validation

- Relative-link audit for changed pages: PASS.
- Required route presence (`/`, `/cs1/`, `/local-ai-lab/`,
  `/local-ai-lab/cs1/`, `/cs2/`, `/dsct/`): PASS.
- Temporary local HTTP smoke test for all six routes: HTTP 200 PASS.
- Safety/publication scan for credentials, internal hosts, Savnac links,
  unsupported acceptance claims, and accidental release links: PASS.
- `git diff --check`: PASS.
- Existing managed CS2/DSCT page remains in `/local-ai-lab/` and its Canvas
  links and managed-lab safety language remain intact.

## Remaining gate

This is a non-production campaign branch. Do not merge or publish it until the
owner Windows dry run accepts the exact Local AI package, the exact student ZIP
is created and tested, and the final release link replaces the maintainer
marker. No production Canvas credential was restored or used.
