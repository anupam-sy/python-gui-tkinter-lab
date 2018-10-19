# Implementation of Lables and Buttons in tkinter

from tkinter import *

def response():
    print("Button clicked.")

def app(root):
    label_01 = Label(root, text="I am Anupam Yadav.")
    label_01.pack()

    button_01 = Button(root, text="OK", command=response)
    button_01.pack()

if __name__ == "__main__":
    root = Tk()
    root.title("Labels and Buttons Implementation")
    root.geometry("200x50")
    app(root)
    root.mainloop()
