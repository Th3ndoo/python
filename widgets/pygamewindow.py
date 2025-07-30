from tkinter import *
from datetime import date

win = Tk()
win.title("my first window")
win.geometry("300x300")
win.configure(bg='cyan')
def greet():
    name = entry1.get()
    
    dt = date.today()
    mygreet = "Welcoe to Codingal "+name + "\n Today's date is " + str(dt)
    text1.delete("1.0","end")
    text1.insert("1.0",mygreet)

label1 = Label(win,bg='teal',fg='white',text='name')
label1.pack(pady=10)
entry1 =  Entry()
entry1.pack(pady=10)
button1 = Button(win,bg='white',fg='teal',text='click me',command=greet)
button1.pack(pady=10)
text1 = Text(win,bg='darkgrey',fg='teal',width=200,height=5)
text1.pack()

win.mainloop()