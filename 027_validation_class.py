# Another class with a class attribute, used for validation purposes
class Pet:
	allowed = ['cat', 'dog', 'fish', 'rat']

	def __init__(self, name, species):
		if species not in Pet.allowed:
        # think about the difference between Pet.allowed and self.allowed
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self,species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

# Using self.allowed at begining:
# if cat.allowed was changed, self.allowed will be also changed.
# Using Pet.allowed at begining: 
# if cat.allowed was changed, self.allowed won't be also changed.

