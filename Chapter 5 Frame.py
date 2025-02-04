<<<<<<< HEAD
from tkinter import * 

root = Tk()
root.geometry("700x700")

# Used to create frames or box type shape 
f1 = Frame(root, bg="black", borderwidth = 3, relief=SUNKEN)
l1 = Label(f1, text = "Chapter Nothing.exe", bg="white", font="Helvetica 15 bold")
f2 = Frame(root, bg="Grey", borderwidth = 4, relief=SUNKEN)
l2 = Label(f2, text = "Typing area", bg = "grey")

f1.pack(side = LEFT, fill="y")
l1.grid(row = 0, column = 0)
f2.pack(side=TOP, fill="x")
l2.pack(side=TOP)

root.mainloop()
=======
from tkinter import * 

root = Tk()
root.geometry("700x700")

# Used to create frames or box type shape 
f1 = Frame(root, bg="black", borderwidth = 3, relief=SUNKEN)
l1 = Label(f1, text = "Chapter Nothing.exe", bg="white", font="Helvetica 15 bold")
f2 = Frame(root, bg="Grey", borderwidth = 4, relief=SUNKEN)
l2 = Label(f2, text = "Typing area", bg = "grey")

f1.pack(side = LEFT, fill="y")
l1.grid(row = 0, column = 0)
f2.pack(side=TOP, fill="x")
l2.pack(side=TOP)

root.mainloop()
>>>>>>> fc6ade0 (Updates)
