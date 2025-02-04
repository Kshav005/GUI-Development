<<<<<<< HEAD
from tkinter import * 

# Creating a slider system for some purpose
def money(): 
    print(f"${myslider2.get()} has been credited in your account!")

root = Tk()
root.geometry("900x700")
root.title("Slider Tutorial")

myslider = Scale(root, from_= 0, to = 900)      # default vertical scale 
myslider.pack()

myslider2 = Scale(root, from_=0, to = 700, orient=HORIZONTAL, tickinterval=350)
myslider2.pack()

a = Button(root, text="Submit", foreground="white", bg = "black", command=money)
a.pack()


=======
from tkinter import * 

# Creating a slider system for some purpose
def money(): 
    print(f"${myslider2.get()} has been credited in your account!")

root = Tk()
root.geometry("900x700")
root.title("Slider Tutorial")

myslider = Scale(root, from_= 0, to = 900)      # default vertical scale 
myslider.pack()

myslider2 = Scale(root, from_=0, to = 700, orient=HORIZONTAL, tickinterval=350)
myslider2.pack()

a = Button(root, text="Submit", foreground="white", bg = "black", command=money)
a.pack()


>>>>>>> fc6ade0 (Updates)
root.mainloop()