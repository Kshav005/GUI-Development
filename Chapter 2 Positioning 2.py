from tkinter import * 

root = Tk()

label1 = Label(root, text = "Meow")


# Used to set a default size of the window (width x height)
root.geometry("500x500")

# Used to set a minimum size (width, height)
root.minsize(500, 500)

# Used to set a maximum size (width, height)
root.maxsize(700, 700)

label1.pack()
root.mainloop()