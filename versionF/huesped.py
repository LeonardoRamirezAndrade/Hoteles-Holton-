#huesped.py
from datetime import datetime

class Huesped:
    def __init__(self, nombreCompleto, cedula, fechaNacimiento, sexo, fechaEntrada, fechaSalida):
        self.nombreCompleto = nombreCompleto
        self.cedula = cedula
        self.fechaNacimiento = fechaNacimiento
        self.sexo = sexo
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida

# El resto de tu programa continúa aquí o puedes realizar las operaciones que necesites con la lista de 'huespedes'


    def datosHuesped(self) -> str:
        return f"{self.nombreCompleto} - {self.cedula} - {self.fechaNacimiento} - {self.sexo} - {self.fechaEntrada} - {self.fechaSalida} / "


