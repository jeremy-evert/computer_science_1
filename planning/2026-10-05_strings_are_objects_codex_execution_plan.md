# Strings Are Objects — Codex Execution Plan

**Course:** COMSC-1033 Computer Science I  
**Created:** 2026-10-05  
**Companion concept map:** `planning/2026-10-05_strings_are_objects_lesson_map.md`

## Mission

Turn the strings lesson into a playful, coherent class experience that begins with text manipulation and quietly teaches students the mental model they will later use for objects, libraries, APIs, networking automation, and game design.

The core through-line is:

> **What is this thing, and what can it do?**

The build should happen in small, independently useful pieces. Do not attempt the entire lesson in one giant edit.

---

# Build order

## Phase 0 — Read before changing anything

Before editing, read:

1. `AGENTS.md`
2. `README.md`
3. `NAMING.md`
4. `lessons/06-strings.md`
5. `planning/2026-10-05_strings_are_objects_lesson_map.md`
6. `docs/course-ethos.md`

Preserve existing course philosophy and repository conventions.

---

# Phase 1 — Build the Mad Lib demo

## Goal

Create one polished Python example that students can understand almost immediately.

## Proposed file

`examples/strings_mad_lib.py`

If `examples/` does not exist, inspect the repo for the closest existing convention before creating a new top-level content category. Do not invent a new category casually.

## Requirements

The program should:

- collect 5–7 pieces of user input
- use an f-string to assemble a short absurd story
- demonstrate at least:
  - `.strip()`
  - `.title()`
  - `.lower()` or `.upper()`
- remain readable to a beginning Python student
- avoid advanced syntax
- include comments only where they genuinely help
- run directly with ordinary Python 3

## Teaching purpose

The Mad Lib is not primarily about formatting.

It creates the question:

> Why can we write `name.strip()` or `place.title()`?

That question leads to methods, dot notation, and objects.

## Acceptance check

Run the program manually.

Confirm that:

- it accepts input
- whitespace cleanup is visible
- capitalization transformations are visible
- the final story is coherent and funny enough to use live
- no unexplained advanced feature appears

---

# Phase 2 — Build the String Laboratory

## Goal

Create a runnable demonstration of string behavior.

## Proposed file

`examples/string_lab.py`

Use the same location selected in Phase 1.

## Demonstrate

At minimum:

```python
text.strip()
text.lower()
text.upper()
text.title()
text.replace(...)
text.split()
text.count(...)
text.find(...)
text.startswith(...)
text.endswith(...)
```

Also demonstrate:

```python
type(text)
dir(text)
help(str.replace)
```

The code should explicitly demonstrate **immutability**:

```python
name = "jeremy"
name.upper()
print(name)
```

Then:

```python
name = name.upper()
print(name)
```

## Teaching purpose

Students should see:

1. strings have behaviors
2. those behaviors are accessed with dot notation
3. methods often return new values
4. the original string does not necessarily change
5. Python can tell us what an unfamiliar object can do

## Acceptance check

The script must run without modification.

Output should be labeled clearly enough that it can be used during live teaching.

---

# Phase 3 — Expand the canonical lesson

## Target file

`lessons/06-strings.md`

## Goal

Turn the current short placeholder into the durable lesson guide.

## Required sections

### 1. Objectives

Students should be able to:

- create and manipulate strings
- index and slice strings
- use common string methods
- explain the basic meaning of `object.method()`
- identify a string as an object of type `str`
- explain that strings are immutable
- use `type()`, `dir()`, and `help()` to investigate unfamiliar objects

### 2. Hook: Mad Lib

Explain how to use the Mad Lib as the opening activity.

### 3. How does a string behave?

Use a few short examples rather than a giant method catalog.

### 4. The dot

Introduce:

```
object.method()
```

Beginner-friendly language:

> Ask an object to use one of the behaviors that belongs to its type.

Avoid pretending this is a full formal definition of object-oriented programming.

### 5. A first object model

Use:

- type
- state/value
- behavior

Recurring question:

> What is this thing, what does it know, and what can it do?

### 6. Immutability

Show that string methods usually produce a new string rather than changing the existing one.

### 7. Discovering behavior

Teach:

```python
type(...)
dir(...)
help(...)
```

Emphasize discovery over memorization.

### 8. Cross-domain object thinking

Briefly connect the idea to:

- video game objects
- network devices/interfaces
- organizational hierarchy
- policy/procedure hierarchy
- Python libraries and APIs

Be precise:

**Do not claim Cisco IOS uses Python-style dot notation.**

The Cisco comparison is about hierarchy, encapsulation, and organizing behavior around things. Python network automation libraries may literally use object and method syntax.

### 9. Practice

Include small experiments students can type themselves.

### 10. Exit question

Use something close to:

> Pick one object we touched today. What type of thing is it, and what can it do?

---

# Phase 4 — Create the presentation source

## Goal

Create a Beamer slide deck that supports live teaching rather than replacing it.

## Proposed location

Prefer a lesson-adjacent location such as:

`slides/06_strings_are_objects.tex`

But before creating a new top-level `slides/` directory:

1. inspect repository conventions
2. inspect sibling course repos if available
3. if no convention exists, document the new category in `NAMING.md`

Do not silently invent a structure.

## Slide philosophy

Slides should be visually sparse.

Prefer:

- one question
- one code example
- one diagram
- one punchline

Avoid paragraphs of lecture notes.

## Suggested slide arc

1. Strings Are Weirdly Powerful
2. Mad Lib
3. What is a string?
4. Better question: how does a string behave?
5. The dot
6. `object.method()`
7. String method demo
8. What makes something an object?
9. Type + state + behavior
10. Strings are immutable
11. You are not supposed to memorize this stuff
12. `type()`, `dir()`, `help()`
13. Object Detective
14. Objects in games
15. Objects in networks
16. Objects in organizations
17. Objects in policies
18. Why object thinking scales
19. Return to the Mad Lib
20. What is this thing, and what can it do?

## Presentation constraints

- target roughly 20 slides
- 16:9 aspect ratio
- syntax-highlighted Python where practical
- large type
- minimal text
- no decorative clutter
- compile cleanly with a normal LaTeX/Beamer toolchain

If the environment has `latexmk`, use it to validate.

---

# Phase 5 — Object Detective activity

## Goal

Create a reusable student activity that teaches investigation.

Because this course treats student deliverables as shared learning resources, design the activity so students can post discoveries that classmates can see.

## Core protocol

Students investigate a provided object:

```python
type(thing)
dir(thing)
help(...)
```

They report:

1. What type is it?
2. Name three methods or useful attributes.
3. Pick one unfamiliar behavior.
4. Test it.
5. What did it return?
6. Did the original object change?
7. What did you learn from another student's investigation?

## Potential objects

Start with strings.

Later variants can use:

- lists
- dictionaries
- files
- modules
- pathlib paths
- simple custom class instances

---

# Phase 6 — Optional game-object bridge

Create a tiny conceptual activity where students invent a game object.

Example:

```
Object: Goose

State:
- name
- health
- anger_level
- location
- stolen_items

Behavior:
- honk()
- chase()
- steal()
- flee()
```

Purpose:

Show that a string and an angry goose look wildly different, but the same organizing idea applies:

- a thing has a type
- it has state
- it has behaviors

No custom Python class is required yet unless it benefits the live lesson.

---

# Phase 7 — Validation and polish

Before declaring the lesson complete:

- run every Python example
- compile the Beamer presentation
- check code snippets in slides against actual runnable examples
- verify terminology is accurate
- keep the Cisco comparison technically honest
- verify links and file references
- remove duplicate explanations
- make sure the lesson still feels like a story, not a glossary

---

# Recommended Codex workflow

Work one phase at a time.

For each phase:

1. read the companion lesson map
2. inspect relevant repository files
3. implement only that phase
4. run or compile what was created
5. report:
   - files changed
   - commands run
   - validation result
   - any design question that should be deferred to Jeremy

Do not rewrite unrelated course materials.

Do not perform broad repository cleanup while working on this lesson.

---

# Best first Codex assignment

Start with **Phase 1 and Phase 2 only**.

Prompt:

> Read `AGENTS.md`, `NAMING.md`, `lessons/06-strings.md`, and both strings planning files. Build the Mad Lib and String Laboratory described in `planning/2026-10-05_strings_are_objects_codex_execution_plan.md`. Follow existing repo conventions for example code placement rather than guessing. Run both scripts. Do not edit the Beamer deck or expand the lesson yet. Commit-ready changes only, then report what you changed and how you validated it.

This is deliberately small.

Once those examples feel right, the examples become the raw material for both the lesson text and the slide deck.

---

# Definition of done for the whole project

The project is complete when the repository contains:

- a durable strings lesson
- a runnable Mad Lib
- a runnable String Laboratory
- an Object Detective student activity
- a Beamer presentation that compiles successfully
- an accurate cross-domain explanation of object thinking
- a clear bridge from strings into later collections, files, modules, and classes

The student-level destination is:

> A string is an object of type `str`. It has methods that I access with dot notation. I do not need to memorize every method because I can investigate an object and learn what it can do. The same way of thinking will appear throughout programming.

