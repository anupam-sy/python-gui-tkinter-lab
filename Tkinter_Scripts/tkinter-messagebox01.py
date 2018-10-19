from tkinter import *

root = Tk()

messagebox.showinfo("Info Title", "This is the tkinter tutorial")
ans = messagebox.askquestion("Quiz", "do you like python?")
if(ans == "yes"):
    print("welcome to the World OF Python.")
else:
    print("Sorry, you may leave now.")

root.mainloop() 

"""
NOTE: askquestion returns 'yes' for "Yes", or 'no' for "No".
"""
