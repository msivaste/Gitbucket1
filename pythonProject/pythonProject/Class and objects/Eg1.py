class student():
    def __init__(self):
        self.name ="Siva"
        self.regno = 123
    def display(self):
        print("Name: ",self.name)
        print("Reg No: ", self.regno)
s1 = student()
s2 = student()
s1.name = "SK"
s1.regno = 456
s2.name = "VJS"
s2.regno = 789
s1.display()
s2.display()