class employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

class child1(employee):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class child2(employee):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
a = child1('Siva',39,200000)
b = child2('Prawin',33,100000)
print(a.age)
print(b.age)
