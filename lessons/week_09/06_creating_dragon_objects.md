# Lesson 06: Creating Dragon Objects

## 1. Big question

Can dragons share behavior while keeping their own data?

## 2. What we already know

`Dragon` defines a kind of object. `__init__` stores data on one instance.

## 3. What we are about to discover

Compare independent instance data with shared class behavior. Follow the next clue in our dragon training-roster investigation.

## 4. Vocabulary

- **State:** The current data stored on an object.
- **Mutable:** Able to change its state after creation.

## 5. Guided experiments

Open [06_creating_dragon_objects.py](06_creating_dragon_objects.py). Its numbered output headings match the experiments below. In a demonstration, pause at each prediction comment before running the matching section. Independently, read the section first, write a prediction, then run `python3 06_creating_dragon_objects.py` and compare. No input is required.

### Experiment 1: Three dragons join the roster

Find the clay, tsunami, and glory constructor calls and their introduce() calls.

- **Predict:** Can one method definition introduce three different dragons?
- **Run:** Clay is a MudWing, Tsunami a SeaWing, and Glory a RainWing.
- **Explain:** Each call initializes an instance with its own attributes. The shared method reads data from the instance supplied as self.

### Experiment 2: Same kind, different objects

Find `type()`, `isinstance()`, and the `id()` comparison.

- **Predict:** Will the classes match? Will the identities match?
- **Run:** The class checks are True; same identity is False. The numerical identities vary between runs.
- **Explain:** Distinct objects alive at the same time have different identities. The same class does not mean the same object.

### Experiment 3: Clay practices; Tsunami watches

Find `self.energy = 3`, `train()`, and the before/after prints.

- **Predict:** Will training Clay reduce Tsunami's energy too?
- **Run:** Clay changes from 3 to 2; Tsunami stays at 3. train() also returns 2.
- **Explain:** train() both changes state and returns a value. It assigns a new integer to Clay's energy attribute; it does not mutate the integer. Each instance has its own attribute. The energy rule is an original classroom scenario.

### Experiment 4: Mutable dragon, immutable string

Find `clay.name.upper()` and the following name print.

- **Predict:** Does a mutable Dragon make its name string mutable?
- **Run:** The result is CLAY; clay.name remains Clay.
- **Explain:** The Dragon can change its attributes. The string object stored in name still cannot change its existing contents. `clay.name = clay.name.upper()` would change the Dragon's attribute by assignment.

## 6. Predict, Run, Explain questions

Before running, which output are you least certain about? After running, which exact line supports or contradicts your prediction? Explain it using the object before the dot, the operation, and its result. Keep a prediction → observation → explanation note for one experiment.

## 7. What did we discover?

Each instance stores its own data. Instances share methods defined by their class. Dragon state can change while string contents cannot.

## 8. Connection to the next lesson

**How can another programmer discover what our Dragon objects can do?**

Continue with [Making Objects Discoverable](07_making_objects_discoverable.md).

## 9. Small student challenges

These are ungraded practice supporting the weekly programming discussion, not additional submissions. If you share code or discoveries in the course discussion, peers will see your work; use fictional dragon data.

1. Create Starflight as a NightWing and show that his starting energy is independent.
2. Call clay.train() four times and show why energy stops at zero.
3. Add an alias with partner = clay. Train partner, then inspect clay.energy: explain why two variables can refer to one object.
