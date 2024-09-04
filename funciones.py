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
def verificar_rut(rut):
    rut = str(rut)
    respuesta = False
    if rut[8] == '-' and len(rut) == 10:
        respuesta = True
    else:
        respuesta = False
    return respuesta
def ing_est():
    p = {}
    nombre = None
    edad = None
    rut = None
    carrera = None
    ano_ingreso = None

    while nombre == None:
           try:
               nombre = input('Ingresa el nombre\n').lower()
               if nombre == '':
                   print('Porfavor ingrese un nombre')
                   nombre = None
           except:
               print('Error ingrese el nombre denuevo')
               nombre = None
    while edad == None:
           try:
                edad = int(input('Ingresa la edad\n'))
                if edad == '':
                    print('Porfavor ingrese una edad')
                    edad = None
           except:
                  edad = None
    while rut == None:
        try:
            rut = input('Ingresar rut del estudiante\n')
            if rut == '':
                print('por favor ingrese un rut')
                rut = None
            else:
                respuesta = verificar_rut(rut)
                if respuesta == False:
                    print('Porfavor ingrese un rut valido')
                    rut = None
        except:
            print('Porfavor ingrese un rut valido')
            rut = None
    while carrera == None:
        try:
            carrera = input("Ingrese la carrera del Estudiante\n").lower()
            if carrera == '':
                print('Por favor ingrese una carrera')
                carrera = None
        except:
            print('error al ingresar carrera')
            carrera = None
    while ano_ingreso == None:
        try:
            ano_ingreso = int(input('Ingrese el año de Ingreso\n'))

            if len(str(ano_ingreso)) > 0 and len(str(ano_ingreso)) < 4 :
                print('Error por favor ingrese un año')
                ano_ingreso = None

        except:
            print('Error por favor ingrese un año')
            ano_ingreso = None

    p['nombre'] = nombre
    p['edad'] = edad
    p['rut'] = rut
    p['carrera'] = carrera
    p['año_ingreso'] = ano_ingreso
    InsertDatos(p, 1)
    continuar = None
    while continuar == None:
        continuar = input('1.-Continuar ingresando estudiantes\n'
                          '2.-salir\n')
        if continuar == 'a':
            ing_curso()
        if continuar == 'b':
            print('Menu')
        else:
            continuar = None


def ing_curso():
    curso = None
    codigo_curso = None
    rut = None
    nota = None
    p = {}
    while curso == None:
        try:
            curso = input('Ingresa el nombre del curso\n').lower()
            if curso == '':
                print('Porfavor ingrese un nombre')
                curso = None
        except:
            print('Error ingrese el nombre denuevo')
            curso = None
    while codigo_curso == None:
        try:
            codigo_curso = input('Ingrese el codigo del curso\n').lower()
            if codigo_curso == '':
                print('Porfavor ingrese el codigo del curso')
                codigo_curso = None
        except:
            print('Porfavor ingrese el codigo denuevo')
            codigo_curso = None
    while rut == None:
        try:
            rut = input('Ingresar rut del estudiante\n')
            if rut == '':
                print('por favor ingrese un rut')
                rut = None
            else:
                respuesta = verificar_rut(rut)
                if respuesta == False:
                    print('Porfavor ingrese un rut valido')
                    rut = None
        except:
            print('Porfavor ingrese un rut valido')
            rut = None
    while nota == None:
        try:
            nota = int(input("Ingrese la nota final del estudiante\n"))
            if nota == '':
                print('Por favor ingrese una nota')
                nota = None
        except:
            print('error Por favor ingrese la nota denuevo')
            nota = None
    if len(curso) > 0:
        p['curso'] = curso
    if len(str(codigo_curso)) > 0:
        p['codigo_curso'] = codigo_curso
    if len(rut) > 0:
        p['rut'] = rut
    if len(str(nota)):
        p['nota'] = nota
    InsertDatos(p, 2)
    continuar = None
    while continuar == None:
        continuar = input('1.-Continuar ingresando estudiantes\n'
                          '2.-salir\n')
        if continuar == 'a':
            ing_curso()
        if continuar == 'b':
            print('Menu')
        else:
            continuar = None


def mostrar_datos():
    seleccion = int(input('Mostrar Datos\n'
                          '1.-datos estudiantes\n'
                          '2.-datos cursos\n'))
    return seleccion
'''
def Muestra_datos_rut():
    rut = input('Ingresa rut\n')
    search = {'rut':rut}
    FilterRut(search)'''