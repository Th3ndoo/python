x = int(input("enter the base"))
y = int(input("enter the power"))
pow = 1
for i in range(1,y+1):
    pow = pow * x

print(f"the {x}*{y} 3is {pow}")