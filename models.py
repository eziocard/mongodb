## este archivo contiene toda la lógica de conexión a la base de datos
from conexion import *

def InsertDatos(p,seleccion):
    if seleccion == 1:
        db = client.Universidad
        collection = db['Estudiantes']
        collection.insert_one(p)
    if seleccion == 2:
        db = client.Universidad
        collection = db['Curso']
        collection.insert_one(p)


## función para filtrar persona por rut
'''
def FilterRut(search):
    # conexión a la base de datos
    db = client.ejemplo1
    collection = db['Person']
    # find realiza una búsqueda en la colección usando el criterio search
    # los resultados los convierte en una lista
    show_data_count = len(list(collection.find(search)))
    # agregamos una condición para verificar si existen resultados
    if show_data_count > 0:
        show_data = collection.find(search)
        # iteramos sobre los resultados para imprimir cada documento
        for i in show_data:
            print(i)
    else:
        print('No existe el rut ingresado')'''
