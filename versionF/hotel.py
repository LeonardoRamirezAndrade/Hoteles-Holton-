import math
import numpy as np
from habitacion import *

class Hotel:

    def __init__(self, ciudad: str,nombre:str, tipoDeHotel: str, numPisos: int, numHabitacionesPorPiso: int, precioBase: float, numeroMaximoHuespedes:int):
        self.ciudad = ciudad
        self.nombre = nombre
        self.tipoDeHotel = tipoDeHotel
        self.numPisos = numPisos
        self.numHabitacionesPorPiso = numHabitacionesPorPiso
        self.habitacionesH = np.full((numPisos, numHabitacionesPorPiso), None) 
        self.precioBase = precioBase
        self.zonasHotel = ('Basica', 'Preferencial', 'De lujo')
        self.estadoHabitacion = ('libre', 'ocupada', 'no habilitada para uso')
        self.ganaciasTotalesTemporales = 0
        self.numeroMaximoHuespedes = numeroMaximoHuespedes
        self.llenarhabitaciones()

    def llenarhabitaciones(self):
        preferencial = math.ceil(self.numPisos*(1/3))  
        deLujo = math.ceil(self.numPisos*(2/3))  

        precioBasico = self.precioBase
        precioPreferencial = precioBasico*0.15 + precioBasico
        precioDeLujo = precioBasico*0.2 + precioBasico

        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                numHabitacion = ((i+1)*100)+(j+1)
                estadoHab = Habitacion(self.estadoHabitacion[0])
                if(i >= 0 and i < preferencial):
                    self.habitacionesH[i][j] = Habitacion(estadoHab, numHabitacion, self.zonasHotel[0], 0, precioBasico, self.numeroMaximoHuespedes)  
                elif(i >= preferencial and i < deLujo): 
                    self.habitacionesH[i][j] = Habitacion(estadoHab, numHabitacion, self.zonasHotel[1], 0, precioPreferencial, self.numeroMaximoHuespedes) 
                elif(i >= deLujo) :
                    self.habitacionesH[i][j] = Habitacion(estadoHab, numHabitacion, self.zonasHotel[2], 0, precioDeLujo, self.numeroMaximoHuespedes)

    
    def mostrarHabitaciones(self) -> str:
        datosHabitaciones = ""
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                datosHabitaciones += f"{self.habitacionesH[i][j].datosHabitacion()}"
                
            datosHabitaciones += "\n"
        return datosHabitaciones
    
    #Historia de usuario # 2: retornes vector con las habitaciones recomendadas

    #Historia de usuario # 3: funcion (numero habitacion, piso, huespedesPasados[])
        #aqui vas a recorrer las habitaciones y vas a buscar la que dijo el usuario, si esta disponible entonces 
        """
        Vas a guardar esa habitacion en una variable por ejp: habitacionEncontrada
        habitacionEncontrada.huespedes = pasados[]

        osea, en la interfaz debes pedir cuantos huespedes se van a quedar  y vas a hacer un while pidiendo cada huesped, lo agregas a un vector y se lo mandas a esta vaina
        """

    #Historia de usuario # 4: crea un metodo igual que datosHabitacion que está en la clase habitación
        #Osea, dentro de huesped vas a crear mostrarDatosHuesped y dentro de Habitacion vas a crear mostrarHuespedes
        #osea, mostrarHuespedes va a ser similar a lo que haces en mostrar habitación dentro de Hotel

    #Historia de usuario # 5:  

    #Historia de usuario # 7:
        #Debes crear un metodo que reciba el numero de habitacion
        #Debes crear una variable y luego haces un for dentro de habitacionesH y buscas la habitacion que tenga el numero de habitacion que te pasaron
        #Luego vas a hacer un por ejemplo si la variable la llamaste habitaciónEncontrada, haces un habitacionEncontrada.estado = self.estadoHabitacion[2]

