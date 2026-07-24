# The judgment-building toolkit — Build / Decide-Compare / Debrief / Quick Check / Judgment Log

**Why this exists.** CS1's content spine pivoted 2026-07-24 ("The Coding
Odyssey" — one persistent per-student project, weekly gates, replacing the
standalone AI-practice-rubric plan; see `jeremy_task_tracking/DECISIONS.md`'s
2026-07-24 entry). Jeremy's framing for the pivot: students today are
"senior executives with decades of clout they can use to make ChatGPT,
Claude, Copilot, Gemini, Grok, and others do their bidding, but none of the
experience to know why it is not good just to throw around their weight."
These five instruments exist to build that judgment directly, not grade it
as a side rubric. None of them existed anywhere in this repo or
`course_foundry` before this pass (confirmed by grep before writing this).

**Grounding.** Drafted from a real query pass against `curriculum_rag_supporter`
(Wiggins & McTighe's *Understanding by Design*, 2005; *How Learning Works*,
2010) — not invented cold. Citations inline below. Also grounded in this
course's own recurring pattern, not a fresh invention:
`docs/philosophy/teaching-patterns.md`'s evidence-based read of the 2021-26
archive already shows formative, pass/fail-or-effort-based, demonstrative
grading as the stable norm here — these instruments formalize that existing
tone, they don't import a stricter one.

**Where each instrument sits, at a glance:**

| Instrument | Grain | Frequency | Ties to |
|---|---|---|---|
| Quick Check | one gate, one concept | ~weekly | the weekly technical topic |
| Build | one checkpoint or continuation | ~weekly (light) + 4 checkpoints (full) | `assignments/A2-coding-odyssey-project.md` |
| Decide/Compare | one real choice, defended | 2 points (Wk 10-11, Wk 16 capstone) | collections-era design choice; capstone |
| Debrief | reflective, cyclical | 4 arc closes + finals | Checkpoints 1-4, Week 17 |
| Judgment Log | cumulative, living | 3 checkpoints (Wk2 / mid / Wk17) | the World Bible |

---

## 1. Quick Check — the weekly gate

**Grain:** the smallest thing that proves this week's concept was actually
used. Not a spec, not a full assessment — a gate.

**Why this shape.** Wiggins & McTighe: effective formative checkpoints are
**specific** (clearly defined, directly tied to the learning objective, p.68)
and **relevant** (each one reflects a necessary step toward the larger goal,
pp.59-60) rather than a scaled-down version of the whole unit's assessment.
A gate that takes more than 2-3 sentences to define has stopped being a gate
and started being a spec — same rule the original Odyssey design named
independently; the RAG pass confirms it's not just a style preference.

**Format:** one criterion, pass/fail (or complete/incomplete, matching this
course's existing effort-based norm — see `docs/philosophy/teaching-patterns.md`).
No partial credit; a gate is not where nuance gets graded (that's Build).
Each Quick Check states:
1. The one concept being gated (e.g., "a loop that processes an unknown
   number of events").
2. Where the evidence must appear (e.g., "in this week's world code, not a
   separate exercise file").
3. Pass/fail line: does it exist and run, yes or no.

**Grading path — mechanical vs. human, decide per gate, not by default.**
Some gates are mechanically checkable (does a loop construct exist in the
diff; does a function with a return value exist) and can run through
Marker's existing per-criterion pipeline as a cheap LOCAL-style check. Others
(a founding charter reads like a real premise; a class models something
that's actually a "major noun" in the student's own world) need a human or a
frontier-agent Quick Check. Naming which is which per week is part of
authoring that week's gate (see `planning/coding-odyssey-arc-map.md`) — not
decided globally here.

---

## 2. Build — construction evidence

**Grain:** did the student actually build/extend the world with this week's
or this checkpoint's concept, correctly, and does it run.

**Two grains of Build, graded differently:**
- **Light Build (weekly creative continuation).** Holistic, not the full
  rubric below — matches this course's existing "effort, then working
  solutions" pattern (`docs/philosophy/teaching-patterns.md`). Did the
  student do something real with the week's open continuation time.
- **Full Build (the 4 Checkpoints + Week 17 final).** The existing
  `assignments/A2-coding-odyssey-project.md` template already names the
  right shape ("submit a working version, explain what changed, and
  demonstrate it") — this rubric formalizes it, doesn't replace it.

**Full Build rubric axes:**

| Axis | What it checks | Note |
|---|---|---|
| Functions | Does it run; does it do what the student claims | Not "is it impressive" — does the claimed behavior actually happen |
| Concept use | Does this arc's target concept genuinely appear (not cosmetically) | The Quick Checks along the way are the evidence trail for this |
| Explanation | Can the student say, in their own words, what changed and why | Matches Checkpoint mechanics already in place ("explain what changed") |
| Demonstrability | Could another person run or follow it | Matches "playability, clarity" already named as a recurring value |

Checkpoint 1 (Wk6, "baby project") is deliberately light on all four axes
per its own existing framing (`reports/007`) — it exists to rehearse the
mechanics, not to be graded at full Build weight. Checkpoints 2-4 and the
Week 17 final use the full rubric.

---

## 3. Decide/Compare — judgment under real trade-offs

**Grain:** commit to a choice *before* comparing it against alternatives,
then defend it against a genuine trade-off — not a retroactive rationalization.

**Two placements, both real weeks, not invented ones:**
1. **Weeks 10-11 (Lists and dictionaries).** A natural home: pick a data
   structure for a specific lookup/tracking need in the student's world,
   commit, then compare against at least one real alternative (e.g., "why a
   dict here and not a list" or "why not a set"). This replaces the
   original brainstorm's generic "Big-O algorithm choice at Week 11" framing
   — the real Week 11 topic is collections, not recursion/Big-O, so the
   decision point follows the real content instead.
2. **Week 16 capstone**, alongside Checkpoint 4 — a bigger version of the
   same move at the scale of the whole world.

**Grading:** does the comparison name a real trade-off (not just restate the
chosen option's benefits), and does the final choice follow from the
comparison rather than precede it cosmetically.

---

## 4. Debrief — the reflective cycle

**Grain:** structured reflection on what was planned, what actually
happened, what broke, and what would be done differently.

**Why this shape.** *How Learning Works*'s metacognitive cycle — assess the
task, evaluate your own knowledge/gaps, plan an approach, monitor progress,
reflect on what worked (pp.217-220) — doesn't happen by default; students
need it modeled and explicitly practiced (p.245: better metacognitive habits
would have changed both example students' outcomes in the source text), and
instructors get better results by walking through their own version of the
cycle rather than assuming it's implicit (p.237). Debrief is that explicit
practice, not a bonus reflection paragraph.

**Placement — the 4 existing Checkpoints plus Week 17, not new dates:**
- **Checkpoint 1 (Wk6):** light Debrief — "what broke when you refactored
  into a bigger loop-driven world?" Matches the checkpoint's own
  already-decided light weight.
- **Checkpoint 2 (Wk9):** standard Debrief.
- **Checkpoint 3 (Wk14): Full Trail Debrief, mandatory.** This is the
  natural point for it — Weeks 12-13 (OOP Rounds 1-2) is where "every major
  noun becomes a class," the real deliberate-refactor-crisis moment in this
  course's actual sequence (not Week 10, which is collections here, not
  OOP). Week 14 already has a "show-and-tell reflection tie-in" on the
  Friday (`planning/week-14.md`) — Full Trail Debrief deepens what's already
  scheduled there rather than adding a new due date. Prompts: what
  specifically broke in the OOP refactor, why, what would be designed
  differently starting fresh.
- **Checkpoint 4 (Wk16) + Week 17 final:** capstone Debrief, paired with
  full show-and-tell (already scheduled) and the final reflection
  (`assignments/A5-final-reflection.md`, already scheduled to start Wk16).

---

## 5. Judgment Log — the cumulative record

**Grain:** not a new document — this *is* the World Bible, viewed as a
running judgment record rather than a project journal. Same file, two
purposes: shows what exists (Build evidence) and shows how the student
decided to get there (Judgment Log).

**Minimum contents** (from the original Odyssey design, unchanged):
founding charter (Week 2), current state, one line per week on what gate was
passed and what broke, a running "known debt" list.

**Three graded checkpoints, not a running grade:**
1. **Week 2** — founding charter exists, committed. **Moved 2026-07-24**
   from Week 1 Friday: Week 1 stays strictly universal across all five
   courses (no CS1-only content, even as a separate module); Week 2 is the
   first unambiguously-CS1 week, opening with the genre pick right before
   that week's gate — see `planning/week-02.md` and
   `assignments/odyssey_gates/week-02.md`.
2. **Mid-semester** — implicitly checked at each Debrief (the Log is the raw
   material each Debrief draws from); no separate standalone grade.
3. **Week 17 final** — the Log as a whole is reviewed alongside the final
   Debrief and show-and-tell. This is also each student's own AI-practice
   "Routine" evidence — the same discipline asked of their fictional world
   is the discipline this actual course roadmap (`ROADMAP.md`) is built
   with, worth pointing out to students directly.

---

## Open, not decided here

- **Which weekly gates route through Marker (mechanical) vs. stay a human
  Quick Check** — a per-week authoring decision, not a global rule; see
  `planning/coding-odyssey-arc-map.md`.
- **Point values / weighting** across the five instruments — not set here;
  matches this course's existing pattern of effort-based, not tightly
  point-standardized, grading (`docs/philosophy/teaching-patterns.md`), but
  a real number is still owed before Savnac load.
- **NRP calibration** — these rubrics are drafted, not yet battery-tested;
  see `jeremy_task_tracking/TASKS.md`'s NRP-tuning follow-on task.
