# Implementation of Self Adjustment in tkinter

from tkinter import *

root = Tk()
root.title("Self Adjustment Implementation")
root.geometry("200x100")

button_01 = Button(root, text="Click me", bg="red")
button_01.pack(fill=X)
button_02 = Button(root, text="Click me", bg="green")
button_02.pack(side=LEFT, fill=Y)

root.mainloop()
