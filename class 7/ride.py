# customize your ride

print("select your ride \n1.B1ike \n2.Car")
ch = int(input("enter your choice"))
if ch == 1:
    print("select your option \n1.Scooter \n2.Yahama")
    ch1 = int(input("enter your choice"))
    if ch1 == 1:
        print("your ride is Scooter")
    elif ch1 == 2:
        print("your ride is Yamaha")
    else:
        print("wrong options")
elif ch == 2:
     print("select your option \n1.Toyota \n2.Hellcat")
     ch1 = int(input("enter your choice"))
     if ch1 == 1:
        print("your ride is Toyota")
     elif ch1== 2:
        print("your ride is Hellcat")
     else:
        print("wrong options")
else:
    print("Wrong option")