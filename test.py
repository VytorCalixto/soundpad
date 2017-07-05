#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from tkinter import Tk, Button
from pygame import mixer
from pydub import AudioSegment

os.system('xset r off')

root = Tk()
root.title("Soundpad")
root.geometry("640x480+50+50")

def click():
    print("Click!")

clickBt = Button(root, text="Botão", command=click)
clickBt.pack()

mixer.init()
original = AudioSegment.from_mp3('piano-stab.mp3')
original.export('/tmp/piano-stab.wav', format='wav')
effect = mixer.Sound('/tmp/piano-stab.wav')
def keyup(e):
    print('up', e.char)
    effect.stop()
def keydown(e):
    print('down', e.char)
    effect.play()

root.bind("<KeyPress>", keydown)
root.bind("<KeyRelease>", keyup)

root.mainloop()
os.system('xset r on')
