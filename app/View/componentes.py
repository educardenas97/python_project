import tkinter as tk


class Componentes(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.elementos = []
        self.master.geometry("700x500")


    def crear_menu(self, posicion):
        return tk.Menu(posicion, tearoff=0)


    def agregar_sub_menu(self, menu, texto, funcion):
        menu.add_command(label=texto, command=funcion)

    def crear_input(self, fila, columna):
        input = tk.Entry(self.master, width=40)
        input.grid(row=fila, column=columna)
        self.elementos.append(input)
        return input

    def mostrar_texto(self, texto, fila, columna):
        elemento_texto = tk.Label(self.master, text=texto)
        elemento_texto.grid(row=fila, column=columna, padx=2)
        self.elementos.append(elemento_texto)

    def crear_boton(self, texto, fila, columna, funcion):
        boton = tk.Button(self.master, text=texto, command=funcion)
        boton.grid(row=fila, column=columna)
        self.elementos.append(boton)

    def limpiar_pantalla(self):
        for elemento in self.elementos:
            elemento.destroy()

    def mostrar_datos(self, lista, fila, columna):
        i = 1
        for element in lista:
            self.mostrar_texto(element, fila+i, columna)
            i += 1
