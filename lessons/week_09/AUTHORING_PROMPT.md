# Original lab authoring request

The following is the original user request, preserved for future review and revision.

---

You are creating a beginner-friendly, discovery-based Python teaching laboratory for Computer Science 1.

WORKING DIRECTORY:
~/git/computer_science_1/lessons/week_09

THEME:
Wings of Fire, the dragon fantasy book series by Tui T. Sutherland.

Use familiar characters such as Clay, Tsunami, Glory, Starflight, and Sunny. Use accurate, simple character details where confident. Invent original classroom scenarios and dialogue rather than quoting copyrighted book passages.

MISSION:
Create seven numbered, executable Python scripts with seven corresponding Markdown learning guides and a README.

Our overarching question is:

"If a string is an object, can we discover how it works and then build objects of our own?"

The entire sequence should tell one connected educational story.

COURSE LEVEL:
Introductory Python, CS1.

Students already know variables, strings, functions, print(), basic conditionals, and simple Python syntax. They have not yet developed a strong mental model of classes and objects.

TEACHING PHILOSOPHY:

1. Show the behavior before introducing the terminology.
2. Start with something familiar, such as a string containing "Clay".
3. Let students predict what Python will do.
4. Run an experiment.
5. Examine the evidence.
6. Explain the underlying idea in plain English.
7. Connect the discovery to the next experiment.
8. Use short code examples with clear output.
9. Avoid introducing too many new concepts simultaneously.
10. Favor curiosity and exploration over memorization.

CREATE THESE FILES:

00_README.md

01_strings_are_objects.py
01_strings_are_objects.md

02_objects_have_behavior.py
02_objects_have_behavior.md

03_exploring_objects.py
03_exploring_objects.md

04_exploring_the_string_class.py
04_exploring_the_string_class.md

05_building_a_dragon_class.py
05_building_a_dragon_class.md

06_creating_dragon_objects.py
06_creating_dragon_objects.md

07_making_objects_discoverable.py
07_making_objects_discoverable.md

Use exactly these filenames unless there is a compelling technical reason to change them.

LESSON REQUIREMENTS:

01: STRINGS ARE OBJECTS

Start with:

dragon_name = "Clay"

Explore:
- print(dragon_name)
- type(dragon_name)
- isinstance(dragon_name, str)
- id(dragon_name)
- type("Clay") versus type(dragon_name)

Explain:
- "Clay" is a string object.
- dragon_name is a variable referring to that object.
- str is its class.
- Objects have types.
- Python can tell us what kind of object we have.

Explain that id() identifies an object during its lifetime, not that students should expect a particular numerical value.

Finish with the question:
"If Clay is an object, what can Clay do?"

02: OBJECTS HAVE BEHAVIOR

Explore:
- dragon_name.upper()
- dragon_name.lower()
- dragon_name.replace()
- dragon_name.startswith()
- dragon_name.count()
- len(dragon_name)

Introduce dot notation:
object.method(arguments)

Discuss:
- Methods are functions accessed through objects.
- Calling a method may return a value.
- A returned value does not automatically replace the original variable.
- Strings are immutable.
- Reassignment versus modifying an object.

Include experiments showing that calling upper() does not change the original string.

Distinguish functions such as len() from methods such as upper().

Finish with:
"How do we discover methods without somebody telling us their names?"

03: EXPLORING OBJECTS

Explore:
- dir(dragon_name)
- help(str.upper)
- help(str.replace)
- callable()
- getattr()
- hasattr()

Introduce the difference between:
- Finding a name
- Inspecting what it does
- Trying it on an object

Show an easy way to filter the result of dir() to hide double-underscore names temporarily:

[name for name in dir(dragon_name) if not name.startswith("_")]

Explain that these hidden names are not unimportant or inaccessible. We are simply reducing the clutter for beginners.

Explain the limitations of dir() and hasattr() and why help() and experiments remain useful.

Include an interactive Python shell mini-lab where students type expressions themselves.

Finish with:
"If these methods belong to a string, where are they defined?"

04: EXPLORING THE STRING CLASS

Explore:
- str
- type("Glory")
- isinstance("Glory", str)
- dir(str)
- str.upper
- help(str)
- str.upper("Glory")
- "Glory".upper()

Show the connection between a string instance and its class.

Explain in beginner-friendly language:
- Class
- Instance
- Attribute
- Method
- Shared behavior

Use str.upper("Glory") versus "Glory".upper() to help students see the connection without overclaiming that all Python methods behave identically.

Explain that str is a built-in class and we are examining its public interface, not reading or recreating its implementation.

Finish with:
"If Python has a class for strings, can we make a class for dragons?"

05: BUILDING A DRAGON CLASS

Create a small Dragon class.

Include:
- class Dragon:
- a class docstring
- __init__()
- self
- name
- tribe
- one simple method such as introduce()

Start with one dragon and avoid unnecessary abstraction.

Clearly distinguish:
- The class as a definition
- __init__ as initialization
- self as a reference to the instance
- Attributes as data stored on the object
- Methods as behavior

Show the relationship between:

"Clay".upper()

and:

clay.introduce()

Do not introduce inheritance, decorators, dataclasses, properties, or advanced class mechanics.

Finish with:
"Now that we have a Dragon class, can we create different dragons?"

06: CREATING DRAGON OBJECTS

Extend the Dragon example with multiple instances:

clay = Dragon("Clay", "MudWing")
tsunami = Dragon("Tsunami", "SeaWing")
glory = Dragon("Glory", "RainWing")

Explore:
- Creating multiple instances
- Calling methods on each instance
- Accessing attributes with dot notation
- Each object having its own data
- Shared methods defined by the class
- isinstance()
- type()
- id() comparisons

Add one method that changes an instance's state, such as training_level or energy, so students can compare mutable Dragon instances to immutable strings.

Make the state change obvious and well explained.

Include an experiment showing that changing Clay's energy does not change Tsunami's energy.

Finish with:
"How can another programmer discover what our Dragon objects can do?"

07: MAKING OBJECTS DISCOVERABLE

Return to our exploration tools:

- dir()
- help()
- getattr()
- hasattr()
- callable()

Enhance the Dragon class with:
- A meaningful class docstring
- An __init__ docstring
- Method docstrings
- Clear names
- Simple type hints where beneficial
- __str__()
- __repr__()

Demonstrate:
- print(clay)
- repr(clay)
- help(Dragon)
- help(Dragon.introduce)
- dir(clay)
- discovery of public methods

Explain:
- __str__ is for a readable string representation.
- __repr__ is for a useful developer-oriented representation.
- Docstrings help other programmers explore code.
- Discoverability is part of good software design.

Explicitly connect this back to exploring the built-in str class.

IMPORTANT DESIGN CHOICE:
Each Python file must run independently with:

python3 01_strings_are_objects.py

through:

python3 07_making_objects_discoverable.py

Do not make later scripts depend on classes defined in earlier scripts.

It is acceptable to progressively redefine the Dragon class in scripts 05, 06, and 07, so each file presents a complete, self-contained teaching example.

PYTHON FILE FORMAT:

At the top of every Python script, include a module docstring containing:
- Lesson number and title
- Learning goal
- Prerequisites
- Three important ideas
- Connection to the previous lesson

Organize the experiments into small named functions or clearly labeled sections.

Make terminal output readable with headings and short explanatory messages.

For each major concept, include:
- A prediction question in a comment
- A small executable experiment
- Visible output
- A concise explanation or follow-up question

Keep the code simple enough for beginners to understand.

MARKDOWN GUIDE FORMAT:

Each Markdown file must contain:

1. Big question
2. What we already know
3. What we are about to discover
4. Vocabulary (maximum 4 new terms per lesson)
5. Guided experiments tied to specific code in the Python script
6. Predict, Run, Explain questions
7. What did we discover?
8. Connection to the next lesson
9. Two or three small student challenges

Guides must support classroom demonstrations as well as independent exploration.

Do not duplicate the entire Python script in Markdown.

README REQUIREMENTS:

00_README.md must include:
- The central learning objective
- A numbered lesson roadmap
- How to run each script
- How to use Python's interactive interpreter
- How to use help() without getting stuck in its pager
- Suggested teaching order
- A short conceptual map:

String object
    -> behavior and methods
    -> inspection tools
    -> str class
    -> our Dragon class
    -> Dragon instances
    -> discoverable software

- A recommended 30-minute instructor demonstration path
- A longer student laboratory path

QUALITY REQUIREMENTS:

- Python 3 standard library only.
- No package installation.
- No external APIs.
- No user input required to run scripts.
- No intentionally unhandled exceptions.
- No enormous dumps of dir() or help() in normal script output.
- Students should be able to discover the full output interactively.
- Avoid overwhelming students with special methods at the beginning.
- Explain Python behavior accurately.
- Do not confuse methods with the values they return.
- Do not confuse assigning a new string with mutating a string.
- Avoid presenting all attributes as methods.
- Provide a memorable connection between the built-in str class and our custom Dragon class.
- Keep examples playful but technically precise.

VALIDATION:

After building the materials:

1. Run all seven Python scripts using python3.
2. Check that every Markdown guide matches its script.
3. Confirm that all seven scripts run independently.
4. Confirm there are no unintended file dependencies.
5. Check for misleading claims about strings, classes, methods, or objects.
6. Report which files were created.
7. Summarize any validation failures.

SCOPE AND SAFETY:

- Work only in lessons/week_09.
- Preserve existing files.
- Do not modify other weeks.
- Do not commit or push automatically.
- Do not install dependencies.

Begin implementation now. Do not stop after writing a plan.

DELIVERABLE:
A complete seven-part Wings of Fire Python object-discovery lab, ready for instructor review and classroom use.

---

## Follow-up authorization

The user subsequently requested:

> make this prompt and all the other supporting items durable artifacts. add a local readme file and then push everything up to main on github.

This explicitly authorizes committing and pushing the completed week_09 materials to main, superseding the original instruction not to commit or push automatically. The restriction on editing other weeks remains in effect.
