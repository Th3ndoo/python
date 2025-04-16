# multiplication table

n = int(input("enter the number"))


res = 1

for i in range(1,11):
    res = n *i
    print(f"{n} x {i} = {res}")