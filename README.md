Antonio:

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


