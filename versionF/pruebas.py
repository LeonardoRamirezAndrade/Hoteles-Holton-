from cadena_holton import *
from hotel import *
from habitacion import *
from huesped import *


cadena = CadenaHolton("Holton")

cadena.agregarHotel("tradicional", 9, 4,"Santa Marta")
cadena.agregarHotel("tres estrellas", 6, 5,"Bógota")
cadena.agregarHotel("boutique", 6, 3,"Medellín")
cadena.agregarHotel("cinco estrellas", 6, 3,"Popayan")

cadena.mostrarHoteles()

print("-------------------------------------------------\n")
recomendadas = cadena.hoteles[1].recomendarHabitaciones(2, "preferencial")
for i in recomendadas:
    print(i.datosHabitacion())

print("-------------------------------------------------\n")

huespedes = []

huespedes.append(Huesped("Juan Perez", 1082908063, "12/12/1990", "M", "12/12/2023", ""))
huespedes.append(Huesped("Maria Perez", 1082908063, "12/12/1990", "F", "12/12/2023", ""))
huespedes.append(Huesped("Jose Perez", 1082908063, "12/12/1990", "M", "12/12/2023", ""))


print(cadena.hoteles[1].mostrarHabitaciones())

cadena.hoteles[1].asignarHabitacion(301, huespedes)


print(cadena.hoteles[1].mostrarHabitaciones())

print("-------------------------------------------------\n")
recomendadas = cadena.hoteles[1].recomendarHabitaciones(2, "basica")
for i in recomendadas:
    print(i.datosHabitacion())

print("-------------------------------------------------\n")


print(cadena.hoteles[1].mostrarHuespedes(301))

