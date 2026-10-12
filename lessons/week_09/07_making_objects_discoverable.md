# Lesson 07: Making Objects Discoverable

## 1. Big question

How can Sunny explore our Dragon objects without a private explanation?

## 2. What we already know

Dragon instances have independent data, shared methods, and mutable state.

## 3. What we are about to discover

Make Dragon objects easy for another programmer to explore. Follow the next clue in our dragon training-roster investigation.

## 4. Vocabulary

- **Docstring:** A string at the beginning of a module, class, or function that documents it.
- **Type hint:** An annotation describing an intended type, not an automatic runtime check.
- **Representation:** Text describing an object.
- **Discoverability:** How easily another programmer can find and understand useful behavior.

## 5. Guided experiments

Open [07_making_objects_discoverable.py](07_making_objects_discoverable.py). Its numbered output headings match the experiments below. In a demonstration, pause at each prediction comment before running the matching section. Independently, read the section first, write a prediction, then run `python3 07_making_objects_discoverable.py` and compare. No input is required.

### Experiment 1: Give the roster a readable voice

Find `__str__()`, `__repr__()`, `print(clay)`, and `repr(clay)`.

- **Predict:** Which representation would help a roster reader? Which helps a programmer?
- **Run:** print shows Clay the MudWing (energy: 3). repr shows the class name and labeled current data.
- **Explain:** print uses __str__ for readable text; repr uses __repr__ for developer-oriented text. Both return strings. The !r inside an f-string requests repr of that field, so string fields show quotes. Our repr is informative, not a promised executable constructor expression.

### Experiment 2: Starflight writes a discovery note for Sunny

Find `dir(clay)`, the public_names and public_methods filters, `hasattr()`, `getattr()`, and `callable()`.

- **Predict:** Are energy, name, and tribe methods?
- **Run:** The public method list contains introduce and train. energy exists but is not callable. Retrieving introduce and then calling it gives the greeting.
- **Explain:** Public attributes include data and methods. callable tells whether parentheses can call a value, not what arguments it needs or whether calling it is wise. This filter is suitable for our simple class; arbitrary attribute access may run code on other classes.

### Experiment 3: Leave useful documentation

Find the class, __init__, and method docstrings; `name: str`, `tribe: str`, `-> str`, and `-> int`.

- **Predict:** What can help explain that dir cannot?
- **Run:** Read the printed documentation excerpts, then run help(Dragon) and help(Dragon.introduce) interactively.
- **Explain:** Docstrings explain purpose, effects, and returned values. Type hints describe intended types but do not enforce them here. The tools we used on str now work on Dragon. Clear names and documentation make discovery part of software design.

### Inspect your own class interactively

Run `python3 -i 07_making_objects_discoverable.py`. After the script finishes, its names remain available at `>>>`. Type:

```python
help(Dragon)
help(Dragon.__init__)
help(Dragon.introduce)
dir(clay)
getattr(clay, "train")
```

Read before calling train: inspection retrieves the method; `clay.train()` changes state. Press **q** to leave a pager. Compare this experience with help(str) from lesson 04. The special names __str__ and __repr__ are no longer mysterious clutter: they customize how our objects become text.

## 6. Predict, Run, Explain questions

Before running, which output are you least certain about? After running, which exact line supports or contradicts your prediction? Explain it using the object before the dot, the operation, and its result. Keep a prediction → observation → explanation note for one experiment.

## 7. What did we discover?

Docstrings explain the interface. __str__ supplies readable text and __repr__ developer text. Discoverable objects use clear names and documented behavior.

## 8. Connection to the next lesson

**From a string object to our own objects: what will you build next?**

Return to the overarching question: a string is an object we can inspect, and a Dragon is an object whose interface we can design. Use the same discovery cycle on the next class you build.

## 9. Small student challenges

These are ungraded practice supporting the weekly programming discussion, not additional submissions. If you share code or discoveries in the course discussion, peers will see your work; use fictional dragon data.

1. Train Clay once, then compare print(clay) and repr(clay) again.
2. Improve the train docstring with an example of its return value at zero energy.
3. Add a documented rest() method that restores energy to 3, then discover it with dir, help, and a small call.
