# CasosDePrueba.py
from cadenaHolton import *
from hotel import *
from huesped import *
from habitacion import *
from datetime import datetime

# Crear una instancia de CadenaHolton
cadena = CadenaHolton("LeoHoteles")

# Primera historia de usuario
cadena.agregarHotel("tradicional", 6, 6, "Bogotá")
print(f"Se agregó el hotel {cadena.hoteles[0].nombre} a la cadena con {cadena.hoteles[0].numPisos} pisos y {cadena.hoteles[0].numHabitacionesPorPiso} habitaciones por piso de tipo {cadena.hoteles[0].tipoDeHotel}")
cadena.agregarHotel("tres estrellas", 9, 3, "Medellín", )
print(f"Se agregó el hotel {cadena.hoteles[1].nombre} a la cadena con {cadena.hoteles[1].numPisos} pisos y {cadena.hoteles[1].numHabitacionesPorPiso} habitaciones por piso de tipo {cadena.hoteles[1].tipoDeHotel}")

# Segunda historia de usuario
mostarHabitaciones = cadena.mostrarHoteles()

# Tercera historia de usuario
hotelE = cadena.hoteles[0]
cadena.asignarHabitacion(101, 1, hotelE)
huesped = Huesped("Juan", "123456789", datetime(2004, 7, 30), "Masculino", datetime(2023, 7, 30), datetime(2023, 7, 31))
asignada = cadena.asignarHabitacion(101, [huesped], hotelE)
print(f"Se asignó la habitación {hotelE.habitacionesH[0][0].numeroHabitacion} del hotel {hotelE.nombre} al huésped {huesped.nombreCompleto}")

HotelE = cadena.hoteles[1]
cadena.asignarHabitacion(201, 2, HotelE)
huesped = Huesped("Pedro", "123456289", datetime(2004, 7, 30), "Masculino", datetime(2023, 7, 30), datetime(2023, 7, 31))
huesped2 = Huesped("Maria", "123416789", datetime(2004, 7, 30), "Femenino", datetime(2023, 7, 30), datetime(2023, 7, 31))
asignada = cadena.asignarHabitacion(201, [huesped, huesped2], HotelE)
print(f"Se asignó la habitación {HotelE.habitacionesH[1][0].numeroHabitacion} del hotel {HotelE.nombre} al huésped {huesped.nombreCompleto} y {huesped2.nombreCompleto}")

# Quinta historia de usuario
habitacionEncontrada = HotelE.buscarHabitacion(201, 2)
montoPagar = cadena.cuantasNoches(habitacionEncontrada) * habitacionEncontrada.precioNoches * len(asignada.huespedes)
print(f"El monto a pagar es de {montoPagar}")

# Sexta historia de usuario
habitacionEncontrada = HotelE.buscarHabitacion(201, 2)
cadena.desocuparHabitacion(habitacionEncontrada)
print(f"Se desocupó la habitación {habitacionEncontrada.numeroHabitacion} del hotel {HotelE.nombre}")

# Septima historia de usuario
ihnabilitar = cadena.inhabilitarHabitacion(201, 2, HotelE)
print(f"Se inhabilitó la habitación {ihnabilitar.numeroHabitacion} del hotel {HotelE.nombre}")

# Octava historia de usuario

InformeDetallado = cadena.informeDetallado()
print(f"El informe detallado es: {InformeDetallado}")

# Novena historia de usuario

zonaConMayorAfluencia = cadena.zonaConMayorAfluencia()
print(f"La zona con mayor afluencia es: {zonaConMayorAfluencia}")

# Decima historia de usuario

porcentajesHombresMujeres = cadena.porcentajesHombresMujeres()
