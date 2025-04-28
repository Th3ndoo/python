# right angle triange

n = int(input("enter the no. of rows"))
space = 20
for i in range(1,n+1,2):
    for k in range(1,space+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    space-=2
space+=4
for i in range(n-2,0,-2):
    for k in range(1,space+1):
        print(" ",end= "")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    space+=2
