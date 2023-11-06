import numpy as np

class Habitación:
    def __init__(self, estado:str, numero:int, zona:str, maximoHuespedes:int):
        self.estado = estado
        self.numero = numero
        self.zona = zona
        self.maximoPersonasHabitación = maximoHuespedes
        self.huespedes = []
        self.estados = ('Libre', 'Ocupada', 'No habilitada')
        self.fechaIngresoHuespedes = None
        self.fehaSalidaHuespedes = None
        self.ValidarAtributosHabitación()

    def ValidarAtributosHabitación(self):
        minimaCadena = 1
        if len(self.estado) < minimaCadena:
            raise ValueError("Este campo no puede ir vacío, debe ingresar el estado de la habitación")
        if self.estado not in self.estados:
             raise ValueError("El tipo de estado ingresado no es correcto")