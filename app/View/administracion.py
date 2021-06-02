from app.Core.main import *
from app.View import funciones


def main():
    funciones.main(menu)


def menu():
    items = [" Agregar Empleado", " Agregar Clientes", " Salir"]
    options = funciones.sub_menu(items, "Menu Administración")
    while options != len(items):
        if options == len(items):
            print("Exit()")
        elif options == 1:
            empleados = agregar_empleado()
            funciones.mostrar_lista(empleados, "Lista de empleados")
        elif options == 2:
            clientes = agregar_cliente()
            funciones.mostrar_lista(clientes, "Lista de clientes")
        else:
            print("Opcion no permitida")

        options = funciones.sub_menu(items, "Menu Administración")
        
    return True

def agregar_empleado():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    ci = int(input("CI: "))
    return app.registrar_empleado(nombre,apellido,ci)


def agregar_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    ci = int(input("CI: "))
    try:
        ruc =  int(input("RUC (en caso de no poseer dejarlo en blanco): "))
    except ValueError:
        ruc = 0
    return app.registrar_cliente(nombre, apellido, ci, ruc)
