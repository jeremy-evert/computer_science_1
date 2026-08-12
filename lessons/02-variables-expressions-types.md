# Variables, expressions, and types

## Objectives

- Store and update values with variables.
- Use arithmetic and comparison expressions.
- Choose and convert among `int`, `float`, `str`, and `bool` as needed.
- Format output predictably.

## Key content

Assignment, operators, precedence, input conversion, formatted strings, and common type errors.

## Why this matters this week

This week's Coding Odyssey Gate (`assignments/odyssey_gates/week-02.md`)
asks your world to state its own founding condition: a settlement's opening
food stock, a case's hours-cold clock, a starship's fuel remaining after a
jump, a business's opening cash on hand. Every one of those is the same
shape — **a variable, an expression that computes something from it, and a
sentence that prints the result** — which is exactly what this lecture
teaches. Nothing below is abstract for its own sake; it's the vocabulary
your gate submission is written in.

## Before class

**No required textbook (reconciled 2026-08-12) — the reading below is
optional, not assigned.** This course has no required textbook or external
course; see `docs/syllabus.md` and `docs/curriculum/recommended-resources.md`
for the recommended (not required) CS50P links for this week
(`cs50.harvard.edu/python/weeks/0/`, `/1/`).

If you'd still like a book-style optional reading, Deitel & Deitel, *Intro
to Python for Computer Science and Data Science* (2020), **Chapter 2,
"Introduction to Python Programming," sections 2.1–2.4, 2.6, and 2.8**
(pp. 49–61, 66–68) covers variables and assignment, arithmetic, `print` and
strings, getting input, and objects and dynamic typing. (Section 2.5,
triple-quoted strings, and 2.7, the `if` statement, are previewed briefly
below but belong to Week 3's branching lesson, `lessons/03-branching.md`.)
Nothing in this lesson or the Week 2 gate requires having read it.

## In class (Monday, ~35–40 minutes of live lecture + worked examples)

Per `docs/course-ethos.md`'s weekly rhythm, Monday's technical topic is the
period's main 35–40 minute active-work block (after the 10–15 minute
Monday Moment) — this is a real, timed lecture, not a five-minute aside. It
still moves fast: six short sections, each with code run live, not slides
read aloud.

### 1. Variables and assignment (Deitel §2.2)

A variable stores a value for later use. Assignment (`=`) is not algebraic
equality — it's an instruction: evaluate the right side completely, then
bind that result to the name on the left.

```python
x = 7
y = 3
total = x + y   # right side evaluates first: 7 + 3 = 10, then bound to total
print(total)    # 10
```

`total` is an **identifier**: letters, digits, and underscores, never
starting with a digit, and case-sensitive (`score` and `Score` are
different names) — see the Python Language Reference's [identifiers and
keywords](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
section, which is exactly what your interpreter enforces if you get this
wrong. PEP 8, [the Style Guide for Python
Code](https://peps.python.org/pep-0008/), is where the "one space on each
side of `=` and binary operators" convention Deitel follows comes from —
worth skimming once; it's the convention every professional Python
codebase you'll touch expects.

### 2. Arithmetic and precedence (Deitel §2.3)

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` `-` | add, subtract | `7 - 2` | `5` |
| `*` | multiply | `7 * 4` | `28` |
| `**` | exponent | `2 ** 10` | `1024` |
| `/` | true division (always float) | `7 / 4` | `1.75` |
| `//` | floor division (truncates toward −∞) | `7 // 4` / `-13 // 4` | `1` / `-4` |
| `%` | remainder | `17 % 5` | `2` |

Precedence, highest to lowest: parentheses, then `**` (right-to-left),
then `*`/`/`/`//`/`%` (left-to-right), then `+`/`-` (left-to-right). The
full, authoritative table (this book only covers a subset) is the Language
Reference's [operator precedence
table](https://docs.python.org/3/reference/expressions.html#operator-precedence).
Parentheses aren't decoration — `10 * (5 + 3)` is `80`; `10 * 5 + 3` is
`53`. When in doubt, add redundant parentheses; clarity costs nothing.

Dividing by zero (`/` or `//`) raises `ZeroDivisionError`; using a variable
that was never assigned raises `NameError` — both show up as a
**traceback**, which names the exception type and the line that triggered
it. Read the traceback's last line first; it says exactly what went wrong.

### 3. Formatted output (Deitel §2.4 + Python docs)

`print` takes a comma-separated list and joins it with spaces:

```python
print('Sum is', 7 + 3)   # Sum is 10
```

Deitel introduces this comma form; the modern, recommended way to build a
formatted string is an **f-string** — prefix a string with `f` and drop
expressions inside `{}`, optionally with a format spec after `:`:

```python
price = 19.999
print(f"Price: ${price:.2f}")     # Price: $20.00
```

(`19.999` rounded to two decimal places is `$20.00` — worth running live so
students see the rounding happen, not just trust the comment.) This is documented in the tutorial's [Formatted String
Literals](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)
section: *"f-strings let you include the value of Python expressions
inside a string by prefixing the string with `f` ... and writing
expressions as `{expression}`."* Use f-strings for anything you build in
this course from here on — they're clearer than comma-`print` once a line
has more than one value in it, and every gate genre's "print the result as
part of a sentence" requirement (see the Quick Check in
`assignments/odyssey_gates/week-02.md`) is easiest to satisfy with one.

### 4. Getting input, and why conversion matters (Deitel §2.6)

`input()` **always returns a string**, even if the user types digits:

```python
value1 = input('Enter first number: ')   # '7', a string
value2 = input('Enter second number: ')  # '3', a string
value1 + value2   # '73'  <- string concatenation, not addition!
```

To do arithmetic, convert first with `int()` or `float()`:

```python
total = int(value1) + int(value2)   # 10
```

`int()` on a non-numeric string (`int('hello')`) raises `ValueError` — a
different exception from `NameError` or `ZeroDivisionError`, and one
you'll see constantly the moment your gate reads user input. `str()` goes
the other direction, converting any value into its string form — see the
built-in functions reference for
[`int`](https://docs.python.org/3/library/functions.html#int),
[`float`](https://docs.python.org/3/library/functions.html#float), and
[`str`](https://docs.python.org/3/library/functions.html#func-str).

### 5. Types and dynamic typing (Deitel §2.8)

Every value is an **object**, and every object has a **type**:

```python
type(7)      # <class 'int'>
type(4.1)    # <class 'float'>
type('dog')  # <class 'str'>
```

Python is **dynamically typed** — a variable can be rebound to a value of
a *different* type at any point; the type lives with the value, not with
the variable name:

```python
x = 7        # x refers to an int
x = 'dog'    # now x refers to a str -- perfectly legal
```

`bool` (`True`/`False`) is the fourth type this week's objectives name, and
it's a genuine numeric subtype, not a separate island — see the standard
library's [Boolean
type](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool)
and [Numeric
Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
sections: *"Booleans are a subtype of integers."* That's why `True + True`
evaluates to `2` — not a bug, a direct consequence of that subtyping.
Comparison expressions (`7 > 4`, `x == y`) *produce* `bool` values — this
is the "comparison expressions" half of this week's objectives, and the
full `if` statement that *acts on* a `bool` is next week's topic
(`lessons/03-branching.md`).

### 6. Common type errors — the ones you will actually hit

| Error | Typical cause | Example |
|---|---|---|
| `TypeError` | mixing incompatible types in an operation | `'3' + 3` |
| `ValueError` | `int()`/`float()` on a string that isn't a valid number | `int('hello')` |
| `ZeroDivisionError` | `/` or `//` with a zero denominator | `5 / 0` |
| `NameError` | using a variable before it's assigned | `z + 7` when `z` was never set |
| `SyntaxError` | `= ` where `==` was meant, or a stray character | `if x = 5:` |

Every one of these produces a traceback. Reading it top-to-bottom the
first time is intimidating; reading its **last line** first is the
practical skill — it names the exception and gives a one-line reason.

## Worked example, tied to the gate

The Odyssey Gate's Frontier Settlement genre example is:

```python
rations_per_colonist = 2
colonist_count = 40
food_stock = rations_per_colonist * colonist_count
print(f"The settlement begins with {food_stock} days of food.")
```

Run this live in class, then swap in one of the other three genres'
numbers from `assignments/odyssey_gates/week-02.md`'s "Suggested textbook
problem" section — same shape (variable, expression, formatted print),
different story. That swap *is* the gate.

## Runnable example file

`lessons/code/week02_variables_expressions_types.py` runs every example
above (plus the historical caffeine half-life problem below) with no input
required — download it, run `python3 week02_variables_expressions_types.py`,
and read the source alongside this page; each function is labeled with the
Deitel section it demonstrates. On GitHub:
<https://github.com/jeremy-evert/computer_science_1/blob/main/lessons/code/week02_variables_expressions_types.py>.

## Historical materials

Chapters 2 and 3 appear in every modern chapter sequence and as fall 2021
homework. Representative labs include repeated division, cost
calculations, and caffeine half-life/formatted-output problems. The
caffeine problem specifically — "caffeine has a half-life of about 6
hours; given a starting amount, output the level after 6, 12, and 24
hours, formatted as floating-point numbers" (as assigned in
`archive/fall-2021/`) — is reproduced as a working function
(`caffeine_half_life`) in this week's runnable example file, using exactly
this lecture's exponentiation operator (`**`) and f-string formatting, so
the historical lab and the current lecture content are the same code, not
two disconnected artifacts.

## Optional extra practice — no story, just the mechanics (ungraded)

**This is not the assignment.** Your real graded weekly deliverable is the
Coding Odyssey Gate
(`assignments/odyssey_gates/week-02.md`) — see
`assignments/A1-weekly-coding-practice.md`: "no separate chapter problem
set is due." The gate file already has its own optional "Suggested
textbook problem" scaffolding, four genre-flavored versions of the gate
itself. **This section is different from that:** eight short, plain,
no-narrative exercises on the raw mechanic — variables, expressions,
conversion, types, formatted output — with no settlement/case/starship/
business wrapper. Use them, some of them, or none of them; they exist only
for extra reps before you attempt the gate, and nothing here is submitted,
collected, or scored. Every answer is given immediately below its
problem, so you can check yourself without waiting on anyone.

A runnable, self-checking version of all eight lives in
`lessons/code/week02_practice_problems.py` — run it and it prints each
problem, the expected answer, and confirms your own reasoning matches via
an `assert`.

**1. Predict the output.**

```python
a = 5
b = 2
c = a + b * 2
print(c)
```

> **Answer:** `9`. Precedence: `b * 2` evaluates first (`4`), then
> `a + 4` (§2.3's precedence table — `*` binds tighter than `+`).

**2. Predict the output — all three lines.**

```python
print(17 / 5)
print(17 // 5)
print(17 % 5)
```

> **Answer:** `3.4`, then `3`, then `2`. `/` is true division (always a
> float); `//` truncates toward negative infinity; `%` is the remainder
> (§2.3).

**3. Fix the type error.**

```python
age = input("Enter your age: ")
next_year = age + 1
```

> **Answer:** `input()` always returns a `str` (§2.6), so `age + 1` raises
> `TypeError: can only concatenate str (not "int") to str`. Fix:
> `next_year = int(age) + 1`.

**4. Write one line.** Given `price = 42.5`, print it formatted to exactly
two decimal places with a leading `$`.

> **Answer:** `print(f"${price:.2f}")` → `$42.50` (§2.4's f-string format
> spec).

**5. Predict the output.**

```python
x = 10
x = "ten"
print(type(x))
```

> **Answer:** `<class 'str'>`. Python is dynamically typed (§2.8) — `x` is
> rebound to a new value of a different type; nothing about the *name*
> `x` was ever fixed to `int`.

**6. What does this code print — and why might that surprise you?**

```python
value1 = "4"
value2 = "5"
print(value1 + value2)
```

> **Answer:** `45` (a two-character string), not `9`. Both operands are
> `str`, so `+` is string concatenation, not arithmetic addition (§2.6) —
> this is exactly the trap `input()` sets if you forget to convert first.

**7. Name the exception each line raises, before you run it.**

```python
print(5 / 0)
print(int("hello"))
print(z + 1)          # z was never assigned
```

> **Answer, in order:** `ZeroDivisionError`, `ValueError`, `NameError`
> (the common-type-errors table above).

**8. Write one line.** Store `3 ** 4` in a variable named `total`, then
print `total`.

> **Answer:** `total = 3 ** 4` then `print(total)` → `81`. (`**` is
> exponentiation, §2.3 — right-associative, evaluated before `*`/`/`.)

## Source and limitation note

- Primary source: Paul & Harvey Deitel, *Intro to Python for Computer
  Science and Data Science: Learning to Program with AI, Big Data and the
  Cloud* (Pearson, 2020), Chapter 2, "Introduction to Python Programming,"
  §§2.1–2.4, 2.6, 2.8 (pp. 49–61, 66–68). Local copy:
  `curriculum_rag_supporter/books/Intro to Python forComputer Science and
  Data Science Learning to Program with AI, Big Data and the Cloud (Paul
  Deitel) (Z-Library).pdf`. This is Deitel's own chapter numbering, not
  zyBooks' — see the chapter-numbering note above.
- Supplementary sources: the official Python documentation — [Formatted
  String
  Literals](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals),
  [Numeric Types — int, float,
  complex](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex),
  [Boolean Type —
  bool](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool),
  built-in
  [`int`](https://docs.python.org/3/library/functions.html#int)/[`float`](https://docs.python.org/3/library/functions.html#float)/[`str`](https://docs.python.org/3/library/functions.html#func-str)/[`bool`](https://docs.python.org/3/library/functions.html#bool),
  [Operator
  Precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence),
  [Identifiers and
  Keywords](https://docs.python.org/3/reference/lexical_analysis.html#identifiers),
  and [PEP 8](https://peps.python.org/pep-0008/).
- This lesson covers Deitel §§2.1–2.4, 2.6, and 2.8 only — §2.5
  (triple-quoted strings) and §2.7 (the `if` statement) are deliberately
  deferred to `lessons/03-branching.md`, since this week's objectives are
  variables/expressions/types, not branching. Deitel's own §2.9 (basic
  descriptive statistics) is out of scope for this lecture entirely.
