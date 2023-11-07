from datetime import date

sexo = {
    "M": "Masculino",
    "F": "Femenino",
    "O": "Otro"
}

class Huesped:
    def __init__(self, nombre:str, fechaDeNacimiento:str, sexoBiologico:str):
        self.nombre = nombre
        self.fechaDeNacimiento = fechaDeNacimiento
        self.sexoBiologico = sexoBiologico

        
    def ValidarAtributosHuesped(self):
        if not self.nombre:
           raise ValueError("El nombre del huésped no puede estar vacío")
        try:
            fecha_nacimiento = date.fromisoformat(self.fechaDeNacimiento)
        except ValueError:
            raise ValueError("La fecha de nacimiento no tiene un formato válido")
        if not self.sexoBiologico in sexo:
            raise ValueError("El sexo del huésped no es válido")


    def CalcularEdadHuesped(self)-> int:
        pass

    def DeterminarMayoriaDeEdad(self)-> str:
       pass
    
