
from funciones import *

def Main():
    while True:
        menu = menu_main()
        if menu == 1:
            menu_ing = menu_ingresar()
            if menu_ing == 1:
               Ingresa(1)
            if menu_ing == 2:
               Ingresa(2)


Main()