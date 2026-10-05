# Leara's guide to running and writing Python on a Chromebook

Hey Leara! You can make useful things, funny things, and things that simply answer “what happens if I try this?” Start small, change one thing, and watch what happens. This is optional practice; follow Canvas for your graded work.

First finish the Linux and tool setup in [your setup guide](README_LE.md). Everything below uses the Chromebook's **Linux Terminal** and Python 3.

## Your everyday coding routine

Open Terminal and enter your folder:

```bash
cd ~/git/computer_science_1/student_work/leara_fernandez
pwd
ls
python3 --version
```

`pwd` tells you where you are. `ls` lists files. The editor changes a file; Python runs the saved file. Saving a file and running it are two separate steps.

Start with the example you already have:

```bash
nano hello_world.py
```

Change the greeting. Save with **Ctrl+O**, then Enter; exit with **Ctrl+X**. Run:

```bash
python3 hello_world.py
```

Use `python3`, including the `3`. Type just the command, without a copied terminal prompt or trailing `]`. If VS Code is already installed and `code` works, you can instead open the folder with `code .`, save using **Ctrl+S**, and run the same Terminal command. Nano is enough to get started.

Try this rhythm: **predict → edit → save → run → compare → explain**. Before running, say what you expect. After running, explain any surprise in your own words.

## Write your own first program

```bash
nano creature_greeting.py
```

Put this Python code in the file. Copy only the code, without Markdown backticks:

```python
creature = input("What creature joins your adventure? ")
print(f"Welcome, {creature}!")

for step in range(1, 4):
    print(f"Step {step}: {creature} explores the forest.")

print("Adventure complete!")
```

Save, exit, and run:

```bash
python3 creature_greeting.py
```

When it asks a question, type an answer and press Enter. Run it again with a different creature. Then change the forest to a place you invent. Finally, change the stop number in `range(1, 4)` and predict how many steps will print. The stop number is excluded.

Use four spaces for each indentation level. Indentation groups the statements inside a loop or decision.

## Try tiny experiments without a file

Enter `python3` by itself in Terminal. Python opens an interactive prompt marked `>>>`. Try these expressions one at a time; do not type `>>>` yourself:

```python
2 + 3
"dragon".upper()
len("dragon")
list(range(1, 4))
exit()
```

`exit()` returns you to the Linux shell. Commands such as `ls`, `git status`, and `python3 hello_world.py` belong in the shell. Python statements such as `print("hello")` belong in a `.py` file or at `>>>`.

Source: [Python's interpreter guide](https://docs.python.org/3/tutorial/interpreter.html).

## When a program fails, become a detective

Read the last line of the error first, then find the filename and line number above it. Inspect that line and the one before it. Make one change and rerun.

| What you see | What to check |
| --- | --- |
| `can't open file` | Run `pwd` and `ls`; check the folder, spelling, and `.py` ending. |
| `SyntaxError` | Check quotes, parentheses, and the colon after `if`, `for`, or `while`. |
| `IndentationError` | Check indentation and whether a block has a statement inside it. |
| `NameError` | Check variable spelling and whether you assigned it before using it. |
| `ValueError` with `int(...)` | Check whether the input can actually become a whole number. |
| It keeps printing forever | Press **Ctrl+C**, then check whether the loop condition can become false. |
| It runs but the answer is wrong | Write an expected result for a small example; print intermediate values. |

Keep a short debugging note: “I expected __. I got __. I changed __. Now __.” Errors are useful evidence.

## Explore the loop examples in this folder

Read each file before running it:

```bash
nano loops.py
python3 loops.py
nano loops_2.py
python3 loops_2.py
```

`loops.py` starts with ranks and repetition, then draws a text map. Start with its first section. Try scores of 69, 70, 79, 80, 89, and 90: what rank should each receive? Change one map dimension and predict the new shape.

`loops_2.py` compares different ways to express logic, then runs a fictional game simulation. Its game uses random numbers and brief pauses, so results can differ. It does not connect to real servers. The “bad” examples illustrate alternatives to discuss; ask when an indexed loop or nested decision might actually be useful.

You do not need to understand the entire file at once. Copy a small section into your own practice file, explain it, and experiment with it.

## Grow by adding one new idea at a time

| Build | Practice | Next small improvement |
| --- | --- | --- |
| A creature greeting | Strings, variables, `input`, `print` | Ask for a location too. |
| A two-choice adventure | `if` / `elif` / `else` | Handle an unexpected choice. |
| A countdown or chant | `for`, `range` | Let the user choose the repetition count. |
| A guessing game | `while`, comparisons | Limit guesses and give a useful hint. |
| A random story generator | Lists, `random.choice` | Combine a character, place, and problem. |
| A reusable story scene | Functions and parameters | Call the same function with different characters. |
| A small quiz | Lists, decisions, counters | Report the score and missed questions. |

Pick an idea you like. Build the smallest version that works before adding another feature. For input-based programs, try an ordinary answer, an empty answer, an unexpected word, and a boundary value. Record what should happen and what actually happens.

When you want to explore freely outside the shared course repository:

```bash
mkdir -p ~/git/leara-python-playground
cd ~/git/leara-python-playground
git init
nano experiment.py
```

This gives you your own local project. Follow the Git checkpoint steps in [your setup guide](README_LE.md). For course work, stay in your own student folder. Peers will see work you share in the course discussion, and collaborators can see pushed files.

## Coding with Gemini: ask for help that helps you learn

Open [Gemini](https://gemini.google.com) in Chrome and type your question. A school account may require the school administrator to enable access. Browser chat can discuss the code you paste; it does not automatically see or edit your Chromebook files. Save any changes yourself and run them in the Linux Terminal. See [Google's Gemini Apps guide](https://support.google.com/gemini/answer/13275745?hl=en).

Give Gemini five useful details: your goal, your experience level, your environment, the relevant code or error, and the kind of help you want. You do not need perfect wording. Google's [prompt-writing tips](https://support.google.com/a/users/answer/14200040?hl=en) recommend clear language, context, and breaking a large task into smaller requests.

Instead of “make me a game,” try:

> I am learning Python 3 in the Linux Terminal on a Chromebook. I know variables, input, print, and if statements. Help me design a two-choice text adventure using only those ideas and no extra packages. Ask me about the setting first. Give me one step at a time and let me write the code.

To understand existing code:

> Explain this loop using a table showing the variable values on each iteration. Ask me to predict the output before showing it. Use beginner language. Here is the code: [paste the small section].

To debug:

> I run `python3 creature_greeting.py` in my Chromebook Linux Terminal. I expected [describe it], but got [describe it]. Here is my code and the complete error: [paste both]. Give me one hint first. If I need a fix, show the smallest change and explain why it works.

To test a program:

> Suggest five inputs for this program, including an empty input and a boundary case. Tell me the expected result for each. Let me run the tests and report the actual results. Here is my code: [paste code].

To choose your next challenge:

> I made a greeting program and a for loop. I like fantasy stories. Suggest three projects I can finish in about 20 minutes using those ideas plus one new concept. Let me choose before giving instructions.

To get feedback:

> Review my code for one correctness issue and one readability improvement. Explain your reasons. Keep my approach and avoid rewriting the whole program. Here is my code: [paste code].

Follow up with precise observations: “That uses a function I have not learned yet,” “Please use only the standard library,” or “Here is the output after that change.” Ask Gemini to explain unfamiliar commands before using them. Check suggestions by running the program yourself; a confident explanation can still be mistaken.

Paste the smallest useful code section and remove private information. Never paste SSH private keys, passwords, or account tokens. For graded work, follow Jeremy's AI-use instructions and be ready to explain your own program.

## Save progress and find your next question

Before a new experiment, check `git status`. After a working change, review `git diff`, stage only the intended file, and commit with a message that describes what changed. Use the sharing workflow in [README_LE.md](README_LE.md) when you are ready to push course work.

Keep a simple learning log with three lines:

- Today I made __.
- One thing I can explain now is __.
- Next I want to find out __.

For more exploration, use the [official Python tutorial](https://docs.python.org/3/tutorial/) as a reference for strings, control flow, lists, and functions. It assumes some programming familiarity, so read a small section alongside a program you can run. Ask Gemini for a simpler explanation when needed, then test it yourself.

You are growing when you can predict more of the output, explain more of the code, and turn a confusing error into a small experiment. Keep making things you are curious about.
