class calculator:
    def __init__(self,a1,b1):
        self.a = a1
        self.b = b1
    def add(self):
        print("Addition: ", self.a + self.b)
    def sub(self):
        print("Subtraction: ", self.a - self.b)
    def mul(self):
        print("Multiplication: ", self.a * self.b)
    def div(self):
        print("Division: ", self.a / self.b)

i1 = calculator(5,5)
i2 = calculator(10,5)

i1.add()
i1.sub()
i1.mul()
i1.div()

i2.add()
i2.sub()
i2.mul()
i2.div()
