
from funciones import *

def Main():
    while True:
        menu = menu_main()
        if menu == 1:
            menu_ing = menu_ingresar()
            if menu_ing == 1:
               ing_est()
            if menu_ing == 2:
               ing_curso()

        if menu == 2:
            seleccion_mostrar = mostrar_datos()
            if seleccion_mostrar == 1:
                MostrarDatos(1)
            if seleccion_mostrar == 2:
                MostrarDatos(2)
Main()