from cadenaHolton import *
from hotel import *
from habitacion import *
from huesped import *


# Crea una instancia de CadenaHolton
cadena_holton = CadenaHolton("HoltonChain")

# Agrega un hotel a la cadena
if not cadena_holton.agregarHotel("tradicional", 6, 10, "Bogotá"):
    print("Failed to add hotel")

# Obtiene el primer hotel en la cadena
if cadena_holton.hoteles:
    hotel_prueba = cadena_holton.hoteles[0]
    # Prueba de Historia de Usuario #2: Recomendar Habitaciones según Preferencias del Huésped
    habitaciones_recomendadas = hotel_prueba.recomendarHabitaciones(2, 'preferencial')
else:
    print("No hotels in the list")

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
