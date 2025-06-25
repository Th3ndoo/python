class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
p1 = point(100,200)
p2 = point(-100,90)

print(p1)
print(p2)