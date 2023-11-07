import numpy as np

class Habitacion:
    def __init__(self, estado:str, numero:int, zona:str, maximoHuespedes:int):
        self.estado = estado
        self.numero = numero
        self.zona = zona
        self.maximoPersonasHabitacion = maximoHuespedes
        self.huespedes = []
        self.estados = ('Libre', 'Ocupada', 'No habilitada')
        self.fechaIngresoHuespedes = None
        self.fechaSalidaHuespedes = None
        self.ValidarAtributosHabitacion()  # Llama a la función de validación en el constructor


    def ValidarAtributosHabitacion(self):
        minimaCadena = 1
        if len(self.estado) < minimaCadena:
            raise ValueError("Este campo no puede ir vacío, debe ingresar el estado de la habitación")
        if self.estado not in self.estados:
            raise ValueError("El tipo de estado ingresado no es correcto")
