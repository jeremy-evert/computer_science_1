# Lesson 01: Strings Are Objects

## 1. Big question

What is Python holding when we write `dragon_name = "Clay"`?

## 2. What we already know

We can assign a string to a variable and display it with `print()`.

## 3. What we are about to discover

Discover the object behind a familiar string variable. Our original classroom story follows Clay, Tsunami, Glory, Starflight, and Sunny as they investigate a training roster.

## 4. Vocabulary

- **Object:** A value Python can work with, such as the string "Clay".
- **Reference:** A connection from a variable to an object.
- **Class:** A definition of a kind of object; str is the string class.
- **Identity:** What distinguishes a particular object during its lifetime.

## 5. Guided experiments

Open [01_strings_are_objects.py](01_strings_are_objects.py). Its numbered output headings match the experiments below. In a demonstration, pause at each prediction comment before running the matching section. Independently, read the section first, write a prediction, then run `python3 01_strings_are_objects.py` and compare. No input is required.

### Experiment 1: A name on the training roster

Find `dragon_name = "Clay"`, `print(dragon_name)`, `type(dragon_name)`, `type("Clay")`, and `isinstance(dragon_name, str)`.

- **Predict:** Will the variable and literal have different types?
- **Run:** Both types display `<class 'str'>`; the same-type and isinstance checks are True.
- **Explain:** The literal is a string object. The variable refers to it. `str` is its class, and type() tells us the kind of object.

### Experiment 2: Identity during an object's lifetime

Find `id(dragon_name)` twice.

- **Predict:** Will the number change between these two calls?
- **Run:** The two numbers match in this run. Your number may differ from a classmate's or on another run.
- **Explain:** id() identifies an object while it lives. Do not memorize the number; an identity may be reused after an object is gone. Matching types alone do not imply matching identities.

## 6. Predict, Run, Explain questions

Before running, which output are you least certain about? After running, which exact line supports or contradicts your prediction? Explain it using the object before the dot, the operation, and its result. Keep a prediction → observation → explanation note for one experiment.

## 7. What did we discover?

A variable refers to an object. str is the class of string objects. id identifies an object during its lifetime.

## 8. Connection to the next lesson

**If Clay is an object, what can Clay do?**

Continue with [Objects Have Behavior](02_objects_have_behavior.md).

## 9. Small student challenges

These are ungraded practice supporting the weekly programming discussion, not additional submissions. If you share code or discoveries in the course discussion, peers will see your work; use fictional dragon data.

1. Change the roster string to "Sunny" and predict which outputs change before running.
2. Compare type("Clay") and type(42). Explain what the evidence says about types.
