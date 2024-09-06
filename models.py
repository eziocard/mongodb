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
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', None)
        print('TABLA ESTUDIANTE')
        print(df)
    if seleccion == 2:
        db = client.Universidad
        collection = db['Curso']
        data = collection.find()
        data = list(data)
        df = pd.DataFrame(data)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', None)
        print('TABLA CURSO')
        print(df)



## función para filtrar persona por rut

def Filtrar(search,seleccion_2):
    if seleccion_2 == 1:
        db = client.Universidad
        collection = db['Estudiantes']
        data = collection.find(search)
        data = list(data)
        df = pd.DataFrame(data)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
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
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', None)
        print('TABLA FILTRADA')
        print(df.head())

## funcion para actualizar registros

def Actualizar(search,seleccion,campo,nuevo_valor):
    #conexion a dbs
    db = client.Universidad
    #seleccion para estudiantes
    if seleccion == 1:
        collection = db['Estudiantes'] 
        criterio = {'rut':search} #creamos un filtro(criterio) en forma de diccionario para proporcionarlo al comando update_one
    elif seleccion == 2:
        collection = db['Cursos']
        criterio = {'codigo_curso':search}

    #crear el nuevo campo
    actualizacion = {'$set':{campo : nuevo_valor}}
    #realizar la actualizacion
    resultado = collection.update_one(criterio,actualizacion)
    #comprobar actualizacion
    if resultado.update_count > 0:
        print(f"Registro perteneciente a {search} actualizado exitosamente")
    else:
        print(f"No se encotro un registro con {search}")

##funcion para eliminar

def eliminar(rut=None,codigo_curso=None):
    #conexion a dbs
    db = client.Universidad
    if rut:
        collection = db['Estudiantes']
        criterio = {'rut' : rut}
        resultado = collection.delete_one(criterio)

        if resultado.deleted_count > 0:
            print(f"Estudiante con RUT {rut} eliminado exitosamente")
        else:
            print(f"RUT: {rut} no encontrado")
    elif codigo_curso:
        collection = db['Cursos']
        criterio = {'codigo_curso' : codigo_curso}
        resultado = collection.delete_one(criterio)
        if resultado.deleted_count > 0:
            print(f"Curso con codigo {codigo_curso} eliminado exitosamente")
        else:
            print(f"Curso: {codigo_curso} no encontrado")

