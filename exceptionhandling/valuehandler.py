# value error
try:
    n = int(input("enter the number"))
    print(n)
except ValueError as e:
    print("the error occured" ,e)