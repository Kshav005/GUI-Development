from tkinter import * 
import tkinter.messagebox as tmsg       # importing some important things

def now() : 
    print("A button is clicked yay!")
    
def helpi() : 
    # returns a window on the screen with "OK" button only
    tmsg.showinfo(title = "Monkey", message="You are donkey and johny is a monkey :D")
    
def ratee() :
    # returns a window with "yes" and "no" buttons 
    a = tmsg.askquestion("Rate when", "Were you satisfied by this app?")
    if a.lower() == 'yes' : 
        print("Say no :(")
    else : 
        print("You are such a loser!")
        
def ex1() : 
    # returns a warning window on the screen
    tmsg.showwarning("Nothing","YOU HAVE BEEN SERIOUSLY WARNED FOR VIOLATING OUR TERMS AND CONDITIONS!!")

def ex2() :
    # same as ".askquestion"
    tmsg.askyesno("sooi", "Am I the one here")

def ex3() : 
    # same as ".showinfo"
    tmsg.askokcancel("Hey", "Do you want to accept?")
    
def ex4() : 
    # returns a window displaying error
    tmsg.showerror("ERROR", "BAD GATEWAY, LOOKS LIKE YOU ARE MISSING BUDDHA.DLL")

root = Tk()
root.geometry("900x700")

men = Menu(root)
men.add_command(label="File", command = now)
men.add_command(label = "Help", command = helpi)
men.add_command(label = "Rate", command = ratee)
men.add_command(label = "ex1", command = ex1)
men.add_command(label = "ex2", command = ex2)
men.add_command(label = "ex3", command = ex3)
men.add_command(label = "ex4", command = ex4)

root.config(menu=men)

root.mainloop()