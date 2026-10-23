# Obsidian views: what, why, and how it got here

Dated design history for the generated-views work in this repo. Course
files stay the source of truth; this is a record of the view-layer
decisions, not curriculum content.

## 2026-10-23 — `views/semester-topic-map.canvas` (commit `ea2699e`)

Built as Phase 1 of a "Wilbur + Repository Views + Memory v0" experiment:
a reproducible Obsidian Canvas over real CS1 files (unit map, weekly
plans, lessons, odyssey gates), answering *why* concepts are sequenced the
way they are, not just where files live. Generator:
`scripts/views/generate_semester_topic_map.py`.

**Design decisions:**
- **`views/`, not `.views/`.** Obsidian hides dot-prefixed folders from
  its file explorer and file index by default — confirmed via the
  Obsidian forum and the existence of several "reveal hidden files"
  community plugins that exist specifically to work around this; no
  built-in setting fixes it. A file in `.views/` would generate correctly
  but never appear in Obsidian's UI or quick switcher. Jeremy's call:
  visible folder over installing a plugin.
- **Groups = Coding Odyssey arcs, left to right by week.** Matches
  `planning/coding-odyssey-arc-map.md`'s own arc structure rather than
  inventing a new grouping.
- **One real finding baked into the map**, not just decoration: Arc 3's
  gate map says a noun already tracked in the Week 10-11 collection
  becomes a Week 12-13 class — meaning this semester deliberately
  reverses the historical zyBooks order (`docs/curriculum/course-
  sequence.md` says classes historically came before collections). The
  "KEY SEQUENCING DECISION" edge in the canvas states this directly.
- **A flagged documentation drift**, also real, not staged: `planning/
  week-09.md` (2026-10-08) says it supersedes the Week 9 framing in
  `planning/coding-odyssey-arc-map.md` and `planning/block-map.md`
  (both 2026-08-12), and says the remap for Week 10+ "is a separate
  mission" — which hadn't happened as of this commit. The canvas has a
  dedicated note calling this out.

## 2026-10-23 — `scripts/views/validate_canvas_layout.py` (same session)

Built after a first version of the canvas was generated but never
visually checked in Obsidian — a real gap, since structural JSON
validation (do the file paths exist, do edges reference real nodes)
doesn't catch a layout that's technically valid but visually unreadable.

Pure stdlib, no new dependency (this repo deliberately has no dependency
manifest yet — see `README.md`'s "Status"). Checks two things a human
would notice immediately but JSON validation can't:
1. An edge's line crossing through an unrelated node's box (excluding
   group nodes, which are translucent background regions in Obsidian —
   an edge passing over one is normal).
2. A text/file node whose content is too long for its declared height
   (would need internal scrolling to read in Obsidian).

Also renders a plain-text SVG (`views/*.svg`, gitignored — regenerate,
don't commit) for an actual visual look, since the geometry check is this
script's approximation of what Obsidian renders, not ground truth from
Obsidian itself.

**First real run found 39 problems** in the canvas that had just been
generated and called done. Root cause of most of them: two lesson nodes
(`lessons/04-loops.md` and `lessons/06-strings.md`) physically overlapped
each other's boxes, and one cross-canvas edge (the drift note back to the
arc-map) ran diagonally through nearly the entire top half of the canvas.
Fixed by: separating the overlapping nodes, repositioning the "first
custom class" lesson node to sit directly above its target instead of
routing a long diagonal across an unrelated row, relocating the drift
note out of the main vertical flow, staggering a same-row triplet so a
skip-edge didn't run straight through the middle node, and dropping one
secondary edge (`lessons/08` → `lessons/10-farkle-ml.md`) whose
information was already carried by an adjacent edge. Iterated against the
validator script rather than hand-deriving final coordinates — four
rounds (39 → 7 → 4 → 0 problems).

**Known limitation:** this machine has no browser automation connected
this session, so the SVG render was never actually screenshotted and
looked at — only the geometry check passed. Treat "0 problems" as "the
approximation found nothing," not as "a human confirmed it looks right."
Actually open `views/semester-topic-map.canvas` in Obsidian before
trusting it fully for a live audience.

## Two Obsidian entry points exist in this repo — not yet reconciled

A second, independently-built tool, `make_obsidian_map.py` (commits
`7b33b6f`, `f0ceff6`, same day), generates a different kind of view: a
whole-repo hub-and-spoke navigation map (`_repo_map/`, gitignored,
rebuilt per run), covering every folder generically. It answers "where
does everything live," not "why this sequence" — genuinely different
purpose from `views/semester-topic-map.canvas`, not a duplicate, but
there are now two separate "open this in Obsidian" starting points in one
repo and no single doc says which to reach for when. Worth a reconciling
pass (even just a top-level pointer doc) before this grows a third.
