from tkinter import *
import random

root = Tk()
root.title("Restaruant management system")
root.geometry('800x400')
root.configure(bg='beige')
frame1 = Frame(root, width = 800, height= 300, relief= SUNKEN, bg = 'purple')
frame1.pack()
label1 = Label(frame1,font=( "arial",18,'bold'),text="Restaruant management system",bg = 'black', fg= 'grey')
label1.grid(row = 0,column = 0,columnspan=4,padx=20,pady=10)


drink = StringVar()
pizza = StringVar()
burger = StringVar()
largeburger = StringVar()
fries = StringVar()

labeldrink = Label(frame1, text = "Drinks", fg = "darkblue", font = ('times',12,'bold'),bg = 'brown')
labeldrink.grid(row=3, column=0,padx=10,pady=10)
entrydrink = Entry(frame1, textvariable=drink, justify=RIGHT)
entrydrink.grid(row = 3, column= 1,padx=10,pady=10)
entrydrink.insert(END,0)

labelpizza = Label(frame1, text = "Pizza", fg = "darkblue", font = ('times',12,'bold'),bg = 'brown')
labelpizza.grid(row=4, column=0,padx=10,pady=10)
entrypizza = Entry(frame1, textvariable=pizza, justify=RIGHT)
entrypizza.grid(row = 4, column= 1,padx=10,pady=10)
entrypizza.insert(END,0)

labelburger = Label(frame1, text = "Burger", fg = "darkblue", font = ('times',12,'bold'),bg = 'brown')
labelburger.grid(row=5, column=0,padx=10,pady=10)
entryburger = Entry(frame1, textvariable=burger, justify=RIGHT)
entryburger.grid(row = 5, column= 1,padx=10,pady=10)
entryburger.insert(END,0)

labellargeburger = Label(frame1, text = "Largeburger", fg = "darkblue", font = ('times',12,'bold'),bg = 'brown')
labellargeburger.grid(row=6, column=0,padx=10,pady=10)
entrylargeburger = Entry(frame1, textvariable=largeburger, justify=RIGHT)
entrylargeburger.grid(row = 6, column= 1,padx=10,pady=10)
entrylargeburger.insert(END,0)

labelfries = Label(frame1, text = "Fries", fg = "darkblue", font = ('times',12,'bold'),bg = 'brown')
labelfries.grid(row=7, column=0,padx=10,pady=10)
entryfries = Entry(frame1, textvariable=fries, justify=RIGHT)
entryfries.grid(row = 7, column= 1,padx=10,pady=10)
entryfries.insert(END,0)

labelorderno = Label(frame1, text = "OrderNo", fg = "darkblue", font = ('times',12,'bold'),bg = 'brown')
labelorderno.grid(row=3, column=2)
entryorderno = Entry(frame1)
entryorderno.grid(row = 3,column=3)

labelcost = Label(frame1, text = "Cost", fg = "darkblue", font = ('times',12,'bold'),bg = 'brown')
labelcost.grid(row=4, column=2)
entrycost = Entry(frame1)
entrycost.grid(row = 4,column=3)

labelservice = Label(frame1, text = "Service", fg = "darkblue", font = ('times',12,'bold'),bg = 'brown')
labelservice.grid(row=5, column=2)
entryservice = Entry(frame1)
entryservice.grid(row = 5,column=3)

labeltax = Label(frame1, text = "Tax", fg = "darkblue", font = ('times',12,'bold'),bg = 'brown')
labeltax.grid(row=6, column=2)
entrytax = Entry(frame1)
entrytax.grid(row = 6,column=3)

labeltotal = Label(frame1, text = "OrderNo", fg = "darkblue", font = ('times',12,'bold'),bg = 'brown')
labeltotal.grid(row=7, column=2)
entrytotal = Entry(frame1)
entrytotal.grid(row = 7,column=3)

def ex():
    root.destroy
def reset():
    entrydrink.delete(0,END)
    entryburger.delete(0,END)
    entrylargeburger.delete(0,END)
    entrypizza.delete(0,END)
    entryfries.delete(0,END)
    
    entrydrink.insert(END,0)
    entrypizza.insert(END,0)

    entryburger.insert(END,0)

    entrycost.delete(0,END)
    entrylargeburger.insert(0,END)
    entryfries.insert(0,END)
    entryorderno.delete(0,END)
    entryservice.delete(0,END)
    entrytax.delete(0,END)
    entrytotal.delete(0,END)

def total():
        global drink
        global burger
        global pizza
        global largeburger
        global fries

        drink = float(drink.get())
        pizza =float(pizza.get())
        burger = float(burger.get())
        largeburger = float(largeburger.get())
        fries = float(fries.get())
        cost= 28 * drink + pizza * 250 + burger * 150 + fries * 75 + largeburger * 200
        print(cost)
        entrycost.insert(0,str(cost))
        service = cost*0.02
        entryservice.insert(0,str('Rs %.2f'% service))
        tax = cost * 0.1
        entrytax.insert(0,str('Rs %.2f'% tax))
        totalcost = cost+service+tax
        entrytotal.insert(0,str('Rs %.2f'% totalcost))
        rand = random.randit(1,10000)

def price():

        top = Toplevel()
        top.geometry("300x200")
        top.title('toplevel')
        l2 = Label(top, text = "Price",font=("Times",22,'bold'))
        l3 = Label(top, text = "Drinks Rs. 20",font = ("Times",12,'bold'))
        l4 = Label(top, text = "Burger Rs. 20",font = ("Times",12,'bold'))
        l5 = Label(top, text = "Pizza Rs. 20",font = ("Times",12,'bold'))
        l6 = Label(top, text = "Largeburger Rs. 20",font = ("Times",12,'bold'))
        l7 = Label(top, text = "Fries Rs. 20",font = ("Times",12,'bold'))
        l2.pack()
        l3.pack()
        l4.pack()
        l5.pack()
        l6.pack()
        l7.pack()

button1 = Button(frame1, text = "Price", fg = "darkblue", font= ('Times',12,'bold'),bg = 'brown',command=price,padx=10,pady=10)
button1.grid(row=10, column= 0, padx=10,pady=10)
button2 = Button(frame1, text = "Total", fg = "darkblue", font= ('Times',12,'bold'),bg = 'brown',command=total,padx=10,pady=10)
button2.grid(row=10, column= 1, padx=10,pady=10)
button3 = Button(frame1, text = "Reset", fg = "darkblue", font= ('Times',12,'bold'),bg = 'brown',command=reset,padx=10,pady=10)
button3.grid(row=10, column= 2, padx=10,pady=10)
button4 = Button(frame1, text = "Exit", fg = "darkblue", font= ('Times',12,'bold'),bg = 'brown',command=exit,padx=10,pady=10)
button4.grid(row=10, column= 3, padx=10,pady=10)


root.mainloop()