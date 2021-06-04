import datetime
import tkinter as tk
from app.Core.Controller import App


class Interfaz(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.elementos = []
        self.crear_menu()
        self.app = App.App('FastShipping', 'Miami Gardens FL 33169')

    def crear_menu(self):
        self.master.title("Menu Principal")

        menu_bar = tk.Menu(self.master)
        self.master.geometry("700x500")
        self.master.config(menu=menu_bar)

        administracion_bar = tk.Menu(menu_bar, tearoff=0)
        administracion_bar.add_command(
            label="Registrar Cliente", command=self.registrar_cliente)
        administracion_bar.add_command(
            label="Registrar Empleado", command=self.registrar_empleado)

        paqueteria_bar = tk.Menu(menu_bar, tearoff=0)
        paqueteria_bar.add_command(
            label="Registrar Paquete", command=self.registrar_paquete)
        paqueteria_bar.add_command(label="Ver paquetes en transito")
        paqueteria_bar.add_command(label="Ver paquetes registrados")

        transporte_bar = tk.Menu(menu_bar, tearoff=0)
        transporte_bar.add_command(label="Registrar transporte", command=self.registrar_transporte)
        transporte_bar.add_command(label="Ver transportes registrados")

        menu_bar.add_cascade(label="Administracion", menu=administracion_bar)
        menu_bar.add_cascade(label="Paqueteria", menu=paqueteria_bar)
        menu_bar.add_cascade(label="Transporte", menu=transporte_bar)

    def registrar_cliente(self):
        self.limpiar_pantalla()
        self.master.title("Registrar Cliente")
        self.mostrar_texto("Nombre", 0, 0)
        nombre = self.crear_input(0,1)
        self.mostrar_texto("Apellido", 1, 0)
        apellido = self.crear_input(1, 1)
        self.mostrar_texto("Cedula", 2, 0)
        cedula = self.crear_input(2, 1)
        self.mostrar_texto("RUC", 3, 0)
        ruc = self.crear_input(3, 1)
        self.crear_boton("Registrar", 4, 1, lambda: self.app.registrar_cliente(
            nombre.get(), apellido.get(), int(cedula.get()), int(ruc.get())))

        self.mostrar_datos(self.app.empresa.clientes, 5)

       
    def registrar_empleado(self):
        self.limpiar_pantalla()
        self.master.title("Registrar Empleado")
        self.mostrar_texto("Nombre", 0, 0)
        nombre = self.crear_input(0,1)
        self.mostrar_texto("Apellido", 1, 0)
        apellido = self.crear_input(1, 1)
        self.mostrar_texto("Cedula", 2, 0)
        cedula = self.crear_input(2, 1)
        self.crear_boton("Registrar", 4, 1, lambda: self.app.registrar_empleado(
            nombre.get(), apellido.get(), int(cedula.get())))

        self.mostrar_datos(self.app.empresa.empleados, 5)
    
    def registrar_paquete(self):
        self.limpiar_pantalla()
        self.master.title("Registrar Paquete")
        self.mostrar_texto("Codigo", 0, 0)
        codigo = self.crear_input(0,1)
        self.mostrar_texto("Peso", 1, 0)
        peso = self.crear_input(1, 1)
        self.mostrar_texto("Descripcion", 2, 0)
        descripcion = self.crear_input(2,1)
        self.mostrar_texto("Valor Articulo*", 3, 0)
        valor_articulo = self.crear_input(3,1)

        self.crear_boton("Registrar", 4, 1, lambda: self.app.registrar_paquete(
            int(codigo.get()), int(peso.get()), descripcion.get(), int(valor_articulo.get())))

        self.mostrar_texto("Paquetes Pendientes: ", 5, 0)
        self.mostrar_texto(self.app.empresa.paquetes_pendientes.qsize(), 5, 1)
        self.mostrar_texto("Paquetes en Transito:", 6, 0)
        self.mostrar_datos(self.app.empresa.paquetes_transito, 7)

    def registrar_transporte(self):
        #Solucionar lo de la fecha
        self.limpiar_pantalla()
        self.master.title("Registrar Transportes")
        self.mostrar_texto("Fecha de salida: YYYY-MM-DD: ", 0, 0)
        fecha_salida = self.crear_input(0, 1)
        self.mostrar_texto("Precio x Kg.", 1, 0)
        precio_por_kg = self.crear_input(1, 1)
        self.mostrar_texto("Capacidad en Kg.", 2, 0)
        capacidad = self.crear_input(2, 1)

        self.crear_boton("Registrar", 3, 1, lambda: self.app.registrar_transporte(
            Interfaz.formatear_fecha(fecha_salida.get()), int(precio_por_kg.get()), int(capacidad.get())))

        self.mostrar_texto("Transportes disponibles: ", 4, 0)
        self.mostrar_datos(self.app.empresa.transportes_disponibles, 5)

    def formatear_fecha(dato):
        year, month, day = map(int, dato.split('-'))
        return datetime.date(year, month, day)


    def crear_input(self, fila, columna):
        input = tk.Entry(root, width=40)
        input.grid(row=fila, column=columna)
        self.elementos.append(input)
        return input

    def mostrar_texto(self, texto, fila, columna):
        elemento_texto = tk.Label(root, text=texto)
        elemento_texto.grid(row=fila, column=columna, padx=2)
        self.elementos.append(elemento_texto)

    def crear_boton(self, texto, fila, columna, funcion):
        boton = tk.Button(self.master, text=texto, command=funcion)
        boton.grid(row=fila, column=columna)
        self.elementos.append(boton)

    def limpiar_pantalla(self):
        for elemento in self.elementos:
            elemento.destroy()

    def mostrar_datos(self, lista, fila):
        i = 1
        for element in lista:
            self.mostrar_texto(element, fila+i, 1)
            i += 1
    


root = tk.Tk()
aplicacion = Interfaz(master=root)


aplicacion.mainloop()
