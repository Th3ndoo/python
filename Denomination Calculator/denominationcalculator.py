from tkinter import *
from tkinter import messagebox
from os import system
system("pip install pillow")
from PIL import Image, ImageTk
root = Tk()
root.title("Denomination Counter")
root.geometry('500x400')
upload = Image.open("cross.jpg")
upload = upload.resize((300,300))
img = ImageTk.PhotoImage(upload)

label = Label(root,image=img)

label.place(x=100,y=20)

label1 = Label(root, text = "hey user! Welcome to Denomination calculator application")
label1.place(x=50, y=320)

def msg():
    msgbox = messagebox.showinfo("alert", "do you want to calculate the denomination count ?")
    if msgbox == 'ok':
        topwin()
button1 = Button(root, text = "Let's get started",command=msg,bg='brown',fg='white')
button1.place(x=150, y=370)

def topwin():
    def calculator():
        global amount
        amount = int(entry1.get())
        note2000 = amount//2000
        amount = amount%2000
        note500 = amount//500
        amount = amount%500
        note100 = amount//100
        amount = amount%100
        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))
    top = Toplevel()
    top.title("toplevel")
    top.geometry("400x400")
    top.configure(bg='black')
    label1 = Label(top, text = "enter total amount")
    label1.place(x=100,y=100)
    entry1 = Entry(top)
    entry1.place(x = 100,y =120)
    lb1 = Label(top, text = "here are the numers of notes for each welcome to the denomination calculator application")
    lb1.place(x = 50,y = 150)
    l1 = Label(top, text = "2000")
    l2 = Label(top, text = "500")
    l3 = Label(top, text = "100")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    btn = Button(top, text = 'calculate', command=calculator)
    entry1.place(x = 100,y = 100)
    btn.place(x = 100, y = 100)
    l1.place(x =100, y = 200)
    l2.place(x = 100,y=230)
    l3.place(x=100,y=250)
    t1.place(x = 200, y=200)
    t2.place(x=200,y=230)
    t3.place(x=200,y = 250)

root.mainloop()