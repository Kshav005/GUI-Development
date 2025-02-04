from tkinter import * 
import datetime 

current = datetime.datetime.now()

datenow = current.date
monthnow = current.month
yearnow = current.year

def clean() : 
    datein.set("")
    monthin.set("")
    yearin.set("")
    
def sub() : 
    dateinfoo = int(datein.get())
    monthinfoo = monthin.get()
    yearinfoo = int(yearin.get())
    
    if monthinfoo.lower() == "january" or monthinfoo == 1 :
        mon = 1
    elif monthinfoo.lower() == "february" or monthinfoo == 2 :
        mon = 2
    elif monthinfoo.lower() == "march" or monthinfoo == 3 :
        mon = 3   
    elif monthinfoo.lower() == "april" or monthinfoo == 4 :
        mon = 4
    elif monthinfoo.lower() == "may" or monthinfoo == 5 :
        mon = 5
    elif monthinfoo.lower() == "june" or monthinfoo == 6 :
        mon = 6
    elif monthinfoo.lower() == "july" or monthinfoo == 7 :
        mon = 7
    elif monthinfoo.lower() == "august" or monthinfoo == 8 :
        mon = 8
    elif monthinfoo.lower() == "september" or monthinfoo == 9 :
        mon = 9
    elif monthinfoo.lower() == "october" or monthinfoo == 10 :
        mon = 10
    elif monthinfoo.lower() == "november" or monthinfoo == 11 :
        mon = 11
    elif monthinfoo.lower() == "december" or monthinfoo == 12 :
        mon = 12   
    
    yearold = yearnow - yearinfoo
    monthold = yearold*12  
    dayold = yearold*365.24
    
    print(f"Year : {yearold}, Month : {monthold}, Day : {dayold}")



root = Tk()
root.geometry("600x600")
root.title("Age Calculator")

date = Label(root, text="Date : ", pady = 5)
month = Label(root, text = "Month : ", pady = 5)
year = Label(root, text="Year : ", pady = 5)
dayol = Label(root, text="")


datein = IntVar()
monthin = StringVar()
yearin = IntVar()
datein.set("")
yearin.set("")

dateinfo = Entry(root, textvariable=datein)
monthinfo = Entry(root, textvariable=monthin)
yearinfo = Entry(root, textvariable=yearin)

subm = Button(root, text="Submit", command = sub, padx=10, width=5, font = "monaco 10 bold")
clea = Button(root, text="Clear", command = clean, width = 7, font="monaco 10 bold")


date.grid(row = 0, column = 0)
dateinfo.grid(row = 0, column = 1)
month.grid(row = 1, column = 0)
monthinfo.grid(row = 1, column = 1)
year.grid(row = 2, column = 0)
yearinfo.grid(row = 2, column = 1)
subm.grid(row = 3, column = 0, padx= 10, pady = 10)
clea.grid(row = 3, column = 1, pady=10)




root.mainloop()