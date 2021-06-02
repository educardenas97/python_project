from app.View.administracion import main as administracion
from app.View.paqueteria import main as paqueteria
from app.View.transportes import main as transportes
from app.View.funciones import *

def menu():
    #Opciones a mostrar en el menu
    items = ["Administracion", "Paquetería", "Transporte", "Salir"]
    secciones = [administracion, paqueteria, transportes]
    #Se ejecuta una subrutina para permitir el input 
    options = sub_menu(items, "Menu Principal")

    while options != len(items): #Loop para seleccionar items
        if options != len(items):
            secciones[options-1]()
        #Se vuelve a habilitar un input para el usuario
        options = sub_menu(items, "Menu Principal")
    
    return True


main(menu)