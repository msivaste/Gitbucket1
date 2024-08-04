class cars:
    def __init__(self):
        self.__maxprice = 1000000
    def sell(self):
        print("Selling price is: ",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice = price
ob1 = cars()
ob1.sell()
ob1.__maxprice = 1000
ob1.sell()
ob1.setmaxprice(1000)
ob1.sell()