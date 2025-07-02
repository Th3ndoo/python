#polymorphism

class ferrari:
    def mileage(self):
        print("6-1hk/l is the mileage")
    def tier(self):
        print("supercar, hyper car")
    def speed(self):
        print("211 mp/h")

class bmw:
    def mileage(self):
        print("200,000 is the mileage on the bmw")
    def tier(self):
        print("compat, excutive, luxury, and perfomance")
    def speed(self):
        print("250 km/h")

obj1 = india()
obj2 = usa()

for i in(obj1,obj2):
    i.capital()
    i.language()
    i.type()