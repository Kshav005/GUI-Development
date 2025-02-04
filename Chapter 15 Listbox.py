<<<<<<< HEAD
from tkinter import * 

root = Tk()
root.geometry("900x700")
root.title("Listbox tutorial")      # shows list of alternatives

# Listbox() used to create a box in which there are various options are given
a = Listbox(root)
a.pack()
a.insert(END, "First item of a listbox")
a.insert(END, "Firstlistbox")
a.insert(END, "First itemtbox")
a.insert(END, "First item oistbox")

=======
from tkinter import * 

root = Tk()
root.geometry("900x700")
root.title("Listbox tutorial")      # shows list of alternatives

# Listbox() used to create a box in which there are various options are given
a = Listbox(root)
a.pack()
a.insert(END, "First item of a listbox")
a.insert(END, "Firstlistbox")
a.insert(END, "First itemtbox")
a.insert(END, "First item oistbox")

>>>>>>> fc6ade0 (Updates)
root.mainloop()