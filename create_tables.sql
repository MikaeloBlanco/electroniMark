CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    rol TEXT NOT NULL,
    sede TEXT NOT NULL
);

create table if not exists carrito(
	Id int primary key AUTOINCREMENT,
    preciototal decimal not null,
    direccion varchar not null,
    fecha varchar not null
);

create table if not exists productos(
	id int primary key AUTOINCREMENT,
    nombre varchar not null,
    precio decimal not null,
    categoria varchar not null
) 