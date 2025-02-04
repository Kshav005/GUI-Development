<<<<<<< HEAD
from tkinter import * 

# A complex but easy way to create a GUI window. For all this stuff, you need to know the class in python basics

class GUI(Tk): 
    def __init__(self) : 
        super().__init__()
        self.geometry("900x700")
        
    def addbutton(self, t) : 
        Button(text=t, bg = "black", fg = "white").pack()

if __name__ == "__main__" : 
    window = GUI()
    window.addbutton("Nice")
    window.addbutton("hello")
    window.mainloop()

=======
from tkinter import * 

# A complex but easy way to create a GUI window. For all this stuff, you need to know the class in python basics

class GUI(Tk): 
    def __init__(self) : 
        super().__init__()
        self.geometry("900x700")
        
    def addbutton(self, t) : 
        Button(text=t, bg = "black", fg = "white").pack()

if __name__ == "__main__" : 
    window = GUI()
    window.addbutton("Nice")
    window.addbutton("hello")
    window.mainloop()

>>>>>>> fc6ade0 (Updates)
