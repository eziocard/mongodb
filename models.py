## este archivo contiene toda la lógica de conexión a la base de datos


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
def Buscar_estudiante(search):
    respuesta = False
    db = client.Universidad
    collection = db['Estudiantes']
    data = collection.find_one(search)
    if data:
        respuesta = True
    else:
        respuesta = False
    return respuesta

def Buscar_curso(search):
    respuesta = False
    db = client.Universidad
    collection = db['Curso']
    data = collection.find_one(search)
    if data:
        respuesta = True
    else:
        respuesta = False
    return respuesta
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
    if seleccion == 1:
        db = client.Universidad
        collection = db['Estudiantes']
        criterio = {'rut': search}
        actualizacion = {'$set': {campo: nuevo_valor}}
        resultado = collection.update_one(criterio, actualizacion)
    if seleccion == 2:
        db = client.Universidad
        collection = db['Curso']
        criterio = {'codigo_curso': search}
        actualizacion = {'$set': {campo: nuevo_valor}}
        resultado = collection.update_one(criterio, actualizacion)
def eliminar(rut=None,codigo_curso=None):
    #conexion a dbs
    db = client.Universidad
    if rut:
        collection = db['Estudiantes']
        criterio = {'rut' : rut}
        resultado = collection.delete_one(criterio)
        
        collection = db['Cursos']
        criterio = {'rut_estudiante' : rut}
        resultado = collection.delete_many(criterio)

        if resultado.deleted_count > 0:
            print(f"Estudiante con RUT {rut} eliminado exitosamente")
        else:
            print(f"RUT: {rut} no encontrado")
    elif codigo_curso:
        collection = db['Cursos']
        criterio = {'codigo_curso' : codigo_curso, 'rut_estudiante' : rut}
        resultado = collection.delete_one(criterio)
        if resultado.deleted_count > 0:
            print(f"Curso con codigo {codigo_curso} eliminado exitosamente")
        else:
            print(f"Curso: {codigo_curso} no encontrado")

