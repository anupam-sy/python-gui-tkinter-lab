# Implementation of Lables and Buttons in tkinter

from tkinter import *

root = Tk()
root.title("Labels and Button Implementation")
root.geometry("200x50")

def response():
    print("Button clicked.")

label_01 = Label(root, text="Managed by Tkinter GUI.")
label_01.pack()

button_01 = Button(root, text="OK", command=response)
button_01.pack()

root.mainloop()
