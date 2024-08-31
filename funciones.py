## este archivo sirve para llamar a las funciones que se enuentran en el
## archivo models.py
## también sirve para solicitar datos de entrada

from models import *



def menu_main():
    opcion =0
    try:
        while opcion < 1 or opcion > 2:
            opcion = int(input('1.-Ingresar\n'
                               '2.-Buscar\n'))
            if opcion < 1 or opcion > 2:
                print('error ingrese denuevo la eleccion')
    except:
        print('error ingrese denuevo la eleccion')
        opcion = menu_main()
    return opcion
def menu_ingresar():
    seleccion = 0
    try:
         while seleccion < 1 or seleccion > 2:
            seleccion = int(input('1.-Estudiante\n'
                                '2.-Curso\n'))
            if seleccion < 1 or seleccion > 2:
                print('error ingrese denuevo la eleccion')


    except:
        print('error ingrese denuevo la eleccion')
        seleccion = menu_ingresar()
    return seleccion
def Ingresa(seleccion):
    if seleccion == 1:
        while True:
            # ingresa datos
            nombre = input('Ingresa el nombre\n')
            try:
                edad = int(input('Ingresa la edad\n'))
            except:
                print('No ingresó un número, se asumirá en cero')
                edad = ''
            rut = input('Ingrese el rut\n')
            carrera = input("Ingrese la carrera del Estudiante\n")
            try:
                ano_ingreso = int(input('Ingrese el año de Ingreso\n'))
            except:  # en caso de ingresar un dato no numérico
                print('No ingresó un número, se asumirá en cero')
                ano_ingreso = ''
            p = {}
            if len(nombre) > 0:
                p['nombre'] = nombre
            if len(str(edad)) > 0:
                p['edad'] = edad
            if len(rut) > 0:
                p['rut'] = rut
            if len(carrera) > 0:
                p['carrera'] = carrera
            if len(str(ano_ingreso)) > 0 or len(str(ano_ingreso)) < 4 :
                p['año_ingreso'] = ano_ingreso
            InsertDatos(p,1)
            opcion = input('si para continuar, no para finalizar\n')
            while opcion != 'si' and opcion != 'no':
                print('Error')
                opcion = input('si para continuar, no para finalizar\n')
            if opcion == 'no':
                break
    if seleccion == 2:
        while True:
            curso = input('Ingresa el nombre del curso\n')
            try:
                codigo_curso = int(input('Ingresa el codigo del curso\n'))
            except:
                print('No ingresó un número, se asumirá en cero')
                codigo_curso = ''
            rut_estudiante = input('Ingrese el rut del estudiante\n')
            try:
                nota = input("Ingrese la nota final del estudiante\n")
            except:
                print('No ingresó un número, se asumirá en cero')
                nota = ''

            p = {}
            if len(curso) > 0:
                p['curso'] = curso
            if len(str(codigo_curso)) > 0:
                p['codigo_curso'] = codigo_curso
            if len(rut_estudiante) > 0:
                p['rut_estudiante'] = rut_estudiante
            if len(str(nota)):
                p['nota'] = nota
            InsertDatos(p,2)
            opcion = input('si para continuar, no para finalizar\n')
            while opcion != 'si' and opcion != 'no':
                print('Error')
                opcion = input('si para continuar, no para finalizar\n')
            if opcion == 'no':
                break
'''
def Muestra_datos_rut():
    rut = input('Ingresa rut\n')
    search = {'rut':rut}
    FilterRut(search)'''