import numpy as np
from hotel import *


class CadenaHolton:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.tiposDeHotel = (('tradicional', 100000), ('tres estrellas', 200000), ('boutique', 300000), ('cinco estrellas', 400000))
        self.numerosDePisos = (6, 9, 12, 15)
        self.numMaxPersonasPorHabitacion = 4
        self.hoteles = []


    def agregarHotel(self, tipoHotel:str, numPisos: int, numHabitacionesPorPiso: int, ciudad:str) -> bool:
        tipoDeHotel = ()
        for h in self.tiposDeHotel:
            if(h[0] == tipoHotel):
                tipoDeHotel = h
                break

        numDePisos = -1
        if(numPisos in self.numerosDePisos):
            numDePisos = numPisos

        numHabitacionesPiso = -1
        if(numHabitacionesPorPiso > 0 and numHabitacionesPorPiso <= numDePisos ):
            numHabitacionesPiso = numHabitacionesPorPiso

        if(tipoHotel != () and numDePisos != -1 and numHabitacionesPiso != -1):
            hotel = Hotel(ciudad, (self.nombre + " " + ciudad), tipoDeHotel[0], numDePisos, numHabitacionesPiso, precioBase = tipoDeHotel[1], numeroMaximoHuespedes = self.numMaxPersonasPorHabitacion)
            self.hoteles.append(hotel)
            return True
        else:
            return False

    def mostrarHoteles(self):
        for hotel in self.hoteles:
            print("-----------------------")
            print(hotel.ciudad)
            print(hotel.nombre)
            print(hotel.tipoDeHotel)
            print(hotel.numPisos)
            print(hotel.numHabitacionesPorPiso)
            print(hotel.precioBase)
            print(hotel.zonasHotel)
            print(hotel.mostrarHabitaciones())   
            print("-----------------------")


   

        