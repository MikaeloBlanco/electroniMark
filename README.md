Antonio:
------------------------------------------------------------------------------------------------------------------------------

Mi tabla es la de empleados.

Los campos que hay que añadir en la tabla son el nombre del empleado, su rol y su sede. El id se añade solo es autoincremental.

Los endpoints que tengo son:

/empladosLista

Muestra una lista de todos los empleados (solicitud GET)


/agregarEmpleado

Añade empleados (solicitud POST)


/editarEmpleado/(id del empleado)

Edita un empleado por un id asociado (solicitud PUT)


/borrarEmpleado/(id del empleado)

Borra los datos de un empleado por un id asociado (solicitud DELETE)


/empleado/(id del empleado)

Te da la información de un empleado en específico pasandole el id (solicitud GET)


/empleadosPorRol/(el rol)

Te da una lista de empleados que tenga el rol que estas buscando para filtrarlos (solicitud GET)


/empleadosPorSed/(la sede)

Te da una lista de empleados que esten en la sede que estas buscando para filtrarlo igual que el de Rol (solicitud GET)


Dejo la URL para hacer las llamadas: http://127.0.0.1:5000(/endpointDeEjemplo)

Y el formato de JSON para probarlo con un empleado de ejemplo:

{
    "nombre": "Solidus Snake",
    "rol": "Expresidente",
    "sede": "Big Shell"
}

------------------------------------------------------------------------------------------------------------------------------

Miguel:

------------------------------------------------------------------------------------------------------------------------------

Mi tabla es la de carrito

Los campos de la tabla carriot son el id, que se autoincrementa,
el idproducto que de momento no interconectado con otras tablas
así que va por su cuenta, preciototal, que se calcula sumando los precios de
los productos, dirección, que es la dirección física de la persona,
y fecha de cuando se realizó.

Los endpoints mios son:

/carritoLista

Muestra una lista de los carritos creados ( solicitud GET )

/agregarCarrito

agrega un carrito nuevo a la Base de Datos ( solicitud POST )

/editarCarrito/ ( usando id del carrito )

Edita el carro selecciona por el id solicitado ( Solicitud de tipo PUT )

/borrarCarrito/ ( usando id del carrito )

Borra la iteración del carrito usando la id ( Solicitud de tipo DELETE )

/carrito/ ( usando id del carrito )

Recoge la información especifica de un carrito por su id ( solicitud de tipo GET )

/carritoPorFecha/ ( usando la fecha del carrito )

Recoge una lista de carritos que compartan la misma fecha de realización ( solicitud de tipo GET )

/carritoPorDirección/ ( usando la dirección del carrito )

Recoge una lista de carritos que se hayan realizado a la mísma direccion solicitada ( solicitud de tipo GET )


{
    "preciototal": 120.99,
    "direccion": "Shadow Mosses, Alaska",
    "fecha": "20/02/2024"
}

------------------------------------------------------------------------------------------------------------------------------

Oscar:

------------------------------------------------------------------------------------------------------------------------------

Mi tabla es la de productos


{
    "nombre": "Tarjeta Gráfica RTX 4070ti Aorus",
    "precio": 578.99,
    "categoria": "Tarjetas graficas"
}

------------------------------------------------------------------------------------------------------------------------------