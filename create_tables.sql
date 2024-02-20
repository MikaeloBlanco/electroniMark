create table if not exists carrito(
	Id int primary key AUTOINCREMENT,
    IdProducto int not null,
    preciototal decimal not null,
    dirección varchar not null,
    fecha varchar not null
) 