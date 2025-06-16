 
def hotelcost(nights):
    return 140 * nights

def planecost(city):
    if city == 'New York':
        return 120
    elif city == 'California':
        return 170
    elif city == "Dallas":
        return 190
    elif city == 'Atlanta':
        return 210
    
def carrentalcost(days):
    if days > 7:
        return days * 40 - 50
    elif days > 3:
        return days * 40 - 30
    else:
        return days * 40
    
def totalcost(city,days,night,sp):
    print("the total cost is $" ,planecost(city) + hotelcost(night) + carrentalcost(days) +sp)

totalcost('Dallas',7,8,250)