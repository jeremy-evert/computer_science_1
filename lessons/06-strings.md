# Strings Are Objects

> What is this thing, and what can it do?

We will make a ridiculous story, investigate its strings, and learn how to
ask Python about their behaviors. This is a first object model; you do not
need to define your own classes yet.

## Objectives

- Create strings and combine them with concatenation and f-strings.
- Index and slice strings to retrieve parts of their text.
- Search and transform text with useful string methods.
- Read `object.method()` and explain the dot and parentheses.
- Identify a string as an object of type `str`, with a value and behaviors.
- Explain string immutability and save transformation results.
- Use `type()`, `dir()`, and `help()` to investigate unfamiliar objects.

## Hook: the Great Campus Goose Emergency

Run the completed [Mad Lib](code/strings_mad_lib.py) from the repository root:

```bash
python3 lessons/code/strings_mad_lib.py
```

Give it six silly answers: a made-up hero's name, an adjective, a singular
noun, a place, a verb, and something absurd. Try extra spaces and mixed
capitals. Type `  cAPTAIN nOODLE  ` for the name. The program shows the raw
name and `Captain Noodle`, then builds a story in which a goose appoints
your noun dean.

Ask: What changed between the name as typed and the name in the story?
Which part of the program made that happen?

The demo saves the cleaned name with this line:

```python
name = raw_name.strip().title()
```

`strip()` returns text with surrounding whitespace removed. `title()` is
called on that returned string and returns title-cased text. These are two
successive method calls. Title casing suits this silly story, but it is not
a reliable rule for every person's preferred name spelling.

Return to the demo after investigating strings: explain why saving the
result matters and why there can be more than one dot in an expression.

## Creating and combining strings

A string represents text. Single or double quotes create string literals;
the surrounding quotes are syntax, not part of the value. `input()` also
returns a string, even when the user types digits.

```python
hero = "Captain Noodle"
place = 'The Moon'
message = hero + " visits " + place
print(message)  # Captain Noodle visits The Moon
print(f"{hero} would like a refund.")
```

`+` joins strings. An f-string inserts values from expressions in braces.
The Mad Lib uses a triple-quoted f-string to span several lines. Spaces
inside quotes belong to the value. Cleanup alone does not validate an
answer: `"   ".strip()` produces an empty string. A program requiring a
nonempty answer must check the cleaned result separately.

## Indexing and slicing

Square brackets select text by position. Positions start at zero;
negative indices count back from the end.

```python
word = "Bulldogs"
print(word[0])    # B
print(word[-1])   # s
print(word[0:4])  # Bull
print(word[4:])   # dogs
print(word[:4])   # Bull
print(word[::2])  # Bldg
```

A slice has the form `start:stop:step`. It includes the start and excludes
the stop. For the usual positive step, omitted bounds use the beginning or
end. The last example selects positions 0, 2, 4, and 6.

An index outside the string, such as `word[8]`, raises `IndexError`.
A slice such as `word[:100]` safely stops at the end. Indexing returns a
one-character string; slicing also returns a string. Python strings are
sequences of Unicode code points; one visible symbol can contain more than
one code point. The letters here keep the position examples simple.

## How does a string behave? The String Laboratory

Run the completed [String Laboratory](code/string_lab.py):

```bash
python3 lessons/code/string_lab.py
```

Its deliberately messy starting value is:

```python
text = "  The Bulldogs Have ESCAPED Again!  "
print(text.strip())
print(text.lower())
print(text.replace("Bulldogs", "Geese"))
```

Predict each result, run it, and compare. `strip()` removes whitespace at
the ends, not between words. `lower()` changes case. `replace()` searches
for an exact substring and returns text with replacements. Spaces remain
unless the operation removes them.

The lab demonstrates different kinds of return value:

| Calls in the lab | What comes back |
| --- | --- |
| `strip()`, `lower()`, `upper()`, `title()`, `replace(...)` | A string (`str`) |
| `split()` | A list (`list`) of pieces; no argument means split on whitespace |
| `count("a")` | An integer (`int`): the number of matching occurrences |
| `find("Bulldogs")` | An integer position: `6` for this value |
| `find("Geese")` | `-1`, meaning no match |
| `startswith("The")`, `endswith("!")` | A Boolean (`bool`): both `False` here |

Searches and these prefix/suffix checks are case-sensitive. The checks are
false because `text` starts and ends with spaces. The lab saves
`clean_text = text.strip()`; those checks on `clean_text` are true.
`find()` uses zero-based positions. Check for `-1` before using a search
result as an index: `text[-1]` means the last character, not "no match."

Predict the value **and its type**. The list returned by `split()` does not
have the string method `upper()`.

## The dot: `object.method()`

Read this pattern as:

> Ask an object to use one of the behaviors that belongs to its type.

In `text.upper()`, `text` refers to a string object. The dot looks up the
attribute named `upper`; here that attribute is a method. The parentheses
call it. Some methods accept arguments, such as the old and new text in
`text.replace("Bulldogs", "Geese")`.

Without parentheses, `text.upper` refers to the method without calling it.
A dot can also access an attribute holding information; not every name
after a dot is a method. Square brackets in `text[0]` select an item,
which is a different operation.

## A first object model: type + state/value + behavior

For the lab's `text`, ask:

| Question | String example |
| --- | --- |
| What kind of thing is it? | Its type is `str`. |
| What information does it hold? | Its value is `"  The Bulldogs Have ESCAPED Again!  "`. |
| What can it do? | Its type supplies behaviors such as `strip()`, `replace()`, and `split()`. |

The information an object holds is often called its **state**. For a
string, the text value is the useful state to discuss. A behavior need
not change that state: it can compute and return a result.

The variable name `text` refers to the object; the name is not the type.
Strings with different values still have type `str`.

Expand our recurring question when investigating a new object:

> What is this thing, what does it know, and what can it do?

## Immutability

The lab makes this distinction visible:

```python
name = "jeremy"
name.upper()
print(name)  # jeremy
name = name.upper()
print(name)  # JEREMY
```

Strings are **immutable**: their contents cannot be changed in place.
`upper()` returns an uppercase string; the first call discards that result.
Assignment makes `name` refer to the returned string. It does not edit
the original string. This is why the Mad Lib saves `raw_name.strip().title()`.

String transformations return string results rather than mutating their
receiver. Other string methods return lists, integers, or Booleans. Do not
assume every method returns a string, or every kind of object is immutable.

Trying `name[0] = "J"` raises `TypeError`. To make different text, construct
another string and save it. You do not need to reason about memory allocation
or object identity to understand this rule.

## Discovering behavior rather than memorizing it

The final part of the lab asks Python three focused questions:

```python
print(type(text))
print(dir(text))
help(str.replace)
```

`type(text)` identifies the type, displayed as `<class 'str'>`.
`dir(text)` lists attribute names, including methods. It does not explain
arguments or promise every listed name is callable. Names with double
underscores have special roles; start with familiar names like `replace`.

`help(str.replace)` describes the method on the string type. Read what it
accepts and returns, then test a small case. `help(text.replace)` also gives
focused help. Passing a method to `help` differs from calling it:
`help(text.replace("Bulldogs", "Geese"))` asks about the returned string.
`help(str)` gives broader documentation when you need it.

Use this loop: identify the type, look for a relevant name, read focused
help, predict a result, and try it. Programming does not require memorizing
the complete method list.

## Cross-domain object thinking

The same questions help us approach larger systems. These bridges introduce
ways to organize information and responsibilities, not full class design.

- **Games:** a conceptual player object might hold health and position and
  offer movement behavior. In a program designed that way, `player.move()`
  could call a method and `player.health` could read an attribute. These
  names are illustrative, not a runnable game API. Game objects often have
  changing state.
- **Networking:** devices have interfaces; interfaces have status and
  configuration. Grouping related information and operations around those
  things helps us navigate a network. Cisco IOS configuration contexts are
  a conceptual comparison involving hierarchy and responsibility.
  **Cisco IOS CLI itself does not use Python-style `object.method()` syntax.**
  Python automation libraries can expose connection objects with methods;
  their documentation determines the actual names and behavior. A conceptual
  interface hierarchy does not guarantee an `interface.enable()` API.
- **Organizations:** university → college → department is a hierarchy of
  relationships and responsibilities. This is a navigation analogy, not
  Python syntax or a claim that departments are programming classes.
- **Policy and procedure:** technology → security → incident response groups
  policies by scope and procedures by responsibility. A procedure describes
  actions people should take; it is not automatically an executable method.
- **Libraries and APIs:** Python's standard library gives a literal example:
  `from pathlib import Path`, then `path = Path("notes.txt")`, creates a
  path object; `path.exists()` calls its method. A dotted call can also
  access a function in a module, so inspect what is left of the dot.
  An API is an interface for using software: it may expose Python objects
  or HTTP requests and data. A remote endpoint is not inherently a Python
  method. Ask what an operation accepts, returns, and changes.

Strings give us practice with these questions before meeting collections,
files, modules, and eventually our own classes.

## Practice: predict, run, explain

These are supporting experiments for class or independent practice, not a
separate graded assignment. Work with a partner: one person predicts, the
other runs, then switch. Use AI as a tutor to question a prediction or explain
an error; type and explain your own experiments.

1. Run the Mad Lib with the padded, mixed-case name above. Locate the line
   that saves the cleaned value. Explain each method call in order.
2. Type the indexing examples. Change a slice bound and predict the selected
   positions. Compare `word[8]` with `word[:100]` separately.
3. Use the lab's exact `text` value. Compare `text.startswith("The")` with
   `text.strip().startswith("The")`. Explain whether `text` changed.
4. Compare `text.find("Bulldogs")` with `text.find("bulldogs")`. Use `type()`
   on a `split()` result and a `count()` result. Explain why their types differ.
5. Read `help(str.replace)`, then replace `"Bulldogs"` with `"Geese"`. Print
   the returned value and the original. Explain what each holds.

When using these discoveries in your existing weekly programming gate,
share them in that gate's graded discussion. Classmates will see your work
and can learn from it; read their approaches too. These experiments add no
new submission deadline.

## Exit question

Pick one object we touched today. What type of thing is it, what value does
it hold, and what can it do? Give one method's return value and explain
whether the original object changes. Discuss your answer with a partner.

> What is this thing, and what can it do?

## Historical materials

Chapter 7 is stable in 2023–26 and is part of the 2024–26 pair-programming sequence.
