class parrot:
    def fly(self):
        print("Parrot can fly")
class penguin:
    def fly(self):
        print("Penguin can't fly")
def flyingstatus(bird):
    bird.fly()

blu = parrot()
peggy = penguin()
flyingstatus(blu)
flyingstatus(peggy)