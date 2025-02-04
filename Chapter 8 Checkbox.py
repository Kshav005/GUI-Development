<<<<<<< HEAD
from tkinter import * 

def work() : 
    print("It works!!!!!!!")


root = Tk()
root.geometry("1000x700")

Label(root, text = "Welcome to the office!", font = "monaco 20 bold", pady = 20).grid(row = 0, column = 2)
name = Label(root, text = "Enter you name : ", font = "monaco 13 italic")
phone = Label(root, text = "Enter you number : ", font = "monaco 13 italic")
gender = Label(root, text = "Gender : ", font = "monaco 13 italic")
age = Label(root, text = "Age : ", font = "monaco 13 italic")

name.grid(row=1, column = 0)
phone.grid(row=2, column = 0)
gender.grid(row=3, column = 0)
age.grid(row=4, column = 0)

name1 = StringVar()
phone1 = StringVar()
gender1 = StringVar()
age1 = StringVar()

name2 = Entry(root, textvariable=name1)
phone2 = Entry(root, textvariable=phone1)
gender2 = Entry(root, textvariable=gender1)
age2 = Entry(root, textvariable=age1)

name2.grid(row=1, column=1)
phone2.grid(row=2, column=1)
gender2.grid(row=3, column=1)
age2.grid(row=4, column=1)

# Checkbox 
chec = IntVar()     # Checkbox only contains 0 and 1 as input value
checkb = Checkbutton(root, text="Check it!")
checkb.grid(row = 5, column = 1)

Button(root, text="Submit :D", command=work).grid(row = 6, column=1)



=======
from tkinter import * 

def work() : 
    print("It works!!!!!!!")


root = Tk()
root.geometry("1000x700")

Label(root, text = "Welcome to the office!", font = "monaco 20 bold", pady = 20).grid(row = 0, column = 2)
name = Label(root, text = "Enter you name : ", font = "monaco 13 italic")
phone = Label(root, text = "Enter you number : ", font = "monaco 13 italic")
gender = Label(root, text = "Gender : ", font = "monaco 13 italic")
age = Label(root, text = "Age : ", font = "monaco 13 italic")

name.grid(row=1, column = 0)
phone.grid(row=2, column = 0)
gender.grid(row=3, column = 0)
age.grid(row=4, column = 0)

name1 = StringVar()
phone1 = StringVar()
gender1 = StringVar()
age1 = StringVar()

name2 = Entry(root, textvariable=name1)
phone2 = Entry(root, textvariable=phone1)
gender2 = Entry(root, textvariable=gender1)
age2 = Entry(root, textvariable=age1)

name2.grid(row=1, column=1)
phone2.grid(row=2, column=1)
gender2.grid(row=3, column=1)
age2.grid(row=4, column=1)

# Checkbox 
chec = IntVar()     # Checkbox only contains 0 and 1 as input value
checkb = Checkbutton(root, text="Check it!")
checkb.grid(row = 5, column = 1)

Button(root, text="Submit :D", command=work).grid(row = 6, column=1)



>>>>>>> fc6ade0 (Updates)
root.mainloop()