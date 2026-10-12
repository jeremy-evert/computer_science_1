# Lesson 02: Objects Have Behavior

## 1. Big question

If Clay is an object, what can Clay do?

## 2. What we already know

`dragon_name` refers to a string object whose class is `str`.

## 3. What we are about to discover

Use string behavior and separate returned values from changes to data. Follow the next clue in our dragon training-roster investigation.

## 4. Vocabulary

- **Method:** A function accessed through an object, such as dragon_name.upper.
- **Return value:** The result a call gives back to the surrounding code.
- **Immutable:** Unable to have its existing contents changed.
- **Reassignment:** Making an existing variable refer to the value on the right of =.

## 5. Guided experiments

Open [02_objects_have_behavior.py](02_objects_have_behavior.py). Its numbered output headings match the experiments below. In a demonstration, pause at each prediction comment before running the matching section. Independently, read the section first, write a prediction, then run `python3 02_objects_have_behavior.py` and compare. No input is required.

### Experiment 1: Sunny tries a loud announcement

Find `dragon_name.upper()`, `.lower()`, and `.replace("Clay", "Sunny")`.

- **Predict:** Will printing the upper() result make the original name uppercase?
- **Run:** The results are CLAY, clay, and Sunny; the original remains Clay.
- **Explain:** A method call can return a value without changing the object or reassigning its variable. `object.method(arguments)` accesses behavior through the object. Empty parentheses still call the method.

### Experiment 2: Questions about the roster entry

Find `.startswith("C")`, `.count("a")`, and `len(dragon_name)`.

- **Predict:** Which results will be text, a Boolean, or a number?
- **Run:** The outputs are True, 1, and 4.
- **Explain:** Not every method returns a string. len() is a function called with the object as an argument; upper() is a method accessed with a dot.

### Experiment 3: Keep the old name, then reassign

Find `original_name = dragon_name` followed by `dragon_name = dragon_name.upper()`.

- **Predict:** Will original_name now show CLAY?
- **Run:** dragon_name shows CLAY; original_name still shows Clay.
- **Explain:** Strings are immutable. Reassignment makes dragon_name refer to the returned string; it does not change the original string's contents.

## 6. Predict, Run, Explain questions

Before running, which output are you least certain about? After running, which exact line supports or contradicts your prediction? Explain it using the object before the dot, the operation, and its result. Keep a prediction → observation → explanation note for one experiment.

## 7. What did we discover?

Methods are accessed through objects. A returned value does not reassign a variable. Strings are immutable; reassignment changes a reference.

## 8. Connection to the next lesson

**How do we discover methods without somebody telling us their names?**

Continue with [Exploring Objects](03_exploring_objects.md).

## 9. Small student challenges

These are ungraded practice supporting the weekly programming discussion, not additional submissions. If you share code or discoveries in the course discussion, peers will see your work; use fictional dragon data.

1. Try replace("a", "aa") and predict both the result and the original name.
2. Save dragon_name.lower() in a new variable and print both variables.
3. Predict startswith("c") versus startswith("C"); run both to investigate case sensitivity.
