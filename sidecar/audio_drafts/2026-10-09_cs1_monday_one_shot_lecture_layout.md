# Monday October 12 CS1 — Strings Have a Secret Menu

**Status:** Jeremy + ChatGPT first-cut lesson map (2026-10-09). No Flo routing, no Claude Code, no Canvas/publication mutation. **Owner-led fast track.**

**Guiding question:** *How can I find out what an unfamiliar Python object knows how to do?*

**Big idea:** Start with our old friend, the string. A string is an object; its type offers behaviors called methods. You don't need to memorize methods when Python can help you discover, inspect, and test them with `type()`, `dir()`, and `help()`.

**Student win at the end:** Given a Python string, a student can point to the receiver in `raw_name.strip()`, say what the method does, ask Python which methods exist, find focused documentation, predict a result, and run/check it.

**Known course context:** Week 9 Monday is *Objects You Already Use*, AI I Lens 9 *Generate*. Wednesday Oct 14 continues to a small first class; Fri Oct 16 is Fall Break, no Friday class. Coding Odyssey Checkpoint 2 is due Friday 11:59 PM CT; a custom class is **not required**. Source: `planning/week-09.md` and `lessons/06-strings.md`.

## One-shot live lecture, approximate 50-minute shape

| Time | Mode | Instructor move | Student evidence |
|---|---|---|---|
| 0–4 | LISTEN | Play private four-minute opener, `CS1 Week 9: Strings Have a Secret Menu`. Familiar Captain Noodle and one question: what can this object do? | Students can name the problem we want to solve. |
| 4–9 | REMEMBER | Revisit Captain Noodle's messy name, `"  cAPTAIN nOODLE  "`. Show `raw_name.strip()`, then `raw_name`. Do not start with new terminology. | Predict whether original spaces go away. |
| 9–15 | SEE | Show the object as a receiver. Decode the dot and parentheses on an enlarged code slide. One term at a time: object, method, receiver. | Point to the receiver in `raw_name.upper()`. |
| 15–23 | DO | Live Python: `type(raw_name)`, `dir(raw_name)`. The list is large: explicitly ignore double-underscore names today; find `strip` and `upper`. | Show one plausible method without memorizing a list. |
| 23–30 | SEE + DO | Use `help(str.strip)` to read the description, then try `raw_name.strip()` and check its output. Explain only the help necessary for this method. | State what `strip()` does and whether the old string changed. |
| 30–40 | PREDICT / RUN / EXPLAIN | Try `raw_name.upper()` and one `replace()` example. Ask students to predict output before execution. Explain saving the returned result only after it matters. | Predict two results and describe one surprise. |
| 40–46 | STUDENT TRY | Give a second string: `msg = "  Geese Rule SWOSU!  "`. Students find one method, consult help, and test it. Pair discussion optional. | Each student can describe *how* they found the method. |
| 46–50 | EXIT | Ask: `What is it? What can it do? How do you know?` Preview Wednesday: defining our first custom class. Briefly connect to Lens 9: choose how to present a message to its audience. | One-sentence explanation of their own discovery. |

**This is a 50-minute classroom pathway, not 50 minutes of nonstop podcast.** The opener is just the first four minutes. Pauses, live Python, code on screen, and learner activity make the full lecture teachable. Scale durations to actual class period after a quick check.

## Teacher's tiny executable lab (do not narrate the punctuation)

```python
raw_name = "  cAPTAIN nOODLE  "
print(type(raw_name))                 # <class 'str'>
print(raw_name.strip())               # cAPTAIN nOODLE
print(raw_name.upper())               #   CAPTAIN NOODLE
print(raw_name)                       # still contains original spaces/case
print("strip" in dir(raw_name))       # True
help(str.strip)                       # a focused description in the terminal
clean = raw_name.strip()
print(clean)                          # cAPTAIN nOODLE
msg = "  Geese Rule SWOSU!  "
print(msg.replace("Geese", "Squirrels"))
```

If using `dir(raw_name)` instead of the boolean filter, expect a very long list including `__...__` entries. Show the list briefly; the goal is **discovery**, not learning the whole API. `help(str.strip)` may enter a pager; use `q` to quit if needed.

**Avoid today:** list-mutating methods, multiple unfamiliar classes, a full lecture on `self`/`__init__`, object identity, f-string review, code pronunciation, all of `dir()`'s special names, or the entire documentation system. Wednesday can tackle first custom class after Monday's foundation is secure.

## Podcast pilot source: already written

`sidecar/audio_drafts/2026-10-09_cs1_week09_monday_strings_have_a_secret_menu_v1.md`

It is a ~560-word Dana/Marcus Kokoro dialogue. **Script is committed, MP3 is not yet rendered on Maise.** Treat this as a listener-led pilot: render it once, listen to it, and fix what bothers Jeremy. Keep the existing 13-minute Concept 1 audio and its listening history intact.

## Direct phone SSH → Codex/Hanna handoff (without Flo)

From an authenticated shell on a machine where `codex` works and this repo is checked out:

```bash
cd ~/git/computer_science_1
git pull --ff-only
codex exec "Read sidecar/audio_drafts/2026-10-09_cs1_week09_monday_strings_have_a_secret_menu_v1.md and this lecture layout. Use the ALREADY WORKING two-voice Kokoro workflow on Maise to render exactly the DANA/MARCUS spoken script as a NEW Jeremy-private MP3. Do not install models, rebuild the pipeline, use Claude Code, involve Flo, or publish to Canvas. Validate duration and decode with ffprobe/ffmpeg, preserve the old audio, and report exact output path so I can listen. If SSH or renderer access is unavailable, stop with the one concrete blocker. Commit only safe source/receipt changes."```

This is a proposed *one-shot user-triggered command*, **not a command that has already been executed**. Check local path or permissions if the repo checkout differs. No promises about Maise access until verified.

## Immediate next decision after hearing the opener

Keep / change / flush each of: (a) Captain Noodle hook, (b) Dana/Marcus banter, (c) explanation of `receiver`, (d) `dir()` + `help()` curiosity hook. Only expand the lesson after this 4-minute test earns it.
