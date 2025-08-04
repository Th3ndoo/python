from tkinter import *

win = Tk()
win.title("Number pad")
win.geometry("200x200")



n = [['9','8','7'],['6','5','4'],['3','2','1'],['0','0' , '*']]
for i in range(0,4):
    win.rowconfigure(i,weight = 1)
    for j in range(0,3):
        win.columnconfigure(j,weight = 1)
        label = Label(win, text = n[i][j],relief='ridge',bg='skyblue',fg='navy',width = 2)
        label.grid(row=i,column= j)
win.mainloop()