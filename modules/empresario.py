# -*- coding: utf-8 -*-


from productos import *

class Empresario:
    def __init__(self,nombre, email):
        self.nombre= nombre	
        self.email = None	#El identificador de cada empresario
        self.productos = None #Objeto de tipo "Productos"
        self.productosVenta = None	#Objeto de tipo "Productos"
    
    
    def getNombre(self):
        return self.nombre
    
    def getEmail(self):
        return self.nombre
    
    def getProductos(self):
         return self.productos
    
    def getProductosVenta(self):
        return self.productosVenta
    
    #Añade un "Producto"
    def aniadirProducto(self,producto):
        pass
    
    #Elimina un "Producto" de productos, si exitía en productosVenta se elimina también de ahí
    def eliminarProducto(self,producto):
        pass
    
    #Añade un "ProductoVenta" a productosVenta, si no existía el "Producto" se crea tambien en productos
    def aniadirProductoVenta(self,producto):
        pass
    
    #Elimina un "ProductoVenta"
    def eliminarProductoVenta(self,producto):
        pass
