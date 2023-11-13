#habitacion.py
from datetime import datetime


class Habitacion:
    def __init__(self, estado: str, numeroHabitacion: int, zona: str, numeroHuespedes: int, precioNoches: int, numerioMaximoHuespedes: int):
        self.estado = estado
        self.numeroHabitacion = numeroHabitacion
        self.zona = zona
        self.numeroHuespedes = numeroHuespedes
        self.precioNoches = precioNoches
        self.numeroMaximoHuespedes = numerioMaximoHuespedes
        self.huespedes = []

    def datosHabitacion(self) -> str:
        datos = f"Habitación {self.numero}: {self.tipo}, {self.numeroHuespedes} huésped(es), Precio: {self.precioNoches} por noche"
        
        # Verificar si hay huéspedes en la habitación
        if self.numeroHuespedes > 0:
            datos += f"\nHuéspedes: {', '.join(self.huespedes)}" # El Join es para unir los elementos de una lista
            datos += f"\nFecha de llegada: {self.fechaLlegada}"

        return datos


    def mostrarDatosHuespedes(self) -> str:
        datosHuespedes = ""
        for i in self.huespedes:
            datosHuespedes += f"{i.datosHuesped()}\n"
        return datosHuespedes
