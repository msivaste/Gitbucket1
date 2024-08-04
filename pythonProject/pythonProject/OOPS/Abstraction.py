from abc import ABC


class car(ABC):
    def mileage(self):
        pass
class renault(car):
    def mileage(self):
        print("Mileage is 16 kms")
class jaguar(car):
    def  mileage(self):
        print("Mileage is 20kms")
class bmw(car):
    def mileage(self):
        print("Mileage is 12kms")
a = renault()
b = jaguar()
c = bmw()
a.mileage()
b.mileage()
c.mileage()