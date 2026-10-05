# Leara's Chromebook setup and Git playground

Hey Leara! This guide gets your Chromebook ready for Git, GitHub, and Codex, then gives you some small experiments to build confidence. Go one section at a time. These activities are optional practice, not another graded assignment.

Git records snapshots of your files. GitHub hosts repositories online. SSH lets your Chromebook prove it is you when connecting to GitHub. Codex is a coding assistant you can ask to explain code and help you practice.

Once setup is finished, continue with [Leara's guide to writing and running Python on a Chromebook](PYTHON_CHROMEBOOK_LE.md), including Gemini prompts and project ideas.

## 1. Turn on Linux

Open **Settings → About ChromeOS → Developers → Linux development environment → Set up**. Follow the prompts, then open the **Terminal** app and select your Linux environment. Setup can take ten minutes or more. If Linux is missing or blocked on a school-managed Chromebook, ask Jeremy or your school administrator for help.

Use the Linux Terminal for the commands below. Copy only the commands inside each block; do not type the backticks. Run one line at a time. If a command fails, stop there and ask for help with its exact error message.

Source: [Google's Chromebook Linux setup guide](https://support.google.com/chromebook/answer/9145439?hl=en).

## 2. Install Git and a few useful tools

```bash
sudo apt update
sudo apt install git openssh-client curl nano python3
git --version
```

If asked whether to continue, type `Y` and press Enter. A password prompt may show no characters as you type; that is normal. `git --version` should print a version number.

Create or sign in to your [GitHub account](https://github.com). In GitHub **Settings → Emails**, find your GitHub-provided **noreply email address** if you want to keep your personal email out of commits. Replace the example below with that address:

```bash
git config --global user.name "Leara Fernandez"
git config --global user.email "REPLACE_WITH_YOUR_GITHUB_NOREPLY_EMAIL"
git config --global init.defaultBranch main
git config --global --list
```

Your name and email become part of your commit history. These settings identify your work; they do not sign you into GitHub.

## 3. Set up your SSH key for GitHub

First check for an existing key:

```bash
ls -la ~/.ssh
```

If the directory does not exist, that is fine. If you already have `id_ed25519` and `id_ed25519.pub`, you can reuse them and skip key generation. Do not overwrite an existing key; ask for help if you are unsure.

For a new key, run:

```bash
ssh-keygen -t ed25519 -C "Leara Chromebook"
```

Press Enter to accept the default file location. Choose a passphrase and enter it twice. The characters will not appear as you type. Then start the SSH agent and load the key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

Copy the entire public-key line, starting with `ssh-ed25519`. On GitHub, go to **Settings → SSH and GPG keys → New SSH key**. Give it the title **Leara Chromebook**, choose **Authentication Key**, paste the line, and save.

The `.pub` file is the public key you add to GitHub. Keep the file without `.pub` private: never paste it into chat, Canvas, or a repository.

Test your connection:

```bash
ssh -T git@github.com
```

The first connection may ask you to trust GitHub's host key. Compare the displayed fingerprint with [GitHub's published SSH fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints) before typing `yes`. Success says `Hi YOUR_USERNAME! You've successfully authenticated...` and explains that GitHub does not provide shell access. That is expected.

If a later Terminal session needs your key again, repeat the `eval` and `ssh-add` commands above.

Sources: [Generate a key and load it into the agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux), [add the public key to GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

## 4. Install Codex

In your Linux Terminal, run the installer from the [official Codex CLI guide](https://developers.openai.com/codex/cli):

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Follow any PATH instructions the installer prints. Close and reopen the Linux Terminal, then check:

```bash
codex --version
```

If you see `command not found`, revisit the installer's PATH instructions or ask Jeremy for help. You will sign in when you start Codex below. GitHub login and Codex login are separate. Use your own ChatGPT account; if your account cannot access Codex, ask Jeremy about the course setup before purchasing anything.

## 5. Clone the course repository

Cloning downloads the repository and its history to your Chromebook:

```bash
mkdir -p ~/git
cd ~/git
git clone git@github.com:jeremy-evert/computer_science_1.git
cd computer_science_1/student_work/leara_fernandez
pwd
ls
git status
```

You should see this README and `hello_world.py`. If Git says the destination already exists, do not clone again; enter your existing `~/git/computer_science_1` folder. If it says `Repository not found`, confirm Jeremy has granted your GitHub account access and accept any invitation. If it says `Permission denied (publickey)`, revisit the SSH test.

Read the program before running it:

```bash
nano hello_world.py
```

In Nano, **Ctrl+X** exits. When you are ready:

```bash
python3 hello_world.py
codex
```

On the first Codex launch, choose **Sign in with ChatGPT** and follow its browser instructions. If the browser does not open, use the link printed in Terminal. Try this prompt:

> Explain hello_world.py like I am new to Python. Do not change any files. Ask me to predict what it will print before explaining the result.

Use Codex as a tutor: ask for hints, make your own prediction, and check the result. Review proposed commands and changes before approving them. Type `/quit` to leave Codex.

## 6. Have some fun in a Git playground

Make a separate local repository so you can experiment freely:

```bash
mkdir -p ~/git/leara-git-playground
cd ~/git/leara-git-playground
git init
nano adventure.txt
```

Write the opening sentence of a silly adventure. In Nano, press **Ctrl+O**, Enter to save, then **Ctrl+X** to exit.

```bash
git status
git add adventure.txt
git diff --staged
git commit -m "Start my adventure"
git log --oneline
```

That is your first checkpoint! `add` selects a file for the next snapshot; `commit` records it locally. Neither command uploads anything.

Add another sentence with `nano adventure.txt`, then inspect and save the change:

```bash
git diff
git add adventure.txt
git commit -m "Add a surprise to the adventure"
git log --oneline
```

Try an alternate ending on a branch:

```bash
git switch -c dragon-ending
nano adventure.txt
git diff
git add adventure.txt
git commit -m "Give the adventure a dragon ending"
git switch main
cat adventure.txt
git switch dragon-ending
cat adventure.txt
```

Notice how switching branches changes the file! To bring the dragon ending into `main`:

```bash
git switch main
git merge dragon-ending
git log --oneline --graph --all
```

More optional challenges:

- Make three commits telling a tiny story. Read an earlier snapshot with `git show HEAD~1:adventure.txt`.
- Add an intentionally silly sentence, commit it, then run `git revert HEAD`. If an editor opens, save the suggested message and exit. Notice the new commit that undoes the sentence while preserving the history.
- Start Codex in the playground and ask: “Give me one Git challenge at a time. Let me type the commands. Explain what changed after each step.”
- Create a small Python joke generator or guessing game. Save a checkpoint each time it gains a feature.

This playground stays on your Chromebook unless you connect it to an online repository and push it.

## 7. Use the course repository carefully

Return to your course folder:

```bash
cd ~/git/computer_science_1/student_work/leara_fernandez
git status
```

The Git repository includes the whole course, even when Terminal is inside your folder. Keep your edits in your own student folder. Peers will see work you share in the course discussion, and repository collaborators can see pushed files. Keep passwords, keys, and personal details out of both.

Before starting work, if `git status` reports a clean working tree:

```bash
git pull --ff-only
```

If you have unfinished edits, finish and commit them first or ask for help. If a pull fails because histories have diverged, ask Jeremy rather than forcing an update.

When Jeremy has confirmed your write access and branch workflow, a branch lets you share a change for review. From your student folder, for example:

```bash
git switch -c leara/hello-practice
nano hello_world.py
python3 hello_world.py
git diff -- hello_world.py
git add hello_world.py
git diff --staged
git commit -m "Practice changing my greeting"
git push -u origin leara/hello-practice
```

Commit only if you made a change you want to keep. Review the staged diff to make sure it includes only your intended work. Open the pull-request link GitHub prints to request review. If pushing is denied, ask Jeremy for access or the course's fork workflow. Do not force-push. Follow Canvas instructions for the actual graded discussion; pushing code alone does not submit that discussion.

## 8. Learn more, a little at a time

- [Pro Git, free online book](https://git-scm.com/book/en/v2): start with **Getting Started** and **Git Basics**. You do not need to read the whole book at once.
- [GitHub's Git Handbook](https://docs.github.com/en/get-started/using-git/about-git): learn the vocabulary and everyday workflow.
- [GitHub Skills](https://skills.github.com/): try **Introduction to GitHub** for guided practice in your own repository.
- [Official Codex CLI guide](https://developers.openai.com/codex/cli): installation, sign-in, and ways to use your coding assistant.

The everyday rhythm is: change a little, run it, inspect `git diff`, stage the intended file, and commit with a useful message. Small checkpoints make it easier to explore and understand your work.
