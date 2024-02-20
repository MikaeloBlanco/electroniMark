create table if not exists carrito(
	Id int primary key AUTOINCREMENT,
    preciototal decimal not null,
    direccion varchar not null,
    fecha varchar not null
) 