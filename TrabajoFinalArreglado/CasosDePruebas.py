from Hotel import *
<<<<<<< HEAD
from cadena import *

# Crear una instancia de Cadena
cadena = Cadena("Mi Cadena de Hoteles")

# Crear una instancia de Hotel
hotel = Hotel("Bogotá", "Hotel Estelar", "5 estrellas", 12, 7, "De lujo")

# Agregar el hotel a la cadena
if cadena.AgregarHotel(hotel):
    print("Hotel agregado con éxito a la cadena.")
else:
    print("No se pudo agregar el hotel a la cadena.")

# Mostrar los ingresos totales obtenidos por la cadena
total_ingresos = cadena.CalcularIngresosTotalesObtenidos()
print(f"Ingresos totales de la cadena: ${total_ingresos}")

# Recomendar una habitación en el hotel
habitacion_recomendada = hotel.RecomendarHabitacion(2, "Piso 1")
if habitacion_recomendada:
    print(f"Habitación recomendada: {habitacion_recomendada.numero} en el {habitacion_recomendada.piso}")
else:
    print("No se encontraron habitaciones disponibles que cumplan con los criterios.")
=======
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
>>>>>>> leoMasJona
