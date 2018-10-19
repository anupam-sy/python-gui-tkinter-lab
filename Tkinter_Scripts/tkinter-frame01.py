# Implementation of Frames in tkinter

from tkinter import *

root = Tk()
root.title("Frame Implementation")
root.geometry("200x50")

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button_01 = Button(topFrame, text="Click me", bg="red")
button_01.pack()
button_02 = Button(bottomFrame, text="Click me", bg="green")
button_02.pack()

root.mainloop()
