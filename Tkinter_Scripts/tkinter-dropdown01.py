# Implementation of Dropdown in tkinter

from tkinter import *

root = Tk()
root.title("Dropdown Implementation")
root.geometry("200x50")

def response():
    print("Button clicked.")

# create a menubar
menubar = Menu(root)

# configure root to use that menubar
# display the menu
root.config(menu=menubar)

# Add items in menu bar
menubar.add_command(label="Hello!", command=response)
menubar.add_command(label="Quit!", command=root.quit)

root.mainloop()

"""
Note: Pulldown menus (and other submenus) are created in a similar fashion.
The main difference is that they are attached to a parent menu
(using add_cascade), instead of a toplevel window.
See the example: tkinter-dropdown02.py
"""
