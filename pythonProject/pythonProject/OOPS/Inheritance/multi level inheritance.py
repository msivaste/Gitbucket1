class animal:
    def sound(self):
        print("Animal sounds")
class cat(animal):
    def meows(self):
        print("Cat Meows")

class kitten(cat):
    def kittensound(self):
        print("Kitten meows")
a = kitten()
a.meows()
a.sound()
a.kittensound()