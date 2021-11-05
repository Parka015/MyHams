
#Clase para almacenar la info de un producto de un empresario, debería estar dentro de algún objeto de la clase "Productos"

class Producto:
    def __init__(self, nom, info):
        self.nombre = nom    # Correspondiente al nombre del producto
        self.informacion= info # Información del producto

    def getNombre(self):
		return self.nombre
	
	def getEnVenta(self):
		return self.en_venta
	
	def getInformacion(self):
		return self.informacion
	

   
