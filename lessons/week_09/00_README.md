# Wings of Fire: discovering Python objects

**If a string is an object, can we discover how it works and then build objects of our own?**

Our central learning objective is to use evidence from familiar strings to explain classes, instances, attributes, methods, identity, and changing state, then build and document a small Dragon class. Start with behavior, predict, run, examine evidence, explain, and follow the next question.

These original classroom scenes are inspired by *Wings of Fire* by Tui T. Sutherland. Clay is a MudWing, Tsunami a SeaWing, Glory a RainWing, Starflight a NightWing, and Sunny a SandWing (she also has NightWing ancestry). Training energy and all dialogue are invented for this lab; no book passages are quoted. You do not need to have read the books.

Students should already know variables, strings, functions, print(), basic conditionals, and simple syntax. Each script is complete and independent, with no imports from another lesson, required user input, packages, or external services. Python 3 and its standard library are sufficient. Markdown guides support a projected demonstration or individual exploration.

This sequence is **ungraded supporting practice** for the week's single graded programming discussion. Follow the existing Canvas discussion prompt for the graded deliverable; these seven guides do not add seven deadlines. Peers will see work shared in that discussion. Use fictional dragon information and avoid personal details.

## Numbered lesson roadmap

1. [Strings are objects](01_strings_are_objects.md): Clay's name has a type and an identity.
2. [Objects have behavior](02_objects_have_behavior.md): methods return results; strings remain immutable.
3. [Exploring objects](03_exploring_objects.md): Starflight finds names, reads documentation, and tries behavior.
4. [Exploring the string class](04_exploring_the_string_class.md): Glory connects instances to str.
5. [Building a Dragon class](05_building_a_dragon_class.md): define and initialize one roster member.
6. [Creating Dragon objects](06_creating_dragon_objects.md): compare three instances and change Clay's energy.
7. [Making objects discoverable](07_making_objects_discoverable.md): give Sunny useful names, documentation, and representations.

## Run the scripts

Open a terminal in this directory:

```bash
cd ~/git/computer_science_1/lessons/week_09
python3 01_strings_are_objects.py
python3 02_objects_have_behavior.py
python3 03_exploring_objects.py
python3 04_exploring_the_string_class.py
python3 05_building_a_dragon_class.py
python3 06_creating_dragon_objects.py
python3 07_making_objects_discoverable.py
```

Run one command at a time. All scripts print labeled experiments and finish on their own. The numerical identities and some inspection details depend on the Python version and run; compare relationships rather than memorizing output. Running later scripts does not require running earlier ones first, although the ideas build in order.

## Use the interactive interpreter

Run `python3` to see the `>>>` prompt. Type expressions such as:

```python
dragon_name = "Clay"
type(dragon_name)
dragon_name.upper()
dragon_name
```

The shell displays expression results automatically; a script normally needs print(). Assignment itself does not display a result. Do not type the prompt characters. Use `exit()` or Ctrl-D to leave Python. To retain a script's class and objects for exploration, run:

```bash
python3 -i 07_making_objects_discoverable.py
```

You can then type `clay`, `repr(clay)`, `dir(clay)`, or `help(Dragon)`. The `-i` option is for optional exploration; the ordinary script command never requires input.

## Use help without getting stuck

At `>>>`, try `help(str.upper)` or `help(str.replace)`. For complete inventories and longer documentation, try `dir(str)`, `help(str)`, `dir(clay)`, and `help(Dragon)` in the appropriate shell. Normal scripts show short samples or documentation excerpts instead of huge dumps.

If documentation opens a pager, use Space for the next page and **q** to return to Python. If you call `help()` with no argument and see `help>`, type `quit` to leave that help session. This is distinct from exiting Python.

For documentation without any pager, type this optional standard-library alternative in Python:

```python
import pydoc
print(pydoc.render_doc(str.upper, renderer=pydoc.plaintext))
```

Replace str.upper with str or Dragon when you want longer documentation. This prints to the terminal, where you can scroll normally.

## Suggested teaching order and conceptual map

Teach 01 through 07 in order. Keep each prediction visible before revealing the output. Let students describe evidence before introducing the vocabulary. Use the guides' challenges as practice, not new graded gates.

```text
String object
    -> behavior and methods
    -> inspection tools
    -> str class
    -> our Dragon class
    -> Dragon instances
    -> discoverable software
```

The memorable bridge is `"Clay".upper()` → `clay.introduce()`: an object before the dot, behavior supplied by its class, and a returned value. The original string cannot change its contents; our Dragon can change its energy attribute. A method may return a value, change state, both, or neither—inspect its documentation and test deliberately.

## Recommended 30-minute instructor demonstration

| Minutes | Focus | Evidence to pause over |
| --- | --- | --- |
| 0–4 | 01 | Predict type checks; compare two id calls without memorizing the number. |
| 4–9 | 02 | Print upper's result and the original; contrast reassignment with mutation. |
| 9–13 | 03 | Find upper, retrieve it, test callable, then call it; use help(str.upper) in the shell. |
| 13–17 | 04 | Compare str.upper("Glory") and "Glory".upper(); name class and instance. |
| 17–22 | 05 | Read the short Dragon definition; trace self.name; call introduce. |
| 22–26 | 06 | Predict whether Clay's training changes Tsunami; inspect before and after. |
| 26–30 | 07 | Compare print/repr; identify data versus methods; open help(Dragon.introduce). |

Pause for one prediction per row. Save the full help(str) and help(Dragon) tours and additional challenges for the longer lab.

## Longer student laboratory path

Allow approximately 90–120 minutes, or split across two meetings:

1. Spend 20 minutes on 01–02: record predictions, run both scripts, and try a reassignment challenge.
2. Spend 20–25 minutes on 03–04: complete the interactive mini-lab, inspect help(str), and compare class/instance call forms.
3. Spend 25–30 minutes on 05–06: create a fourth dragon, trace independent attributes, train to zero, and investigate an alias.
4. Spend 20–25 minutes on 07: inspect the class interactively, compare representations before/after training, and add a documented rest method.
5. Use remaining time to compare explanations with a partner. When sharing through the weekly graded discussion, follow its existing programming prompt and remember peers can see your work.

For each major experiment, keep three short notes: prediction, observed output, and explanation. Edit a copy or save your changes deliberately so you can compare the original example with your experiment. The aim is evidence-based understanding, not memorizing method names.
