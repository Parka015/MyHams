
#Clase para almacenar todos los productos de un empresario (esten en venta o no)

class Productos:
    def __init__(self):
        self.productos= []
        self.productosVenta = None	#Será un objeto de tipo "productosVenta"

    def getProductos(self):
		return self.productos
	
	def getProductosVenta(self):
		return self.productos
	
	def aniadirProducto(self,producto):
		pass
	
	def eliminarProducto(self,nombre_producto):
		pass
	
	def aniadirProductoVenta(self,producto):
		pass
	
	def eliminarProductoVenta(self,nombre_producto):
		pass
	
   
