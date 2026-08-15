# COMSC 1033 — Course Ethos and Weekly Contract

**Stated by Jeremy, 2026-07-15. This is the canonical description of what the
course asks of students and what it gives them.** When another document in
this repo disagrees with this one, this one wins until Jeremy says otherwise.

## The class in one sentence

A supportive class structure where students learn to program through lecture,
paired programming, and show-and-tell — with an AI-fluency strand and a
professional-development strand woven through every week.

## The weekly rhythm

This rhythm is shared across all of Jeremy's courses — the canonical
cross-course statement lives at `swosu_cs_curriculum/shared/weekly-rhythm.md`;
this file instantiates it for CS1.

**Every class period (50 min):** 10–15 minutes presented (10 of material, a
few for questions), then 35–40 minutes of active work. The presented segment
uses a slide deck **with a live clock in the corner** — the deck exists to
keep the demo on time as much as to present. Fifteen minutes is a hard
ceiling.

| Day | 10–15 min strand | Source repo | 35–40 min active work |
|---|---|---|---|
| **Monday** | **Monday Moment** — AI fluency | `ai_fluency/ai_i/` | Main topic of the week — lecture with live worked examples |
| **Wednesday** | **Wacky Wednesday** — professional minds | `professional_minds/` | Paired programming |
| **Friday** | **Fun Friday** — professional minds | `professional_minds/` | Show-and-tell |

**Week 1 is the same in every course:** Monday — getting the most out of
this class and this semester (best practices); Wednesday — getting the most
out of your degree (LinkedIn Learning, degree check, degree plan, progress
report, course substitutions, degree audits); Friday — getting the most out
of your career (daily 3-things journal; weekly two paragraphs into the vita;
monthly rotate a resume line into the CV; internships, resume tips, the job
search).

**Each strand item ships in three forms** (resolves the format tension,
2026-07-15):

1. **Digest document** — a few minutes to read on their own. Most students
   won't read it before class; those who do expand their learning.
2. **Live demo** — the principle demonstrated, not just described, inside
   the 15-minute ceiling, slide-deck-and-clock keeping it honest.
3. **Podcast** — humor-forward discussion of the topic. Three strand
   podcasts per week **plus a fourth podcast covering the meat of the Monday
   lecture** (four per week total).

Aspirational, wanted but not committed: **a graphic novel with recurring
characters** carrying the same ideas, and beyond it a **3–5 minute
AI-animated video per lesson** (pipe dream, on the record 2026-07-15).

**Tooling as curriculum (2026-07-15).** Students meet Ollama + Open WebUI on
the classroom GPUs (3070 Ti / 5080) as their chat bot — and learn to run
experiments against it: same prompt across local model, free tier, paid
tier; compare, log limits, reason about fit. The motto: **"Trust the tools
less. Love the tools more."** The NRP appears as a recurring instructor-run
Friday show-and-tell spotlight — Jeremy demos something real on the National
Research Platform most weeks; students watch, not operate, in CS1.

**Parking lot (wanted, unbuilt):** a video chat app for the class — thought
about all summer, not started; revisit when the pipeline is humming.

## What we ask of students (weekly)

Six recurring student artifacts, each with its own reusable template:

1. **Monday Moment practice assignment** — helps students establish best
   practices for whatever the week's Monday Moment teaches.
2. **Wacky Wednesday reflection** — how the Wednesday professional-minds
   lesson ties into the week.
3. **Weekly topic reinforcement** — practice reinforcing the week's technical
   course topic. **Reconciled 2026-07-27:** this practice happens inside the
   student's Reasoning Odyssey world (`assignments/A2-coding-odyssey-project.md`),
   not through a separate textbook problem set — the textbook chapter
   supplies the concept and stays part of the lecture/conversation, but
   every technical week's gate or checkpoint *is* this artifact. See
   `assignments/A1-weekly-coding-practice.md`.
4. **Fun Friday reflection** — how the Friday professional-minds lesson ties
   into the week.
5. **Paired-programming report** — evaluates how the student contributed to
   Wednesday's paired programming.
6. **Friday feedback report** — evaluates the feedback the student gave in
   the Friday show-and-tell discussion.

Templates for these live in `templates/weekly/` (to be authored; see the
build checklist below).

## What we give students

1. **Slide presentations in class** — the three weekly decks above plus
   lecture slides.
2. **Transcriptions of the class recordings.**
3. **A LaTeX document of the material being taught** — the course's written
   technical text.
4. **A chat bot** for discussing their ideas — a thinking partner, consistent
   with the standing "AI as tutor, not typist" stance and the Marker/Coach
   doctrine (explains and questions; does not write the student's fixes or
   solution code).
5. **Examples of worked solutions** — nothing hidden; students see what good
   work looks like.
6. **Automated feedback "out-of-office reply" in Canvas** — every submission
   gets a prompt automated response (the Harbor → Guidepost → Marker → Coach
   pipeline), so no student waits in silence.
7. **A shared repository** where the class shares code and ideas and helps
   each other grow.
8. **A supportive class structure** — the umbrella promise all of the above
   serves. Students are not expected to arrive knowing how to program;
   practice, visible progress, explanation, revision, and asking for help are
   the core of the course.

## Build checklist derived from this contract

Per week with class meetings (16 instructional weeks + finals; see
`planning/`):

- [ ] Monday Moment deck (15 min) — from `ai_fluency/ai_i/`
- [ ] Wacky Wednesday deck (15 min) — from `professional_minds/`
- [ ] Fun Friday deck (15 min) — from `professional_minds/`
- [ ] Lecture material: slides + transcript + LaTeX section + worked examples

Once, then reused weekly:

- [ ] Six weekly assignment/report templates (`templates/weekly/`)
- [ ] Chat bot (tutor-not-typist rules)
- [ ] Canvas automated-feedback reply (pipeline exists; wire to this course)
- [ ] Shared class repository (structure + contribution norms)

## Grading direction (decided 2026-07-15; percentages finalized 2026-08-12, `docs/grading-model.md`)

- **No traditional tests.** Points come from the weekly artifacts.
- Points attach to: (a) the Monday Moment quiz, (b) the Wednesday
  reflection, (c) the Friday reflection, plus the reinforcement assignment
  and the two weekly reports. If we want students to do the work, it earns
  points and gets graded.
- **The homework category splits up** — the old single 68% "homework" bucket
  becomes named categories. Final split: `docs/grading-model.md`.
- **The weekly reinforcement assignment is graded on two axes:** the working
  result, and the process — rhetoric (challenged the question or answered
  it as written?), planning (plan first or winged it?), tool transparency
  (which services, free or paid, disclosed), and knowledge management
  (prompts and chats tracked). Knowledge management and resource tracking
  are part of the ethos, even in CS1. **Reconciled 2026-07-27:** the working
  result is that week's Reasoning Odyssey gate or checkpoint, not a separate
  chapter problem set — see `assignments/A1-weekly-coding-practice.md`.
- **The final is a reflection paper** (decided 2026-07-15) — template basis:
  `assignments/A5-final-reflection.md`. Weight in `docs/grading-model.md`.
- **Collaboration is encouraged.** Pairs may share one repo. Each student
  documents their own contributions; the git log must show a
  lines-of-code split no more lopsided than 80/20.
- **Resource budgeting is a graded skill, not an equity filter.** Students
  track which services/models/tiers they used, what limits they hit, and why
  that tool fit the problem — different models hit different. Graded on the
  tracking and reasoning, never on how much money was spent.

## Known tensions to resolve

1. ~~**Monday Moment length.**~~ **Resolved 2026-07-15:** both formats, with
   different jobs — a few-minute digest document for self-paced reading,
   plus a live in-class demo capped at 15 minutes by a slide deck with a
   live on-screen clock. The tutor-not-typist ethos carries forward.
2. ~~**Class-time budget.**~~ **Resolved 2026-07-15:** 10–15 presented /
   35–40 active is the explicit, chosen shape of every period.
3. **Weekly student load.** Six artifacts per week across ~15 full weeks is
   roughly 90 submissions per student per semester. Intentional, and exactly
   why the automated-feedback reply exists — but the grading model must
   keep each artifact small enough to complete and grade weekly.
4. **Syllabus.** Needs serious work (Jeremy, 2026-07-15): fold in this
   contract, the new grading categories, the university's final-exam policy,
   and the Faculty Commons template items already listed in its own
   finalization checklist.
5. ~~**Weekly production load (instructor side).**~~ **Resolved 2026-07-15
   with a production stack:** LaTeX/Markdown docs, Beamer slides, automated
   pipeline for podcast + graphic novel, transcripts slurped from class
   recordings after the fact, worked examples produced live on Mondays.
   Artifact priority per lesson: LaTeX document → Beamer slides → podcast →
   graphic novel. Build order: map every 10–15-minute block for the semester
   first (highest ROI), then grind one lesson at a time through the pipeline
   (Codex gpt-5.6-luna, medium). One caveat carried forward: a static Beamer
   PDF can't show a live on-slide clock — present via `pdfpc`/`pympress`,
   whose presenter console provides the live timer.
6. ~~**Weekly reinforcement vs. the Reasoning Odyssey.**~~ **Resolved
   2026-07-27:** the 2026-07-24 Odyssey pivot (weekly gates, genre menu,
   World Bible — `docs/curriculum/judgment_toolkit.md`) made the Odyssey the
   spine of the course, but this file, `docs/grading-model.md`, and most of
   `planning/week-NN.md` still described the weekly reinforcement
   assignment as a separate textbook-chapter problem set running alongside
   it. Jeremy's call, 2026-07-27: every week is a Reasoning Odyssey week — the
   textbook chapter supplies the concept and stays part of the lecture and
   conversation, but the gate or checkpoint *is* the practice, not an
   addition to it. All affected documents reconciled to this on that date.
