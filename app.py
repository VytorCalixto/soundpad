from tkinter import Frame, Button, LEFT, Label, StringVar
from grid import Grid

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.config()

        self.frame = Frame(master)
        self.frame.focus_set()
        self.frame.pack()

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
    def update(self):
        self.padGrid.update()
