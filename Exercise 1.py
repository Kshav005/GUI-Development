from tkinter import * 

root = Tk()
root.geometry("800x800")

image1 = PhotoImage(file="E:\\download.png")
image2 = PhotoImage(file="E:\\download (1).png")
image3 = PhotoImage(file="E:\\hello.png")

heading1 = Label(root, text="KNews")
image11 = Label(image = image1)
heading2 = Label(root, text='''There was a boy murdered, his name was found to be Tom. There is a rumor going on that Jerry killed him.
                 The cops say that Jerry used a sharp knife to kill Tom. Tom was barely alive at that time but Jerry stabbed him 9394394 times. But as soon as Jerry tried
                 to run away, the cops arrived at the place of incident. There is a attic in the room which needs a ladder to hide above.''')
image12 = Label(image = image2)
heading3 = Label(root, text='''Once of a time, there was a kid who was found dead on the graveyard. It doesn't seem to be unique 
                 but the fact was found that he was found lying above a skelton of his grandpa. Now his dead body is nowhere to be found. The cops arrived at the scene
                 of incident and found 1003030 bones in the area. The boy's name is found to be Sooi''')
image13 = Label(image = image3)
heading4 = Label(root, text='''This newspaper is found to be trending worldwide. It's the best newspaper in the the whole world. USA was accused of making some plan against us. Who will save us
                 from this end. Will we be ending here? Or is there some high respected lawyer who is willing to help this cute newspaper. The leader of this newspaper is Keshav Pal but no one knows his whereabouts.''')

heading1.grid(row = 0, column = 0)
image11.grid(row = 0, column = 1)
heading2.grid(row = 1, column = 1)
image12.grid(row = 0, column = 2)
heading3.grid(row = 1, column = 2)
image13.grid(row = 0, column = 3)
heading4.grid(row = 1, column = 3)
 
root.mainloop()


