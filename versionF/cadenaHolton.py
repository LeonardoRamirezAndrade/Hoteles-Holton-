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
    def asignarHabitacion(self, numeroHabitacion: int, huespedes:[Huesped], hotel: Hotel):

        for i in range(hotel.numPisos):
            for j in range(hotel.numHabitacionesPorPiso):
                habitacion = hotel.habitacionesH[i][j]
                if habitacion.numeroHabitacion == numeroHabitacion and habitacion.estado == 'libre':
                    habitacion.estado = 'ocupada'
                    habitacion.huespedes = huespedes
                    return True  # Habitación asignada exitosamente

        return False
    
    
    def mostrarHoteles(self):
        for hotel in self.hoteles:
            print(f"Nombre del hotel: {hotel.nombre}, Ciudad: {hotel.ciudad}, Tipo de hotel: {hotel.tipoDeHotel}")
            print(hotel.mostrarH())
            print("\n")
    
    def buscarHotel(self, hotel: str)->int:
        for i in range(len(self.hoteles)):
            if self.hoteles[i].nombre == hotel:
                return i
            
        return -1


    def mostrarHuespedesHabitacion(self, numeroHabitacion: int, posicionHotel: int) -> str:
        datosHuespedes = ""
        habitacionEncontrada = None

        hotelE = self.hoteles[posicionHotel]
        # Buscar la habitación en la lista de hoteles
        if hotelE is not None:
            for i in range(hotelE.numPisos):
                for j in range(hotelE.numHabitacionesPorPiso):
                    habitacion = hotelE.habitacionesH[i][j]
                    if habitacion.numeroHabitacion == numeroHabitacion:
                        habitacionEncontrada = habitacion
                        break
        if habitacionEncontrada is not None:
            datosHuespedes = habitacionEncontrada.mostrarDatosHuespedes()
        else:
            datosHuespedes = "No se encontró la habitación"

        return datosHuespedes
    
    #    Historia de usuario # 8: Como Gerente     #de Holtons en Colombia, deseo recibir un     #informe detallado que muestre los ingresos     #obtenidos por la cadena, el número de     #huéspedes atendidos y la cantidad de     #habitaciones ocupadas, para evaluar el     #cumplimiento de nuestras metas     #empresariales.

    def mostrarInforme(self):
        numeroHOcupadas = 0
        numeroHAtendidos = 0
        ganaciasT = 0
        for hotel in self.hoteles:
            numeroHOcupadas += hotel.numHOcupadas()
            numeroHAtendidos += hotel.numeroHuespedesAtendidos
            ganaciasT += hotel.ganaciasTotales
        print("Ganancias totales: ", ganaciasT)
        print("Numero de huespedes atendidos: ", numeroHAtendidos)
        print("Numero de habitaciones ocupadas: ", numeroHOcupadas)

    def mostrarHotelesSel(self):
        
        for i in range(len(self.hoteles)):
            print(f"{i + 1}. {self.hoteles[i].nombre}") 
        

   