# Monday, Aug. 31 — Files, Terminals, and Your First Python Program

## Big idea

The file manager and terminal are two ways to work with the same filesystem. The computer is literal: it performs the exact command and code you give it. Your job is to make a small prediction, try it, read the result, and adjust.

## The 8 things to remember

1. `ls` lists what is in the current directory.
2. `cd GIT` changes the current directory to `GIT` (use the directory name that exists on your machine).
3. The terminal does not guess what you mean; ask it to list or inspect the location again after you create a file.
4. `Ctrl+S` saves a file. An unsaved marker means the editor has changes that are not on disk yet.
5. File extensions matter: `.txt` is text, `.md` is Markdown, and `.py` is Python source.
6. A line beginning with `#` is a Python comment. It helps humans and does not run as code.
7. Python is case-sensitive: `print` and `Print` are different names.
8. An error is information. Read it, make one small correction, and run the program again.

## Commands / code we used

```text
ls
cd GIT
```

```python
# A short note for another human
print("hello world")
```

The lecture also inspected file contents and demonstrated a PowerShell here-string piped into `Set-Content`. Treat that as an example to understand, not as a command to memorize before Wednesday.

## Vocabulary

- **Current directory:** the location the terminal is working in now.
- **File extension:** the ending such as `.txt` or `.py` that identifies a file type.
- **Comment:** human-facing source text beginning with `#` in Python.
- **Function:** a named operation; `print()` sends text to the output.
- **Case-sensitive:** uppercase and lowercase letters are treated as different.
- **Terminal:** a text interface for giving exact commands to the computer.

## Common mistakes / what the errors mean

- The file is not visible in the terminal: list the directory again and check that you are in the same location.
- The program displays nothing: check whether the line is a comment or whether the file was saved.
- `Print(...)` fails while `print(...)` works: Python cares about capitalization.
- A red error appears: do not guess broadly. Read the message, inspect the line, change one thing, and rerun.

## If you got lost

Open the file manager and terminal side by side. Confirm the directory shown in both. Create one tiny file, save it, list the directory, and open the `.py` file. Ask a classmate, instructor, or approved tool to explain an unfamiliar error, then verify the explanation by running the smallest safe test.

## Before Wednesday

Bring a saved, tiny Python file containing a comment and one `print("hello world")` line. Be ready to predict what it will do before running it. Wednesday begins the paired reasoning exercise; Friday is the show-and-tell/check-in.
