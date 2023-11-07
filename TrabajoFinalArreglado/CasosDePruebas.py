from Hotel import *
from Huesped import *
from Habitación import *

# Crear una instancia de Hotel
# Crear una instancia de la clase Hotel
hotel = Hotel("Bogotá", "Hotel Estelar", "5 estrellas", 12, 6, "De lujo")
habitacion = Habitación("Libre", 1, "Piso 1", 2)
hotel.CrearHabitaciones(habitacion)

# Mostrar información del hotel
print(f"Hotel: {hotel.nombre}")
print(f"Ciudad: {hotel.ciudad}")
print(f"Tipo de Hotel: {hotel.tipoDeHotel}")
print(f"Pisos: {hotel.pisos}")
print(f"Habitaciones por piso: {hotel.habitacionesPorPiso}")
print(f"Cantidad total de habitaciones: {hotel.cantidadTotalDeHabitaciones}")

# Recomendar una habitación
habitacion = hotel.RecomendarHabitación(2, "Piso 1")
if habitacion:
    print(f"Habitación recomendada: {habitacion.numero} en el {habitacion.piso}")
else:
    print("No se encontraron habitaciones disponibles que cumplan con los criterios.")