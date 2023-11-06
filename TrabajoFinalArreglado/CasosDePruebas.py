# Importa la clase Hotel desde tu archivo
from Hotel import Hotel

# Crea una instancia de Hotel
mi_hotel = Hotel(ciudad="Bogotá", nombre="Hotel Ejemplo", tipoDeHotel="Cinco estrellas", pisos=6, habitacionesPorPiso=4)

# Imprime algunos atributos para verificar que se han inicializado correctamente
print("Nombre del hotel:", mi_hotel.nombre)
print("Ciudad:", mi_hotel.ciudad)
print("Tipo de hotel:", mi_hotel.tipoDeHotel)
print("Número de pisos:", mi_hotel.pisos)
print("Número de habitaciones por piso:", mi_hotel.habitacionesPorPiso)
print("Cantidad total de habitaciones:", mi_hotel.cantidadTotalDeHabitaciones)
