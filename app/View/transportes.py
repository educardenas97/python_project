from app.Core.main import *
from app.View import funciones
import datetime

def main():
    funciones.main(menu)

def menu():
    items = ["Registrar Transporte", "Ver transportes disponibles", "Salir"]
    options = funciones.sub_menu(items, "Menu Transportes")

    while options != len(items):
        if options == 1:
            funciones.mostrar_lista(registrar_transporte(), "Transporte registrado")
        elif options == 2:
            funciones.mostrar_lista(
                mostrar_disponibles(), "Transportes disponibles")
        else:
            print("Opcion no permitida")
            
        options = funciones.sub_menu(items, "Menu Transportes")

    return True


def registrar_transporte():
    salida_fecha = formatear_fecha(input('Insertar fecha de salida con el siguiente formato: YYYY-MM-DD: '))
    print("En caso de dejarse en blanco se asumirá el tiempo habitual de transporte")
    try:
        llegada_fecha = salida_fecha = formatear_fecha(
            input('Insertar fecha de llegada con el siguiente formato: YYYY-MM-DD: '))
    except ValueError:
        llegada_fecha = 0

    precio = int(input('Precio por Kg. en $: '))
    capacidad = int(input('Capacidad en Kg.:'))
    transportes  = app.registrar_transporte(salida_fecha, precio, capacidad, llegada_fecha)
    return transportes

def mostrar_disponibles():
    return app.empresa.transportes_disponibles

def formatear_fecha(dato):
    year, month, day = map(int, dato.split('-'))
    return datetime.date(year, month, day)

