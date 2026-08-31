# CS1 lecture digest — Monday, August 31, 2026

## Evidence and privacy

- Course: Computer Science I (COMSC-1033), Fall 2026.
- Source: fresh local Whisper/CTranslate2 transcription of the protected MP4.
- Protected MP4: `Fall 2026 Computer Science I (COMSC-1033-1415)-20260831_095929-Meeting Recording.mp4`.
- Fresh transcript: `Fall 2026 Computer Science I (COMSC-1033-1415)-20260831_095929-Meeting Recording.vtt` in the protected input directory on April.
- The digest intentionally omits student names, chat, incidental remarks, and identifying classroom details.

## Teaching goals

1. Help students see the GUI file manager and terminal as two views of the same filesystem.
2. Establish the command-line mental model: the computer does exactly what was specified, not what the user intended.
3. Make file extensions and the difference between text and executable Python files concrete.
4. Introduce `print()` as a Python function, comments as human-facing explanation, and case sensitivity as a machine rule.
5. Normalize errors as information and invite curiosity, checking, and small recoverable experiments.

## Concepts actually covered

### Filesystem and navigation

The lecture began by reconnecting students with the course/resource dashboard, then shifted to the Windows file manager and PowerShell. The same location can be viewed in both tools: the file manager shows files visually, while the terminal reports the current location and its contents. The transcript explicitly demonstrates `ls` to inspect the current directory and `cd GIT` to move into a directory. The tilde (`~`) was explained as a home-location shorthand in the Unix-style mental model; the Windows lesson used the analogous user-folder view.

### Creating, saving, and naming files

Students created a text file named `hello class.txt`, typed a short message, and observed the unsaved indicator (the “dot of shame”). `Ctrl+S` saved the file. The terminal did not automatically show the newly created file until it was asked to refresh/list the directory. The up arrow recalled the previous command, and Tab completion was demonstrated as both a speed aid and a check on the name being entered.

### `.txt`, `.md`, and `.py`

The lecture contrasted a text file (`.txt`), Markdown (`.md`), and a Python source file (`.py`). An extension is the ending that identifies the kind of file. The instructor created `hello in Python.py`, explained that a Python file is still text on disk, and then showed that it only becomes useful as a program when its contents and execution context are correct.

### First Python program and comments

The working example used a `print("hello world")`-style program. A line beginning with `#` was identified as a comment: it is part of the source text for human readers but is ignored by Python when the program runs. The instructor used `cat hello world`/file-content inspection and a small PowerShell here-string plus pipe/`Set-Content` example to show how multiline text can be moved into a file; this was an explanation of what the command does, not a required memorization list.

### Precision and case sensitivity

Changing lowercase `print` to uppercase `Print` produced an error. The point was not that the computer is “bad,” but that it is literal and case-sensitive. The same behavior was used to reinforce a larger precision/literal-machine mindset: humans can understand intent, while the machine follows exact names, punctuation, and structure.

### Errors, tools, and learning

The instructor deliberately introduced a malformed `print` call, showed the error output, then corrected the parentheses and reran it. The class was asked to inspect the error rather than walk away. ChatGPT was used as an available translation/checking tool, but the code still had to be correct. The desired habit is: predict, try a small change, read the result, ask a tool or person for help, and verify.

## Useful examples and timestamps

| Approx. time | Evidence / teaching move |
|---|---|
| 00:04–00:08 | File manager, PowerShell, current location, home/user-folder conventions |
| 00:08–00:10 | `ls`, `cd GIT`, terminal as an exact reality check |
| 00:09–00:12 | Create/save `hello class.txt`; unsaved indicator and refresh/list behavior |
| 00:12–00:14 | Up-arrow history and Tab completion |
| 00:16–00:22 | `.txt` versus `.py`, file extensions, create and run a Python file |
| 00:22–00:25 | `#` comments and writing code for other humans to read |
| 00:28–00:32 | Case-sensitive `print`, errors as information, literal-machine mindset |
| 00:33–00:38 | PowerShell here-string, pipe, `Set-Content`, and asking tools to translate commands |
| 00:40–00:43 | Understanding check: predict output, comments, lowercase versus uppercase |
| 00:46–00:50 | `print()` as a function; deliberate syntax error, correction, and curiosity |
| 00:50–00:51 | Wednesday paired reasoning and Friday show-and-tell preview |

## Corrections and follow-up notes

- **LECTURE SAID:** the terminal/PowerShell view and file-manager view show the same underlying location when pointed at the same directory.
  **FOLLOW-UP NOTE:** the exact command syntax differs by shell; students should use the syntax provided for their current environment rather than assume PowerShell, Bash, and Python commands are interchangeable.
- **LECTURE SAID:** “`print` is a function” and the English word helps make the behavior memorable.
  **FOLLOW-UP NOTE:** in Python, `print` is a built-in function and its spelling/case and parentheses are part of the exact syntax.

## Unfinished threads and next steps

- Wednesday should open the Week 3 material and use a paired reasoning exercise: make a prediction, consult available resources, explain the evidence, and check the result.
- Friday should use show-and-tell to discuss how the small programs went.
- Students should practice opening, reading, changing, saving, and rerunning a small Python file; no full-hour recording is required for recovery.
