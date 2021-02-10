class Button(object):
	html = ""
	def get_html(self):
		return self.html

class Image(Button):
	html = "<img></img>"

class Input(Button):
	html = "<input></input>"

class Flash(Button):
	html = "<obj></obj>"

class ButtonFactory():
	def create_button(self, typ):
		targetclass = typ.capitalize()
		return globals()[targetclass]()

"""
La clase boton ayuda a crear las etiquetas html y la página html asociada.
El cliente no tendrá acceso a la lógica del código y la salida represanta la creación de la pagina html.
"""

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
	print(button_obj.create_button(b).get_html())

"""
El código python incluye la lógica de las etiquetas html, que especifican el valor. 
El usuario final puede echar un vistazo al archivo HTML creado por el código Python.
"""