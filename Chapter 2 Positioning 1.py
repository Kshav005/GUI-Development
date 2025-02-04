from tkinter import *

root = Tk()

myLabel1 = Label(root, text = "Hello there")
myLabel2 = Label(root, text = "My name is hehe.")

# Grid is used to position elements more easily and effeciently, place can also be used!
myLabel1.grid(row = 0, column= 0)
myLabel2.grid(row = 1, column = 2)

root.mainloop()