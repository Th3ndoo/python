# Inheretence vehicle

class vehicle:
    def __init__(self,name,mileage,maxspeed):
        self.name = name
        self.mileage = mileage
        self.maxspeed = maxspeed
    def disp(self):
        print(f"the name of the vehicle {self.name}")
        print(f"the mileage of the vehicle {self.mileage}")
        print(f"the maxspeed of the vehicle {self.maxspeed}")

class bus(vehicle):
    pass


b1 = bus("school volvo",20,100)

b1.disp()