# mid prouct

n = int(input("enter the nuvber : "))

str1 = str(n)

i = len(str1)

mid = int(i/2)

if i%2 == 1:
    mid = int(i/2)
else:
    mid = int(i/2) - 1

prod = int(str1[mid]) * int(str1[mid + 1])
print("the product of mid number is : ", prod)