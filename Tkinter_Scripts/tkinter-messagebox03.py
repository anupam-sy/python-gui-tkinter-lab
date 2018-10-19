from tkinter import *

root = Tk()

messagebox.showinfo("Info Title", "This is the tkinter tutorial")
ans = messagebox.askokcancel("Quiz", "Want to proceed?")
if(ans == True):
    print("welcome to the World OF Python.")
else:
    print("Sorry, you may leave now.")

root.mainloop()

"""
NOTE: askokcancel, askretrycancel, and askyesno all return a bool value:
      True for "OK" or "Yes" choices, False for "No" or "Cancel" choices.
"""
