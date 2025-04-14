# progra to calculate the electricity bill

units = int(input("enter the units"))

if units < 50:
    amt = units * 2.60 + 25
elif units < 100:
    amt = units * 3.25 + 35
elif units < 200:
    amt =  units * 5.26 +45
else:
    amt = units * 8.45 + 100

print(f"the units consumes {units} and the electricity bill amt is ${amt}")