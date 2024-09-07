## este archivo sirve para llamar a las funciones que se enuentran en el
## archivo models.py
## también sirve para solicitar datos de entrada

from models import *



def menu_main():
    opcion =0
    print('Menu Principal')
    try:
        while opcion < 1 or opcion > 4:
            opcion = int(input('1.-Ingresar\n'
                               '2.-Buscar\n'
                               '3.-Actualizar\n'
                               '4.-Eliminar\n'))
            if opcion < 1 or opcion > 4:
                print('error ingrese denuevo la eleccion')
    except:
        print('error ingrese denuevo la eleccion')
        opcion = menu_main()
    return opcion
def menu_ingresar():
    seleccion = 0
    print('Menu Ingresar')
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
    nombre = False
    edad = False
    rut = False
    carrera = False
    ano_ingreso = False
    continuar = False
    while nombre == False:
           try:
               nombre = input('Ingresa el nombre\n').lower()
               if nombre == '':
                   print('Porfavor ingrese un nombre')
                   nombre = False
           except:
               print('Error ingrese el nombre denuevo')
               nombre = False
    while edad == False:
           try:
                edad = int(input('Ingresa la edad\n'))
                if edad == '':
                    print('Porfavor ingrese una edad')
                    edad = False
           except:
                  edad = False
    while rut == False:
        try:
            rut = input('Ingresar rut del estudiante\n')
            if rut == '':
                print('por favor ingrese un rut')
                rut = False
            else:
                respuesta = verificar_rut(rut)
                if respuesta == False:
                    print('Porfavor ingrese un rut valido')
                    rut = False
        except:
            print('Porfavor ingrese un rut valido')
            rut = False
    while carrera == False:
        try:
            carrera = input("Ingrese la carrera del Estudiante\n").lower()
            if carrera == '':
                print('Por favor ingrese una carrera')
                carrera = False
        except:
            print('error al ingresar carrera')
            carrera = False
    while ano_ingreso == False:
        try:
            ano_ingreso = int(input('Ingrese el año de Ingreso\n'))

            if len(str(ano_ingreso)) > 0 and len(str(ano_ingreso)) < 4 :
                print('Error por favor ingrese un año')
                ano_ingreso = False

        except:
            print('Error por favor ingrese un año')
            ano_ingreso = False

    p['nombre'] = nombre
    p['edad'] = edad
    p['rut'] = rut
    p['carrera'] = carrera
    p['año_ingreso'] = ano_ingreso
    InsertDatos(p, 1)
    print('Dato ingresado con exito')




def ing_curso():
    curso = False
    codigo_curso = False
    rut = False
    nota = False
    p = {}
    while curso == False:
        try:
            curso = input('Ingresa el nombre del curso\n').lower()
            if curso == '':
                print('Porfavor ingrese un nombre')
                curso = False
        except:
            print('Error ingrese el nombre denuevo')
            curso = False
    while codigo_curso == False:
        try:
            codigo_curso = input('Ingrese el codigo del curso\n').lower()
            if codigo_curso == '':
                print('Porfavor ingrese el codigo del curso')
                codigo_curso = False
        except:
            print('Porfavor ingrese el codigo denuevo')
            codigo_curso = False
    while rut == False:
        try:
            rut = input('Ingresar rut del estudiante\n')
            if rut == '':
                print('por favor ingrese un rut')
                rut = False
            else:
                respuesta = verificar_rut(rut)
                if respuesta == False:
                    print('Porfavor ingrese un rut valido')
                    rut = None
        except:
            print('Porfavor ingrese un rut valido')
            rut = False
    while nota == False:
        try:
            nota = int(input("Ingrese la nota final del estudiante\n"))
            if nota == '':
                print('Por favor ingrese una nota')
                nota = False
        except:
            print('error Por favor ingrese la nota denuevo')
            nota = False
    if len(curso) > 0:
        p['curso'] = curso
    if len(str(codigo_curso)) > 0:
        p['codigo_curso'] = codigo_curso
    if len(rut) > 0:
        p['rut'] = rut
    if len(str(nota)):
        p['nota'] = nota
    InsertDatos(p, 2)
    print('Dato ingresado con exito')


def mostrar_datos():
    seleccion = False
    seleccion_2 =False
    ano_ingreso = False
    codigo_curso = False
    nota = False
    while seleccion == False:
        try:
            seleccion = int(input('Menu Mostrar Datos\n'
                                  '1.-Datos estudiantes\n'
                                  '2.-Datos cursos\n'))
            if seleccion == '':
                print('Por favor eliga una opcion')
                seleccion = False


            if seleccion == 1:
                while seleccion_2 == False:
                    print('Menu Mostrar Estudiantes')
                    try:
                        seleccion_2 = int(input('1.-Mostrar Todos\n'
                                                '2.-filtrar por carrera\n'
                                                '3.-filtrar por año de ingreso\n'))
                        if seleccion_2 == '':
                            print('Por favor eliga una opcion')
                        if seleccion_2 == 1:
                            MostrarDatos(1)
                        if seleccion_2 == 2:
                            carrera = input('Ingresa la Carrera\n')
                            search = {'carrera': carrera}
                            Filtrar(search,seleccion)
                        if seleccion_2 == 3:
                            while ano_ingreso == False:
                                try:
                                    ano_ingreso = int(input('Ingrese el año de Ingreso\n'))
                                    search = {'año_ingreso':ano_ingreso}
                                    Filtrar(search,seleccion)

                                    if len(str(ano_ingreso)) > 0 and len(str(ano_ingreso)) < 4:
                                        print('Error por favor ingrese un año')
                                        ano_ingreso = False

                                except:
                                    print('Error por favor ingrese un año')
                                    ano_ingreso = False

                    except:
                        print('Por favor eliga una opcion')
                        seleccion_2 = False

            elif seleccion == 2:
                while seleccion_2 == False:
                    print('Menu Mostrar Curso')
                    try:
                        seleccion_2 = int(input('1.-Mostrar todos\n'
                                                '2.-Filtrar por codigo\n'
                                                '3.-Filtrar por nota\n'))
                        if seleccion_2 == '':
                            print('Error ingrese una opcion')
                        if seleccion_2 == 1:
                            MostrarDatos(2)
                        elif seleccion_2 == 2:
                            while codigo_curso == False:
                                try:
                                    codigo_curso = input('Ingrese el codigo del curso\n').lower()
                                    if codigo_curso == '':
                                        print('Porfavor ingrese el codigo del curso')
                                        codigo_curso = False
                                    else:

                                        search = {'codigo_curso': codigo_curso}
                                        Filtrar(search, seleccion)

                                except:
                                    print('Porfavor ingrese el codigo denuevo')
                                    codigo_curso = False
                        elif seleccion_2 == 3:
                            while nota == False:
                                try:
                                    nota = int(input("Ingrese la nota final del estudiante\n"))
                                    if nota == '':
                                        print('Por favor ingrese una nota')
                                        nota = False
                                    else:
                                        search = {'nota': nota}
                                        Filtrar(search, seleccion)
                                except:
                                    print('error Por favor ingrese la nota denuevo')
                                    nota = False


                    except:
                        print('Error ingrese una opcion')
                        seleccion_2 = False

            else:
                print('Error ingrese una opcion')
                seleccion = False
        except:
            print('Error ingrese una opcion')
            seleccion = False
    return seleccion

def ActualizarDatos():
    seleccion = menu_ingresar()
    campo = False
    identificador = False
    if seleccion == 1:
        while identificador == False:
            try:
                identificador = input('Ingresar rut del estudiante\n')
                if identificador == '':
                    print('por favor ingrese un rut')
                    identificador = False
                else:
                    respuesta = verificar_rut(identificador)
                    if respuesta == False:
                        print('Porfavor ingrese un rut valido')
                        identificador = False
                    else:
                        search = {'rut': identificador}
                        verificar_2 = Buscar_estudiante(search)
                        if verificar_2 == True:
                            break
                        if verificar_2 == False:
                            print('el estudiante no esta ingresado en la base de datos intente denuevo')
                            identificador = False
            except:
                print('Porfavor ingrese un rut valido')
                identificador = False

        while campo == False:
            campo = int(input('Ingrese el campo que desea actualizar:\n'
                          ' 1.-nombre\n'
                          '2.- edad\n'
                          '3.- rut\n'
                          '4.-carrera\n'
                          '5.-año_ingreso\n'))
            if campo == 1:
                campo = 'nombre'
            elif campo == 2:
                campo = 'edad'
            elif campo == 3:
                campo = 'rut'
            elif campo == 4:
                campo = 'carrera'
            elif campo == 5:
                campo = 'año_ingreso'
            else:
                print('Ingrese una opcion')
                campo = False
        nuevo_valor = input(f'Ingrese el nuevo valor para {campo}\n')
        Actualizar(identificador, seleccion, campo, nuevo_valor)
    elif seleccion == 2:
        identificador = False
        while identificador == False:
            identificador = input("Ingresar el codigo del curso \n")
            search = {'codigo_curso': identificador}
            verificar = Buscar_curso(search)
            if verificar == False:
                print('el curso no fue encontrado por favor ingresar nuevamente')
                identificador = False
            else:
                while campo == False:
                    campo = input('Ingrese el campo que desea actualizar: \n'
                                  '1.-nombre curso\n'
                                  '2.-nota_final\n')
                    if int(campo) == 1:
                        campo = 'curso'
                    elif int(campo) == 2:
                        campo = 'nota_final'
                    elif int(campo) < 1 or campo > 2:
                            print('Ingrese una opcion')
                            campo = False
                    elif campo == '':
                        print('Ingrese una opcion')
                        campo = False
        nuevo_valor = input(f'Ingrese el nuevo valor para {campo}\n')
        Actualizar(identificador, seleccion, campo, nuevo_valor)
        menu_main()


def eliminar_datos():
    seleccion = menu_ingresar()
    if seleccion == 1:
        identificador = input("Ingresar el Rut del estudiante a eliminar\n")
        eliminar(rut=identificador)
    elif seleccion == 2:
        identificador_rut = input("Ingresar el Rut del estudiante asociado al curso a eliminar\n")
        identificador_curso = input("Ingresar el codigo del curso asociado al estudiante a eliminar\n")
        eliminar(rut=identificador_rut ,codigo_curso=identificador_curso)