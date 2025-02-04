from tkinter import * 

root = Tk()
root.geometry("1000x1000")

frame = Frame(root, relief=SUNKEN, borderwidth = 5, padx = 50)
title = Label(frame, text = "Sharmaji Dance Classes",  bg = "black", fg = "white", font = "bold 15")
frame.place(anchor=CENTER, relx=0.5, rely=0.05)
title.grid()

frame1 = Frame(root, relief=RIDGE, borderwidth = 7, padx = 50, pady = 100, height = 8)
firsname = Label(frame1, text = "First Name : ", font = "monaco 10 italic")
lastname = Label(frame1, text = "Last Name : ", font = "monaco 10 italic")
age = Label(frame1, text = "Age : ", font = "monaco 10 italic")
month = Label(frame1, text = "Birthday Month : ", font = "monaco 10 italic")
year = Label(frame1, text = "Birthday Year : ", font = "monaco 10 italic")

firstinfo = StringVar()
lastinfo = StringVar()
ageinfo = StringVar()
monthinfo = StringVar()
yearinfo = StringVar() 

first = Entry(root, textvariable=firstinfo)
last = Entry(root, textvariable=lastinfo)
agein = Entry(root, textvariable=ageinfo)
monthin = Entry(root, textvariable=monthinfo)
yearin = Entry(root, textvariable=yearinfo)

first.place(relx=0.65, rely= 0.34, anchor=CENTER)
last.place(relx=0.65, rely=0.37, anchor=CENTER)
agein.place(relx=0.65, rely=0.401, anchor=CENTER)
monthin.place(relx=0.65, rely=0.431, anchor=CENTER)
yearin.place(relx=0.65, rely=0.462, anchor=CENTER)



frame1.place(relx=0.44, rely= 0.4, anchor=CENTER)
firsname.grid()
lastname.grid()
age.grid()
month.grid()
year.grid()





root.mainloop()



