import tkinter as tk


class Componentes(tk.Frame):
    """Clase Componentes
        En esta clase se abstraen los elementos de la interfaz
        grafica generada por la biblioteca Tkinter. Esto con el
        fin de simplificar su uso
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #El arreglo contiene todos los elementos generados 
        self.elementos = []
        self.master.geometry("700x500")

    def crear_menu(self, posicion, tearoff=0):
        return tk.Menu(posicion, tearoff)


    def agregar_sub_menu(self, menu, texto, funcion):
        """Funcion agregar_sub_menu
            Función que agrega un sub menu al item facilitado
            como argumento
            Parametros: menu, texto(str), funcion
        """
        menu.add_command(label=texto, command=funcion)

    def crear_input(self, fila=0, columna=0):
        """Funcion: crear_input
            Esta función genera un cuadro de input en pantalla,
            necesita la posición en pantalla
            Parametros: fila, columna
        """
        input = tk.Entry(self.master, width=40)
        input.grid(row=fila, column=columna)
        self.elementos.append(input)
        return input

    def mostrar_texto(self, texto, fila=0, columna=0):
        """Funcion: mostrar_texto
            Genera un cuadro de texto con los
            elementos suministrados. Necesita la posición en pantalla
            Parametros: texto(str), fila(int), columna(int)
        """
        elemento_texto = tk.Label(self.master, text=texto)
        elemento_texto.grid(row=fila, column=columna, padx=2)
        self.elementos.append(elemento_texto)

    def crear_boton(self, texto, fila, columna, funcion):
        """Funcion: crear_boton
            Genera un boton y asigna una funcion al mismo
            Parametros: texto(str), fila(int), columna(int), funcion
        """
        boton = tk.Button(self.master, text=texto, command=funcion)
        boton.grid(row=fila, column=columna)
        self.elementos.append(boton)

    def limpiar_pantalla(self):
        """Funcion: limpiar_pantalla
            Elimina los elementos de la GUI
        """
        for elemento in self.elementos:
            elemento.destroy()

    def mostrar_datos(self, lista, fila=0, columna=0):
        """Funcion: mostrar_datos
            Muestra en pantalla los elementos de la lista
            Parametros: lista([]), fila(int), columna(int)
        """
        i = 1
        for element in lista:
            self.mostrar_texto(element, fila+i, columna)
            i += 1
