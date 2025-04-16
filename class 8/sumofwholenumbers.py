# sum of whole numbers
n = int(input("enter the number"))
sum = 0
for i in range(0,n+1):
    sum = sum + i 

print(f"the sum of whole numbers from 0 to {n} is {sum}")
