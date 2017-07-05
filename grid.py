from tkinter import Frame
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
        # self.grid = [[None for x in range(self.width)] for y in range(self.height)]
        self.grid = [None for x in range(self.width * self.height)]
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x * self.height + y] = Pad(self.frame, x, y)
                self.grid[x * self.height + y].setPadNumber(x * self.height + y + 1)

    def keydownPad(self, pad):
        pad = pad - 1
        if(pad > self.width*self.height):
            print("Trying to access inexistent pad")
            return
        self.grid[pad].onKeydown()

    def keyupPad(self, pad):
        pad = pad - 1
        if(pad > self.width*self.height):
            print("Trying to access inexistent pad")
            return
        self.grid[pad].onKeyup()

    def stopAll(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x * self.height + y].onStop()

    def update(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x * self.height + y].update()
