from Hotel import *
from Cadena import *

# Crear una instancia de Cadena
cadena = Cadena("Mi Cadena de Hoteles")

# Crear una instancia de Hotel
hotel = Hotel("Bogotá", "Hotel Estelar", "5 estrellas", 12, 6, "De lujo")

# Agregar el hotel a la cadena
if cadena.AgregarHotel(hotel):
    print("Hotel agregado con éxito a la cadena.")
else:
    print("No se pudo agregar el hotel a la cadena.")

# Mostrar los ingresos totales obtenidos por la cadena
total_ingresos = cadena.CalcularIngresosTotalesObtenidos()
print(f"Ingresos totales de la cadena: ${total_ingresos}")

# Recomendar una habitación en el hotel
habitacion_recomendada = hotel.RecomendarHabitación(2, "Piso 1")
if habitacion_recomendada:
    print(f"Habitación recomendada: {habitacion_recomendada.numero} en el {habitacion_recomendada.piso}")
else:
    print("No se encontraron habitaciones disponibles que cumplan con los criterios.")
