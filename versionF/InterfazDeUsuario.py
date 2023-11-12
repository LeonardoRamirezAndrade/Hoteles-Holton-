#IntefazDeUsuario.py

from cadenaHolton import *
from hotel import *
from habitacion import *
from huesped import *

# Crear una instancia de CadenaHolton fuera de la función main
cadenaHoltonInstance = CadenaHolton(input("Ingrese el nombre de la cadena de hoteles: "))

cantidadDeHotelesIgualCero = len(cadenaHoltonInstance.hoteles) == 0

def mostrarMenuPrincipal():
    print(f"Bienvenido a {cadenaHoltonInstance.nombre} ")
    print("1. Agregar Hotel")
    print("2. Mostrar Hoteles")
    print("3. Recomendar Habitaciones")
    print("4. Asignar Habitación")
    print("5. Mostrar Huéspedes de una Habitación")
    print("6. Calcular Monto a Pagar")
    print("7. Desocupar Habitación")
    print("8. Inhabilitar Habitación")
    print("9. Mostrar Informe")
    print("10. Mostrar Zona con Mayor Afluencia")
    print("11. Mostrar Porcentaje de Hombres y Mujeres")
    print("12. Salir")

def main():

    while True:
        mostrarMenuPrincipal()

        try:
            opcion = int(input(" Por favor, elija una opción (1-12): "))

            if opcion == 1:
                while True:
                    tipoHotel = str(input("Ingrese el tipo de hotel (tradicional/tres estrellas/boutique/cinco estrellas): "))
                    tipoHotel = tipoHotel.lower()
                    if tipoHotel not in ("tradicional", "tres estrellas", "boutique", "cinco estrellas"):
                        print("Error: El tipo de hotel ingresado no es válido.")
                        continue

                    notificacion = print("Número de pisos permitidos: 6, 9, 12, 15")

                    numPisos = int(input("Ingrese el número de pisos: "))
                    if numPisos not in (6, 9, 12, 15):
                        print("Error: El número de pisos ingresado no es válido.")
                        continue

                    print("Número de habitaciones por piso: Debe ser menor o igual al número de pisos.")

                    numHabitacionesPorPiso = int(input("Ingrese el número de habitaciones por piso: "))
                    
                    ciudad = input("Ingrese la ciudad: ")

                    if cadenaHoltonInstance.agregarHotel(tipoHotel, numPisos, numHabitacionesPorPiso, ciudad):
                        print("Hotel agregado con éxito.")
                        break  # Sale del bucle si el hotel se agregó con éxito
                    else:
                        print("Error al agregar el hotel. Verifique los datos ingresados.")

            elif opcion == 2:
                cadenaHoltonInstance.mostrarHoteles()
                if not cadenaHoltonInstance.hoteles:
                    print("No hay hoteles registrados.")
                    continue

            elif opcion == 3:
                notificacion = print("Cantidad de huéspedes: Debe ser menor o igual a 4.")
                cantidadHuespedes = int(input("Ingrese la cantidad de huéspedes: "))
                if cantidadDeHotelesIgualCero:
                    print("No hay hoteles registrados.")
                    continue
                if cantidadHuespedes > 4:
                    print("Error: La cantidad de huéspedes no puede ser mayor a 4.")
                    continue
                elif cantidadHuespedes < 1:
                    print("Error: La cantidad de huéspedes no puede ser menor a 1.")
                    continue

                zonaPreferida = input("Ingrese la zona preferida (basica/preferencial/de lujo): ")
                zonaPreferida = zonaPreferida.lower()
                if zonaPreferida not in ("basica", "preferencial", "de lujo"):
                    print("Error: La zona preferida ingresada no es válida.")
                    continue

                if cadenaHoltonInstance.hoteles:
                    hotel_seleccionado = cadenaHoltonInstance.hoteles[0]  # Aquí deberías seleccionar el hotel adecuado según tus necesidades
                    habitacionesRecomendadas = hotel_seleccionado.recomendarHabitaciones(cantidadHuespedes, zonaPreferida)
                    print("Habitaciones recomendadas:")
                    for habitacion in habitacionesRecomendadas:
                        print(habitacion.datosHabitacion())
                    break
                else:
                    print("No hay hoteles registrados.")
                    continue
            
            elif opcion == 4:
                while True:
                    numeroHabitacion = int(input("Ingrese el número de la habitación: "))

                    cantidadHuespedes = int(input("Ingrese la cantidad de huéspedes: "))

                    if cantidadHuespedes > 4:
                        print("Error: La cantidad de huéspedes no puede ser mayor a 4.")
                        continue

                    elif cantidadHuespedes < 1:
                        print("Error: La cantidad de huéspedes no puede ser menor a 1.")
                        continue

                    huespedes = []
                    for i in range(cantidadHuespedes):
                        nombre = input("Ingrese el nombre del huésped: ")
                        identificacion = int(input("Ingrese la identificación del huésped: "))
                        fechaNacimiento = input("Ingrese la fecha de nacimiento del huésped (AAAA-MM-DD): ")
                        genero = input("Ingrese el género del huésped (masculino/femenino): ")
                        genero = genero.lower()
                        if genero not in ("masculino", "femenino"):
                            print("Error: El género ingresado no es válido.")
                            continue

                        fechaLlegada = input("Ingrese la fecha de llegada del huésped (AAAA-MM-DD): ") #Estos datos se pueden ingresar de la siguiente manera ejemplo: 2021-05-20
                        fechaSalida = input("Ingrese la fecha de salida del huésped (AAAA-MM-DD): ")
                        huesped = Huesped(nombre, identificacion, fechaNacimiento, genero, fechaLlegada, fechaSalida)
                        huespedes.append(huesped)
                    
                    if cadenaHoltonInstance.hoteles:
                        hotelSeleccionado = cadenaHoltonInstance.hoteles[0]  # Ajusta esto según tus necesidades
                        if hotelSeleccionado.asignarHabitacion(numeroHabitacion, huespedes):
                            print("Habitación asignada con éxito.")
                            break
                        else:
                            print("Error al asignar la habitación. Verifique los datos ingresados.")
                    else:
                        print("No hay hoteles registrados.")

            
            elif opcion == 5:
                numeroHabitacion = int(input("Ingrese el número de la habitación: "))
                print(cadenaHoltonInstance.mostrarHuespedesHabitacion(numeroHabitacion))

            elif opcion == 6:
                numeroHabitacion = int(input("Ingrese el número de la habitación: "))
                print(f"Monto a pagar por la habitación {numeroHabitacion}: ${cadenaHoltonInstance.montoAPagar(numeroHabitacion)}")
            
            elif opcion == 7:
                numeroHabitacion = int(input("Ingrese el número de la habitación: "))
                if cadenaHoltonInstance.desocuparHabitacion(numeroHabitacion):
                    print("Habitación desocupada con éxito.")
                else:
                    print("Error al desocupar la habitación. Verifique los datos ingresados.")
            elif opcion == 8:
                numeroHabitacion = int(input("Ingrese el número de la habitación: "))
                if cadenaHoltonInstance.inhabilitarHabitacion(numeroHabitacion):
                    print("Habitación inhabilitada con éxito.")
                else:
                    print("Error al inhabilitar la habitación. Verifique los datos ingresados.")
            
            elif opcion == 9:
                if cadenaHoltonInstance.hoteles == []:
                    print("No hay hoteles registrados.")
                    continue
                cadenaHoltonInstance.mostrarInforme()
            
            elif opcion == 10:
                if cadenaHoltonInstance.hoteles == []:
                    print("No hay hoteles registrados.")
                    continue
                print(f"Zona con mayor afluencia: {cadenaHoltonInstance.mostrarZonaMayorAfluencia()}")
                

            elif opcion == 11:
                if cadenaHoltonInstance.hoteles == []:
                    print("No hay hoteles registrados.")
                    continue
                elif cadenaHoltonInstance.mostrarPorcentajeHombres() == -1:
                    print("No hay huéspedes registrados.")
                    continue
                elif cadenaHoltonInstance.mostrarPorcentajeMujeres() == -1:
                    print("No hay huéspedes registrados.")
                    continue
                print(f"Porcentaje de hombres: {cadenaHoltonInstance.mostrarPorcentajeHombres()}%")
                print(f"Porcentaje de mujeres: {cadenaHoltonInstance.mostrarPorcentajeMujeres()}%")

            elif opcion == 12:
                print("Gracias por usar la aplicación. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, elija una opción válida.")

        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
    
