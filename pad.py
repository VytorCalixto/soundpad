# -*- coding: utf-8 -*-
from Tkinter import Frame, Button, Label, Scale, HORIZONTAL, RAISED, Checkbutton
import tkFileDialog
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

        self.title = Label(self.frame, text="No sound")
        self.title.grid(row=0, columnspan=2)

        self.play = Button(self.frame, text="Play")
        self.play.grid(row=1)

        self.open = Button(self.frame, text="Open", command=self.onOpen)
        self.open.grid(row=1, column=1)

        self.loop = Checkbutton(self.frame, text="Loop")
        self.loop.grid(row=2, columnspan=2)

        self.volume = Scale(self.frame, from_=0, to=100, orient=HORIZONTAL)
        self.volume.grid(row=3, columnspan=2)

    def setTitle(self, text):
        self.title.config(text=text)

    def onOpen(self):
        ftypes = [('MP3 files', '*.mp3'), ('WAV files', '*.wav'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        filename = dlg.show()

        if filename != '':
            self.loadSound(filename)

    def onPlay(self):
        print "click"
        if self.sound is not None:
            self.sound.play()

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
