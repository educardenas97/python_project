import tkinter as tk
from app.Core.Controller import App
from app.View.interfaz import *
from app.View.componentes import *


root = tk.Tk()
componentes = Componentes(master=root)
controlador = App.App("Fast Shipping", "Pepe loca")
interfaz = Interfaz(controlador, componentes)
interfaz.mostrar_menu()


componentes.mainloop()