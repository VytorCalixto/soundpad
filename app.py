from Tkinter import Frame, Button, LEFT

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.focus_set()
        frame.pack()

        self.button = Button(frame, text="Play")
        self.button.pack(side=LEFT)

    def setPlayCallback(self, cb, text):
        self.button.config(command=cb, text=text)
