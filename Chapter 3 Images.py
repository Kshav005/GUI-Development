from tkinter import * 

root = Tk()
root.geometry("500x500")

# Adding images using PhotoImage(file = "your\\file\\directory\\where\\image\\is\\there")
image1 = PhotoImage(file = "E:\\hello.png")
label1 = Label(image = image1)
label1.pack()

root.mainloop()