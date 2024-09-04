## este archivo contiene toda la lógica de conexión a la base de datos
from IPython.core.display_functions import display

from conexion import *
import pandas as pd
def InsertDatos(p,seleccion):
    if seleccion == 1:
        db = client.Universidad
        collection = db['Estudiantes']
        collection.insert_one(p)
    if seleccion == 2:
        db = client.Universidad
        collection = db['Curso']
        collection.insert_one(p)
def MostrarDatos(seleccion):
    if seleccion == 1:
        db = client.Universidad
        collection = db['Estudiantes']
        data = collection.find()
        data = list(data)
        df = pd.DataFrame(data)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print('TABLA ESTUDIANTE')
        print(df.head())
    if seleccion == 2:
        db = client.Universidad
        collection = db['Curso']
        data = collection.find()
        data = list(data)
        df = pd.DataFrame(data)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print('TABLA CURSO')
        print(df.head())



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
