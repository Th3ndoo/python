from tkinter import *

win = Tk()
win.title("Number pad")
win.geometry("400x500")

win.configure(bg='grey')
def greet():
    name = entry1.get()
    greet = "Welcome!" + name +"\n Congratulations for your new account"
    text1.delete("1.0","end")
    text1.insert("1.1",greet)

label1 = Label(win,text = 'Name',bg = 'grey',fg = 'black',width= 20)
label1.grid(row=1,column=1)
entry1 =  Entry()
entry1.grid(row=1,column=2)
label2 = Label(win,text= 'password', bg = 'grey',fg = 'black',width= 30)
label2.grid(row=2,column=1)
entry2 = Entry(show = "*")
entry2.grid(row=2,column=2)
button1 = Button(win, text = 'login', bg = 'black', fg = 'white',command=greet)
button1.grid(row= 3, column= 1, columnspan=2)
text1 = Text(win, relief= 'sunken', bd = 5, width=40, bg= 'lightgrey')
text1.grid(row = 4,column=1,columnspan=2)

win.mainloop()