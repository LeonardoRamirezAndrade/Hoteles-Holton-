#Hotel.py

import math #Importamos la libreria math para poder usar el metodo ceil que redondea un numero hacia arriba
import numpy as np
from huesped import *
from habitacion import *
from datetime import datetime

class Hotel:

    def __init__(self, ciudad: str,nombre:str, tipoDeHotel: str, numPisos: int, numHabitacionesPorPiso: int, precioBase: float, numeroMaximoHuespedes:int): #Constructor de la clase hotel
        self.ciudad = ciudad
        self.nombre = nombre
        self.tipoDeHotel = tipoDeHotel
        self.numPisos = numPisos
        self.numHabitacionesPorPiso = numHabitacionesPorPiso
        self.habitacionesH = np.full((numPisos, numHabitacionesPorPiso), None) #Se crea una matriz de habitaciones en la cual el none se usa para indicar que la habitacion esta vacia
        self.precioBase = precioBase
        self.zonasHotel = ('basica', 'preferencial', 'de lujo')
        self.estadoHabitacion = ('libre', 'ocupada', 'no habilitada para uso')
        self.numeroMaximoHuespedes = numeroMaximoHuespedes
        self.llenarhabitaciones()
        self.numeroHuespedesAtendidos = 0
        self.ganaciasTotales = 0
        self.habitacionesOcupadas = set() #Se crea un set para guardar las habitaciones ocupadas, un set es un conjunto de datos que no se pueden repetir


    def numHOcupadas(self): #Metodo para calcular el numero de habitaciones ocupadas
        numHabitacionesOcupadas = 0
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                if(self.habitacionesH[i][j].estado == self.estadoHabitacion[1]):
                    numHabitacionesOcupadas += 1
        return numHabitacionesOcupadas

    def llenarhabitaciones(self): #Metodo para llenar las habitaciones del hotel
        preferencial = math.ceil(self.numPisos*(1/3))  #Esto hace que la preferencial ocupe el 33.33% de los pisos
        deLujo = math.ceil(self.numPisos*(2/3))  

        precioBasico = self.precioBase 
        precioPreferencial = precioBasico*0.15 + precioBasico #Esta parte del codigo hace que el precio preferencial se le adicione el 15% del precio base, y al precio de lujo se le adicione el 20% del precio base
        precioDeLujo = precioBasico*0.2 + precioBasico

        for i in range(self.numPisos): 
            for j in range(self.numHabitacionesPorPiso): #Estos dos for los usamos para crear la matriz
                numHabitacion = ((i+1)*100)+(j+1) #Se calcula el numero de habitacion
                estadoHab = self.estadoHabitacion[0] 
                if(i >= 0 and i < preferencial):  #Se asigna la zona de la habitacion en este caso basica
                    self.habitacionesH[i][j] = Habitacion(estadoHab, numHabitacion, self.zonasHotel[0], 0, precioBasico, self.numeroMaximoHuespedes)   #esta parte del codigo hace que se cree una habitacion con los datos que se le pasan al constructor de la clase habitacion 
                elif(i >= preferencial and i < deLujo):  #Se asigna la zona de la habitacion en este caso preferencial
                    self.habitacionesH[i][j] = Habitacion(estadoHab, numHabitacion, self.zonasHotel[1], 0, precioPreferencial, self.numeroMaximoHuespedes) 
                elif(i >= deLujo) : #Se asigna la zona de la habitacion en este caso de lujo
                    self.habitacionesH[i][j] = Habitacion(estadoHab, numHabitacion, self.zonasHotel[2], 0, precioDeLujo, self.numeroMaximoHuespedes)

    
    def mostrarH(self):
        datosHabitaciones = ""
    
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                datosHabitaciones += f"{self.habitacionesH[i][j].datosHabitacion()}\n" 

        return datosHabitaciones
    
     #Se retorna un string con los datos de las habitaciones
         
    
    #Historia de usuario # 2: retornes vector con las habitaciones recomendadas
    #    Como Gerente de 
    #Holtons en Colombia, quiero calcular el monto 
    #que los huéspedes de una habitación deben 
    #pagar al momento de su salida, asegurando que 
    #la cantidad se determine según las reglas y 
    #tarifas de cobro de la empresa

    def recomendarHabitaciones(self, cantidadHuespedes, zonaPreferida):
        habitacionesRecomendadas = []

        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                habitacion = self.habitacionesH[i][j]
                if habitacion.estado == 'libre':
                    if cantidadHuespedes <= 2 or (cantidadHuespedes > 2 and habitacion.zona == zonaPreferida):
                        habitacionesRecomendadas.append(habitacion)

        # Filtrar las habitaciones recomendadas si la zona preferida es "de lujo"
        if zonaPreferida == "de lujo":
            habitacionesRecomendadas = [hab for hab in habitacionesRecomendadas if hab.zona == zonaPreferida]
        elif zonaPreferida == "preferencial":
            habitacionesRecomendadas = [hab for hab in habitacionesRecomendadas if hab.zona == zonaPreferida]
        elif zonaPreferida == "basica":
            habitacionesRecomendadas = [hab for hab in habitacionesRecomendadas if hab.zona == zonaPreferida]
        else:
            habitacionesRecomendadas = []

        return habitacionesRecomendadas
    
    def obtenerZonaHabitacion(self, numeroHabitacion: int) -> str:
    # Obtener la zona de una habitación específica
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                if self.habitacionesH[i][j].numeroHabitacion == numeroHabitacion:
                    return self.habitacionesH[i][j].zona
        return ""



    #Historia de usuario # 5:     Como Gerente de    Holtons en Colombia, quiero calcular el monto     que los huéspedes de una habitación deben     pagar al momento de su salida, asegurando que     la cantidad se determine según las reglas y     tarifas de cobro de la empresa

    def cuantasNoches(self, habitacion: Habitacion) -> int:
        if len(habitacion.huespedes) > 0:
            huesped = habitacion.huespedes[0]

            try:
                fechaEntrada = datetime.strptime(huesped.fechaEntrada, "%Y-%m-%d")
                fechaSalida = datetime.strptime(huesped.fechaSalida, "%Y-%m-%d")
            except ValueError:
                print("Error en el formato de las fechas.")
                return 0

            # Calcula la diferencia en días
            diferencia = fechaSalida - fechaEntrada
            return diferencia.days
        else:
            return 0

    #    Historia de usuario # 6: Como Gerente de     #Holtons en Colombia, quiero que las     #habitaciones de huéspedes que acaban de     #realizar su salida queden disponibles, para así     #poder asignarlas a nuevos huéspedes que     #lleguen a un hotel.

    def montoAPagar(self, numeroHabitacion:int) -> float:
        monto = 0
        habitacionEncontrada = None
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                if(self.habitacionesH[i][j].numeroHabitacion == numeroHabitacion):
                    habitacionEncontrada = self.habitacionesH[i][j]
                    break
        numeroHuespedes = len(habitacionEncontrada.huespedes)
        monto = self.cuantasNoches(habitacionEncontrada) * habitacionEncontrada.precioNoches * numeroHuespedes #Aquí se completa la historia de usuario # 5
        habitacionEncontrada.estado = self.estadoHabitacion[0] #Aquí se completa la historia de usuario # 6
        habitacionEncontrada.huespedes = [] #Aquí se completa la historia de usuario # 6
        self.numeroHuespedesAtendidos += numeroHuespedes
        self.ganaciasTotales += monto
        return monto
       
    
    # Historia de usuario # 7: Como Gerente de 
    #Holtons en Colombia, deseo establecer como no 
    #disponibles aquellas habitaciones que no estén 
    #en condiciones óptimas, para asegurar que no 
    #se asignen a huéspedes

    def inhabilitarHabitacion(self, numeroHabitacion:int):
        habitacionEncontrada = None
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                if(self.habitacionesH[i][j].numeroHabitacion == numeroHabitacion):
                    habitacionEncontrada = self.habitacionesH[i][j]
                    break
        if(habitacionEncontrada != None):
            habitacionEncontrada.estado = self.estadoHabitacion[2]
        else:
            print("No se encontró la habitación")


    #Historia de usuario # 9: Como Gerente     #de Holtons en Colombia, quisiera conocer  #cuál es la zona del hotel con mayor #afluencia y la tasa de ocupación en #determinado momento, para impulsar #estrategias que incrementen la afluencia de #huéspedes en nuestros establecimientos.

    def mostrarZonaMayorAfluencia(self):
        afluenciaBasico = 0
        afluenciaPreferencial = 0
        afluenciaDeLujo = 0
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                if(self.habitacionesH[i][j].estado == self.estadoHabitacion[1]):
                        if(self.habitacionesH[i][j].zona == self.zonasHotel[0]):
                            afluenciaBasico += 1
                        elif (self.habitacionesH[i][j].zona == self.zonasHotel[1]):
                            afluenciaPreferencial += 1
                        elif (self.habitacionesH[i][j].zona == self.zonasHotel[2]):
                            afluenciaDeLujo += 1
            
        if(afluenciaBasico == 0 and afluenciaPreferencial == 0 and afluenciaDeLujo == 0):
            return "Ninguna. No hay habitaciones ocupadas"
        else:
            mayorAfluencia = max(afluenciaBasico, afluenciaPreferencial, afluenciaDeLujo)
            if(mayorAfluencia == afluenciaBasico):
                return self.zonasHotel[0]
            elif(mayorAfluencia == afluenciaPreferencial):
                return self.zonasHotel[1]
            elif(mayorAfluencia == afluenciaDeLujo):
                return self.zonasHotel[2]
            

    #    Historia de usuario # 10: Como 
    #Gerente de Holtons en Colombia, quisiera 
    #conocer el porcentaje histórico de hombres 
    #y mujeres que se han alojado en los hoteles 
    #de nuestra cadena. Esto con el objetivo de 
    #determinar si existe alguna preferencia 
    #según el sexo del huésped.

    def mostrarPorcentajeHombresYMujeres(self):
        porcentajeHombres = 0
        porcentajeMujeres = 0
        totalHombres = 0
        totalMujeres = 0
        for i in range(self.numPisos):
            for j in range(self.numHabitacionesPorPiso):
                if(self.habitacionesH[i][j].estado == self.estadoHabitacion[1]):
                    k = self.habitacionesH[i][j].huespedes[0]
                    if(k.sexo == "masculino"):
                        totalHombres += 1
                    elif(k.sexo == "femenino"):
                        totalMujeres += 1
        if(totalHombres != 0):
            porcentajeHombres = (totalHombres/(totalHombres+totalMujeres))*100
        if(totalMujeres != 0):
            porcentajeMujeres = (totalMujeres/(totalHombres+totalMujeres))*100
        return porcentajeHombres, porcentajeMujeres