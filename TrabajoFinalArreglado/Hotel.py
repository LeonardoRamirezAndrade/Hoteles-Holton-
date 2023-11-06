from datetime import date

import numpy as np

from array import array

import random

class Hotel:

    def __init__(self, ciudad:str, nombre:str, tipoDeHotel:str, pisos:int, habitacionesPorPiso:int):
        if pisos in (6, 9, 12, 15):
            if habitacionesPorPiso <= pisos:
                self.nombre = nombre
                self.tipoDeHotel = tipoDeHotel
                self.ciudad = ciudad
                self.pisos = pisos
                self.habitacionesPorPiso = habitacionesPorPiso
                self.habitaciones = np.full((pisos, habitacionesPorPiso), None) #Matriz para almacenar las habitaciones
                self.cantidadTotalDeHabitaciones = pisos * habitacionesPorPiso
                self.CrearHabitaciones()

    def CrearHabitaciones(self):
        for pisos in range(self.pisos):
            for NumeroDeHabitacion in range(self.habitacionesPorPiso):
                estado = 'Libre'
                numero = NumeroDeHabitacion + 1
                zona = f"Piso {pisos + 1}"
                maximo_personas = 4

    def mostrarHotel(self):
        pass
    
    def RecomendarHabitación(self) ->int:
        pass

    def AsignarHabitación(self ) ->bool:
        pass
    
    
    def Aceder_A_DatosHuespedesDeUnaHabitaciòn(self)-> bool:
        pass

    def RegistrarSalidaDeHuespedes(self) ->bool:
        pass



    def CalcularMonto_A_PagarHuspedesDeUnaHabitaciòn(self) ->float:
        pass
    
    def EstablecerHabitaciónComoNoDisponible(self) -> bool:
        pass
            

    def CalcularIngresosObtenidos(self):
        pass

    def CalcularCantidadDeHuespedesAtendidos(self) -> int:
        pass

    def CalcularCantidadDeHabitacionesOcupadas(self) -> int:
        pass

    def DeterminarZonaConMayorAfluencia(self) -> str:
        pass

    def CalcularTasaDeOcupaciòn(self) -> float:
        pass

    def CalcularCantidadDeHombresYMujeresAtendidos(self) -> int:
        pass


 

    



