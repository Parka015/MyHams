
# Clase para almacenar todos los productos de un empresario (esten en venta o no)

class Productos:
    def __init__(self):
        self.productos= []	#El identificador de cada producto será su nombre
        self.productosVenta = None	#Será un objeto de tipo "productosVenta"
    
    
    def getProductos(self):
        return self.productos
    
    def getProductosVenta(self):
        return self.productosVenta
    
    def aniadirProducto(self,producto):
        pass
    
    def eliminarProducto(self,producto):
        pass
    
    def aniadirProductoVenta(self,producto):
        pass
    
    def eliminarProductoVenta(self,producto):
        pass
    

   
