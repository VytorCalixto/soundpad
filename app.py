from tkinter import Frame, Button, LEFT
from grid import Grid

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.config()

        self.frame = Frame(master)
        self.frame.focus_set()
        self.frame.pack()

        gridWidth = 3
        gridHeight = 3
        self.padGrid = Grid(self.frame, gridWidth, gridHeight)
