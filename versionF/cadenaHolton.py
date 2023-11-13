#cadenaHolton.py
import numpy as np
from hotel import *


class CadenaHolton: #Clase que representa la cadena de hoteles Holton
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.tiposDeHotel = (('tradicional', 100000), ('tres estrellas', 200000), ('boutique', 300000),
                             ('cinco estrellas', 400000))  # Tipo de hotel y precio base
        self.numerosDePisos = (6, 9, 12, 15)  # Numero de pisos permitidos
        self.numPisos = 0
        self.numHabitacionesPorPiso = 0
        self.numMaxPersonasPorHabitacion = 4
        self.hoteles = []  # Lista de hoteles
            
    def agregarHotel(self, tipoHotel: str, numPisos: int, numHabitacionesPorPiso: int, ciudad: str) -> bool:
    # Validar el tipo de hotel
        if tipoHotel not in ("tradicional", "tres estrellas", "boutique", "cinco estrellas"):
            return False

        # Validar el número de pisos
        if numPisos not in self.numerosDePisos:
            return False

        # Validar el número de habitaciones por piso
        if numHabitacionesPorPiso <= 0 or numHabitacionesPorPiso > numPisos:
            return False

        # Buscar la información del tipo de hotel
        tipoDeHotel = next((h for h in self.tiposDeHotel if h[0] == tipoHotel), None)

        # Verificar si se encontró la información del tipo de hotel
        if tipoDeHotel is None:
            return False

        # Crear una instancia de Hotel
        hotel = Hotel(ciudad, f"{self.nombre} {ciudad}", tipoDeHotel[0], numPisos, numHabitacionesPorPiso,
                    precioBase=tipoDeHotel[1], numeroMaximoHuespedes=self.numMaxPersonasPorHabitacion)

        # Agregar el hotel a la lista
        self.hoteles.append(hotel)

        return True


                
        #Historia de usuario # 3: Como Gerente de 
    #Holtons en Colombia, quiero calcular el monto 
    #que los huéspedes de una habitación deben 
    #pagar al momento de su salida, asegurando que 
    #la cantidad se determine según las reglas y 
    #tarifas de cobro de la empresa
    #    
    #  
    def asignarHabitacion(self, numeroHabitacion, huespedes):
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                habitacion = self.habitacionesH[i][j]
                if habitacion.numeroHabitacion == numeroHabitacion and habitacion.estado == 'libre':
                    habitacion.estado = 'ocupada'
                    habitacion.huespedes = huespedes
                    return True  # Habitación asignada exitosamente

        return False
    
    
    def mostrarHoteles(self):
        for hotel in self.hoteles:
            print(f"Nombre del hotel: {hotel.nombre}, Ciudad: {hotel.ciudad}, Tipo de hotel: {hotel.tipoDeHotel}")
            hotel.mostrarHabitaciones()
            print()

    def mostrarHuespedesHabitacion(self, numeroHabitacion: int) -> str:
        datosHuespedes = ""
        habitacionEncontrada = None
        hotelEncontrado = None

        # Buscar la habitación en la lista de hoteles
        for hotel in self.hoteles:
            for i in range(hotel.numPisos):
                for j in range(hotel.numHabitacionesPorPiso):
                    habitacion = hotel.habitacionesH[i][j]
                    if habitacion.numeroHabitacion == numeroHabitacion and habitacion.estado == "ocupada":
                        habitacionEncontrada = habitacion
                        hotelEncontrado = hotel
                        break
                if habitacionEncontrada:
                    break

        if habitacionEncontrada is not None:
            datosHuespedes = habitacionEncontrada.mostrarDatosHuespedes()
        else:
            datosHuespedes = "No se encontró la habitación"

        return datosHuespedes

