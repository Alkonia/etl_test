DB_CONNECT = {
    "drivername": "postgresql",
    "username": "postgres",
    "host": "localhost",
    "port": "5432",
    "database": "etl",
    "password": "juan1234"
}

MODELS = {
    "clientes": "clientes",
    "salas": "salas",
    "multiplex": "multiplex",
    "peliculas": "peliculas",
    "fechas": "fechas",
    "ventas_taquilla": "ventas_taquilla"
}

FILE_MODELS = {
    MODELS["clientes"]: "Anexo 2 - CLIENTES.csv",
    MODELS["salas"]: "Anexo 3- SALAS.csv",
    MODELS["multiplex"]: "Anexo 4 - MULTIPLEX.csv",
    MODELS["peliculas"]: "Anexo 5 - PELICULAS.csv",
    MODELS["fechas"]: "Anexo 6 - FECHAS.csv",
    MODELS["ventas_taquilla"]: "Anexo7 - ventas_taquilla.csv",
}
