from tkinter import *

root = Tk()

filename = filedialog.askopenfilename(initialdir = "D:\\", title = "Select file")
print("You have opened : ", filename)

root.mainloop()

"""
NOTE: The tkFileDialog module provides two different pop-up windows you can
use to give the user the ability to find existing files or create new files.

1. askopenfilename() : Intended for cases where the user wants to select an
existing file. If the user selects a nonexistent file, a popup will appear
informing them that the selected file does not exist.
"""
