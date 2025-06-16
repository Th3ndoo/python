# reverse order

n = int(input("enter a number: "))

rev= 0
t = n

while t > 0:
    r = t%10
    rev = rev*10 + r
    t//=10

print(f"reverse of {n} is {rev}")