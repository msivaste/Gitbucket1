class goa:
    name ="Baga"
    drink = "Bar"
    def party(self):
        print("Lets party")
    def beach(self):
        print("Enjoy the beach")

ramesh = goa()
suresh = goa()

ramesh.party()
suresh.beach()
print((ramesh.name))

ramesh.name ="Ramesh"
suresh.name = "Suresh"
ramesh.drink = "Yes"
suresh.drink = "No"
print(ramesh.name)
print("Drink: ", ramesh.drink)
print(suresh.name)
print("Drink: ", suresh.drink)