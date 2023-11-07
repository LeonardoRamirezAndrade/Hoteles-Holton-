class Habitacion:
    def __init__(self, estado: str, numeroHabitacion: int, zona: str, numeroHuespedes: int, precioNoches:int, numerioMaximoHuespedes:int):
        self.estado = estado
        self.numeroHabitacion = numeroHabitacion 
        self.zona = zona
        self.numeroHuespedes = numeroHuespedes
        self.precioNoches = precioNoches
        self.numeroMaximoHuespedes =  numerioMaximoHuespedes
        self.huespedes = []


    def datosHabitacion(self) -> str:
        return f"{self.numeroHabitacion} - {self.precioNoches} / " 



    