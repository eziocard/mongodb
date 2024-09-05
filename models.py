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

def Filtrar(search,seleccion_2):
    if seleccion_2 == 1:
        db = client.Universidad
        collection = db['Estudiantes']
        data = collection.find(search)
        data = list(data)
        df = pd.DataFrame(data)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print('TABLA FILTRADA')
        print(df.head())

    if seleccion_2 == 2:
        db = client.Universidad
        collection = db['Curso']
        data = collection.find(search)
        data = list(data)
        df = pd.DataFrame(data)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print('TABLA FILTRADA')
        print(df.head())


