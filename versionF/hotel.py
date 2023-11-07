import numpy as np

class Hotel:

    def __init__(self, ciudad: str,nombre:str, tipoDeHotel: str, numPisos: int, numHabitacionesPorPiso: int, precioBase: float):
        self.ciudad = ciudad
        self.nombre = nombre
        self.tipoDeHotel = tipoDeHotel
        self.numPisos = numPisos
        self.numHabitacionesPorPiso = numHabitacionesPorPiso
        self.habitacionesH = np.full((numPisos, numHabitacionesPorPiso), None) 
        self.precioBase = precioBase
        self.zonasHotel = ('Basica', 'Preferencial', 'De lujo')

