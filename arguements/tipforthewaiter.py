# tip for the waiter
def tip(amt,per):
    t = amt * 2/100
    tamt = amt + t
    tamt = round(tamt,2)
    print(f"the amt to be paid ${tamt}")

billamt = float(input("enter the bill amount"))
t = float(input("enter the percentage for the tip"))
tip(billamt,t)