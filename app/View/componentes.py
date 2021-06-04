import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.elementos = []
        self.crear_menu()

    def crear_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.geometry("400x500")
        self.master.config(menu=menu_bar)

        
        transporte_bar = tk.Menu(menu_bar, tearoff=0)
        transporte_bar.add_command(label="Registrar transporte")
        transporte_bar.add_command(label="Ver transportes registrados")

        menu_bar.add_cascade(label="Transporte", menu=transporte_bar)

    def mostrar_texto(self, texto, fila, columna):
        elemento_texto = tk.Label(root, text=texto)
        elemento_texto.grid(row=fila, column=columna, padx=2)
        self.elementos.append(elemento_texto)


    def crear_boton(self, texto, fila, columna):
        boton = tk.Button(self.master, text=texto)
        boton.grid(row=fila, column=columna)
        self.elementos.append(boton)

    def say_hi(self):
        print("hi there, everyone!")

    


root = tk.Tk()
app = Application(master=root)
app.mostrar_texto("Texto random", 0, 0)
app.crear_boton("boton más random", 1, 2)

app.crear_boton("boton aúnmás random", 2, 2)



app.mainloop()
