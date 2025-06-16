# map function

list1 = [1,12,34,56]
list2 = [89,34,56,65]

res = map(lambda x,y:x+y,list1,list2)

print("the addition of two lists is ",list(res) )

def sqr(a):
    return a *a

a = [3,4,6,7]
square = list(map(sqr,a))
print("the sqaure of the function is",square )
