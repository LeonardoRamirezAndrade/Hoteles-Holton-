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
huespedes.append(Huesped("Pedro Perez", 1082908063, "12/12/1990", "M", "12/12/2023", ""))


print(cadena.hoteles[1].mostrarHabitaciones())

cadena.hoteles[1].asignarHabitacion(301, huespedes)


print(cadena.hoteles[1].mostrarHabitaciones())

print("-------------------------------------------------\n")
recomendadas = cadena.hoteles[1].recomendarHabitaciones(2, "basica")
for i in recomendadas:
    print(i.datosHabitacion())

print("-------------------------------------------------\n")


print(cadena.hoteles[1].mostrarHuespedes(301))

print("-------------------------------------------------\n")

# Crear una cadena Holton y agregar un hotel
cadena_holton = CadenaHolton("HoltonChain")
cadena_holton.agregarHotel("tradicional", 6, 3, "Bogotá")

# Obtener el primer hotel de la cadena
primer_hotel = cadena_holton.hoteles[0]

# Mostrar las habitaciones del hotel
print("Historia de Usuario #1: Llenado de Habitaciones al Crear un Hotel")
print(primer_hotel.mostrarHabitaciones())
print("----------------------------------------------")

# Recomendar habitaciones para 2 personas en la zona preferencial
print("Historia de Usuario #2: Recomendar Habitaciones según Preferencias del Huésped")
habitaciones_recomendadas = primer_hotel.recomendarHabitaciones(2, 'preferencial')
for habitacion in habitaciones_recomendadas:
    print(habitacion.datosHabitacion())
print("----------------------------------------------")

# Asignar huéspedes a una habitación
print("Historia de Usuario #3: Asignar Huéspedes a una Habitación")
huesped1 = Huesped("Juan Pérez", 123456789, "1990-01-01", "Masculino", "2023-11-01", "2023-11-05")
huesped2 = Huesped("Ana Gómez", 987654321, "1985-05-15", "Femenino", "2023-11-01", "2023-11-05")
primer_hotel.asignarHabitacion(101, [huesped1, huesped2])
print(primer_hotel.mostrarHuespedes(101))
print("----------------------------------------------")

# Mostrar huéspedes de una habitación
print("Historia de Usuario #4: Mostrar Huéspedes de una Habitación")
print(primer_hotel.mostrarHuespedes(101))
print("----------------------------------------------")

# Calcular el monto a pagar por los huéspedes
print("Historia de Usuario #5: Calcular el Monto a Pagar por los Huéspedes")
monto_pagar = primer_hotel.montoAPagar(101)
print(f"Monto a pagar por la habitación 101: ${monto_pagar}")
print("----------------------------------------------")


print("----------------------------------------------")

from hotel import Hotel
from huesped import Huesped

# Crea una instancia de CadenaHolton
cadena_holton = CadenaHolton("HoltonChain")

# Agrega un hotel a la cadena
cadena_holton.agregarHotel("tradicional", 6, 10, "Bogotá")

# Obtiene el primer hotel en la cadena
hotel_prueba = cadena_holton.hoteles[0]

# Prueba de Historia de Usuario #2: Recomendar Habitaciones según Preferencias del Huésped
habitaciones_recomendadas = hotel_prueba.recomendarHabitaciones(2, 'preferencial')
print("Historia de Usuario #2: Recomendar Habitaciones")
print("Habitaciones Recomendadas:")
for habitacion in habitaciones_recomendadas:
    print(habitacion.datosHabitacion())
print("\n")

# Prueba de Historia de Usuario #5: Calcular el Monto a Pagar por los Huéspedes
# Agrega huéspedes a una habitación
huesped1 = Huesped("Juan Pérez", 123456789, "1990-01-01", "Masculino", "2023-11-01", "2023-11-05")
huesped2 = Huesped("Ana Gómez", 987654321, "1985-05-15", "Femenino", "2023-11-01", "2023-11-05")
hotel_prueba.asignarHabitacion(101, [huesped1, huesped2])

# Calcula el monto a pagar
monto_pagar = hotel_prueba.montoAPagar(101)
print("Historia de Usuario #5: Calcular el Monto a Pagar por los Huéspedes")
print(f"Monto a pagar por la habitación 101: ${monto_pagar}")
print("\n")

# Prueba de Historia de Usuario #6: Desocupar Habitación
hotel_prueba.desocuparHabitacion(101)
print("Historia de Usuario #6: Desocupar Habitación")
print("Estado de la habitación 101 después de desocupar:")
print(hotel_prueba.mostrarHabitaciones())
print("\n")

# Prueba de Historia de Usuario #7: Inhabilitar Habitación
hotel_prueba.inhabilitarHabitaciones(102)
print("Historia de Usuario #7: Inhabilitar Habitación")
print("Estado de la habitación 102 después de inhabilitar:")
print(hotel_prueba.mostrarHabitaciones())
print("\n")

# Prueba de Historia de Usuario #8: Mostrar Informe
print("Historia de Usuario #8: Mostrar Informe")
hotel_prueba.mostrarInforme()
print("\n")

# Prueba de Historia de Usuario #9: Mostrar Zona con Mayor Afluencia
print("Historia de Usuario #9: Mostrar Zona con Mayor Afluencia")
zona_mayor_afluencia = hotel_prueba.mostrarZonaMayorAfluencia()
print(zona_mayor_afluencia)
print("\n")

# Prueba de Historia de Usuario #10: Mostrar Porcentaje de Hombres y Mujeres
print("Historia de Usuario #10: Mostrar Porcentaje de Hombres y Mujeres")
porcentaje_hombres, porcentaje_mujeres = hotel_prueba.mostrarPorcentajeHombresYMujeres()
print(f"Porcentaje de Hombres: {porcentaje_hombres}%")
print(f"Porcentaje de Mujeres: {porcentaje_mujeres}%")
