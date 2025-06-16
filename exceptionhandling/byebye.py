# program to handle error

try :
    valid = False
    while not valid:
        n = int(input("enter the number"))
        if n%2 == 0:
            print("bye")
        else:
            valid = True
        
except:
    print("error occured")