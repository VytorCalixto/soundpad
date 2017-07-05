import Tkinter as tk
import random

def update():
    l.config(text=str(random.random()))
    root.after(1000, update)


counter = 0
def bt():
    global counter
    counter = counter + 1
    l1.config(text='Counter: %d' % (counter))


root = tk.Tk()
l = tk.Label(text='0')
l.pack()
l1 = tk.Label(text='Counter: %d' % (counter))
l1.pack()
b = tk.Button(text='Count!', command=bt)
b.pack()
root.after(1000, update)
root.mainloop()
