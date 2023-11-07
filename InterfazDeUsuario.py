import numpy as np
import csv
from InterfazDelGerente import identificarError, ciudades, TipoDeHotel, CantidadDePisos, main

def leerDatosDesdeCSV(archivoCSV):
    datos = []
    with open(archivoCSV, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            datos.append(row)
    return datos

archivoCSV = 'DatosDelHotelGerente.csv'
datosHotel = leerDatosDesdeCSV(archivoCSV)

print("Muy buenos días", "\n ¿Cuál es su sexo ?")
print("1: Masculino")
print("2: Femenino")

sexo = identificarError([1, 2], "(Usando números) Escriba su genero: ")
if sexo == 1:
    sexo = "Masculino"
    identificadorDeGenero = "Señor"
elif sexo == 2:
    sexo = "Femenino"
    identificadorDeGenero = "Dama"

print(f"Muy buenos días {identificadorDeGenero}, les muestro los hoteles disponibles: ")

# for i, hotel in enumerate(datosHotel, start=1):
#    print(f"{i}: {ciudades[ubicación]}, {TipoDeHotel[tipoHotel]}, {CantidadDePisos[CantidadPiso]}, {cantidadHabitacionesTexto}")

# Solicitar al usuario que seleccione un hotel
# while True:
#    try:
#        seleccion = int(input("Seleccione un hotel (ingrese el número correspondiente): "))
#        if 1 <= seleccion <= len(datosHotel):
#            hotel_seleccionado = datosHotel[seleccion - 1]
#            print(f"Ha seleccionado el hotel: {ciudades[ubicación]}, {TipoDeHotel[tipoHotel]}, {CantidadDePisos[CantidadPiso]}, {cantidadHabitacionesTexto}")
#            break
#        else:
#            print("Opción no válida. Ingrese un número válido.")
#    except ValueError:
#        print("Opción no válida. Ingrese un número válido.")

# Convertir la lista de listas en una matriz NumPy
matrizDatos = np.array(datosHotel)

if __name__ == "__main__":
    identificadorDeGenero = None
    main()
