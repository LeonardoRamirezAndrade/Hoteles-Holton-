# Hoteles Holton

En este proyecto, hemos creado 4 clases esenciales para gestionar un sistema de hoteles. Estas clases son: `CadenaHolton`, `Huésped`, `Habitación` y `Hotel`. A través de estas clases, hemos implementado varias bibliotecas y funciones para su funcionamiento.

## Clase Cadena Holton

La clase `CadenaHolton` almacena datos importantes relacionados con la cadena de hoteles Holton. Estos datos incluyen:

- Cantidad de habitaciones disponibles.
- Capacidad de cada hotel.
- Listado de hoteles disponibles.
- Tipos de hoteles dentro de la cadena.
- Precio por noche por persona en cada tipo de hotel.

### Método Agregar Hotel

El método `agregarHotel` se utiliza para agregar un nuevo hotel a la cadena Holton. Requiere cuatro parámetros:

- Tipo de hotel.
- Número de pisos.
- Número de habitaciones por piso.
- Ciudad.

### Método Mostrar Hoteles

El método `mostrarHoteles` se encarga de mostrar todos los hoteles almacenados en la cadena. Para cada hotel, muestra los siguientes datos:

- Ciudad.
- Nombre.
- Tipo de hotel.
- Número de pisos.
- Número de habitaciones por piso.
- Precio base por noche por persona.
- Zonas del hotel.
- Información detallada de las habitaciones.

Este método realiza una iteración de los datos almacenados en `self.hoteles` y muestra la información de cada hotel.
