# Implementation of Grid in tkinter for placing widgets instead of Pack.

from tkinter import *

def app(root):

    def submit():
        print("Response submitted.")
        print("User ID:", entry_01.get(), "Password:", entry_02.get())

    def cancel():
        print("Response cleared.")
    
    label_01 = Label(root, text="User ID: ")
    label_01.grid(row=0, column=0)
    label_02 = Label(root, text="Password: ")
    label_02.grid(row=1, column=0)

    entry_01 = Entry(root)
    entry_01.grid(row=0, column=1)
    entry_01.focus_set() # To set focus on this entry filed.
    entry_02 = Entry(root, show="*")
    entry_02.grid(row=1, column=1)

    button_01 = Button(root, text="Submit", command=submit)
    button_01.grid(row=2, column=0)
    button_02 = Button(root, text="Cancel", command=cancel)
    button_02.grid(row=2, column=1)

if __name__ == "__main__":
    root = Tk()
    root.title("Grid Implementation")
    root.geometry("200x100")
    app(root)
    root.mainloop()
