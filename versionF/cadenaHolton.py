#cadenaHolton.py
import numpy as np
from hotel import *


class CadenaHolton: #Clase que representa la cadena de hoteles Holton
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.tiposDeHotel = (('tradicional', 100000), ('tres estrellas', 200000), ('boutique', 300000),
                             ('cinco estrellas', 400000))  # Tipo de hotel y precio base
        self.numerosDePisos = (6, 9, 12, 15)  # Numero de pisos permitidos
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
    def asignarHabitacion(self, numeroHabitacion: int, huespedesPasados: list[Huesped]):
        habitacionEncontrada = None
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                if (
                    self.habitacionesH[i][j].numeroHabitacion == numeroHabitacion
                    and self.habitacionesH[i][j].estado == self.estadoHabitacion[0]
                ):
                    habitacionEncontrada = self.habitacionesH[i][j]
                    break
        if habitacionEncontrada != None:
            if len(huespedesPasados) <= self.numeroMaximoHuespedes and len(huespedesPasados) > 0:
                habitacionEncontrada.huespedes = huespedesPasados
                habitacionEncontrada.estado = self.estadoHabitacion[1]
            else:
                print("No se puede asignar la habitacion, la cantidad de huespedes es incorrecta")
        else:
            print("No se encontro la habitacion")
    
    def mostrarHoteles(self):
        if len(self.hoteles) == 0:
            print("No hay hoteles registrados.")
        else:
            for hotel in self.hoteles:
                print("------------------------")
                print(hotel.datosHotel())
                print("------------------------")


cadenaHoltonInstance = CadenaHolton("Holton")

