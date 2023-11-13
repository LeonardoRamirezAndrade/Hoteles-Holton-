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
    print("7. Inhabilitar Habitación")
    print("8. Mostrar Informe")
    print("9. Mostrar Zona con Mayor Afluencia")
    print("10. Mostrar Porcentaje de Hombres y Mujeres")
    print("11. Salir")


def main():
    cadenaHoltonInstance = CadenaHolton(input("Ingrese el nombre de la cadena de hoteles: "))

    
    cadenaHoltonInstance.agregarHotel("tradicional", 6, 6, "Bogotá") #Estos son ejemplos ya construidos para que no se tenga que ingresar todo de nuevo y ver que todo funciona
    cadenaHoltonInstance.agregarHotel("tres estrellas", 9, 9, "Medellín")
    cadenaHoltonInstance.agregarHotel("boutique", 12, 12, "Cali")
    cadenaHoltonInstance.agregarHotel("cinco estrellas", 15, 15, "Cartagena")
    cadenaHoltonInstance.agregarHotel("tradicional", 6, 5, "Barranquilla")
    cadenaHoltonInstance.agregarHotel("tres estrellas", 15, 12, "Manizales")
    cadenaHoltonInstance.agregarHotel("boutique", 6, 6, "Pereira")
    cadenaHoltonInstance.agregarHotel("cinco estrellas", 15, 6, "Santa Marta")

    huesped1 = []
    huesped2 = []
    huesped3 = []
    huesped4 = []
    huesped5 = []
    huesped6 = []
    huesped7 = []
    huesped8 = []
    huesped9 = []
    huesped10 = []

    huesped1.append(Huesped("Juan Pérez", 1000001, "1985-03-15", "masculino", "2023-11-01", "2023-11-06"))
    huesped2.append(Huesped("María González", 1000002, "1990-07-22", "femenino", "2023-11-01", "2023-11-11"))
    huesped3.append(Huesped("Carlos Rodríguez", 1000003, "1982-11-10", "masculino", "2023-11-01", "2023-11-16"))
    huesped4.append(Huesped("Ana López", 1000004, "1978-05-03", "femenino", "2023-11-01", "2023-11-21"))
    huesped5.append(Huesped("Luisa Mendoza", 1000005, "1988-09-18", "femenino", "2023-11-01", "2023-11-26"))
    huesped6.append(Huesped("Javier Gómez", 1000006, "1975-12-07", "masculino", "2023-11-01", "2023-12-01"))
    huesped7.append(Huesped("Sofía Ramírez", 1000007, "1983-04-25", "femenino", "2023-11-01", "2023-12-06")) 
    huesped8.append(Huesped("Pedro Herrera", 1000008, "1989-08-12", "masculino", "2023-11-01", "2023-12-11"))
    huesped9.append(Huesped("Laura Torres", 1000009, "1980-01-30", "femenino", "2023-11-01", "2023-12-16"))
    huesped10.append(Huesped("Gabriel Castro", 1000010, "1987-06-14", "masculino", "2023-11-01", "2023-12-21"))

    cadenaHoltonInstance.asignarHabitacion(101, huesped1, cadenaHoltonInstance.hoteles[0]) #la razon por la que se coloca cero es porque en la lista de hoteles se empieza a contar desde 0
    cadenaHoltonInstance.asignarHabitacion(102, huesped2, cadenaHoltonInstance.hoteles[0])
    cadenaHoltonInstance.asignarHabitacion(203, huesped3, cadenaHoltonInstance.hoteles[1])
    cadenaHoltonInstance.asignarHabitacion(204, huesped4, cadenaHoltonInstance.hoteles[1])
    cadenaHoltonInstance.asignarHabitacion(505, huesped5, cadenaHoltonInstance.hoteles[2])
    cadenaHoltonInstance.asignarHabitacion(506, huesped6, cadenaHoltonInstance.hoteles[3])
    cadenaHoltonInstance.asignarHabitacion(402, huesped7, cadenaHoltonInstance.hoteles[3]) 
    cadenaHoltonInstance.asignarHabitacion(101, huesped8, cadenaHoltonInstance.hoteles[4])
    cadenaHoltonInstance.asignarHabitacion(101, huesped9, cadenaHoltonInstance.hoteles[5])
    cadenaHoltonInstance.asignarHabitacion(302, huesped10, cadenaHoltonInstance.hoteles[7])

    while True:
        mostrarMenuPrincipal()

        try:
            opcion = int(input("Por favor, elija una opción (1-11): "))

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

            elif opcion == 2:
                
                if len(cadenaHoltonInstance.hoteles) == 0:
                    print("No hay hoteles registrados.")
                else:
                    cadenaHoltonInstance.mostrarHoteles() #Se encuentra en cadenaHolton.py

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
                        print("\nSeleccione el hotel de donde quiere ver recomendaciones:\n")                        
                        cadenaHoltonInstance.mostrarHotelesSel()
                        print('Escriba "todos" si quiere ver recomendaciones de todos los hoteles')
                        hotelElegido = input("\nSeleccione una opcion: ")

                        if hotelElegido!="todos":
                            hotelElegido = int(hotelElegido)
                            
                            hotel_seleccionado = cadenaHoltonInstance.hoteles[hotelElegido-1]  # Se resta 1 porque la lista de hoteles empieza en 0 y el usuario ingresa un número que empieza en 1
                            print("----------------------------------------------------------------------------------------------")
                            print(f"Nombre del hotel: {hotel_seleccionado.nombre}, Ciudad: {hotel_seleccionado.ciudad}, Tipo de hotel: {hotel_seleccionado.tipoDeHotel}")
                            habitacionesRecomendadas = hotel_seleccionado.recomendarHabitaciones(cantidadHuespedes, zonaPreferida)
                            print("Habitaciones recomendadas:")
                            for habitacion in habitacionesRecomendadas:
                                print(habitacion.datosHabitacion())
                        else:
                            for hotel in cadenaHoltonInstance.hoteles:
                                print("----------------------------------------------------------------------------------------------")
                                print(f"Nombre del hotel: {hotel.nombre}, Ciudad: {hotel.ciudad}, Tipo de hotel: {hotel.tipoDeHotel}")
                                habitacionesRecomendadas = hotel.recomendarHabitaciones(cantidadHuespedes, zonaPreferida)
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
                        print("\nSeleccione el hotel de donde quiere asignar una habitación\n")
                        cadenaHoltonInstance.mostrarHotelesSel()
                        hotelElegidoPosicion = int(input("\nSeleccione una opcion: "))
                        
                        hotelE = cadenaHoltonInstance.hoteles[hotelElegidoPosicion-1]

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
                        
                        cadenaHoltonInstance.asignarHabitacion(numeroHabitacion, huespedes, hotelE )

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
            elif opcion == 5: #historia de usuario 4
                print("\nSeleccione el hotel de donde quiere ver información de un usuario\n")
                cadenaHoltonInstance.mostrarHotelesSel()
                hotelElegidoPosicion = int(input("\nSeleccione una opcion: "))

                numeroHabitacion = int(input("Ingrese el número de la habitación: "))
                print(f"Huéspedes de la habitación {numeroHabitacion}:")
                print(cadenaHoltonInstance.mostrarHuespedesHabitacion(numeroHabitacion, hotelElegidoPosicion-1))                

            elif opcion == 6:
                print("\nSeleccione el hotel de donde quiere ver información de un usuario\n")
                cadenaHoltonInstance.mostrarHotelesSel()
                hotelElegidoPosicionA = int(input("\nSeleccione una opcion: "))
                numeroHabitacion = int(input("Ingrese el número de la habitación: "))
                print(f"Monto a pagar por la habitación {numeroHabitacion}: ${cadenaHoltonInstance.hoteles[hotelElegidoPosicionA-1].montoAPagar(numeroHabitacion)}")

            elif opcion == 7:
                print("\nSeleccione el hotel de donde quiere inhabilitar una habitación\n")
                cadenaHoltonInstance.mostrarHotelesSel()
                hotelElegidoPosicion = int(input("\nSeleccione una opcion: "))
                
                numeroHabitacion = int(input("Ingrese el número de la habitación: "))
                if cadenaHoltonInstance.hoteles[hotelElegidoPosicion-1].inhabilitarHabitacion(numeroHabitacion):
                    print("Habitación inhabilitada con éxito.")
                else:
                    print("Error al inhabilitar la habitación. Verifique los datos ingresados.")

            elif opcion == 8:
                if cadenaHoltonInstance.hoteles == []:
                    print("No hay hoteles registrados.")
                    continue

                cadenaHoltonInstance.mostrarInforme()

            elif opcion == 9:
                if cadenaHoltonInstance.hoteles == []:
                    print("No hay hoteles registrados.")
                    continue
                print("\nSeleccione el hotel de donde quiere ver información\n")
                cadenaHoltonInstance.mostrarHotelesSel()
                hotelElegidoPosicion = int(input("\nSeleccione una opcion: "))
                hotel = cadenaHoltonInstance.hoteles[hotelElegidoPosicion-1]
                print(f"Nombre del hotel: {hotel.nombre}, Ciudad: {hotel.ciudad}, Tipo de hotel: {hotel.tipoDeHotel}")
                print(f"Zona con mayor afluencia: {hotel.mostrarZonaMayorAfluencia()}")


            elif opcion == 10:
                if cadenaHoltonInstance.hoteles == []:
                    print("No hay hoteles registrados.")
                    continue
                
                cadenaHoltonInstance.mostrarHotelesSel()
                hotelElegidoPosicion = int(input("\nSeleccione una opcion: "))
                hotel = cadenaHoltonInstance.hoteles[hotelElegidoPosicion-1]
                print(f"Nombre del hotel: {hotel.nombre}, Ciudad: {hotel.ciudad}, Tipo de hotel: {hotel.tipoDeHotel}")
                print(f"Porcentaje de hombres: {hotel.mostrarPorcentajeHombresYMujeres()[0]}%")
                print(f"Porcentaje de mujeres: {hotel.mostrarPorcentajeHombresYMujeres()[1]}%")

            elif opcion == 11:
                print("Gracias por usar la aplicación. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, elija una opción válida.")

        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()