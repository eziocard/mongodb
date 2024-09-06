
from funciones import *

def Main():
    while True:
        menu = menu_main()
        if menu == 1:
            menu_ing = menu_ingresar()
            if menu_ing == 1:
                continuar = False
                while not continuar:
                    ing_est()
                    try:
                        continuar = int(input('Desea seguir ingresando datos:\n'
                                              '1.-si\n'
                                              '2.-no\n'))
                        if continuar == 1:
                            continuar = False
                        elif continuar == 2:
                            continuar = True
                        else:
                            print('Por favor ingrese una de las alternativas')
                    except:
                        print('Por favor ingrese una de las alternativas')
                        continuar = False


            if menu_ing == 2:
               ing_curso()

        if menu == 2:
            seleccion_mostrar = mostrar_datos()
        if menu == 3:
            ActualizarDatos()
            mostrar_datos()
        if menu == 4:
            eliminar_datos()
            mostrar_datos()


Main()
