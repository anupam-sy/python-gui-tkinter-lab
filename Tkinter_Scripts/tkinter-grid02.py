# Implementation of Grid in tkinter for placing widgets instead of Pack.

from tkinter import *

def app(root):
    
    label_01 = Label(root, text="User ID: ")
    label_01.grid(row=0, column=0)
    label_02 = Label(root, text="Password: ")
    label_02.grid(row=1, column=0)

    entry_01 = Entry(root)
    entry_01.grid(row=0, column=1)
    entry_01.focus_set() # To set focus on this entry filed.
    entry_02 = Entry(root, show="*")
    entry_02.grid(row=1, column=1)

    label = Label(root, text="TEST-IMAGE-CONFIGURATION")
    label.grid(row=0, column=2, columnspan=2, rowspan=2)

    button_01 = Button(root, text="Submit")
    button_01.grid(row=2, column=0, columnspan=2)
    button_02 = Button(root, text="Cancel")
    button_02.grid(row=2, column=2, columnspan=2)

if __name__ == "__main__":
    root = Tk()
    root.title("Grid Implementation")
    root.geometry("400x100")
    app(root)
    root.mainloop()
