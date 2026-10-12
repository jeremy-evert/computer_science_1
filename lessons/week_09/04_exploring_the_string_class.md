# Lesson 04: Exploring the String Class

## 1. Big question

Where does the behavior of a string instance come from?

## 2. What we already know

`dir()` finds names; `help()` explains them; a small call tests behavior.

## 3. What we are about to discover

Connect a string instance to the built-in str class. Follow the next clue in our dragon training-roster investigation.

## 4. Vocabulary

- **Instance:** An object of a particular class.
- **Shared behavior:** Behavior supplied by a class for its instances.
- **Interface:** The names and behavior we can use to interact with an object.
- **Built-in:** Available directly in Python without defining or importing it ourselves.

## 5. Guided experiments

Open [04_exploring_the_string_class.py](04_exploring_the_string_class.py). Its numbered output headings match the experiments below. In a demonstration, pause at each prediction comment before running the matching section. Independently, read the section first, write a prediction, then run `python3 04_exploring_the_string_class.py` and compare. No input is required.

### Experiment 1: Glory examines the class behind her name

Find `str`, `type("Glory")`, `isinstance("Glory", str)`, `dir(str)`, and `str.upper`.

- **Predict:** Will upper appear on the class as well as on a string?
- **Run:** The class is str, isinstance returns True, and upper is listed on str.
- **Explain:** A class defines a kind of object. A string is an instance of str. An attribute is a named thing available through an object or class; methods are callable behavior, but not all attributes are methods.

### Experiment 2: Two routes to string behavior

Find `str.upper("Glory")` and `"Glory".upper()`.

- **Predict:** Will the two forms return identical text?
- **Run:** Both return GLORY; the same behavior also works for Clay.
- **Explain:** For this method, the class form receives the string explicitly. The instance form supplies the string through the object before the dot. This example connects class and instance; it is not a universal rule about every Python method.

### Experiment 3: Inspect the public interface

Find `dir(str)` and `str.__doc__`.

- **Predict:** Does knowing names reveal how Python implements strings?
- **Run:** Inspect the small sample in the script, then type help(str) in the shell.
- **Explain:** str is a built-in class. We are examining its public interface and documentation, not reading or recreating its implementation. The class supplies behavior shared by its string instances.

### See the full class interactively

In `python3`, type `str`, `dir(str)`, `str.upper`, and `help(str)` one at a time. The script intentionally shows only a sample and a documentation excerpt. The shell gives you the full inventory and documentation when you want them. Press **q** to leave a pager.

## 6. Predict, Run, Explain questions

Before running, which output are you least certain about? After running, which exact line supports or contradicts your prediction? Explain it using the object before the dot, the operation, and its result. Keep a prediction → observation → explanation note for one experiment.

## 7. What did we discover?

An instance has a class. A class supplies shared behavior. The public interface is not the implementation.

## 8. Connection to the next lesson

**If Python has a class for strings, can we make a class for dragons?**

Continue with [Building a Dragon Class](05_building_a_dragon_class.md).

## 9. Small student challenges

These are ungraded practice supporting the weekly programming discussion, not additional submissions. If you share code or discoveries in the course discussion, peers will see your work; use fictional dragon data.

1. Compare str.lower("Tsunami") with "Tsunami".lower().
2. Find count on str, read help(str.count), and test it on "Sunny".
