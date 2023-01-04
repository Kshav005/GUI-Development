from tkinter import * 

root = Tk()
root.geometry("900x700")
root.title("Radio Buttons Tutorial")

var = IntVar()

t = Label(root, text="What would you like to eat today?", font = "comicsands 15 bold")
t.pack()

# Radiobutton() can be used to insert radio buttons into the GUI window
radio1 = Radiobutton(root, text = "Samosa?", pady = 10, variable=var, value=1)
radio2 = Radiobutton(root, text = "Idli?", pady = 10, variable=var, value=2)
radio3 = Radiobutton(root, text = "Samsa?", pady = 10, variable=var, value=3)
radio4 = Radiobutton(root, text = "Sa?", pady = 10, variable=var, value=4)
radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()




root.mainloop()

