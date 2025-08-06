from tkinter import * 
from tkinter import messagebox

window = Tk()
window.geometry("300x300")
window.title("message box")
window.configure(bg = 'beige')

def msg(event):
    messagebox.showwarning("Alert","Virus Detected!!!")

button1 = Button(window,text = "Click to Scan",bg = 'tomato',fg = 'brown',width = 20,height= 2)
button1.place(x=100,y=150)
button1.bind("<Button-1>",msg)

window.mainloop()