<<<<<<< HEAD
from tkinter import * 
import random 

# A program to get the current position of the mouse pointer
wid = random.uniform(0, 1)
hei = random.uniform(0, 1)

def fun(event) : 
    print(f"Huh? {event.x} and {event.y}")
    


root = Tk()
root.title("Anything.py")
root.geometry("900x700")

but = Button(root, text="Click Me!")

# bind() is used to bind events within some widget, here if you click the button, the current value of the mouse pointer will be printed in the terminal
but.bind("<Button-1>", fun)
but.place(relx=wid, rely=hei)

root.mainloop()


=======
from tkinter import * 
import random 

# A program to get the current position of the mouse pointer
wid = random.uniform(0, 1)
hei = random.uniform(0, 1)

def fun(event) : 
    print(f"Huh? {event.x} and {event.y}")
    


root = Tk()
root.title("Anything.py")
root.geometry("900x700")

but = Button(root, text="Click Me!")

# bind() is used to bind events within some widget, here if you click the button, the current value of the mouse pointer will be printed in the terminal
but.bind("<Button-1>", fun)
but.place(relx=wid, rely=hei)

root.mainloop()


>>>>>>> fc6ade0 (Updates)
