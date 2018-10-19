# Implementation of Statusbar in tkinter

from tkinter import *

root = Tk()
root.title("Statusbar Implementation")
root.geometry("200x50")

def response():
    print("Button clicked.")

toolbar = Frame(root, bg="gray")
toolbar.pack(side=TOP, fill=X)
button01 = Button(toolbar, text="Insert", command=response)
button01.pack(side=LEFT, padx=2, pady=3)

button02 = Button(toolbar, text="Delete", command=response)
button02.pack(side=LEFT, padx=2, pady=3)

statusbar = Label(root, text="Thanks for visiting.", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()

"""
Note: Status bar is nothing but simply a label generally packed at the bottom. 
"""
