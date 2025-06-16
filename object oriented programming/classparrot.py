class parrot:
    species = "maccaw"
    def __init__(self,name,age):
        self.name = name
        self.age = age


p1 = parrot("Luna",2)
p2 = parrot("Jason",1.5)

print(f"\n my name is {p1.name} and my age is {p1.age}  i belong to species {p1.species}")
print(f"\n my name is {p2.name} and my age is {p2.age} i belong to species {p2.species}")