import csv

class Dog(object):
	def __init__(self, name = None, breed = None):
		self.name = name
		self.breed = breed
	
	#return dog, name and breed, ex: jack pitbull.
	def nameBreed(self):
		return("%s %s" % (self.name, self.breed))
	

	@classmethod
	#returns all dogs inside dog.txt as list of Dog objects.
	def getAllDogs(self):
		db = open('dog.txt','r')
		result = []
		filas = csv.reader(db)

		for item in filas:
			dog = Dog(item[0], item[1])
			result.append(dog)
		
		return result


