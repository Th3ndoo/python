# function - calculator
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a/b

print("calculator")
print("\n1.Addition \n2.Subtraction \n3.Multiplication \n4. Division")
ch = input("enter your choice")
n1 = int(input("enter your no.1 "))
n2 = int(input("enter the nuo.2 2 "))

if ch == "1":
    res = add(n1,n2)
    print(f'{n1}+{n2}={res} ')
elif ch == "2":
    res = sub(n1,n2)
    print(f'{n1}-{n2}={res}')
elif ch == "3":
    res = mul(n1,n2)
    print(f'{n1}X{n2}={res}')
elif ch == "4":
    res = div(n1,n2)
    print(f'{n1}/{n2}={res}')
else:
    print("invalid")