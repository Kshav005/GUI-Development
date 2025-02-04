<<<<<<< HEAD
from tkinter import *


# Entries are the input field in which a user is required to fill in some information
def getinfo() : 
    print(f"Username =", userinfo.get())      # The value stored in the variables can be obtained using "variable.get()" and it will return the value 
    print(f"Password =", passinfo.get())

root = Tk()
root.geometry("1000x1000")

user = Label(root, text = "Username : ", font = "comicsansms 14 bold")
password = Label(root, text = "Password : ", font = "comicsansms 14 bold")
user.grid()
password.grid(row = 1)


# 4 Variable Classes in TKinter -- BooleanVar, DoubleVar, IntVar, StringVar

userinfo = StringVar()
passinfo = StringVar()

userin = Entry(root, textvariable=userinfo)
passin = Entry(root, textvariable=passinfo)

userin.grid(row = 0, column = 1)
passin.grid(row = 1, column = 1 )

Button(root, text="Submit", command = getinfo).grid()

=======
from tkinter import *


# Entries are the input field in which a user is required to fill in some information
def getinfo() : 
    print(f"Username =", userinfo.get())      # The value stored in the variables can be obtained using "variable.get()" and it will return the value 
    print(f"Password =", passinfo.get())

root = Tk()
root.geometry("1000x1000")

user = Label(root, text = "Username : ", font = "comicsansms 14 bold")
password = Label(root, text = "Password : ", font = "comicsansms 14 bold")
user.grid()
password.grid(row = 1)


# 4 Variable Classes in TKinter -- BooleanVar, DoubleVar, IntVar, StringVar

userinfo = StringVar()
passinfo = StringVar()

userin = Entry(root, textvariable=userinfo)
passin = Entry(root, textvariable=passinfo)

userin.grid(row = 0, column = 1)
passin.grid(row = 1, column = 1 )

Button(root, text="Submit", command = getinfo).grid()

>>>>>>> fc6ade0 (Updates)
root.mainloop()