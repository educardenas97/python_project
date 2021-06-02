from app.Core.main import *
from app.View import funciones

def main():
    funciones.main(menu)

def menu():
    items = ["Registrar Paquete", "Paquetes en Transito", "Paquetes pendientes", "Paquetes entregados", "Salir"]
    options = funciones.sub_menu(items, "Menu Paqueteria")

    while options != len(items):
        if options == 1:
            funciones.mostrar_lista([registrar_paquete()], "Sistema ->", False)
        elif options == 2:
            funciones.mostrar_lista(paquetes_en_transito(), "Paquetes en transito")
        elif options == 3:
            funciones.mostrar_lista([paquetes_pendientes()], "Cantidad: paquetes pendientes", False)
        elif options == 4:
            funciones.mostrar_lista(paquetes_entregados(), "Paquetes en entregados")
        else:
            print("Opcion no permitida")

        options = funciones.sub_menu(items, "Menu Paqueteria")

    return True


def registrar_paquete():
    codigo = int(input("Codigo: "))
    peso = int(input("Peso (en Gr.): "))
    description = input("Description: ")
    try:
        valor_articulo =  int(input("Valor del articulo en $ (en caso de no poseer dejarlo en blanco): "))
    except ValueError:
        valor_articulo = 0

    respuesta = app.registrar_paquete(codigo, peso, description, valor_articulo)

    return "Paquete en espera, posición: {}".format(respuesta) if type(respuesta) == type(codigo) else respuesta

def paquetes_pendientes():
    paquetes = app.empresa.paquetes_pendientes.qsize()
    return paquetes

def paquetes_entregados():
    paquetes = app.empresa.paquetes_entregados
    return paquetes

def paquetes_en_transito():
    paquetes = app.empresa.paquetes_transito
    return paquetes
