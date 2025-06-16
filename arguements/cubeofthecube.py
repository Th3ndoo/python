# cube for dividable by 3

def cube(x):
    return x**3

def divisible_by_3(x):
    if x%3 == 0:
       return cube(x)
    else:
        return False
    
n = int(input("enter the number"))
res = divisible_by_3(n)
if not res:
    print(f"{n} is not divisible by 3")
else:
    print(f"the cube of the {n} is {res}")