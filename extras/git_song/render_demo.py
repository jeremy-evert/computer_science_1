#!/usr/bin/env python3
"""Original 2/4 Git/GitHub country-comedy SKETCH: guide vocal + simple backing.

Requires Python 3 with numpy, and the espeak and ffmpeg executables. No network.
Run: python3 extras/git_song/render_demo.py
This creates an MP3; eSpeak talks in rhythm rather than singing.
"""
from __future__ import annotations
from pathlib import Path
import math
import subprocess
import tempfile
import wave

import numpy as np

SR = 24000
BPM = 124
BAR_SECONDS = 2 * 60 / BPM
LINE_SECONDS = 4 * BAR_SECONDS
HERE = Path(__file__).resolve().parent

PARTS = [
    ("INTRO", ["One, two, three! That squirrel says I forgot the push!"]),
    ("VERSE 1", [
        "Well, I changed three files on a Friday night,",
        "Had a bug in the barn, and my terminal bright,",
        "I told my buddy, Check GitHub! I fixed that code!",
        "He said, That page still shows last week's load!",
    ]),
    ("CHORUS", [
        "Git add to the stage, git commit makes it stay,",
        "Push it to the remote if your friends should see today,",
        "Git remembers local history, GitHub hosts the show,",
        "If you never push your commits, your friends will never know!",
    ]),
    ("VERSE 2", [
        "I ran git status, saw the files I'd changed,",
        "Added just the ones I wanted, kept the rest arranged,",
        "I committed with a message: Fixed the dancing goose!",
        "But the website hadn't changed. I knew I'd missed a step, caboose!",
    ]),
    ("CHORUS", [
        "Git add to the stage, git commit makes it stay,",
        "Push it to the remote if your friends should see today,",
        "Git remembers local history, GitHub hosts the show,",
        "If you never push your commits, your friends will never know!",
    ]),
    ("BRIDGE", [
        "The squirrel on the fence said, Boy, I know your plight,",
        "You saved it to your laptop and you thought that made it right,",
        "Git is version control, GitHub's where you share,",
        "A push sends your committed work to the remote over there!",
    ]),
    ("FINAL CHORUS", [
        "Git add to the stage, git commit makes it stay,",
        "Push it to the remote if your friends should see today,",
        "Git remembers local history, GitHub hosts the show,",
        "If you never push your commits, your friends will never know!",
    ]),
    ("OUTRO", [
        "So I typed git push; my buddy said, Well I'll be!",
        "Then that squirrel stole my peanuts and stole the harmony!",
    ]),
]

# Original riff: quirky I / bVII / V two-step; not borrowed from another song.
CHORDS = [
    ([196.0, 246.94, 293.66], 98.0),
    ([196.0, 246.94, 293.66], 98.0),
    ([174.61, 220.0, 261.63], 87.31),
    ([146.83, 185.0, 220.0], 73.42),
]


def render() -> Path:
    lines = [(section, line) for section, group in PARTS for line in group]
    duration = (len(lines) + 1) * LINE_SECONDS
    size = math.ceil(duration * SR)
    backing = np.zeros(size, dtype=np.float32)
    rng = np.random.default_rng(20261009)

    def layer(start, sound, gain=1.0):
        index = int(start * SR)
        length = min(len(sound), size - index)
        if length > 0:
            backing[index:index + length] += gain * sound[:length]

    def pluck(freq, seconds, decay=7, bright=.2):
        t = np.arange(int(seconds * SR), dtype=np.float32) / SR
        env = np.minimum(1.0, t/.004) * np.exp(-decay*t)
        return env * (np.sin(2*np.pi*freq*t)
                      + bright*np.sin(4*np.pi*freq*t))

    def hat(seconds=.055):
        t = np.arange(int(seconds * SR), dtype=np.float32) / SR
        return rng.standard_normal(t.size).astype(np.float32)*np.exp(-65*t)

    for li, (section, _) in enumerate(lines):
        start = li*LINE_SECONDS
        for bar in range(4):
            at = start + bar*BAR_SECONDS
            chord, bass = CHORDS[(li+bar) % len(CHORDS)]
            layer(at, pluck(bass, .35, decay=9), .26)
            layer(at+BAR_SECONDS/2, pluck(bass*1.5, .25, decay=12), .18)
            t = np.arange(int(SR*.12))/SR
            kick = np.sin(2*np.pi*(65*t - 30*t*t))*np.exp(-40*t)
            layer(at, kick.astype(np.float32), .28)
            layer(at+BAR_SECONDS/2, hat(.10), .095)
            for eighth in range(4):
                at8 = at+eighth*BAR_SECONDS/4
                freq = chord[(bar+eighth)%3]*(2 if eighth%2 == 0 else 1)
                layer(at8, pluck(freq, .16, decay=22, bright=.6), .12)
                layer(at8, hat(.04), .03)
        if "CHORUS" in section:
            for beat, freq in [(0,392),(2,440),(4,493.88),(6,392)]:
                layer(start+beat*60/BPM, pluck(freq,.18,decay=14), .075)

    vocals = np.zeros(size, dtype=np.float32)
    with tempfile.TemporaryDirectory(prefix="git-song-") as scratch:
        for i, (section, words) in enumerate(lines):
            file = Path(scratch)/f"line_{i:02d}.wav"
            pitch = 67 if "CHORUS" in section else (
                49 if section == "BRIDGE" else 60)
            subprocess.run(
                ["espeak","-v","en-us+m3","-s","193","-p",str(pitch),
                 "-a","190","-w",str(file),words],
                check=True, capture_output=True)
            with wave.open(str(file),"rb") as wavefile:
                rate=wavefile.getframerate()
                channels=wavefile.getnchannels()
                raw=wavefile.readframes(wavefile.getnframes())
            voice=np.frombuffer(raw,dtype=np.int16).astype(np.float32)/32768
            if channels>1:
                voice=voice.reshape(-1,channels).mean(axis=1)
            new_n=max(1,int(len(voice)*SR/rate))
            voice=np.interp(np.linspace(0,len(voice)-1,new_n),
                            np.arange(len(voice)),voice).astype(np.float32)
            limit=int((LINE_SECONDS-.35)*SR)
            if len(voice)>limit:
                voice=np.interp(np.linspace(0,len(voice)-1,limit),
                                np.arange(len(voice)),voice).astype(np.float32)
            fade=min(len(voice)//10,int(.04*SR))
            if fade:
                voice[:fade] *= np.linspace(0,1,fade)
                voice[-fade:] *= np.linspace(1,0,fade)
            offset=int((i*LINE_SECONDS+.20)*SR)
            vocals[offset:offset+len(voice)] += .58*voice

    result=.65*backing+vocals
    peak=float(np.max(np.abs(result)))
    if peak>.94:
        result *= .94/peak
    outfile=HERE/"git_aint_github_scrappy_v0.mp3"
    with tempfile.TemporaryDirectory(prefix="git-song-wave-") as scratch:
        tempwav=Path(scratch)/"master.wav"
        with wave.open(str(tempwav),"wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(SR)
            wf.writeframes((np.clip(result,-1,1)*32767)
                            .astype("<i2").tobytes())
        subprocess.run(
            ["ffmpeg","-hide_banner","-loglevel","error","-y","-i",
             str(tempwav),"-codec:a","libmp3lame","-b:a","192k",str(outfile)],
            check=True)
    print(f"Ready: {outfile}; {duration:.1f} seconds; {len(lines)} lines")
    return outfile


if __name__ == "__main__":
    render()
