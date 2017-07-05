# -*- coding: utf-8 -*-
from tkinter import Frame, Button, Label, Scale, HORIZONTAL, RAISED, Checkbutton, IntVar, DoubleVar, filedialog
import os
from pydub import AudioSegment
from audioMixer import AudioMixer

class Pad(Frame):
    def __init__(self, master, x, y):
        Frame.__init__(self, master)
        self.master.config()

        self.frame = Frame(master, bd=2, relief=RAISED)
        self.frame.grid(row=x, column=y)

        self.sound = None
        self.filename = ""

        self.title = Label(self.frame, text="No sound")
        self.title.grid(row=0, columnspan=2)

        self.play = Button(self.frame, text="Play")
        self.play.grid(row=1)

        self.open = Button(self.frame, text="Open", command=self.onOpen)
        self.open.grid(row=1, column=1)

        self.looping = IntVar()
        self.loopBt = Checkbutton(self.frame, text="Loop", variable=self.looping, \
            command=self.onLoop, onvalue=-1, offvalue=0)
        self.loopBt.grid(row=2, columnspan=2)

        self.soundVolume = DoubleVar()
        self.soundVolume.set(1.0)
        self.volume = Scale(self.frame, from_=0, to=1, orient=HORIZONTAL,\
            resolution=0.01, label="Volume", showvalue=0, variable=self.soundVolume,\
            command=self.onVolume)
        self.volume.grid(row=3, columnspan=2)

    def setTitle(self, text):
        self.title.config(text=text)

    def onOpen(self):
        ftypes = [('MP3 files', '*.mp3'), ('WAV files', '*.wav'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        filename = dlg.show()

        if filename != '':
            self.loadSound(filename)

    def onLoop(self):
        if self.sound is None:
            return
        if(self.looping.get() > -1):
            self.sound.fadeout(1000)
            self.play.config(text="Play")

    def onVolume(self, val):
        if self.sound is None:
            return
        print(self.soundVolume.get())
        self.sound.set_volume(self.soundVolume.get())

    def onPlay(self):
        if self.sound is None:
            return
        print(self.sound.get_num_channels())
        if self.sound.get_num_channels() > 0:
            self.sound.stop()
            self.play.config(text="Play")
        else:
            self.sound.set_volume(self.soundVolume.get())
            self.sound.play(self.looping.get())
            self.play.config(text="Stop")

    def loadSound(self, filename):
        extension = os.path.splitext(filename)[1]
        name = os.path.basename(os.path.splitext(filename)[0])
        fl = filename
        if extension == ".mp3":
            original = AudioSegment.from_mp3(filename)
            # TODO: definir antes uma pasta onde salvar os arquivos da sessão
            fl = os.path.join(os.getcwd(), "data", name+".wav")
            original.export(fl, format="wav")
        self.sound = AudioMixer.mixer.Sound(fl)
        self.play.config(command=self.onPlay)
        self.setTitle(name)
        self.filename = fl
