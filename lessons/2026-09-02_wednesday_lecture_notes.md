# Wednesday, Sept. 2 — Reading and Running AI-Generated Code

## Big idea

A chat AI tool (Copilot / ChatGPT) is a fast way to get a first draft of code, but it only knows what you actually told it. Your job is to read what it gives you, notice the parts that describe your task's own missing details (save location, how to run it), and verify the result actually does what you meant.

## The 7 things to remember

1. A generated script is still just Python — read the comments (`#`), `print()` calls, and variable assignments before you run anything.
2. A variable's name supplies context a bare number can't: `8` means nothing on its own; `food_stock = 8` does.
3. `@' ... '@` in PowerShell is a "here-string" — a block of multi-line text you can pipe into a command.
4. `|` is the pipe operator: it takes the output of one command and feeds it into the next, unchanged.
5. `Set-Content` writes piped text into a file, creating or overwriting it.
6. `python .\yourfile.py` runs a Python file the same way regardless of which editor last touched it — the file on disk is the only thing that matters.
7. When something in generated code is confusing or seems wrong, ask the tool to explain it — you stay the one deciding whether the explanation makes sense.

## Commands / code we used

```powershell
cd ~
cd GIT
```

```powershell
$code = @'
# generated Python code goes here
'@
$code | Set-Content -Path frontiersettlement.py -Encoding utf8
```

```powershell
python .\frontiersettlement.py
```

The lecture also opened the same `.py` file in Notepad from the file explorer — a reminder that a Python file is plain text no matter which tool opens it.

## Vocabulary

- **Here-string:** a PowerShell block, opened with `@'` and closed with `'@`, that holds multi-line text as one value.
- **Pipe (`|`):** sends the output of the command on its left into the command on its right.
- **Variable:** a name bound to a value, used to make code and its intent easier to follow.
- **`if` statement:** a block that runs only when its condition is true — here, only when the food stock is low.

## Common mistakes / what the errors mean

- A pasted multi-line command triggers a warning in the terminal: this is expected — PowerShell is confirming you meant to run all of it, not just the first line.
- Generated code fails to save or run where you expect: check that you know your current directory (`cd ~`, `cd GIT`, and look around) before running anything.
- A stray character (smart quote, extra space, an emoji some tools insert automatically) breaks a pasted block: reread the pasted text before running it if something you didn't type shows up.

## If you got lost

Open a chat AI tool and ask it, in plain English, for a small script that matches something you understand (a rule with one condition is enough). Read the result line by line before running it: find the comments, the `print()` calls, and any variable assignment. Ask the tool to explain any single line you can't already describe yourself.

## Before Friday

Continue the paired-reasoning work started in class (foreman plans, worker types — swap roles from last week). Be ready to explain, for the file your pair produced, what each variable represents and what the `if` condition is checking.
