from cadenaHolton import *
from hotel import *
from habitacion import *
from huesped import *

def mostrarMenuPrincipal():
    print(f"Bienvenido a Hotel ")
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
    cadenaHoltonInstance = CadenaHolton(input("Ingrese el nombre de la cadena de hoteles: "))

    while True:
        mostrarMenuPrincipal()

        try:
            opcion = int(input("Por favor, elija una opción (1-12): "))

            if opcion == 1:
                while True:
                    tipoHotel = str(input("Ingrese el tipo de hotel (tradicional/tres estrellas/boutique/cinco estrellas): "))
                    tipoHotel = tipoHotel.lower()
                    if tipoHotel not in ("tradicional", "tres estrellas", "boutique", "cinco estrellas"):
                        print("Error: El tipo de hotel ingresado no es válido.")
                        continue

                    print("Número de pisos permitidos: 6, 9, 12, 15")

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

                    if cadenaHoltonInstance.agregarHotel(tipoHotel, numPisos, numHabitacionesPorPiso, ciudad):
                        print("Hotel agregado con éxito.")
                        break  # Sale del bucle si el hotel se agregó con éxito
                    else:
                        print("Error al agregar el hotel. Verifique los datos ingresados.")


            elif opcion == 2:
                cadenaHoltonInstance.mostrarHoteles()
                if len(cadenaHoltonInstance.hoteles) == 0:
                    print("No hay hoteles registrados.")

            elif opcion == 3:
                while True:
                    print("Cantidad de huéspedes: Debe ser menor o igual a 4.")     
                    cantidadHuespedes = int(input("Ingrese la cantidad de huéspedes: "))

                    if cadenaHoltonInstance.hoteles == []:
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
                nuevaHabitacion = True
                while nuevaHabitacion:
                    try:
                        numeroHabitacion = int(input("Ingrese el número de la habitación: "))
                        cantidadHuespedes = int(input("Ingrese la cantidad de huéspedes: "))

                        if cantidadHuespedes > 4 or cantidadHuespedes < 1:
                            print("Error: La cantidad de huéspedes debe estar entre 1 y 4.")
                            continue

                        huespedes = []

                        for i in range(cantidadHuespedes):
                            nombreCompleto = input(f"Ingrese el nombre completo del huésped {i + 1}: ")
                            cedula = int(input(f"Ingrese la cédula del huésped {i + 1}: "))
                            
                            # Validar la edad del huésped
                            fechaNacimiento = input(f"Ingrese la fecha de nacimiento del huésped {i + 1} (Formato YYYY-MM-DD): ")
                            fechaNacimientoParts = fechaNacimiento.split("-")
                            edad = datetime.now().year - int(fechaNacimientoParts[0])

                            if edad < 18:
                                print("Error: El huésped es menor de edad y no puede alojarse solo.")
                                continue

                            print("Sexo: Masculino/Femenino")
                            sexo = input(f"Ingrese el sexo del huésped {i + 1}: ")
                            sexo = sexo.lower()

                            # Validar el sexo
                            if sexo not in ("masculino", "femenino"):
                                print("Error: El sexo ingresado no es válido.")
                                continue

                            fechaEntrada = input(f"Ingrese la fecha de entrada del huésped {i + 1} (Formato YYYY-MM-DD): ")
                            fechaSalida = input(f"Ingrese la fecha de salida del huésped {i + 1} (Formato YYYY-MM-DD): ")

                            huespedes.append(Huesped(nombreCompleto, cedula, fechaNacimiento, sexo, fechaEntrada, fechaSalida))

                        cadenaHoltonInstance.asignarHabitacion(numeroHabitacion, huespedes)

                        while True:
                            print("¿Desea agregar otra habitación?")
                            print("1. Sí")
                            print("2. No")

                            try:
                                opcion = int(input("Por favor, elija una opción (1-2): "))

                                if opcion == 1:
                                    break  # Continuar con la iteración del bucle exterior para agregar otra habitación
                                elif opcion == 2:
                                    nuevaHabitacion = False  # Salir del bucle exterior
                                    break
                                else:
                                    print("Opción no válida. Por favor, elija una opción válida.")
                                    continue

                            except ValueError:
                                print("Error: Por favor, ingrese un número válido.")
                                continue

                    except ValueError:
                        print("Error: Por favor, ingrese un número válido.")
            elif opcion == 5:
                numeroHabitacion = int(input("Ingrese el número de la habitación: "))
                print(f"Huéspedes de la habitación {numeroHabitacion}:")
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