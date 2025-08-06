from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Event handling")
window.configure(bg="cyan")

def handle_keypresss(event):
    print(event.char)

def mouse_handle(event):
    print("the mouse is clicked")

button1 = Button(window, text = "click me", bg= 'black',fg='cyan',width='20')
button1.place(x = 120, y= 150)
window.bind("<Key>",handle_keypresss)

button1.bind("<Button-1>", mouse_handle)
window.mainloop()