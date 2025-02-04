<<<<<<< HEAD
from tkinter import *

# Creating sub menu for the menu options, kind of a dropdown

def hey() : 
    print("Clicked!")

root = Tk()
root.geometry("900x800")
root.title("Dropdown.exe")

men = Menu(root)

# tearoff with the value 0 is used to disable the dropdown menu to open in a seperate window
men1 = Menu(men, tearoff = 0)
men1.add_command(label="NOthing", command = hey)
men1.add_command(label="No", command = hey)
men1.add_separator()     # Used to make a seperating line the menu
men1.add_command(label="Never", command = hey)
men1.add_command(label="Ethan", command = hey)
men1.add_command(label="Ethanol", command = hey)
men1.add_command(label="Ethano", command = hey)
men1.add_command(label="Ethan", command = hey)
men1.add_separator()
men1.add_command(label="Etha", command = hey)
men1.add_command(label="Eth", command = hey)
men1.add_command(label="E", command = hey)
men1.add_command(label="Et", command = hey)
men1.add_command(label="Ett", command = hey)

men2 = Menu(men, tearoff = 0)
men2.add_command(label="Meow", command = hey)
men2.add_command(label="am", command = hey)
men2.add_separator()
men2.add_command(label="Cat", command = hey)
men2.add_command(label="Ean", command = hey)
men2.add_command(label="Etnol", command = hey)
men2.add_command(label="Etan", command = hey)
men2.add_command(label="Ethan", command = hey)
men2.add_separator()
men2.add_command(label="Ea", command = hey)
men2.add_command(label="Eh", command = hey)
men2.add_command(label="E", command = hey)
men2.add_command(label="Etr3", command = hey)
men2.add_command(label="Etgt", command = hey)

men.add_cascade(label = "File", menu = men1)       # use ".add_cascade" to create the sub menu
men.add_cascade(label = "Edit", menu = men2)

root.config(menu=men)

=======
from tkinter import *

# Creating sub menu for the menu options, kind of a dropdown

def hey() : 
    print("Clicked!")

root = Tk()
root.geometry("900x800")
root.title("Dropdown.exe")

men = Menu(root)

# tearoff with the value 0 is used to disable the dropdown menu to open in a seperate window
men1 = Menu(men, tearoff = 0)
men1.add_command(label="NOthing", command = hey)
men1.add_command(label="No", command = hey)
men1.add_separator()     # Used to make a seperating line the menu
men1.add_command(label="Never", command = hey)
men1.add_command(label="Ethan", command = hey)
men1.add_command(label="Ethanol", command = hey)
men1.add_command(label="Ethano", command = hey)
men1.add_command(label="Ethan", command = hey)
men1.add_separator()
men1.add_command(label="Etha", command = hey)
men1.add_command(label="Eth", command = hey)
men1.add_command(label="E", command = hey)
men1.add_command(label="Et", command = hey)
men1.add_command(label="Ett", command = hey)

men2 = Menu(men, tearoff = 0)
men2.add_command(label="Meow", command = hey)
men2.add_command(label="am", command = hey)
men2.add_separator()
men2.add_command(label="Cat", command = hey)
men2.add_command(label="Ean", command = hey)
men2.add_command(label="Etnol", command = hey)
men2.add_command(label="Etan", command = hey)
men2.add_command(label="Ethan", command = hey)
men2.add_separator()
men2.add_command(label="Ea", command = hey)
men2.add_command(label="Eh", command = hey)
men2.add_command(label="E", command = hey)
men2.add_command(label="Etr3", command = hey)
men2.add_command(label="Etgt", command = hey)

men.add_cascade(label = "File", menu = men1)       # use ".add_cascade" to create the sub menu
men.add_cascade(label = "Edit", menu = men2)

root.config(menu=men)

>>>>>>> fc6ade0 (Updates)
root.mainloop()