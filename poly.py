## poly.py #####################################################################
################################################################################

class Pet:
	def __init__(self, name, species):
		self.Name = name
		self.Species = species
	def getName(self):
		return self.Name
	def getSpecies(self):
		return self.Species
		
class Dog(Pet):
	def __init__(self, name, breed):
		self.Species = "Dog"
		self.Name = name
		self.Breed = breed
		
	def getBreed(self):
		return self.Breed
		
		
if (__name__=="__main__"):
	Bailey = Dog("Bailey", "Schnauzer")
	print Bailey.getName()
	print Bailey.getSpecies()
	print Bailey.getBreed()	
	

