# Hoteles Holton

## Descripción del Proyecto

Hoteles Holton es un sistema de gestión hotelera que permite la creación, administración y consulta de información relacionada con hoteles, habitaciones y huéspedes.

## Clases Principales

### 1. CadenaHolton

La clase `CadenaHolton` representa la cadena de hoteles y ofrece funciones clave como:

- `agregarHotel(tipoHotel, numPisos, numHabitacionesPorPiso, ciudad)`: Agrega un nuevo hotel a la cadena.
- `mostrarHoteles()`: Muestra información detallada de todos los hoteles registrados.
- `asignarHabitacion(numeroHabitacion, huespedes, hotel)`: Asigna una habitación a huéspedes en un hotel específico.
- `mostrarInforme()`: Muestra un informe general con ganancias totales, número de huéspedes y habitaciones ocupadas.
- `mostrarZonaMayorAfluencia()`: Indica la zona con mayor afluencia en los hoteles de la cadena.
- `mostrarPorcentajeHombresYMujeres()`: Calcula y muestra el porcentaje de hombres y mujeres entre los huéspedes.

### 2. Hotel

La clase `Hotel` representa un hotel individual y ofrece funciones como:

- `montoAPagar(numeroHabitacion)`: Calcula el monto a pagar por una habitación.
- `inhabilitarHabitacion(numeroHabitacion)`: Inhabilita una habitación específica.
- `mostrarPorcentajeHombresYMujeres()`: Calcula y muestra el porcentaje de hombres y mujeres entre los huéspedes del hotel.

### 3. Habitacion

La clase `Habitacion` representa una habitación en un hotel con información sobre el estado, capacidad y zona.

### 4. Huesped

La clase `Huesped` representa a un huésped con datos como nombre, cédula, fecha de nacimiento, sexo, y fechas de entrada y salida.

## Funcionalidades Principales

- **Registro de Hoteles**: Agrega nuevos hoteles con diferentes tipos y configuraciones.
- **Asignación de Habitaciones**: Permite asignar habitaciones considerando el tipo de hotel, disponibilidad y preferencia de zona.
- **Cálculo de Monto a Pagar**: Calcula el monto total a pagar por una habitación según la duración de la estadía y el número de huéspedes.
- **Inhabilitación de Habitaciones**: Marca habitaciones como no disponibles para su uso.
- **Informe General**: Proporciona un informe con ganancias totales, número de huéspedes y habitaciones ocupadas.
- **Recomendación de Habitaciones**: Recomienda habitaciones disponibles según la cantidad de huéspedes y preferencia de zona.
- **Consulta de Información**: Permite ver información detallada de hoteles, huéspedes y habitaciones.

## Instrucciones de Uso

1. **Inicio del Programa**: Al ejecutar el programa, se solicitará el nombre de la cadena de hoteles.
2. **Menú Principal**: Se presentará un menú con diversas opciones, como agregar hoteles, mostrar información, asignar habitaciones, entre otros.
3. **Interacción con el Usuario**: El programa guiará al usuario para ingresar datos relevantes y realizar acciones específicas.
4. **Visualización de Resultados**: Se mostrarán informes, recomendaciones y detalles de la cadena de hoteles según las acciones realizadas.
5. **Salir del Programa**: El usuario puede seleccionar la opción para salir del programa cuando lo desee.

## Requisitos y Consideraciones

- Se deben seguir las indicaciones y restricciones proporcionadas por el programa al ingresar datos.
- Se recomienda ingresar información válida y coherente para obtener resultados precisos.
- Las fechas deben ingresarse en formato YYYY-MM-DD.
- Al realizar acciones que afectan la disponibilidad de habitaciones, se actualizará la información en tiempo real.

## Colaboradores principales del Codigo

- Leonardo Ramirez Andrade & Jonathan Vizcaino Macias
