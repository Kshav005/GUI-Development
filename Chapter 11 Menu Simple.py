from tkinter import * 

# We are going to create menu bar using all the things we have learnt!
def file() : 
    print("You opened a file!")
def edit() : 
    print("You clicked on edit button!")
def view(): 
    print("You clicked on view button!")


root = Tk()
root.geometry("700x700")
root.title("Namaste India.exe")



# Creating menu options
men = Menu(root)
men.add_command(label="File", command = file)
men.add_command(label = "Edit", command = edit)
men.add_command(label = "View", command = view)
men.add_command(label="Exit", command = quit)

# Used to place everythig automatically
root.config(menu=men)

root.mainloop()