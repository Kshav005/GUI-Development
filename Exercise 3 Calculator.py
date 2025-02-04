
# Buttons are yet to be programmed.

from tkinter import * 

one, two, three, four, five, six, seven, eight, nine, zero = 1,2,3,4,5,6,7,8,9,0



def num1() :
    pass
    
def num2() :
    pass

def num3() :
    pass

def num4() :
    pass

def num5() :
    pass

def num6() :
    pass

def num7() :
    pass

def num8() :
    pass

def num9() :
    pass

def num() :
    pass


def equal() :  
    if val2.get() == "+"  : 
        val4.set(val1.get() + val3.get()) 
    elif val2.get() == "-"  : 
        val4.set(val1.get() - val3.get())
    elif val2.get() == "*" or val2.get() == "x" : 
        val4.set(val1.get() * val3.get())
    elif val2.get() == "/"  : 
        val4.set(val1.get() / val3.get())


def add() : 
    val2.set("+")
def minus() : 
    val2.set("-")
def multiply() : 
    val2.set("x")
def divide() : 
    val2.set("/")


def clear() : 
    pass

def allclear() : 
    val1.set("")
    val2.set("")
    val3.set("")
    val4.set("")
    



root = Tk()
root.geometry("445x200")
root.title("Calculator Sasta")
root.wm_iconbitmap("C:\\Users\\PC\\Desktop\\Coding Tutorial\\TKinter\\photos\\cat.ico")

val1 = IntVar()
val2 = StringVar()
val3 = IntVar()
val4 = IntVar()
val1.set("")
val2.set("")
val3.set("")
val4.set("")

val1info = Entry(root, textvariable=val1, font= "comicssansms 12 bold", justify=CENTER, width = 7)
val2info = Entry(root, textvariable=val2, font= "comicssansms 12 bold", justify=CENTER, width = 3)
val3info = Entry(root, textvariable=val3, font= "comicssansms 12 bold", justify=CENTER, width = 7)
val4info = Entry(root, textvariable=val4, font= "comicssansms 12 bold", justify=CENTER, width = 7, state=DISABLED)

val1info.grid(row = 1, column = 0, padx = 7)
val2info.grid(row = 1, column = 1, pady = 10)
val3info.grid(row = 1, column = 2, padx = 7)
val4info.grid(row = 1, column = 4, padx = 7)

Button(root, text="0", command = num, width=10).grid(row = 3, column = 0, padx = 5, pady = 5)
Button(root, text="1", command = num1, width=10).grid(row = 3, column = 1, padx = 5, pady = 5)
Button(root, text="2", command = num2, width=10).grid(row = 3, column = 2, padx = 5, pady = 5)
Button(root, text="3", command = num3, width=10).grid(row = 4, column = 0, padx = 5, pady = 5)
Button(root, text="4", command = num4, width=10).grid(row = 4, column = 1, padx = 5, pady = 5)
Button(root, text="5", command = num5, width=10).grid(row = 4, column = 2, padx = 5, pady = 5)
Button(root, text="6", command = num6, width=10).grid(row = 5, column = 0, padx = 5, pady = 5)
Button(root, text="7", command = num7, width=10).grid(row = 5, column = 1, padx = 5, pady = 5)
Button(root, text="8", command = num8, width=10).grid(row = 5, column = 2, padx = 5, pady = 5)
Button(root, text="9", command = num9, width=10).grid(row = 6, column = 0, padx = 5, pady = 5)
Button(root, text="AC", command = allclear, width=10).grid(row = 3, column = 3, padx = 5, pady = 5)
Button(root, text="C", command = clear, width=10).grid(row = 4, column = 3, padx = 5, pady = 5)
Button(root, text="=", command = equal, width=5).grid(row = 1, column = 3, pady = 5)
Button(root, text="-", command = minus, width=10).grid(row = 6, column = 2, padx = 5, pady = 5)
Button(root, text="x", command = multiply, width=10).grid(row = 6, column = 3, padx = 5, pady = 5)
Button(root, text="/", command = divide , width=10).grid(row = 5, column = 3, padx = 5, pady = 5)
Button(root, text="+", command = add , width=10).grid(row = 6, column = 1, padx = 5, pady = 5)



root.resizable(False, False)
root.config(background="#e6005c")
root.mainloop()


