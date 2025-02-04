<<<<<<< HEAD
from tkinter import *

root = Tk()
root.geometry("900x700")
root.title("Scroll Bar tutorial")

# Creating a scrollbar for the listbox using Scrollbar()
sc = Scrollbar(root)
sc.pack(side=RIGHT, fill = Y)

li = Listbox(root, yscrollcommand= sc.set)
for i in range(1, 500) : 
    li.insert(END, f"Item {str(i)}")
    

li.pack(fill="both")    # "both" used for expanding the scrolls vertically and horizontally
sc.config(command=li.yview)

=======
from tkinter import *

root = Tk()
root.geometry("900x700")
root.title("Scroll Bar tutorial")

# Creating a scrollbar for the listbox using Scrollbar()
sc = Scrollbar(root)
sc.pack(side=RIGHT, fill = Y)

li = Listbox(root, yscrollcommand= sc.set)
for i in range(1, 500) : 
    li.insert(END, f"Item {str(i)}")
    

li.pack(fill="both")    # "both" used for expanding the scrolls vertically and horizontally
sc.config(command=li.yview)

>>>>>>> fc6ade0 (Updates)
root.mainloop()