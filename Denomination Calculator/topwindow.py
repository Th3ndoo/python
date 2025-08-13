from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("The main window")

def top():
    toplevel = Toplevel()
    toplevel.geometry("200x200")
    toplevel.configure(bg='beige')
    label2 = Label(toplevel,text = "the main window",fg = 'brown',font='arial')
    label2.place(x=20,y=20)

label1 = Label(root,text = "the main window")
label1.place(x=140,y=200)
button1 = Button(root,text = "click me", command = top)
button1.place(x=140,y=240)

root.mainloop()