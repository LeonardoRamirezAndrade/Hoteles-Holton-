class Huesped:
    def __init__(self, nombreCompleto:str, cedula:int, fechaNacimiento: str, sexo:str, fechaEntrada:str, fechaSalida:str):  
        self.nombreCompleto = nombreCompleto
        self.cedula = cedula
        self.fechaNacimiento = fechaNacimiento
        self.sexo = sexo
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida

    def datosHuesped(self) -> str:
        return f"{self.nombreCompleto} - {self.cedula} - {self.fechaNacimiento} - {self.sexo} - {self.fechaEntrada} - {self.fechaSalida} / "


