# Implementation of Lables and Buttons in tkinter

from tkinter import *

class createApp():

    def __init__(self, root):
        label_01 = Label(root, text="I am Anupam Yadav.")
        label_01.pack()

        button_01 = Button(root, text="OK", command=self.response)
        button_01.pack()

    def response(self):
        print("Button clicked.")

if __name__ == "__main__":
    root = Tk()
    root.title("Label and Button Implementation")
    root.geometry("200x50")
    AppObj = createApp(root)
    root.mainloop()
