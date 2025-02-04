from tkinter import * 

# Functions
def exitfile() : 
    pass

def savefile() : 
    pass

def openfile() : 
    pass

def newfile() : 
    pass






if __name__ == "__main__" : 
    root = Tk()
    root.geometry("900x700")
    root.title("Untitled - Notebook")
    

    # Add text area 
    textar = Text(root, font="lucida 13")
    
    file = None

    # Menu Bar 
    men = Menu(root)
    fil = Menu(men, tearoff=0)
    
# File Menu
    fil.add_command(label="New", command = newfile)    # To open new file 
    fil.add_command(label = "open", command = openfile)   # To open already existed file 
    fil.add_command(label="Save", command = savefile)  # To save the file 
    fil.add_separator()
    fil.add_command(label = "Exit", command = exitfile)
    men.add_cascade(label="File", menu=men)
    
# Edit Menu 
    ed = Menu(men, tearoff=0)
    ed.add_command(label = "Cut", command = cut)
    ed.add_command(label = "Copy", command = copy)
    ed.add_command(label = "Paste", command = paste)
    
    
    root.config(menu=men)
    
    
    
    











    root.mainloop()