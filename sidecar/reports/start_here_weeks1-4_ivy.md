# CS1 Start Here + week rail + Weeks 1–3 overview pages — Ivy evidence

Date: 2026-09-08
Role: Ivy / Foreman Intern, for Anna's bite
`jobs/anna/bites/cs1_start_here_weeks1-4.md` (5-class layout campaign,
second bite, Commons already deployed). No Canvas contact — page-body
generation only; Anna deploys from April with read-back verification.

## Pages built (all new — CS1 had no front page and no overview-page
pattern at all before this bite)

- `sidecar/canvas_pages/start-here-this-week.html` — the front page.
  Intended slug `start-here-this-week`, matching the CS2 reference
  implementation's own slug.
- `sidecar/canvas_pages/week-01-overview.html` — real content, Week 1's
  orientation arc.
- `sidecar/canvas_pages/week-02-overview.html` — real content, foundations
  + variables/expressions/types.
- `sidecar/canvas_pages/week-03-overview.html` — real content, branching.
- `sidecar/canvas_pages/week-04-overview.html` — **placeholder stub**, per
  Flo's mid-bite update (relayed by Anna): the rail's Week 4 chip should
  resolve to a real published page rather than render unlinked, but the
  page itself must not contain fabricated curriculum. It says exactly
  that in its own body (grep for "placeholder page" to confirm), states
  the one topic line the `week-04` gate assignment's own description
  gives, and points to the gate + rubric as "where the work actually is."
  I drafted this myself rather than asking Anna to — it's a small, low-risk
  addition and I was already deep in the same content; flagging per her
  offer to do it herself if that was simpler.

Intended slugs for the three real overview pages: `week-01-overview`,
`week-02-overview`, `week-03-overview` — my choice, no existing convention
to match since CS1 has never had one; consistent with the Week 4 stub's
`week-04-overview` so the whole rail uses one naming pattern.

## Source citations (topic language traceable to real files, not invented)

- **Week 1**: `planning/week-01.md` — the "no programming content of any
  kind," three-question orientation framing, and the Monday/Wednesday/
  Friday day topics are quoted/paraphrased directly from that file.
- **Week 2**: `planning/week-02.md` + `lessons/01-foundations-print-input.md`
  + `lessons/02-variables-expressions-types.md`. The "founding condition"
  framing (variable + expression + printed sentence) is quoted near-verbatim
  from `lessons/02`'s own "why this matters this week" section.
- **Week 3**: `planning/week-03.md` + `lessons/03-branching.md`. The
  "first real decision" / "letting the value of an expression choose which
  lines of code run" framing is quoted near-verbatim from `lessons/03`.
- **Week 4 stub**: the one topic sentence ("deepen last week's single `if`
  into a real decision with at least three distinct outcomes") is the
  exact phrase Anna's bite file already extracted from the live `week-04`
  assignment description — I did not fetch or paraphrase it myself, used
  it verbatim as given.

All four repo files were read fresh after fast-forwarding
`computer_science_1`'s local `main` to `origin/main` first (it was 20-ish
commits behind) — per this session's standing rule to never trust a stale
local checkout.

## Rail

`course_foundry.week_rail.render_week_rail(4, 74029, {1: "week-01-overview",
2: "week-02-overview", 3: "week-03-overview", 4: "week-04-overview"},
palette="plain")`. Weeks 5–17 have no slug — rendered as unlinked text per
the component's own design (never guess a URL); Anna's bite said she'll
check and stub those. Verified: no `<script>`/`<style>`/forbidden CSS
property in any of the five new page bodies (grepped each file
individually, zero matches for all six).

## Flagged for Anna before deploy

1. **Week 1's three orientation-day links** (`{{ANNA: confirm...}}`
   placeholder in `week-01-overview.html`) — I don't have live-verified
   Canvas slugs for the Monday/Wednesday/Friday orientation pages, only
   their topics from `planning/week-01.md`. Same for the getting-to-know-you
   quiz and the A01–A09 portfolio-baseline assignment set.
2. **Week 4 stub page** — drafted by me (see above); tell me if you'd
   rather replace it with your own version, same spirit as Commons' Week
   17 stub.
3. **Module reorganization** (yours, not mine, per the bite): move to an
   "Optional archive" sub-header — Week 2's Monday/Wed/Fri mini-activities
   and lecture slide files; Week 3's Aug 31 and Sept 2 lecture recording,
   notes, and digest pages. (Item list per your own bite's live-check
   findings, not independently re-verified by me.)
4. **Weeks 5–17 overview-page stubs** — not built here, per the bite
   ("I'll check + stub").

## Spend split

Anthropic only (Ivy's own reasoning) — no Codex dispatch this bite. Direct
authoring made sense here the same way it did for Commons' Part B: this is
new-content generation grounded in already-read source files, not a task
that benefits from a second agent's independent judgment, and keeping it
in one pass avoided a round-trip for what's fundamentally straightforward
page assembly once the source material was actually read. Durable-artifact
angle: this bite's real payoff is that it's the *second* course to reuse
`render_week_rail` unchanged — confirms the Part-A investment already paid
off exactly as intended.

IVY CS1 START HERE READY FOR ANNA
