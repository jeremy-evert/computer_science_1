# Branching and decision-making

## Objectives

- Translate conditions into Boolean expressions.
- Use `if`/`elif`/`else` to handle alternatives.
- Test boundary and invalid cases.

## Why this matters this week

Last week your world could only ever say one thing. This week's Reasoning
Odyssey Gate (`assignments/odyssey_gates/week-03.md`) asks your world to
make its first real decision: print a different line depending on some
piece of world state — a settlement's food stock, a case's hours-cold
clock, a starship's fuel remaining, a business's cash on hand. That's
exactly what branching is: **letting the value of an expression choose
which lines of code run.**

## Before class

**No required textbook.** The reading/watching below is optional, not
assigned — see `docs/syllabus.md` and `docs/curriculum/recommended-resources.md`.
This week's recommended (not required) material is CS50P's Conditionals
lecture (week 2) — a free, open Harvard course (CC BY-NC-SA 4.0):

- Lecture page: <https://cs50.harvard.edu/python/weeks/2/>
- Watch the lecture: <https://video.cs50.io/-7xg8pGcP6w>
- Lecture slides (PDF): <https://cdn.cs50.net/python/2022/x/lectures/2/lecture2.pdf>
- Source code shown in lecture: <https://cdn.cs50.net/python/2022/x/lectures/2/src2/>

The official [Python tutorial's `if`
Statements section](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
is a good supplement if you want the language's own reference
description instead of a lecture.

## In class: how to play with `if` statements

### 1. A program is normally a straight line

Without branching, every line runs, top to bottom, every time:

```python
print("Checking status...")
print("All clear.")
```

`if` breaks that straight line. It asks a yes/no question and only runs
the lines under it when the answer is yes.

### 2. Comparisons produce the yes/no answer

A comparison expression evaluates to a `bool` — `True` or `False`:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | equal to | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 3` | `True` |
| `<` `>` | less than, greater than | `3 < 5` | `True` |
| `<=` `>=` | less/greater than or equal | `5 <= 5` | `True` |

`==` tests equality; `=` assigns a value. Mixing them up (`if x = 5:`) is
a `SyntaxError`, not a quiet bug — Python won't let you make this mistake
silently.

### 3. The `if` statement itself

```python
food_stock = 15

if food_stock < 20:
    print("Warning: supplies are running low.")
```

Three parts every time: the `if` keyword, a condition that evaluates to
`True` or `False`, and a colon. Everything **indented under it** only
runs when the condition is `True`. Python uses indentation itself to mark
that block — not `{}`, not `end` — so a wrong indent level is a real
error, not a style preference.

### 4. `else`: the other branch

```python
if food_stock < 20:
    print("Warning: supplies are running low.")
else:
    print("The settlement is stable.")
```

Exactly one of these two blocks runs, never both, never neither. `else`
has no condition of its own — it means "every other case."

### 5. `elif`: more than two outcomes

```python
if food_stock < 5:
    print("Critical: rationing begins immediately.")
elif food_stock < 20:
    print("Warning: supplies are running low.")
else:
    print("The settlement is stable.")
```

Python checks each condition top to bottom and runs the **first** one
that's `True`, then skips the rest — order matters. If `food_stock` is
`3`, the first branch fires and the other two are never even checked,
even though `3 < 20` is also true.

### 6. Combining conditions: `and`, `or`, `not`

```python
if food_stock < 20 and colonist_count > 40:
    print("Warning: low supplies for a large settlement.")
```

`and` requires both sides to be `True`; `or` requires at least one;
`not` flips a `True`/`False`. These combine with comparisons to build
richer conditions without nesting.

### 7. Nested conditions

An `if` can contain another `if`:

```python
if food_stock < 20:
    if colonist_count > 40:
        print("Warning: low supplies for a large settlement.")
    else:
        print("Warning: supplies are low, but the group is small.")
```

Nesting works, but it gets hard to read fast. Prefer `and`/`or` (step 6)
over nesting when you can — same logic, one condition to check instead of
two indent levels to track.

### 8. Boundary and invalid cases — why this week's objectives say "test" them

A condition like `food_stock < 20` has an edge: what happens at exactly
`20`? Run your code with a boundary value (`food_stock = 20`, not just
`15` or `5`) and confirm it lands in the branch you actually intended.
This is the same discipline as last week's type-conversion errors: the
case that breaks your program is rarely the obvious one.

## Worked example, tied to the gate

```python
food_stock = 15
colonist_count = 40

if food_stock < 20:
    print(f"Warning: only {food_stock} days of food remain.")
else:
    print(f"The settlement is stable with {food_stock} days of food.")
```

Run this once with `food_stock = 15` (the warning fires) and once with
`food_stock = 25` (it doesn't) — showing both branches actually run is
part of this week's Quick Check in `assignments/odyssey_gates/week-03.md`.

## Historical materials

Chapter 4 is stable from fall 2022 through spring 2026. Historical labs
include smallest-number and interstate-highway classification problems;
branching is also a common early project ingredient.

## Source and limitation note

- Recommended reading: CS50P, Harvard's free CS50 for Python course,
  Conditionals lecture, <https://cs50.harvard.edu/python/weeks/2/>.
  License: CC BY-NC-SA 4.0 (confirmed at `cs50.harvard.edu/python/license/`),
  linked only, no content copied — see
  `docs/curriculum/recommended-resources.md`.
- Supplementary source: the official Python documentation's [`if`
  Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
  and [Boolean Operations — `and`, `or`,
  `not`](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
  sections.
- This lesson is optional-reading-supported, not textbook-required — see
  `docs/syllabus.md`.
