# Week 9: Objects You Use, Classes You Write

Last week, you practiced with strings. A string is more than text sitting in
memory: it is an object with a type, a value, and methods. Lists work the same
way. This week, you will use those objects on purpose and write a small class
of your own.

## Objects have state and behavior

An object's state is the information it currently holds. Its behavior is what
it can do. For a string, the characters are its value and methods such as
`.strip()` and `.title()` provide behavior.

Dot notation accesses an attribute. A data attribute stores information; a
method is callable, and parentheses call it: `object.method()`. Without
parentheses, `object.attribute` reads the stored information.

Run this small example. The original string keeps its spaces. Strings are immutable; transformation
methods such as `.strip()` and `.title()` return new strings instead of
changing the original.

```python
label = "  moon station  "
print(label.strip().title())
print(repr(label))
```
<!-- expected-output
Moon Station
'  moon station  '
-->

The list below behaves differently. `.append()` changes the list itself. The
list's state has one more item after the method call.

```python
signals = ["ping", "ping"]
signals.append("reply")
print(signals)
print(signals.count("ping"))
```
<!-- expected-output
['ping', 'ping', 'reply']
2
-->

## A class is a blueprint

A class describes how to make a kind of object. An instance is one object made
from that class. For example, a `Rover` class can describe what every rover
needs to know and what every rover can report.

The special method `__init__` runs when a new instance is created. `self` means
“this particular rover.” The two assignments below store state on that rover.
The reporting method reads the same state later.

```python
class Rover:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def status(self):
        return f"{self.name} has {self.battery}% battery."


scout = Rover("Scout", 80)
print(scout.name)
print(scout.battery)
print(scout.status())
```
<!-- expected-output
Scout
80
Scout has 80% battery.
-->

For now, keep your classes small: use `__init__`, a few instance attributes,
and one useful method. You do not need inheritance, modules, class variables,
or objects working together yet.

### Try it

Before you run the examples, predict which lines show a returned value and
which line shows changed list state. Then make a tiny class with a name and one
number. Explain what each `self` means as you read the class.

The practice here is ungraded. Use conversation with peers to compare
predictions and explanations, then bring questions to class.
