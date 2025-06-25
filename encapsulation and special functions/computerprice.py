class computer:
    def __init__(self):
        self.__maxprice = 890

    def dispprice(self):
        print("the max price is",self.__maxprice)

    def setmaxprice(self,price):
        self.__maxprice = price

    
c1 = computer()
c1.__maxprice = 1200
c1.dispprice()
c1.setmaxprice(3000)
c1.dispprice()