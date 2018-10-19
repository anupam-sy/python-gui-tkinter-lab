from tkinter import *

root = Tk()

filename = filedialog.asksaveasfilename(initialdir = "D:\\", title = "Select file")
print("You have saved the file name : ", filename)

root.mainloop()

"""
NOTE: The tkFileDialog module provides two different pop-up windows you can
use to give the user the ability to find existing files or create new files.

2. asksaveasfilename() : Intended for cases where the user wants to create a
new file or replace an existing file. If the user selects an existing file,
a pop-up will appear informing that the file already exists, and asking if
they really want to replace it.
"""
