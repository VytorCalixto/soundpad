#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from tkinter import Tk
from audioMixer import AudioMixer
from pydub import AudioSegment
from app import App

# Disables key repetition
os.system('xset r off')

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.title("Soundpad v0")
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background="#535353")

AudioMixer.mixer.init()
AudioMixer.mixer.set_num_channels(18)
# original = AudioSegment.from_mp3('piano-stab.mp3')
# original.export('/tmp/piano-stab.wav', format='wav')
# effect = AudioMixer.mixer.Sound('/tmp/piano-stab.wav')
# def btCallback():
#     print "Click!"
#     effect.play()

app = App(root)

updateRate = 100

def update():
    root.after(updateRate, update)
    app.update()

root.after(updateRate, update)
root.mainloop()
# Reenables key repetition
os.system('xset r on')
