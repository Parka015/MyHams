
#1)Para no duplicar informacion, todas los productosVenta que se creen debe ser
#creados desde la clase Producto con el metodo "ponerEnVenta"
#2)El resto de operaciones que sean sobre productoVenta estarán aqui
#3)Para eliminar un productosVenta al igual como el punto uno, se hace desde Producto con "retirarDeVenta"

from producto import *


class productoVenta(Producto):
    
    def __init__(self,nom,info, cantidad, precio):   
        
        # Invoca al constructor de clase Producto
        Producto.__init__(self, nom, info)

        self.cantidad = cantidad
        self.precio = precio
        
    def getPrecio(self):
        return self.precio
    
    def getCantidad(self):
        return self.cantidad
    

        
a = productoVenta ("patata", "Verdura", 10, 20)

print(f"nombre: {a.informacion}")