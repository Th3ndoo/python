cp = float(input("enter the cost price of the item"))
sp = float(input('enter the selling price of the item'))

if cp < sp:
    profit = sp-cp
    print(f"you got a profit of {profit}")

else:
    loss = cp - sp
    print(f"you got a loss of {loss}")
