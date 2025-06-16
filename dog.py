class dog:
    species = "Golden Retriever"
    def __init__(self,name,age):
        self.name = name
        self.age = age


d1 = ("Brookylyn",4)
d2 = ("Spike",9)
print(f"\n my name is {d1.name} and my age is {d1.age} i belong to species {d1.species}")
print(f"\n my name is {d2.name} and my age is {d2.age} i belong to species {d2.species}")