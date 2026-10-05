# Strings Are Objects: Lesson Map

**Course:** COMSC-1033 Computer Science I  
**Date started:** 2026-10-05  
**Status:** Living plan / foundation for a future Beamer presentation, code examples, and class activities

## Big idea

The lesson begins with something students already understand intuitively: **text**.

Then we pull the floorboard up.

A Python string is not just a row of characters. A string is an **object**. It has a type, a value, and a collection of behaviors that Python makes available through methods.

That makes strings a nearly perfect first doorway into object-oriented thinking because students can see the object, manipulate it, and immediately observe what its methods do.

The conceptual journey is:

> **Text -> String -> Object -> Dot notation -> Discoverable behavior -> Object thinking everywhere**

The point is not to teach full object-oriented programming yet. The point is to give students a mental model they can reuse later when they meet lists, files, modules, classes, APIs, game objects, network automation libraries, and larger software systems.

---

## Story of the day

### Act 1: Make text do something funny

Open with a **Mad Lib**.

Students provide a few words:

- a name
- an adjective
- a noun
- a place
- a verb
- something absurd

Python assembles the story.

This gives us an easy, playful reason to use:

- variables
- input
- strings
- concatenation or f-strings
- formatting
- simple string cleanup

Possible opening line:

> Today we are going to make Python say ridiculous things, and accidentally discover object-oriented programming along the way.

The Mad Lib is the hook, not the destination.

---

## Act 2: Ask a different question

Instead of asking:

> What is a string?

Ask:

> **How does a string behave?**

Example:

```python
message = "  hello computer science  "
```

What can this thing do?

```python
message.upper()
message.lower()
message.strip()
message.title()
message.replace("computer", "chaos")
message.split()
message.startswith("hello")
```

The important observation is that the operations seem to **belong to the string**.

That is the doorway.

---

## Act 3: The dot

The central symbol of the lesson is tiny:

```
.
```

A useful first mental model:

> **object.method()**

Read it conversationally as:

> "Hey object, do this thing."

Examples:

```python
name.upper()
sentence.split()
answer.strip()
filename.endswith(".txt")
```

The dot is a way of saying:

> "Look inside the world of this object and use something that belongs to it."

Later we can refine that language into attributes, methods, classes, instances, and namespaces.

For today, the goal is recognition.

---

## Act 4: So what is an object?

A beginner-friendly object model:

### An object has:

1. **A type**
   - What kind of thing is this?

2. **A value or state**
   - What information is this thing currently holding?

3. **Behavior**
   - What can this kind of thing do?

For a string:

```python
name = "Jeremy"
```

- type: `str`
- value: `"Jeremy"`
- behaviors: `.upper()`, `.lower()`, `.replace()`, `.split()`, and many more

This gives us the first reusable object question:

> **What is it, what does it know, and what can it do?**

---

## Act 5: Strings have behavior, but they are immutable

This is a useful surprise.

```python
name = "jeremy"
name.upper()

print(name)
```

The original string is still:

```
jeremy
```

Why?

Because strings are **immutable**.

The method usually returns a **new string** instead of modifying the original one.

```python
name = name.upper()
```

This is a beautiful place to introduce the idea that objects do not all behave the same way.

Different types have different rules.

---

## Act 6: How do I discover what an object can do?

This may be the most valuable habit in the entire lesson.

Students should not think programming means memorizing every method.

Instead, teach them to investigate.

### Ask Python what something is

```python
type("hello")
```

### Ask what is available

```python
dir("hello")
```

### Ask for help

```python
help(str)
help(str.replace)
```

Potential live exercise:

```python
mystery = "SWOSU Bulldogs"

print(type(mystery))
print(dir(mystery))
```

Then pick one unfamiliar method and experiment with it.

The habit we want:

> **I do not have to know everything about an object. I need to know how to interrogate it.**

That idea scales far beyond strings.

---

## Act 7: Why strings are the gateway drug to objects

Strings work beautifully for this because:

- students already understand text
- results are immediately visible
- strings have lots of useful methods
- dot notation appears naturally
- mistakes are usually low-risk
- students can experiment interactively
- strings connect input, output, files, web data, APIs, and user interfaces

The real lesson is not `.upper()`.

The real lesson is:

> **When Python gives me a thing, I should wonder what kind of object it is and what behaviors are attached to it.**

---

# The object idea outside strings

The second half of the lesson should widen the lens.

We should make the case that this way of thinking shows up everywhere.

## 1. Video games

Conceptual examples:

```
player.health
player.inventory
player.move()
player.attack()

car.speed
car.accelerate()
car.brake()

enemy.position
enemy.take_damage()
```

A game world becomes manageable when complicated things are modeled as objects with state and behavior.

---

## 2. Networks and Cisco

Important distinction:

Cisco IOS CLI itself is **not generally dot notation**.

But the same hierarchical/object mental model appears when we think about:

- devices
- interfaces
- VLANs
- routing tables
- configurations
- nested configuration contexts

And once we automate networks in Python, actual objects become common:

```python
device.connect()
interface.enable()
interface.description
connection.send_command(...)
```

Conceptually:

```
switch
    -> interfaces
        -> ethernet1/1
            -> status
            -> vlan
            -> description
```

The important connection is:

> A complicated system becomes easier to reason about when we organize related information and behaviors around the thing they belong to.

---

## 3. Organizational charts

Conceptual structure:

```
university
    .college
        .department
            .faculty
```

Or:

```
company.sales.manager
company.it.helpdesk
company.hr.policies
```

This is not Python code. It is a way to show that humans naturally organize complicated systems into **things inside things**, with responsibilities attached to them.

---

## 4. Policy and procedure

A policy system can also be understood hierarchically:

```
university
    .technology
        .security
            .password_policy
            .acceptable_use
            .incident_response
```

Again, not literal Python.

The useful mental model is that we create names, containers, relationships, and responsibilities so that a giant system can be navigated without holding the whole thing in our head at once.

---

## 5. Software libraries and APIs

Eventually students will see code such as:

```python
requests.get(...)
response.json()

path.exists()
path.read_text()

player.inventory.add(...)
database.connect(...)
```

The lesson today gives them a way to approach unfamiliar code without panic:

1. What object am I looking at?
2. What type is it?
3. What does it contain?
4. What methods are available?
5. What does this method return?

---

# Possible classroom activities

## Activity A: Mad Lib

Students collect input and assemble a ridiculous story.

Version 1 can use plain variables and f-strings.

Version 2 can require string methods:

```python
name = input("Name: ").strip().title()
place = input("Place: ").strip().title()
verb = input("Verb: ").strip().lower()
```

The point is to make the transformation visible.

---

## Activity B: String Method Petting Zoo

Give students one string:

```python
text = "  The Bulldogs Have Escaped Again!  "
```

Ask them to experiment with:

- `.strip()`
- `.lower()`
- `.upper()`
- `.title()`
- `.replace()`
- `.split()`
- `.count()`
- `.find()`
- `.startswith()`
- `.endswith()`

For each method:

1. Predict what it will do.
2. Run it.
3. Describe what came back.
4. Decide whether the original string changed.

---

## Activity C: Object Detective

Give students unfamiliar objects later in the course.

Their investigation protocol:

```python
type(thing)
dir(thing)
help(...)
```

Questions:

- What type is it?
- Name three methods it has.
- Pick one method and test it.
- What does the method return?
- Does it modify the object or return something new?

This can become a repeating course ritual.

---

## Activity D: Design a game object without coding it

Example prompt:

> We are building the world's least sensible video game. Pick one object in the game.

Students define:

```
Object: Goose

State:
- name
- health
- anger_level
- location
- stolen_items

Behavior:
- honk()
- chase()
- steal()
- flee()
```

Then connect that conceptual object back to the string they used earlier.

A string is less dramatic than an angry goose, but the organizing idea is the same.

---

# Candidate slide arc

The eventual Beamer deck could follow this sequence:

1. **Strings Are Weirdly Powerful**
2. Mad Lib opener
3. What is a string?
4. Better question: how does a string behave?
5. The dot
6. `object.method()`
7. String method demonstrations
8. What makes something an object?
9. Type + state + behavior
10. Strings are immutable
11. You are not supposed to memorize everything
12. `type()`, `dir()`, `help()`
13. Object Detective mini-lab
14. Objects in games
15. Objects in networks
16. Objects in organizations
17. Objects in policies and systems
18. Why object thinking scales
19. Return to the Mad Lib
20. Exit question: "What object are you holding, and what can it do?"

---

# Instructor through-line

Possible recurring phrase:

> **What is this thing, and what can it do?**

That question can follow students through the rest of CS1.

When they meet a list:

> What is this thing, and what can it do?

When they meet a file:

> What is this thing, and what can it do?

When they meet a module:

> What is this thing, and what can it do?

When they eventually create their own classes:

> Now we get to decide what the thing knows and what the thing can do.

That turns today's string lesson into groundwork for later object-oriented programming instead of an isolated chapter on text manipulation.

---

# Build plan

Do **not** try to build everything at once.

Suggested small bites:

### Bite 1: Foundation
- this lesson map
- settle the core story and language

### Bite 2: Mad Lib
- one polished Python Mad Lib
- intentionally demonstrate `.strip()`, `.title()`, etc.

### Bite 3: String laboratory
- small runnable Python demo
- method experiments
- immutability demonstration
- `type()`, `dir()`, and `help()`

### Bite 4: Beamer deck
- build the slide deck from the arc above
- favor live coding and visual diagrams over dense text

### Bite 5: Object Detective activity
- student-facing exercise
- ideally structured as a shared graded discussion consistent with the course design rules

### Bite 6: Cross-domain examples
- Cisco/networking
- video games
- organizational systems
- policy/procedure
- APIs and libraries

### Bite 7: Polish
- speaker notes
- timing
- transitions
- optional challenge material

---

# What success looks like

By the end of the lesson, a student should be able to say:

> A string is an object of type `str`. It has methods that I can access with dot notation. I do not have to memorize every method because I can investigate an object and learn what it can do. The same way of thinking will show up again in more complicated programs and systems.

That is the destination.

The Mad Lib is simply how we sneak through the side door.
