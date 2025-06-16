# palidroe turple of not
def flipflop(t):
    s = 0
    e = len(t)-1
    while s<e:
        if t[s] != t[e]:
            return False
        else:
            s+=1
            e-=1
    return True

t = (1,2,3,3,2,1)

res = flipflop(t)

if res:
    print("The tuple is palidrome")
else:
    print("the tuple is not a palidroe")