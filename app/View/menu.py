from tkinter import *
from app.Core.main import *


root = Tk()

vista = []


#Menu Bar
def main():
    menu_bar =  Menu(root)
    root.geometry("400x500")
    root.config(menu=menu_bar)


    administracion_bar = Menu(menu_bar, tearoff=0)
    administracion_bar.add_command(
        label="Registrar Cliente", command=registrar_cliente)
    administracion_bar.add_command(
        label="Registrar Empleado", command=registrar_empleado)

    paqueteria_bar = Menu(menu_bar, tearoff=0)
    paqueteria_bar.add_command(label="Registrar Paquete")
    paqueteria_bar.add_command(label="Ver paquetes en transito")
    paqueteria_bar.add_command(label="Ver paquetes registrados")

    transporte_bar = Menu(menu_bar, tearoff=0)
    transporte_bar.add_command(label="Registrar transporte")
    transporte_bar.add_command(label="Ver transportes registrados")

    menu_bar.add_cascade(label="Administracion", menu=administracion_bar)
    menu_bar.add_cascade(label="Paqueteria", menu=paqueteria_bar)
    menu_bar.add_cascade(label="Transporte", menu=transporte_bar)

def registrar_cliente():
    global vista
    root.title("Registrar Cliente")

    nombre_titulo = Label(root, text="Nombre: ")
    nombre_titulo.grid(row=0, column=0, padx=2)
    vista.append(nombre_titulo)

    nombre = Entry(root, width=30)
    nombre.grid(row=0, column=1, padx=2)
    vista.append(nombre)

    text = Label(root, text="Apellido: ")
    text.grid(row=1, column=0, padx=2)

    apellido = Entry(root, width=30)
    apellido.grid(row=1, column=1, padx=2)

    cedula_titulo = Label(root, text="Cedula: ")
    cedula_titulo.grid(row=2, column=0, padx=2)
    vista.append(cedula_titulo)

    cedula = Entry(root, width=30)
    cedula.grid(row=2, column=1, padx=2)
    vista.append(cedula)


def registrar_empleado():
    global vista
    for element in vista:
        element.destroy()

    root.title("Registrar Empleado")

    text = Label(root, text="Nombre: ")
    text.grid(row=0, column=0)

    nombre = Entry(root, width=30)
    nombre.grid(row=0, column=1)

    text = Label(root, text="Apellido: ")
    text.grid(row=1, column=0)

    apellido = Entry(root, width=30)
    apellido.grid(row=1, column=1)



main()
root.mainloop()
