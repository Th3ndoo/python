class vehicle:
    def fare(self,n,amt):
        print("The toal fair is", n * amt)

class bus(vehicle):
    pass

b1 = bus()
b1.fare(20,1000)