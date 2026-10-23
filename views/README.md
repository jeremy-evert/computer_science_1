# Opening the CS1 semester map in Obsidian (show-and-tell quickstart)

## One-time setup

1. Open Obsidian.
2. **Open folder as vault** → pick this repo's root folder
   (`computer_science_1`, the one with `README.md`, `lessons/`, `planning/`
   in it — not this `views/` folder itself).
3. In the left file explorer, open `views/` → `semester-topic-map.canvas`.

That's it — no plugins needed. (Earlier drafts of this put generated views
in a dot-prefixed `.views/` folder; Obsidian hides dot-prefixed folders
from its file explorer by default with no built-in setting to reveal
them, so it's a plain `views/` folder instead, specifically so this step
just works.)

## What you're looking at

- **Four colored groups**, left to right = the five Coding Odyssey arcs in
  calendar order: Foundations (Wk 1-6) → First Real Choices (Wk 7-9) →
  **Systems That Remember Themselves (Wk 10-14, highlighted — this week)**
  → Thanksgiving/Farkle/Finals (Wk 15-17).
- **Nodes are real repo files** — click one to open the actual lesson or
  weekly plan behind it. Nothing on this canvas is invented; every node is
  a file that exists in this repo right now.
- **Edges carry the "why,"** not just "these are near each other." Each
  arrow's label says what concept the next step actually depends on — e.g.
  why collections (Wk 10-11) come before classes (Wk 12-13) this semester,
  reversed from the old zyBooks chapter order.
- **One red/highlighted text node** calls out a real, still-open
  documentation inconsistency (Week 9's plan vs. the older arc-map/
  block-map) — worth pointing at live as an example of the map catching a
  real gap, not just looking pretty.

## For show-and-tell today

Good talking points, in order:
1. Zoom out — show the whole semester at a glance, four arcs.
2. Click into the Week 10 group (highlighted) — this week's actual files.
3. Follow one edge's label out loud — e.g. "strings → objects → a
   *collection* of objects → your own *class*" — to show the map answers
   "why this order," not just "where's this file."
4. Point at the flagged documentation-drift node as a real, found issue,
   not a staged one.
5. If you're also demoing Wilbur: this canvas has a plain-text twin
   (`character_garden/context_packs/cs1-week10-canvas-summary.md`) that
   gets pasted into his terminal, since he can't open files or see the
   canvas directly. Same graph, two forms — one for a person looking at a
   screen, one for a model reading text.

## Regenerating after course changes

This file (the `.canvas`) is generated, not hand-edited. If `planning/`,
`lessons/`, or `docs/curriculum/` change, regenerate it:

```sh
python3 scripts/views/generate_semester_topic_map.py
```

Course files stay the source of truth; this view is disposable and
reproducible from them.
