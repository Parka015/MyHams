# -*- coding: utf-8 -*-
# 1)Clase para almacenar una lista de productos tipo "Producto" o "ProductoVenta"
# 2)Gestiona los productos desde una abstracción superior por lo que la creación y eliminación de 
# objetos tipo "Producto" o "ProductoVenta" debería hacerse desde aquí. 


class Productos:
    def __init__(self):
        self.productos= []	#Lista de objetos tipo "Producto" o "ProductoVenta"
        
     
    def getProductos(self):
        return self.productos
    
    def aniadirProducto(self,producto):
        pass
    
    def eliminarProducto(self,producto):
        pass
    

   
