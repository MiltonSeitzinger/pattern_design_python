class Singleton():
	__instance = None

	@staticmethod
	def getInstance():
		if Singleton.__instance == None:
			Singleton()
		return Singleton.__instance
	
	def __init__(self):
		if Singleton.__instance != None:
			raise Exception("This class is a Singleton")
		else:
			Singleton.__instance = self

s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)
# El número de instancias creadas es el mismo y no hay diferencia en los objetos listados en la salida.
