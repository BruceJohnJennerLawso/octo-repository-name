## poly.py #####################################################################
################################################################################

class Pet(object):
	def __init__(self, name, species):
		self.Name = name
		self.Species = species
	def getName(self):
		return self.Name
	def getSpecies(self):
		return self.Species
		
class Dog(Pet):
	def __init__(self, name, breed):
		super(Dog,self).__init__(name, "Dog")
		self.Breed = breed
		
	def getBreed(self):
		return self.Breed
		
class Schnauzer(Dog):
	def __init__(self, name):
		super(Schnauzer,self).__init__(name, "Schnauzer")
		
		
if (__name__=="__main__"):
	Bailey = Schnauzer("Bailey")
	print Bailey.getName()
	print Bailey.getSpecies()
	print Bailey.getBreed()	
	

