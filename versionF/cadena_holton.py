import numpy as np
from hotel import *


class CadenaHolton: #Clase que representa la cadena de hoteles Holton
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.tiposDeHotel = (('tradicional', 100000), ('tres estrellas', 200000), ('boutique', 300000), ('cinco estrellas', 400000)) #Tipo de hotel y precio base
        self.numerosDePisos = (6, 9, 12, 15) #Numero de pisos permitidos
        self.numMaxPersonasPorHabitacion = 4
        self.hoteles = [] #Lista de hoteles


    def agregarHotel(self, tipoHotel:str, numPisos: int, numHabitacionesPorPiso: int, ciudad:str) -> bool: #Metodo para agregar un hotel a la cadena
        tipoDeHotel = () 
        for h in self.tiposDeHotel: #Validacion de tipo de hotel
            if(h[0] == tipoHotel): 
                tipoDeHotel = h
                break

        numDePisos = -1 #Validacion de numero de pisos
        if(numPisos in self.numerosDePisos):
            numDePisos = numPisos 

        numHabitacionesPiso = -1 #Validacion de numero de habitaciones por piso
        if(numHabitacionesPorPiso > 0 and numHabitacionesPorPiso <= numDePisos ):
            numHabitacionesPiso = numHabitacionesPorPiso 

        if(tipoHotel != () and numDePisos != -1 and numHabitacionesPiso != -1): #Si los datos son validos se agrega el hotel
            hotel = Hotel(ciudad, (self.nombre + " " + ciudad), tipoDeHotel[0], numDePisos, numHabitacionesPiso, precioBase = tipoDeHotel[1], numeroMaximoHuespedes = self.numMaxPersonasPorHabitacion) #Se crea el hotel
            self.hoteles.append(hotel)
            return True
        else:
            return False

    def mostrarHoteles(self): #Metodo para mostrar los hoteles de la cadena
        for hotel in self.hoteles:
            print("------------------------")
            print(hotel.ciudad)
            print(hotel.nombre)
            print(hotel.tipoDeHotel)
            print(hotel.numPisos)
            print(hotel.numHabitacionesPorPiso)
            print(hotel.precioBase)
            print(hotel.zonasHotel)
            print(hotel.mostrarHabitaciones())  
            print("------------------------")


   

        