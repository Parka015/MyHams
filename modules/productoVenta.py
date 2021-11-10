# -*- coding: utf-8 -*-
# Para no duplicar informacion, todas los "productoVenta" que se creen debe ser
# creados desde la clase "Productos" lo mismo ocurre con la eliminación


from producto import *


class ProductoVenta(Producto):
    
    def __init__(self,nom,info, cantidad, precio):   
        
        # Invoca al constructor de clase Producto
        Producto.__init__(self, nom, info)

        self.cantidad = cantidad
        self.precio = precio
        
    def getPrecio(self):
        return self.precio
    
    def getCantidad(self):
        return self.cantidad
    

