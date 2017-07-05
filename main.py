#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Tkinter import Tk
from pygame import mixer
from pydub import AudioSegment
from app import App

# Disables key repetition
os.system('xset r off')

root = Tk()
root.title("Soundpad v0")
root.geometry("640x480+50+50")

mixer.init()
original = AudioSegment.from_mp3('piano-stab.mp3')
original.export('/tmp/piano-stab.wav', format='wav')
effect = mixer.Sound('/tmp/piano-stab.wav')
def btCallback():
    print "Click!"
    effect.play()

app = App(root)
app.setPlayCallback(btCallback, "Play a Sound!")

root.mainloop()
# Reenables key repetition
os.system('xset r on')
