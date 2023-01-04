from tkinter import * 

root = Tk()
root.geometry("900x700")

# Canvas(root, w, h) used to set max and min value to which canva can draw through
canva = Canvas(root, width=900, height = 700)

# draws a line from x1, y1 to x2, y2 (x1, y1, x2, y2)
canva.create_line(0, 100, 500, 100)
canva.pack()

# to create rectangle with this parameter --> (top left point coordinates, bottom right point coordinates)
canva.create_rectangle(3, 5, 500, 300)

# .create_text() is used to make a text, optional for Label
canva.create_text(200, 200, text="How are you my friend")


root.mainloop()