import math
import numpy as np
from huesped import *
from habitacion import *

class Hotel:

    def __init__(self, ciudad: str,nombre:str, tipoDeHotel: str, numPisos: int, numHabitacionesPorPiso: int, precioBase: float, numeroMaximoHuespedes:int): #Constructor de la clase hotel
        self.ciudad = ciudad
        self.nombre = nombre
        self.tipoDeHotel = tipoDeHotel
        self.numPisos = numPisos
        self.numHabitacionesPorPiso = numHabitacionesPorPiso
        self.habitacionesH = np.full((numPisos, numHabitacionesPorPiso), None) 
        self.precioBase = precioBase
        self.zonasHotel = ('basica', 'preferencial', 'de lujo')
        self.estadoHabitacion = ('libre', 'ocupada', 'no habilitada para uso')
        self.ganaciasTotalesTemporales = 0
        self.numeroMaximoHuespedes = numeroMaximoHuespedes
        self.llenarhabitaciones()

    def llenarhabitaciones(self): #Metodo para llenar las habitaciones del hotel
        preferencial = math.ceil(self.numPisos*(1/3))  #Esto hace que la preferencial ocupe el 33.33% de los pisos
        deLujo = math.ceil(self.numPisos*(2/3))  

        precioBasico = self.precioBase 
        precioPreferencial = precioBasico*0.15 + precioBasico #Esta parte del codigo hace que el precio preferencial se le adicione el 15% del precio base, y al precio de lujo se le adicione el 20% del precio base
        precioDeLujo = precioBasico*0.2 + precioBasico

        for i in range(self.numPisos): #Se llena la matriz de habitaciones
            for j in range(self.numHabitacionesPorPiso):
                numHabitacion = ((i+1)*100)+(j+1) #Se calcula el numero de habitacion
                estadoHab = self.estadoHabitacion[0] 
                if(i >= 0 and i < preferencial):  #Se asigna la zona de la habitacion
                    self.habitacionesH[i][j] = Habitacion(estadoHab, numHabitacion, self.zonasHotel[0], 0, precioBasico, self.numeroMaximoHuespedes)   #esta parte del codigo hace que se cree una habitacion con los datos que se le pasan al constructor de la clase habitacion 
                elif(i >= preferencial and i < deLujo):  
                    self.habitacionesH[i][j] = Habitacion(estadoHab, numHabitacion, self.zonasHotel[1], 0, precioPreferencial, self.numeroMaximoHuespedes) 
                elif(i >= deLujo) :
                    self.habitacionesH[i][j] = Habitacion(estadoHab, numHabitacion, self.zonasHotel[2], 0, precioDeLujo, self.numeroMaximoHuespedes)

    
    def mostrarHabitaciones(self) -> str: #Metodo para mostrar las habitaciones del hotel
        datosHabitaciones = ""
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                datosHabitaciones += f"{self.habitacionesH[i][j].datosHabitacion()}"
                
            datosHabitaciones += "\n"
        return datosHabitaciones
    
    #Historia de usuario # 2: retornes vector con las habitaciones recomendadas
    def recomendarHabitaciones(self, cantidadHuespedes:int, zonaPreferida: str): #Metodo para recomendar habitaciones
        cantidadH = -1;
        if(cantidadHuespedes>0 and cantidadHuespedes <= self.numeroMaximoHuespedes):
            cantidadH = cantidadHuespedes
        zonaPref = ""
        if(zonaPreferida in self.zonasHotel):
            zonaPref = zonaPreferida

        habitacionesRecomendadas = []
        if(cantidadH != -1 and zonaPref != ""): #Si los datos son validos se recomiendan las habitaciones
            for i in range(self.numPisos):
                for j in range(self.numHabitacionesPorPiso):
                    if(self.habitacionesH[i][j].zona == zonaPref and self.habitacionesH[i][j].estado == self.estadoHabitacion[0]):
                        habitacionesRecomendadas.append(self.habitacionesH[i][j])
        return habitacionesRecomendadas




    #Historia de usuario # 3: funcion (numero habitacion, piso, huespedesPasados[])
        #aqui vas a recorrer las habitaciones y vas a buscar la que dijo el usuario, si esta disponible entonces 
        """
        Vas a guardar esa habitacion en una variable por ejp: habitacionEncontrada
        habitacionEncontrada.huespedes = pasados[]

        osea, en la interfaz debes pedir cuantos huespedes se van a quedar  y vas a hacer un while pidiendo cada huesped, lo agregas a un vector y se lo mandas a esta vaina
        
        """
    def asignarHabitacion(self, numeroHabitacion: int, huespedesPasados: list[Huesped]):
        habitacionEncontrada = None
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                if(self.habitacionesH[i][j].numeroHabitacion == numeroHabitacion and self.habitacionesH[i][j].estado == self.estadoHabitacion[0]):
                    habitacionEncontrada = self.habitacionesH[i][j]
                    break
        if(habitacionEncontrada != None):
            if(len(huespedesPasados) <= self.numeroMaximoHuespedes and len(huespedesPasados) > 0):
                habitacionEncontrada.huespedes = huespedesPasados
                habitacionEncontrada.estado = self.estadoHabitacion[1]
            else:
                print("No se puede asignar la habitacion, la cantidad de huespedes es incorrecta")
        else:
            print("No se encontro la habitacion")



    #Historia de usuario # 4: crea un metodo igual que datosHabitacion que está en la clase habitación
        #Osea, dentro de huesped vas a crear mostrarDatosHuesped y dentro de Habitacion vas a crear mostrarHuespedes
        #osea, mostrarHuespedes va a ser similar a lo que haces en mostrar habitación dentro de Hotel

    def mostrarHuespedes(self, numeroHabitacion:int) -> str:
        datosHuespedes = ""
        habitacionEncontrada = None
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                if(self.habitacionesH[i][j].numeroHabitacion == numeroHabitacion):
                    habitacionEncontrada = self.habitacionesH[i][j]
        if(habitacionEncontrada != None):
            datosHuespedes = habitacionEncontrada.mostrarDatosHuespedes()
        return datosHuespedes


    #Historia de usuario # 5:  

    #Historia de usuario # 7:
        #Debes crear un metodo que reciba el numero de habitacion
        #Debes crear una variable y luego haces un for dentro de habitacionesH y buscas la habitacion que tenga el numero de habitacion que te pasaron
        #Luego vas a hacer un por ejemplo si la variable la llamaste habitaciónEncontrada, haces un habitacionEncontrada.estado = self.estadoHabitacion[2]

