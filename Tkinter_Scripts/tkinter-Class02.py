from tkinter import *

class MyApp():
 
    #----------------------------------------------------------------------
    
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("My APP")
        self.frame = Frame(self.root)
        self.frame.pack()
 
        btn = Button(self.frame, text="Initial window", command=self.openTopWindow)
        btn.pack()
 
    #----------------------------------------------------------------------
        
    def hide(self):
        """"""
        self.root.withdraw()
 
    #----------------------------------------------------------------------
        
    def openTopWindow(self):
        """"""
        self.hide()
        topWindow = Toplevel()
        topWindow.geometry("400x300")
        topWindow.title("otherFrame")
        handler = lambda: self.onCloseOtherWindow(topWindow)
        btn = Button(topWindow, text="Close Window", command=handler)
        btn.pack()
 
    #----------------------------------------------------------------------
        
    def onCloseOtherWindow(self, topWindow):
        """"""
        topWindow.destroy()
        self.show()
 
    #----------------------------------------------------------------------
        
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()
 
#----------------------------------------------------------------------

if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    AppObj = MyApp(root)
    root.mainloop()
