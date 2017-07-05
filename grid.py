from Tkinter import Frame
from pad import Pad

class Grid:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.grid = None
        self.width = 0
        self.height = 0

    def __init__(self, master, w, h):
        self.frame = Frame(master)
        self.frame.pack()
        self.createGrid(w, h)

    def createGrid(self, w, h):
        self.width = w
        self.height = h
        self.grid = [[None for x in range(self.width)] for y in range(self.height)]
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y] = Pad(self.frame, x, y)
