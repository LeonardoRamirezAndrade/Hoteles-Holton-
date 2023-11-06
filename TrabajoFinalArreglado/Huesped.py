from datetime import date

class Huesped:
    def __init__(self, nombre:str, fechaDeNacimiento:str, sexoBiologico:str):
        self.nombre = nombre
        self.fechaDeNacimiento = fechaDeNacimiento
        self.sexoBiologico = sexoBiologico

        
    def ValidarAtributosHuesped(self):
       pass

    def CalcularEdadHuesped(self)-> int:
        pass

    def DeterminarMayoriaDeEdad(self)-> str:
       pass
    
        