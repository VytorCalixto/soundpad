# -*- coding: utf-8 -*-
from tkinter import Frame, Button, Label, Scale, HORIZONTAL, RAISED, Checkbutton, IntVar, DoubleVar, filedialog
import os
from pydub import AudioSegment
from audioMixer import AudioMixer
import math

class Pad(Frame):
    def __init__(self, master, x, y):
        Frame.__init__(self, master)
        self.master.config()

        self.frame = Frame(master, bd=2, relief=RAISED, bg="#BDBDBD")
        self.frame.grid(row=x, column=y)

        self.sound = None
        self.channel = None
        self.filename = None

        self.padNumber = Label(self.frame, text="PAD - ")
        self.padNumber.grid(row=0, columnspan=2)

        self.title = Label(self.frame, text="No sound")
        self.title.grid(row=1, columnspan=2)

        self.play = Button(self.frame, text="▶")
        self.play.grid(row=2)

        self.open = Button(self.frame, text="Load", command=self.onOpen)
        self.open.grid(row=2, column=1)

        self.looping = IntVar()
        self.loopBt = Checkbutton(self.frame, text="Loop", variable=self.looping, \
            command=self.onLoop, onvalue=-1, offvalue=0)
        self.loopBt.grid(row=3)

        self.isSensitive = IntVar()
        self.sensitive = Checkbutton(self.frame, text="Sensitive", variable=self.isSensitive)
        self.sensitive.grid(row=3, column=1)

        self.soundVolume = DoubleVar()
        self.soundVolume.set(1.0)
        self.volume = Scale(self.frame, from_=0, to=1, orient=HORIZONTAL,\
            resolution=0.01, label="Volume", showvalue=0, variable=self.soundVolume,\
            command=self.onVolume)
        self.volume.grid(row=4, columnspan=2)

    def setPadNumber(self, text):
        self.padNumber.config(text=text)

    def setTitle(self, text):
        self.title.config(text=text)

    def onLoop(self):
        if self.sound is None:
            return
        if self.looping.get() != -1:
            fadeout = int(math.ceil(self.sound.get_length()/3)) * 1000
            if fadeout < 3000:
                fadeout = 3000
            if fadeout > 5000:
                fadeout = 5000
            self.sound.fadeout(fadeout)

    def onVolume(self, val):
        if self.sound is None:
            return
        self.sound.set_volume(self.soundVolume.get())

    def onPlay(self):
        if self.sound is None:
            return
        # Limit to one channel only
        if self.sound.get_num_channels() > 0:
            self.sound.stop()
        self.sound.set_volume(self.soundVolume.get())
        self.channel = self.sound.play(loops=self.looping.get(), fade_ms=1000)

    def onStop(self):
        if self.sound is None:
            return
        self.sound.fadeout(1500)
        self.returnToPlay()

    def returnToPlay(self):
        self.play.config(text="▶", command=self.onPlay)

    def returnToStop(self):
        self.play.config(text="⏹", command=self.onStop)

    def onOpen(self):
        ftypes = (('OGG files', '*.ogg'),('MP3 files', "*.mp3;"),('WAV files', '*.wav'),("All Files", "*"))
        filename = filedialog.askopenfilename(initialdir="~", title="Open a sound", filetypes=ftypes)

        if filename:
            self.loadSound(filename)

    def loadSound(self, filename):
        if filename is None:
            return
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

    def onKeydown(self):
        self.frame.config(bg="#eeaa00")
        if self.channel is None:
            self.onPlay()
            return

        if self.channel.get_sound() == self.sound and self.channel.get_busy():
            self.onStop()
        else:
            self.onPlay()

    def onKeyup(self):
        self.frame.config(bg="#bdbdbd")
        if self.isSensitive.get() == 1:
            self.onStop()

    def update(self):
        if self.channel is not None:
            sound = self.channel.get_sound()
            if sound == self.sound:
                if self.channel.get_busy():
                    self.returnToStop()
                    return
                else:
                    self.returnToPlay()
                    return
            else:
                self.returnToPlay()
                return
        self.returnToPlay()
        return
