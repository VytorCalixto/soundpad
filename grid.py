from tkinter import Frame
from pad import Pad

class Grid(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.config()

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
        self.grid = [None for x in range(self.width * self.height)]
        for x in range(self.width):
            for y in range(self.height):
                index = x * self.height + y
                self.grid[index] = Pad(self.frame, x, y)
                self.grid[index].setPadNumber(y+1 + (self.height - x - 1) * self.height)

    def keydownPad(self, pad):
        x = self.height - int((pad - 1) / self.height) - 1
        y = (pad - 1) % self.width
        index = x * self.height + y
        if(index > self.width*self.height):
            print("Trying to access inexistent pad")
            return
        self.grid[index].onKeydown()

    def keyupPad(self, pad):
        x = self.height - int((pad - 1) / self.height) - 1
        y = (pad - 1) % self.width
        index = x * self.height + y
        if(index > self.width*self.height):
            print("Trying to access inexistent pad")
            return
        self.grid[index].onKeyup()

    def stopAll(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x * self.height + y].onStop()

    def update(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x * self.height + y].update()
