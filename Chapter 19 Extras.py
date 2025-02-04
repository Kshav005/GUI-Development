<<<<<<< HEAD
from tkinter import *

root = Tk()
root.geometry("900x700")
root.title("Namaste.py")

# ".wm_iconbitmap" is used to set an icon in the title of the window (only images with extension .ico)
root.wm_iconbitmap("C:\\Users\\PC\\Desktop\\Coding Tutorial\\TKinter\\photos\\1.ico")       # Enter you image directory here (folder in which it is placed)

# Change background of the whole window
root.configure(background="grey")

# To get info about you monitor size 
wid = root.winfo_screenwidth()
hei = root.winfo_screenheight()

print(f"{wid}x{hei}")





=======
from tkinter import *

root = Tk()
root.geometry("900x700")
root.title("Namaste.py")

# ".wm_iconbitmap" is used to set an icon in the title of the window (only images with extension .ico)
root.wm_iconbitmap("C:\\Users\\PC\\Desktop\\Coding Tutorial\\TKinter\\photos\\1.ico")       # Enter you image directory here (folder in which it is placed)

# Change background of the whole window
root.configure(background="grey")

# To get info about you monitor size 
wid = root.winfo_screenwidth()
hei = root.winfo_screenheight()

print(f"{wid}x{hei}")





>>>>>>> fc6ade0 (Updates)
root.mainloop()