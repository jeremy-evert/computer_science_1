# Git Ain't GitHub: the disposable-first music experiment

## Listener verdict, 2026-10-09: V0 REJECTED

Jeremy lasted roughly **five seconds** of `git_aint_github_scrappy_v0.mp3` before wanting to turn it off: the vocal sounded like a **Simon Speak & Spell**. The song was **not** acceptable to listen to or share with friends. **Never promote this file as the finished song, a successful singing demo, or a user-approved teaching product.** Keep v0 only as a historical source/negative control. The failure is the robotic eSpeak guide vocal, not proof that country-comedy, the Git/GitHub concept, or music mnemonics failed.

**Hard next gate: first 15–25 seconds must contain a genuinely melodic, recognizable *sung* human-like voice, not eSpeak, Kokoro talk-read, pitch-shifted narration, or speech pasted on instruments.** No full-song render or tool building until a short sung sample passes Jeremy's five-second test. If no capable vocal music-generation tool is installed and available, report this plainly and request the smallest feasible way to get one, rather than shipping another robot read.

**Immediate working brief:** [v1_sung_chorus_first.md](./v1_sung_chorus_first.md). Direct Codex/Hanna, no Flo or Claude Code. User explicitly wants to hear a song; a TTS-over-beats MP3 does not count.

**We actually made a v0 on 2026-10-09. No Flo or Claude Code.**

This is a public, shareable teaching artifact. The point is to hear an original, ridiculously campy Git-versus-GitHub country-comedy story now, react to it, and iterate. The accompanying 108-second MP3 was produced in the current ChatGPT session, not yet uploaded to GitHub; the conversation supplies the playback link. The generator source is in this folder and can reproduce a fresh version on a Linux box.

## Run it

Requires Python 3 + `numpy`, `espeak`, and `ffmpeg` on PATH. Check before using; don't install host packages or change system services as a side effect. In a repo checkout:

```bash
python3 extras/git_song/render_demo.py
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 extras/git_song/git_aint_github_scrappy_v0.mp3
```

The script outputs one MP3 into this directory. It creates a simple original two-step instrumental, then mixes in a spoken/robotic guide vocal. **It is a musical sketch, not a human singing performance or a Kokoro/ACE-Step claim.** Its instructional content is in [lyrics.md](./lyrics.md). The generator uses deterministic backing; identical output is not guaranteed across different versions of eSpeak/FFmpeg.

## How to ship a better version on Maise, via Codex/Hanna, without Flo

Jeremy rejected the sketch after five seconds; treat it only as proof that the eSpeak path is unacceptable. Later, from a properly authenticated session, let Codex/Hanna reuse **existing verified** audio/music tools. Choose a music-capable generator if available; Kokoro is TTS for dialogue, not a convincing singer. Use this version as a reference for pace and refrain, not its specific original notes as mandatory. Preserve the lyric's Git correctness and use a **new filename** for every revision. Don't publish to students or modify a live private audio library without an explicit decision.

Smallest delivery contract: (1) audio file, (2) duration/format validation, (3) title/lyrics/source refs, (4) playback link or copied private media path. No multi-agent review ceremony.

## Next experiment

Do NOT replay/recommend v0 as a song. First priority: a **real sung 15–25-second chorus sample** while keeping the guitar/banjo bounce and Git/GitHub distinction. Then consider a shareable 60-second classroom cut.
