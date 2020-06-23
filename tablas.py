import sqlite3
conexion =sqlite3.connect ("destinos.db")
consulta= conexion.cursor()
sql="""
CREATE TABLE IF NOT EXISTS destinos(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombreCiudad VARCHAR(40) NOT NULL,
    descripcionCiudad VARCHAR(100) NOT NULL,
    precioTour FLOAT NOT NULL,
    ofertaTour BOOLEAN NOT NULL,
    imagenCiudad VARCHAR (100) NOT NULL
)
"""
if(consulta.execute(sql)):print("Tabla creada")
else: print("ERROR DE CREACION")
consulta.close()
conexion.commit()
conexion.close()