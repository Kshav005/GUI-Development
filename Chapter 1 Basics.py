from tkinter import * 

# Making A Label Widget (used to write texts)
root = Tk()
myLabel = Label(root, text = "Hello World!")

# Used to position things in the widget
myLabel.pack()

# .mainloop is used to create an infinite loop for the GUI app
root.mainloop()