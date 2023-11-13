from cadenaHolton import *
from hotel import *
from huesped import *
from habitacion import *
from datetime import datetime

# Crear una instancia de CadenaHolton
cadena = CadenaHolton("Mi Cadena de Hoteles")

# Primera historia de usuario

print(cadena.agregarHotel("tradicional", 6, 6, "Bogotá"), f"Se agregó el hotel {cadena.hoteles[0].nombre} a la cadena")
print(cadena.agregarHotel("tres estrellas", 9, 9, "Medellín", ))
print(cadena.agregarHotel("boutique", 12, 12, "Cali"))
print(cadena.agregarHotel("cinco estrellas", 15, 15, "Cartagena"))
print(cadena.agregarHotel("tradicional", 6, 6, "Bogotá"))
print(cadena.agregarHotel("tres estrellas", 9, 9, "Medellín"))
print(cadena.agregarHotel("boutique", 12, 12, "Cali"))
print(cadena.agregarHotel("cinco estrellas", 15, 15, "Cartagena"))



    
# Segunda historia de usuario

# Crear una instancia de Hotel



