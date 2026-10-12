# Lesson 03: Exploring Objects

## 1. Big question

How can Starflight discover behavior without knowing its name first?

## 2. What we already know

String methods return values. Calling `upper()` does not change the original string.

## 3. What we are about to discover

Find, inspect, and try an object’s public attributes. Follow the next clue in our dragon training-roster investigation.

## 4. Vocabulary

- **Attribute:** A named thing available through an object; not necessarily a method.
- **Inspection:** Asking Python for evidence about an object.
- **Callable:** An object that can be called using parentheses.
- **Public name:** Here, a name without a leading underscore, intended for ordinary use.

## 5. Guided experiments

Open [03_exploring_objects.py](03_exploring_objects.py). Its numbered output headings match the experiments below. In a demonstration, pause at each prediction comment before running the matching section. Independently, read the section first, write a prediction, then run `python3 03_exploring_objects.py` and compare. No input is required.

### Experiment 1: Starflight searches for clues

Find `dir(dragon_name)` and `[name for name in dir(dragon_name) if not name.startswith("_")]`.

- **Predict:** Will a name list explain the arguments each method needs?
- **Run:** The script shows a count, eight public names, and an upper membership check. Counts and names may vary with Python versions.
- **Explain:** The bracket expression builds a list of names that pass the condition. Read it as “keep each name that does not begin with an underscore.” It hides all leading-underscore names, including double-underscore names. They remain accessible and important; we are reducing clutter.

### Experiment 2: Find a name, retrieve its value, then try it

Find `hasattr()`, `getattr(dragon_name, "upper")`, and `callable(upper_method)`.

- **Predict:** Does retrieving upper already produce CLAY?
- **Run:** hasattr reports True for upper and False for breathe_fire. The retrieved method is callable; upper_method() returns CLAY. The string itself is not callable.
- **Explain:** Finding a name, inspecting what it does, and trying it are separate steps. getattr without a default can raise AttributeError for a missing name; this experiment retrieves a known name.

### Experiment 3: Inspect before experimenting

Find `str.upper.__doc__`, `str.replace.__doc__`, and `.replace("a", "o")`.

- **Predict:** How can documentation help choose arguments?
- **Run:** Read the short documentation and observe Cloy. Then use the shell mini-lab below.
- **Explain:** dir() is a convenient inventory, not a guarantee of every possible attribute. hasattr() tests whether attribute access succeeds, not whether a value is callable or a call will work. On more complex objects, access can run code; avoid blindly calling everything you find.

### Interactive shell mini-lab

Start `python3` in this directory. Type these lines one at a time (do not type the `>>>` prompt). Before each line, predict; afterward, explain the evidence.

```python
dragon_name = "Clay"
dir(dragon_name)
[name for name in dir(dragon_name) if not name.startswith("_")]
help(str.upper)
help(str.replace)
hasattr(dragon_name, "upper")
upper_method = getattr(dragon_name, "upper")
callable(upper_method)
upper_method()
dragon_name.replace("a", "o")
dragon_name
```

Use **q** to leave a documentation pager and return to `>>>`. If you enter the separate `help>` prompt by calling help() without an argument, type `quit` to return to Python. See the README for a no-pager alternative. Explain why the final name is still Clay.

## 6. Predict, Run, Explain questions

Before running, which output are you least certain about? After running, which exact line supports or contradicts your prediction? Explain it using the object before the dot, the operation, and its result. Keep a prediction → observation → explanation note for one experiment.

## 7. What did we discover?

dir lists names, not explanations. help and experiments supply evidence. An attribute is not necessarily callable.

## 8. Connection to the next lesson

**If these methods belong to a string, where are they defined?**

Continue with [Exploring the String Class](04_exploring_the_string_class.md).

## 9. Small student challenges

These are ungraded practice supporting the weekly programming discussion, not additional submissions. If you share code or discoveries in the course discussion, peers will see your work; use fictional dragon data.

1. Discover endswith with dir, read help(str.endswith), then try it on "Clay".
2. Retrieve lower using getattr, check callable, and call it.
3. Use getattr(dragon_name, "breathe_fire", None) and explain why supplying a default avoids a missing-name error.
