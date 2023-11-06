from Huesped import Huesped
from Hotel import Hotel

class Cadena:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.hoteles = []
        self.tiposDeHotel = ('Tradicional', 'Tres Estrellas', 'Boutique', 'Cinco estrellas')
        self.zonasHotel = ('Basica', 'Preferencial', 'De lujo')
        self.numerosDePisos = (6, 9, 12, 15)
        

    def AgregarHotel(self, hotel:Hotel)-> bool:
        hotelAgregado = False
        if (hotel.habitacionesPorPiso <= hotel.pisos and
            hotel.pisos in self.numerosDePisos and
            hotel.tipo in self.tiposDeHotel):
            self.hoteles.append(hotel)
            hotelAgregado = True
        return hotelAgregado

    def CalcularIngresosTotalesObtenidos(self)-> bool:
        totalIngresos = 0
        if len(self.hoteles) > 0:
            for hotel in self.hoteles:
                totalIngresos += hotel.CalcularIngresosObtenidos()
        return totalIngresos

    def CalcularTotalDeHuespedesAtendidos(self)-> int:
        pass

    def CalcularCantidadTotalDeHabitacionesOcupadas(self)->int:
        pass
    
    def CalcularPorcentajeDeHombres_Y_MujersQueSeHanAtendido(self)-> list:
        pass
    

