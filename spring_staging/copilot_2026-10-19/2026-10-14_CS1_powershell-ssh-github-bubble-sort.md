**Getting a Student Set Up**

PowerShell, SSH Keys, GitHub, Editors, Python Bubble Sort, and Codex

*CS1 classroom artifact \| Wednesday, October 14, 2026 \| Jeremy Evert, SWOSU*

The Big Picture

This session turned a Windows machine into a working command-line development environment for a student (a student). The point was not to memorize commands, but to follow a path where every step leaves evidence we can check:

> PowerShell -\> files -\> SSH keys -\> GitHub -\> editor -\> Python -\> algorithm -\> measurement -\> AI-assisted coding

The habit underneath everything: **inspect -\> act -\> observe -\> verify.**

1\. Check Whether SSH Is Already Working

This four-part diagnostic answers: does the key exist, is it loaded, does GitHub recognize it, and does this repository actually use it?

> Write-Host "\`n=== SSH KEY FILES ===" -ForegroundColor Cyan
>
> Get-ChildItem \$HOME\\ssh
>
> Write-Host "\`n=== KEYS LOADED IN SSH AGENT ===" -ForegroundColor Cyan
>
> ssh-add -l
>
> Write-Host "\`n=== GITHUB SSH TEST ===" -ForegroundColor Cyan
>
> ssh -T git@github.com
>
> Write-Host "\`n=== CURRENT REPOSITORY REMOTES ===" -ForegroundColor Cyan
>
> git remote -v

|                                  |                                                                   |
|----------------------------------|-------------------------------------------------------------------|
| **Result**                       | **What it means**                                                 |
| id_ed25519 / id_ed25519.pub      | A key pair exists. The .pub file is public; the other is PRIVATE. |
| The agent has no identities.     | The SSH agent runs but holds no key right now.                    |
| Cannot connect to agent          | The ssh-agent service is probably not running.                    |
| git@github.com:USER/REPO.git     | The repo talks to GitHub over SSH.                                |
| https://github.com/USER/REPO.git | The repo uses HTTPS, even if SSH keys work.                       |

2\. Create SSH Keys for a New Student

Step 1: Generate the key

Run this in PowerShell under the student's own Windows account. Press Enter to accept the default file location.

> ssh-keygen -t ed25519 -C "STUDENT_GITHUB_EMAIL"
>
> id_ed25519 PRIVATE KEY - never share, never commit, never email
>
> id_ed25519.pub PUBLIC KEY - this is what GitHub gets

Step 2: Copy the public key and register it

> Get-Content \$HOME\\ssh\id_ed25519.pub \| Set-Clipboard

On GitHub: **Settings -\> SSH and GPG keys -\> New SSH key**. Give it a useful name such as Student - CS Lab Computer, paste, and save.

Step 3: Test it

> ssh -T git@github.com

The first connection asks whether to trust GitHub's host; answer yes. Success is GitHub greeting the account by name and noting that it does not provide shell access. That greeting is the victory condition.

Mental model

> STUDENT'S COMPUTER GITHUB
>
> private key ---- proves identity ----\> public key
>
> (stays home) (registered in Settings)

**Teaching tip:** stop at each checkpoint (create, register, test) so we never troubleshoot five things at once.

3\. Command-Line Editors

Nano: the gentle option

> winget install --id okibcn.nano -e
>
> nano --version
>
> nano test.txt

|                 |                       |
|-----------------|-----------------------|
| **Key**         | **Action**            |
| Ctrl+O, Enter   | Save                  |
| Ctrl+X          | Exit                  |
| Ctrl+K / Ctrl+U | Cut line / paste line |
| Ctrl+W          | Search                |

The ^ shown at the bottom of Nano means Ctrl.

Vim: what we actually wanted

> winget install --id vim.vim -e

Close PowerShell, open a new window, then:

> vim --version
>
> vim bubble_sort.py

|             |                                         |
|-------------|-----------------------------------------|
| **Command** | **Action**                              |
| i           | Insert mode (start typing)              |
| Esc         | Leave insert mode                       |
| :w          | Save ("write")                          |
| :q          | Quit                                    |
| :wq         | Save and quit                           |
| :q!         | Quit WITHOUT saving: the emergency exit |

The ancient rite of passage, "How do I get out of Vim?", is answered by: Esc, then :q!, then Enter.

4\. Troubleshooting: "No package found matching input criteria"

That message is evidence, not a dead end. It usually means WinGet cannot see its package catalog. Inspect before repeating the install:

> winget source list
>
> winget source update
>
> winget search vim

If the search still finds nothing, reset the sources (may require an Administrator PowerShell):

> winget source reset --force
>
> winget source update
>
> winget search vim
>
> winget install --id vim.vim -e

Lesson: when a command fails, examine what the tool can actually see rather than hammering the same command again.

5\. Moving a File Into a Neighboring Folder

> Move-Item .\bubble_sort.py .\week_09\\
>
> Get-ChildItem .\week_09\\

General pattern: Move-Item SOURCE DESTINATION. The Linux-style alias mv also works in PowerShell. Always verify the move with Get-ChildItem.

6\. Python: A List of n Random Numbers

> import random
>
> n = 10
>
> numbers = \[\]
>
> for i in range(n):
>
> numbers.append(random.randint(1, 100))
>
> print(numbers)

- n = 10 says how many numbers we want.

- numbers = \[\] creates an empty list.

- for i in range(n): repeats the body n times.

- random.randint(1, 100) picks an integer from 1 through 100, inclusive on both ends.

- .append(...) adds it to the end of the list.

7\. Bubble Sort That Narrates Its Work

> import random
>
> n = 10
>
> numbers = \[\]
>
> for i in range(n):
>
> numbers.append(random.randint(1, 100))
>
> print("Starting list:")
>
> print(numbers)
>
> print()
>
> comparisons = 0
>
> swaps = 0
>
> for pass_number in range(n - 1):
>
> print(f"--- Pass {pass_number + 1} ---")
>
> for i in range(n - 1 - pass_number):
>
> comparisons += 1
>
> print(f"Compare {numbers\[i\]} and {numbers\[i + 1\]}")
>
> if numbers\[i\] \> numbers\[i + 1\]:
>
> print(f" SWAP {numbers\[i\]} and {numbers\[i + 1\]}")
>
> numbers\[i\], numbers\[i + 1\] = numbers\[i + 1\], numbers\[i\]
>
> swaps += 1
>
> print(f" {numbers}")
>
> print()
>
> print("Sorted list:")
>
> print(numbers)
>
> print()
>
> print(f"Total comparisons: {comparisons}")
>
> print(f"Total swaps: {swaps}")

The heart of the algorithm

> if numbers\[i\] \> numbers\[i + 1\]:
>
> numbers\[i\], numbers\[i + 1\] = numbers\[i + 1\], numbers\[i\]

Are these two neighbors in the wrong order? If yes, switch them. Each pass carries the largest unsorted value to the right, which is where the name "bubble" comes from.

Why each pass gets shorter

range(n - 1 - pass_number) skips the tail of the list, because after each pass one more large value is already in its final position.

Measuring instead of guessing

The counters turn "bubble sort feels slow" into evidence. Because the passes shrink, the comparison count is always the same for a given n, no matter what the data is:

comparisons = (n-1) + (n-2) + ... + 1 = n(n-1)/2

|       |                 |                                        |
|-------|-----------------|----------------------------------------|
| **n** | **Comparisons** | **Swaps**                              |
| 10    | 45              | 0 (already sorted) up to 45 (reversed) |
| 20    | 190             | depends on the data                    |
| 50    | 1,225           | depends on the data                    |
| 100   | 4,950           | depends on the data                    |

**Classroom prompt:** predict the comparison count before running with n = 20, 50, and 100. Then ask: doubling n roughly does what to the work? That is the doorway to O(n²).

8\. Installing and Launching Codex

WinGet is not the route here. The well-established installation uses Node.js and npm, with the package name **@openai/codex** (not plain "codex"):

> node --version
>
> npm --version
>
> npm install -g @openai/codex
>
> codex --version

If node or npm is not recognized, install Node.js LTS first, reopen PowerShell, then retry. Then launch Codex from a clean repository:

> cd path\to\repository
>
> git status
>
> codex

The first run prompts for sign-in. Workflow: **repo -\> clean git status -\> Codex -\> one bounded task -\> inspect the diff -\> commit.**

**Correction note:** during the live session I also offered a one-line PowerShell installer from a chatgpt.com URL and attached citations to several install commands. My web lookups had actually failed at those moments, so those sources were never verified. Use the npm route above unless OpenAI's current Codex documentation shows a standalone Windows installer.

9\. Command Cheat Sheet

|                                     |                                     |
|-------------------------------------|-------------------------------------|
| **Command**                         | **Purpose**                         |
| Get-ChildItem \$HOME\\ssh           | List SSH key files                  |
| ssh-keygen -t ed25519 -C "email"    | Create a new key pair               |
| Get-Content ...pub \| Set-Clipboard | Copy the public key                 |
| ssh-add -l                          | Show keys loaded in the agent       |
| ssh -T git@github.com               | Ask GitHub: do you recognize me?    |
| git remote -v                       | SSH or HTTPS remote?                |
| git status                          | Is the working tree clean?          |
| winget source list / update         | Inspect and refresh WinGet catalogs |
| winget install --id vim.vim -e      | Install Vim                         |
| winget install --id okibcn.nano -e  | Install Nano                        |
| Move-Item .\f.py .\folder\\         | Move a file                         |
| npm install -g @openai/codex        | Install the Codex CLI               |
| codex                               | Launch Codex in the current repo    |

10\. The Larger Lesson

Every step produced something we could check: the key files existed, GitHub greeted us, the remote showed its protocol, WinGet showed its sources, the moved file appeared in the folder, the random list printed, and bubble sort reported its comparisons and swaps.

**Don't just make the computer do something. Make it show you evidence of what it did.**
