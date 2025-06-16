class vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage


car = vehicle(120,13)

print("the maxspeed of the car is",car.maxspeed)
print("the mileage of the car is",car.mileage)

bus = vehicle(100,10)

print("the maxspeed of the bus is",bus.maxspeed)
print("the mileage of the bus is",bus.mileage)