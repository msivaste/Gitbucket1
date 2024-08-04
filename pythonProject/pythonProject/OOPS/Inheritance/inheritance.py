class animal:
    def sound(self):
        print("Animal sounds")
class cat(animal):
    def meows(self):
        print("Cat Meows")
a = cat()
a.meows()
a.sound()