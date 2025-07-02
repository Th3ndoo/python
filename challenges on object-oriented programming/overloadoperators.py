# operator overloding 

class A:
    def __init__(self,x):
        self.x = x

    def __lt__(self,other):
        if self.x < other.x:
            print("obj1 is less than obj2")
        else:
            print("obj2 is less than obj1")

    def __eq__(self,other):
        if self.x == other.x:
            return "obj1 is equal to obj2"
        else:
            return "obj2 is not equal to obj1"
        
obj1 = A(30)
obj2 = A(23)

print(obj1<obj2)
print(obj1==obj2)