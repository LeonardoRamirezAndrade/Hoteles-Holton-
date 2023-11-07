from cadena_holton import *
from hotel import *


cadena = CadenaHolton("Holton")

cadena.agregarHotel("tradicional", 6, 4,"Santa Marta")
cadena.agregarHotel("tres estrellas", 6, 5,"Bógota")
cadena.agregarHotel("boutique", 6, 3,"Medellín")

cadena.mostrarHoteles()

