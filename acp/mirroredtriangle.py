# mirrored triangle

space = 20
n = int(input("enter the no. of rows"))

for i in range(1,n+1):
    for k in range (1,space):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    space-=2