# Implementation of Toolbar in tkinter

from tkinter import *

root = Tk()
root.title("Toolbar Implementation")
root.geometry("200x50")

def response():
    print("Button clicked.")

toolbar = Frame(root, bg="gray")
toolbar.pack(side=TOP, fill=X)

button01 = Button(toolbar, text="Insert", command=response)
button01.pack(side=LEFT, padx=2, pady=3)

button02 = Button(toolbar, text="Delete", command=response)
button02.pack(side=LEFT, padx=2, pady=3)

root.mainloop()

"""
Note: Toolbars provide a quick access to the most frequently used commands.
There is no toolbar widget in Tkinter, we can use frames to implement it. 
"""
