from tkinter import *
import tkinter.messagebox as tkmb


root = Tk()
root.geometry("500x300")
root.title("Shopping.exe")
root.wm_iconbitmap("C:\\Users\\PC\\Desktop\\Coding Tutorial\\TKinter\\photos\\shop.ico")

def clearr() : 
    fname.set("")
    lname.set("")
    ii1.set("Select Item")
    ii2.set("Select Item")
    ii3.set("Select Item")
    pay.set(0)

def subm() : 
    f = fname.get()
    l = lname.get()
    i11 = ii1.get()
    i22 = ii2.get()
    i33 = ii3.get()
    dayyy = dayy.get()
    timeee = timee.get()
    payyy = pay.get()
    if payyy == 2 : 
        payment = "Cash"
    elif payyy == 3 : 
        payment = "Paytm"
    else : 
        payment = "Not Selected"
        
    if payment == "Not Selected" : 
        tkmb.showerror("Detail absent","Select the payment method first!")  
    else : 
        conf = tkmb.askquestion("Confirmation", "Do you want to proceed and confirm your order?")
        if conf == "yes" :
            tkmb.showinfo("Order Placed!", "Your order has been placed succesfully! Thanks for choosing our company.")
            with open("shoplist.txt", "a") as fi : 
                fi.write(f"First Name - {f}\nLast Name - {l}\nItem 1 - {i11}\nItem 2 - {i22}\nItem 3 - {i33}\n Delivery - {dayyy} ({timeee})\nMode of Payment - {payment}\n\n")
            fname.set("")
            lname.set("")
            ii1.set("Select Item")
            ii2.set("Select Item")
            ii3.set("Select Item")
            dayy.set("Select Day for the delivery")
            timee.set("Select Delivery Time")
            pay.set(0)
        else : 
            tkmb.showinfo("Order not confirmed", "You didn't confirm your order :(")
    

firstname = Label(root, text="First Name - ")
lastname = Label(root, text="Last Name - ")
i1 = Label(root, text="Item 1 = ")
i2 = Label(root, text="Item 2 = ")
i3 = Label(root, text="Item 3 = ")
dayinfo = Label(root, text="Day of Delivery - ")
timeinfo = Label(root, text="At What Time?")

fname = StringVar()
lname = StringVar()
ii1 = StringVar()
ii1.set("Select Item")
ii2 = StringVar()
ii2.set("Select Item")
ii3 = StringVar()
ii3.set("Select Item")
dayy = StringVar()
dayy.set("Select Day for the Delivery")
timee = StringVar()
timee.set("Select Delivery Time")
pay = IntVar()

fnameinfo = Entry(root, textvariable=fname)
lnameinfo = Entry(root, textvariable=lname)
iii1 = OptionMenu(root, ii1, "Bread ($2)", "Jam ($3)", "50mL Water Bottle ($7)", "Potatoes ($4)", "Tomatoes ($3)", "Jelly ($3)", "1kg Milk ($10)", "2kg Milk ($13)", "4kg Milk ($20)", "Sauce ($5)", "Chips ($4)", "Biscuits ($2)", "Maggi ($1)", "Yipee ($1)", "Manchurian ($12)", "Rice ($10)", "Cookies ($6)", "Incense Stick ($1)", "Matchbox ($2)", "Shampoo ($5)", "Soap ($3)", "Toothpaste ($2)")
iii2 = OptionMenu(root, ii2, "Bread ($2)", "Jam ($3)", "50mL Water Bottle ($7)", "Potatoes ($4)", "Tomatoes ($3)", "Jelly ($3)", "1kg Milk ($10)", "2kg Milk ($13)", "4kg Milk ($20)", "Sauce ($5)", "Chips ($4)", "Biscuits ($2)", "Maggi ($1)", "Yipee ($1)", "Manchurian ($12)", "Rice ($10)", "Cookies ($6)", "Incense Stick ($1)", "Matchbox ($2)", "Shampoo ($5)", "Soap ($3)", "Toothpaste ($2)")
iii3 = OptionMenu(root, ii3, "Bread ($2)", "Jam ($3)", "50mL Water Bottle ($7)", "Potatoes ($4)", "Tomatoes ($3)", "Jelly ($3)", "1kg Milk ($10)", "2kg Milk ($13)", "4kg Milk ($20)", "Sauce ($5)", "Chips ($4)", "Biscuits ($2)", "Maggi ($1)", "Yipee ($1)", "Manchurian ($12)", "Rice ($10)", "Cookies ($6)", "Incense Stick ($1)", "Matchbox ($2)", "Shampoo ($5)", "Soap ($3)", "Toothpaste ($2)")
day = OptionMenu(root, dayy, "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
time = OptionMenu(root, timee, "8:00-10:00 am", "10:00-12:00 am", "12:00-2:00 pm", "2:00-4:00 pm", "4:00-6:00 pm", "6:00-8:00 pm")

iii1.config(bg="#08D57B")
iii2.config(bg="#08C6D6")
iii3.config(bg="#D38BFF")


payment2 = Radiobutton(root, text="Cash", variable=pay, value=2, font="comicsansms 13 italic")
payment3 = Radiobutton(root, text="Paytm", variable=pay, value=3, font="comicsansms 13 italic")
submit = Button(root, text="Submit", command = subm, font="monaco 10 bold", width = 10, fg = "#1D0373")
clearall = Button(root, text="Clear all", command = clearr, font="monaco 10 bold", width = 10, fg="#B40707")



firstname.grid(row=0, column=0, pady=5)
fnameinfo.grid(row=0, column=1, pady = 5)
lastname.grid(row=1, column=0, pady = 5)
lnameinfo.grid(row=1, column=1, pady = 5)
i1.grid(row=2, column=0, pady = 5)
iii1.grid(row=2, column=1, pady = 5, padx=5)
i2.grid(row=3, column=0, pady = 5)
iii2.grid(row=3, column=1, pady = 5)
i3.grid(row=4, column=0, pady = 5)
iii3.grid(row=4, column=1, pady = 5)
payment2.grid(row = 1, column = 2, padx = 0)
payment3.grid(row = 2, column = 2, padx = 0)
dayinfo.grid(row = 5, column=0)
day.grid(row=5, column=1, padx = 10)
timeinfo.grid(row = 6, column=0, padx = 10)
time.grid(row=6, column = 1)
submit.grid(row=7, column=0, pady = 15, padx = 10)
clearall.grid(row=7, column=1)


root.mainloop()