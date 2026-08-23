# Prompt 108B — CS1 Local AI website adversarial review

## Verdict

`PASS`

Reviewed the exact pushed website head
`11dcbe10f941544cfdaae5913ba17e1a8046e563` on
`swosu-computing:campaign/week2-local-ai-launch`.

## Findings

No material website defect was found.

- Route clarity: PASS. `/local-ai-lab/` visibly separates “CS1: Build Your
  Own Local AI Lab” from “CS2 + DSCT: Managed Classroom Lab.” The existing
  managed classroom content and CS2/DSCT links remain reachable. `/cs1/`
  links the staged Week 2 route.
- Release path: PASS. The CS1 page has no clickable ZIP/download URL. The
  maintainer-only marker `FINAL DOWNLOAD INSERTED AFTER OWNER WINDOWS DRY RUN`
  is an HTML comment, not student-facing release content.
- Canonical sequence: PASS. The CS1 page names exactly `00 START HERE` through
  `09 AIDER TOY EXERCISES` in order and uses the exact approved model
  `qwen3:8b`. It does not duplicate the package's long command manual.
- Safety/recovery: PASS. The page keeps the setup loopback-only, rejects cloud
  credentials/network exposure, frames `NOT READY` as useful evidence, directs
  students to Canvas/help, and keeps SSH/remotes/push/pull outside Week 2.
- Existing-site regression: PASS. Root, Bootstrap, CS1, CS2, DSCT, Local AI
  hub, and staged CS1 routes exist; the served-route smoke test returned HTTP
  200 for all six relevant paths. Existing managed-lab language and Canvas
  routes remain in the hub.
- Publication hygiene: PASS. No credential, private host, Savnac link, fake
  ZIP, Windows-acceptance claim, TinyURL change, or final-release claim was
  introduced. The existing managed page's loopback reference is unchanged and
  describes a local service, not a public destination.

## Validation

- Relative-link audit: PASS.
- Canonical sequence and route assertions: PASS.
- Temporary local HTTP smoke test for `/`, `/cs1/`, `/local-ai-lab/`,
  `/local-ai-lab/cs1/`, `/cs2/`, and `/dsct/`: HTTP 200 PASS.
- Changed-file safety scan and `git diff --check`: PASS, with the pre-existing
  managed-page loopback prose distinguished from newly introduced content.

## Remaining boundary

The branch remains staged only. Do not merge or publish it, create the final
ZIP, alter TinyURL, or restore/use production Canvas credentials before the
owner Windows dry run and exact release-artifact test.
