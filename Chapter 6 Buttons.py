from tkinter import * 


def nothing(): 
    print("Output printed here!")

root = Tk()
root.geometry("800x800")

frame = Frame(root, bg = "black", borderwidth = 4)
frame.pack(side = LEFT, anchor = "nw")



# Button() used to make buttons 
b1 = Button(frame, bg="Green", fg = "black", text = "Print the output", command = nothing)
b1.pack()

root.mainloop()