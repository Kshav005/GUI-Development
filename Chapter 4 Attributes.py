from tkinter import * 

root = Tk()

root.geometry("700x700")

# Title, which is showed on the window at the top
root.title("Nothing.exe")


# Important Attributes For Label
# text - adds an text 
# bd - background 
# fg - foreground 
# font - sets the font 
# padx - x padding 
# pady - y padding 
# relief - border styling(SUNKEN, RAISED, GROOVE, RIDGE)


name = Label(root, text = '''It spits fire that is hot enough to melt boulders. 
             It may cause forest fires by blowing flames.''',
             bg = "red", fg = "white", font = "comicsansms 10 italic", borderwidth=5, relief=SUNKEN)                                  


# Important Attributes for Pack
# anchor = compass direction for position (nw, e, s, sw)
# side = by default it is top (bottom, left, right)
# fill = extends to the axis (X, Y)
# padx = x padding 
# pady = y padding


name.pack(side = TOP, anchor = "ne", fill = X)
root.mainloop()