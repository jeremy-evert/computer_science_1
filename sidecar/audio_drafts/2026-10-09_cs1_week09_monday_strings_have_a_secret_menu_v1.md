# CS1 Week 9 Monday opening audio v1 — Strings Have a Secret Menu

**Status:** DRAFT 1, instructor listening pilot. Script written 2026-10-09. **No MP3 has been rendered or published by this commit.**
**For:** Monday, 2026-10-12, Computer Science I (COMSC-1033). Private Jeremy-first trial; no Canvas/student upload authorization.
**Specific instructional purpose:** A friendly approximately four-minute *introduction* to Monday's larger objects-first lesson, not a compressed substitute for the full approximately 30-minute lecture.
**Source:** `planning/week-09.md`, `lessons/06-strings.md` (Captain Noodle Mad Lib; strings, `dir()`, `help()`), and owner feedback in `sidecar/owner_feedback/2026-10-09_week09_concept1_audio_density_and_object_discovery.md`.
**Voice mapping:** `DANA = af_sarah`; `MARCUS = af_heart` (Kokoro). **Spoken word count:** 560. Estimate ~4 minutes depending on renderer pacing. Use actual MP3 duration as ground truth.
**Listener-facing title:** CS1 · Week 9 · Strings Have a Secret Menu
**Sequence:** Intro 1 of Monday's objects-and-discovery lesson.

## Why this episode exists

Jeremy likes the string-to-object connection but the previous 13-minute single-track concept podcast moved through too many unfamiliar ideas too quickly. In this opening, introduce only one usable idea: **a familiar string is an object with methods, and `dir()` and `help()` let you investigate what it can do.** Avoid list mutation, custom classes, `__init__`, identity/reference deep dives, or reading literal code punctuation aloud. Explain *receiver* once using the object before the dot. Preserve space for slides, an actual Python demonstration, and pauses in the complete lesson.

## Narration for Kokoro (parse only DANA and MARCUS turns)

DANA: Remember Captain Noodle? Last week, we gave Python a name with some strange capital letters and extra spaces, and somehow it came back looking presentable. Which raises a pretty good question. How did that string know what to do?

MARCUS: It didn't have to guess. In Python, a string isn't just a pile of letters. It's an object. That sounds like a big new idea, but you've already used objects. Every time you asked a string to strip away extra spaces or turn letters uppercase, you were asking an object to do something it knows how to do.

DANA: So when I have a string, I'm not stuck with only the text inside it?

MARCUS: Exactly. You have the text, and Python also gives you a collection of useful behaviors. We call those behaviors methods. But today, you don't need to memorize a whole collection of methods. You're going to learn how to find them.

DANA: Wait. I can ask Python what a string can do?

MARCUS: You can. First, pick one string. Let's use Captain Noodle's messy name. Give it a variable name, maybe raw name. The variable gives us a way to refer to that string object. Now imagine you want to remove the spaces at the beginning and end. You already know a method that does that. Strip.

DANA: I remember. And the string before the dot is the one receiving the request. That's the receiver.

MARCUS: Right. The receiver is just the object we're working with. No mystery. But here's the new trick. What if you forgot the name strip? What if somebody handed you an object you'd never met before?

DANA: I'd probably start guessing and then ask the internet.

MARCUS: Or ask Python first. There's a built-in function called dir. Short for directory. When you give dir your string, Python shows you names of things associated with that object, including methods you might use.

DANA: So dir is my menu. It tells me what's available.

MARCUS: That's a useful way to start. It shows names, not full instructions, and it isn't guaranteed to list every possibility. You'll see some strange names with underscores, too. Ignore those for now. Find something familiar, like strip or upper.

DANA: Fine. I've found upper on the menu. But what does it actually do? What goes inside the parentheses? And does it change my original string?

MARCUS: That's where help comes in. Ask Python for help with the upper method. It gives you documentation, the description of how that method works. Then try it on a tiny example. Look at the result. And check whether your original string changed.

DANA: So instead of memorizing a hundred commands, I have a little investigation routine. Pick an object. Look at its menu with dir. Read about one method with help. Make a prediction. Try it.

MARCUS: Perfect. And notice what happened. We started with an old friend, a string. We didn't need to build a class or learn a dozen new terms. We learned that a familiar value has behaviors, and we learned how to discover them.

DANA: Which means that when Python hands me something unfamiliar, I don't have to panic. I can get curious.

MARCUS: Exactly. Today we'll put this on screen and try it with real Python. First Captain Noodle. Then one new string you choose. The big question isn't, can you memorize every method? It's, can you find out what an object can do?

## Companion screen demonstration (NOT read aloud)

Show this on a simple Beamer slide or in a Python interpreter **after** the audio hook, not as narration of punctuation:

```python
raw_name = "  cAPTAIN nOODLE  "
print(raw_name.strip())      # cAPTAIN nOODLE
print(raw_name.upper())      #   CAPTAIN NOODLE  
print(raw_name)              #   cAPTAIN nOODLE  
print(type(raw_name))        # <class 'str'>
print("strip" in dir(raw_name))  # True
help(str.strip)              # documents strip() (interactive help)
```

**Instructor prompts:** Which object receives `strip()`? What did `dir()` tell us? What did `help()` add? What is still in `raw_name` after the calls? Students should make a prediction before running the program. If an explanation of why strings do not change would overload the intro, postpone it until the guided live example.

## Single-pass fast-track rendering request

1. Pull this one source file to the existing authorized Kokoro host/workflow; use the **existing proven DANA/MARCUS two-voice renderer** and Audiobookshelf publication pattern. Do not build a new engine, platform, quiz, presentation, or distribution system.
2. Render only the narrated DANA/MARCUS lines, preserving their order. Validate decodable, non-silent output; record actual duration and checksum.
3. Publish as **Jeremy-private** under Learning Foundry with the descriptive title/sequence above, making sure it is not another generic `Short`. **Create a new item; preserve the existing 13-minute recording and Jeremy's 74% listening progress.**
4. Report the real Audiobookshelf item/path and playback/readback result. **First-cut quality is enough for a Jeremy listening test.** Correct substantive mistakes before private listening; student-facing release remains a separate approval and QC path.
5. Await Jeremy's reaction to the actual four-minute recording before expanding to the remainder of Monday's lecture.

**Stop condition:** No student publication, no surprise cloud TTS charges, no rewriting unrelated lessons, no interruption of the existing live-course preparation. Report any genuine renderer/host access blocker rather than declaring an unverified success.
