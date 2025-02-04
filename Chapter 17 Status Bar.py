from tkinter import *

# Creating a status bar which is situated in the bottom. In MS word, the status bar shows the number of words written on the document with some other useful options
root = Tk()
root.title("Status Bar")
root.geometry("900x700")

stat = StringVar()
stat.set("Ready!")
sbar = Label(root, textvariable=stat, anchor="w", relief=SUNKEN)

sbar.pack(side = BOTTOM, fill = X)

root.mainloop()