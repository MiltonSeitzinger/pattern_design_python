from model import Dog
import view

def showAll():
	#gets list of all Dog objects
	dog_in_db = Dog.getAllDogs()
	#calls view
	return view.showAllDogView(dog_in_db)
	
def start():
	view.startView()
	value = input("Insert value: ")
	if value == 'y':
		return showAll()
	else:
		return view.endView()

if __name__ == "__main__":
	#running controller function
	start()