import numpy as np
import csv
import os

<<<<<<< HEAD

=======
>>>>>>> leoMasJona
def identificarError(opciones, mensajeParaGerente):
    while True:
        try:
            opción = int(input(mensajeParaGerente))
            if opción in opciones:
                return opción
            else:
                print("Opción no válida. Por favor, elija una opción válida.")
        except ValueError:
            print("Opción no válida. Por favor, elija una opción válida.")

def seleccionarCantidadDeHabitaciones(pisos):
    cantidad_de_habitaciones = {}
    for i in range(1, pisos * 6 + 1):
        cantidad_de_habitaciones[i] = f"{i} habitaciones por piso"
    return cantidad_de_habitaciones

def guardarDatosEnCSV(ciudad, tipo_hotel, cantidad_pisos, cantidad_habitaciones):
    with open('DatosDelHotelGerente.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ciudad, tipo_hotel, cantidad_pisos, cantidad_habitaciones])

def borrarCSV():
    if os.path.exists('DatosDelHotelGerente.csv'):
        os.remove('DatosDelHotelGerente.csv')
        print("El archivo CSV ha sido borrado.")
    else:
        print("El archivo CSV no existe, no se puede borrar.")

def main():
    print("Bienvenido señor gerente a los Hoteles Holtons en Colombia \n")

    print("¿Qué quiere hacer hoy?")
    print("1: Continuar con los hoteles")
    print("2: Borrar todos los datos del CSV")

    primeraElección = identificarError([1, 2], "Ingrese su opción: ")
    if primeraElección == 2:
        borrarCSV()
        return

    print("Podemos comenzar con la expansión en las siguientes ciudades:")
    
    print("\n", ciudades, "\n")

    ubicación = identificarError(ciudades.keys(), "Ingrese la ubicación del hotel: ")
    print(f"Usted ha seleccionado la ciudad de: {ciudades[ubicación]}")
    
    print("Podemos comenzar con la selección de los tipos de hoteles que desea expandir: \n",)

    print("\n", TipoDeHotel, "\n")

    tipoHotel = identificarError(TipoDeHotel.keys(), "Ingrese el tipo de hotel: ")
    print(f"\nUsted ha escogido el tipo de hotel: {TipoDeHotel[tipoHotel]}, ubicado en {ciudades[ubicación]}")

    print("Podemos comenzar con la cantidad de pisos que tendrá el hotel:")
    
    print("\n", CantidadDePisos, "\n")

    CantidadPiso = identificarError(CantidadDePisos.keys(), "Ingrese la cantidad de pisos: ")
    print(f"\nUsted ha escogido esta cantidad de pisos: {CantidadDePisos[CantidadPiso]}, ubicado en {ciudades[ubicación]}")

    pisos = CantidadPiso

    cantidadHabitaciones = seleccionarCantidadDeHabitaciones(pisos)
    print("\nSeleccione la cantidad de habitaciones por piso:")
    print(cantidadHabitaciones)

    cantidadHabitacionesSeleccionada = identificarError(cantidadHabitaciones.keys(), "Ingrese la cantidad de habitaciones por piso: ")
    cantidadHabitacionesTexto = cantidadHabitaciones[cantidadHabitacionesSeleccionada]

    guardarDatosEnCSV(ciudades[ubicación], TipoDeHotel[tipoHotel], CantidadDePisos[CantidadPiso], cantidadHabitacionesTexto)


if __name__ == "__main__":
    main()
    ciudades = {
        1: "Bogota",
        2: "Santa Marta",
        3: "Barranquilla",
        4: "Medellin",
        5: "Cali",
        6: "Bucaramanga",
        7: "Manizales"
    }
    TipoDeHotel = {
        1: "Tradicional",
        2: "Tres estrellas",
        3: "Boutique",
        4: "Cinco estrellas"
    }
    CantidadDePisos = {
        1: "6 pisos",
        2: "9 pisos",
        3: "12 pisos",
        4: "15 pisos"
<<<<<<< HEAD
    } 
=======
    } 
>>>>>>> leoMasJona
