create table if not exists productos(
	id int primary key AUTOINCREMENT,
    nombre varchar not null,
    precio decimal not null,
    categoria varchar not null
) 