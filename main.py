#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from tkinter import Tk, Menu
from audioMixer import AudioMixer
from app import App

# Disables key repetition
os.system('xset r off')

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.title("Soundpad v0")
#root.geometry("%dx%d+0+0" % (w, h))
root.configure(background="#535353")

AudioMixer.mixer.init()
AudioMixer.mixer.set_num_channels(5*9)

app = App(root)

def exit():
    global root
    app.save()
    # Reenables key repetition
    os.system('xset r on')
    try:
        AudioMixer.mixer.quit()
        root.destroy()
    except:
        print("Exiting...")

mainMenu = Menu(root)
fileMenu = Menu(mainMenu, tearoff=0)
fileMenu.add_command(label="New Session", command=app.new)
fileMenu.add_command(label="Open Session", command=app.open)
fileMenu.add_command(label="Save Session", command=app.save)
fileMenu.add_command(label="Save Session As", command=app.saveAs)
fileMenu.add_command(label="Quit", command=exit)
mainMenu.add_cascade(label="File", menu=fileMenu)
root.config(menu=mainMenu)

updateRate = 300

# Update cycle
def update():
    root.after(updateRate, update)
    app.update()

root.after(updateRate, update)

root.mainloop()

exit()
