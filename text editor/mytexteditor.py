from tkinter import *
from tkinter.filedialog import askopenfile,asksaveasfile

window = Tk()
window.title("Text editor")
window.geometry("500x400")
def openfile():
    file1 = askopenfile(mode='r',filetypes=[('text files','* text')])
    if file1 is not None:
        content = file1.read()
        text1.delete("1.0","end")
        text1.insert(END,content)
    file1.close()

def savefile():
    file2 = asksaveasfile (mode='w',filetypes=[('text files','*.txt')])
    if file2 is not None:
        mytext1 = text1.get(1.0,END)
        file2.write(mytext1)
    
    file2.close()


button1 = Button(window, text = "open", command=openfile)
button2 = Button(window, text = "save as", command=savefile)
text1 = Text(window, width = 50,height=15,relief="sunken",bg="grey",fg='red',bd=3)
button1.grid(row=0,column=0)
button2.grid(row=1,column=0)
text1.grid(row=0,column=1,rowspan=2,pady = 10,padx=10)

window.mainloop()