# Lesson 05: Building a Dragon Class

## 1. Big question

Can we define a kind of object for our dragon training roster?

## 2. What we already know

A string instance uses behavior supplied by the built-in `str` class.

## 3. What we are about to discover

Define a small class and initialize one Dragon instance. Follow the next clue in our dragon training-roster investigation.

## 4. Vocabulary

- **Initialization:** Giving a newly created instance its starting data.
- **self:** The conventional parameter name referring to the instance receiving a method call.
- **Data attribute:** Data stored under a name on an object, such as clay.tribe.
- **Class definition:** The class block describing the data setup and behavior of a kind of object.

## 5. Guided experiments

Open [05_building_a_dragon_class.py](05_building_a_dragon_class.py). Its numbered output headings match the experiments below. In a demonstration, pause at each prediction comment before running the matching section. Independently, read the section first, write a prediction, then run `python3 05_building_a_dragon_class.py` and compare. No input is required.

### Experiment 1: Build one roster member

Find `class Dragon:`, its docstring, `__init__(self, name, tribe)`, and `clay = Dragon("Clay", "MudWing")`.

- **Predict:** Does the class definition itself create Clay?
- **Run:** The call creates Clay; clay.name is Clay and clay.tribe is MudWing.
- **Explain:** The class block is the definition. Calling Dragon(...) creates an instance and invokes __init__ to initialize it. __init__ does not return the new instance. self refers to that instance; self.name and self.tribe store its data. The name argument and the name attribute are distinct roles.

### Experiment 2: Give our object behavior

Find `message = clay.introduce()` and `print(message)`.

- **Predict:** Does introduce() print or return?
- **Run:** The returned message is “Hello! I am Clay, a MudWing.” print displays it.
- **Explain:** introduce is a method; name and tribe are data attributes. In clay.introduce(), Python supplies clay as self. We do not pass clay a second time.

### Experiment 3: Connect our discovery to strings

Find `"Clay".upper()` and `clay.introduce()`.

- **Predict:** What is the object before the dot in each call?
- **Run:** Both calls return strings, but their objects are different kinds.
- **Explain:** The first object is a string instance; the second is a Dragon instance. Each call accesses behavior supplied by its class. Our class is a complete local definition; this script imports no earlier lesson.

## 6. Predict, Run, Explain questions

Before running, which output are you least certain about? After running, which exact line supports or contradicts your prediction? Explain it using the object before the dot, the operation, and its result. Keep a prediction → observation → explanation note for one experiment.

## 7. What did we discover?

A class defines a kind of object. __init__ initializes an instance. self refers to the instance receiving the method call.

## 8. Connection to the next lesson

**Now that we have a Dragon class, can we create different dragons?**

Continue with [Creating Dragon Objects](06_creating_dragon_objects.md).

## 9. Small student challenges

These are ungraded practice supporting the weekly programming discussion, not additional submissions. If you share code or discoveries in the course discussion, peers will see your work; use fictional dragon data.

1. Create Sunny as a SandWing using this same class, then call introduce().
2. Change the greeting returned by introduce() and predict how its output changes.
