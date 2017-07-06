from tkinter import Frame, Button, LEFT, Label, StringVar, filedialog
from grid import Grid
import pickle

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.config()

        self.frame = Frame(master)
        self.frame.focus_set()
        self.frame.pack()

        self.savefile = None

        self.keyHistory = []

        self.text = StringVar()
        self.label = Label(self.frame, textvariable=self.text)
        self.label.pack()

        gridWidth = 3
        gridHeight = 3
        self.padGrid = Grid(self.frame, gridWidth, gridHeight)
        self.frame.bind("<KeyPress>", self.keydown)
        self.frame.bind("<KeyRelease>", self.keyup)

    def keyup(self, e):
        key = (e.keycode, e.char)
        # print key
        if key in self.keyHistory:
            self.keyHistory.pop(self.keyHistory.index(key))
            self.text.set(str(self.keyHistory))

            self.keyupHandler(key)

    def keydown(self, e):
        key = (e.keycode, e.char)
        # print key
        if not key in self.keyHistory:
            self.keyHistory.append(key)
            self.text.set(str(self.keyHistory))
            self.keydownHandler(key)

    def keydownHandler(self, key):
        keycode = key[0]
        keychar = key[1]
        if keychar == '0':
            self.padGrid.stopAll()
        try:
            if int(keychar) >= 1 and int(keychar) <= 9:
                self.padGrid.keydownPad(int(keychar))
        except:
            pass

    def keyupHandler(self, key):
        keycode = key[0]
        keychar = key[1]
        try:
            if int(keychar) >= 1 and int(keychar) <= 9:
                self.padGrid.keyupPad(int(keychar))
        except:
            pass

    def open(self):
        ftypes = (("Soundpad Save Files", "*.sdp"), ("All Files", "*"))
        filename = filedialog.askopenfilename(title="Open a session", filetypes=ftypes)

        if filename:
            self.savefile = filename
            self.loadSavefile()

    def loadSavefile(self):
        savefile = open(self.savefile, "rb")
        sounds = pickle.load(savefile)
        print("Load!")
        print(str(sounds))
        w = self.padGrid.width
        h = self.padGrid.height
        for x in range(w):
            for y in range(h):
                index = x * h + y
                info = sounds[index]
                pad = self.padGrid.grid[index]
                pad.soundVolume.set(info["volume"])
                pad.looping.set(info["loop"])
                pad.isSensitive.set(info["sensitive"])
                pad.loadSound(info["filename"])

    def save(self):
        if self.savefile is None:
            self.saveAs()
        else:
            self.writeSavefile()

    def saveAs(self):
        ftypes = (("Soundpad Save Files", "*.sdp"), ("All Files", "*"))
        filename = filedialog.asksaveasfilename(initialfile="session1.sdp", filetypes=ftypes)

        if filename:
            self.savefile = filename
            self.writeSavefile()

    def writeSavefile(self):
        print (self.savefile)
        savefile = open(self.savefile, 'wb')
        w = self.padGrid.width
        h = self.padGrid.height
        sounds = []
        for x in range(w):
            for y in range(h):
                index = x * h + y
                pad = self.padGrid.grid[index]
                info = {"filename": pad.filename, "loop": pad.looping.get(), \
                    "volume": pad.soundVolume.get(), "sensitive": pad.isSensitive.get()}
                sounds.append(info)
        print(str(sounds))
        pickle.dump(sounds, savefile)
        savefile.close()

    def update(self):
        self.padGrid.update()
