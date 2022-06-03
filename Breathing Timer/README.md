# Breathing Timer

I guess this is the first "app" that I've ever created on my own volition then.

I've been trying to practice mindfulness and relaxation techniques, and this breathing pattern was recommened:
> - Breathe in for 4 seconds
> - Hold breathe for 7 seconds
> - Breathe out for 8 seconds

<br>
<br>

## Problem:
- Its hard to keep track of the timings while working/learning. So I wanted to make a tool to help myself.

<br>
<br>

## Solution:
- Nothing spectacular. Just a simple use of `time.sleep()` for the appropriate durations.
- Initially I used a text prompt for "Breathe in, Hold, Breathe out", but this was futile. Can't look at a text prompt while working.
- So the 'reminder' had to be a sound, so I can still be notified even if this app was running in the background.
- Grabbed a stock .mp3 file for a `ping` sound.

<br>
<br>

## Learning points:

### Playing .mp3 files
- Initially, I used a simple `playsound` module.
- But the .mp3 file was too loud. And the simple module did not allow for handling of the .mp3 file apart from `play`.
- Interestingly, the solution was to use `pygame`, which allowed for changing the volume of the .mp3 file, without having to toy with the base .mp3.

<br>
<br>

## Using VScode to run .py files in dir
- Spent a good 2 hours trying to figure out why the `ping.mp3` could not be referenced by VScode when running the .py file, even when I've specifically placed them in the same working dir.
- Turns out VScode requires you to enable an option when running .py files, such that the terminal runs it from the .py dir.

<br>
<br>

## Using Markdown
- To format and type this README.
