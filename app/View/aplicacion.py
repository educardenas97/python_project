import tkinter as tk
from app.Core.Controller import App as controlador
from app.View import Interfaz as vista
from app.View import Componentes as componentes


root = tk.Tk()
componentes = componentes.Componentes(master=root)
controlador = controlador.App("Fast Shipping", "Pepe loca")
interfaz = vista.Interfaz(controlador, componentes)
interfaz.mostrar_menu()


componentes.mainloop()
