# Chicken Coop Exercise:
# For individual chicken, eggs should always start out at 0.
# For the chicken coop, count the total eggs number.


class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

   # increment and return the particular eggs amount
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs



c1=Chicken(name="Alice",species="Partridge Silkie")
c2=Chicken(name="Amelia",species="Speckled Sussex")
Chicken.total_eggs #0
c1.lay_egg() #1
Chicken.total_eggs #1
c2.lay_egg() #1
c2.lay_egg() #2
Chicken.total_eggs #3