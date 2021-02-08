from model import Dog

def showAllDogView(list):
	print("In our db we have %i users. Here they are : " % len(list))
	for item in list:
		print(item.nameBreed())

def startView():
	print('MVC - the simplets example')
	print('Do you want to see everyone in my db? [y/n]')

def endView():
	print('Goodbay')