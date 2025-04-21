# Armtrong

n = int(input("enter a number: "))

t = n
s = 0

while t > 0:
    r = t%10
    s+= r**3
    t//=10

if n == s:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")
