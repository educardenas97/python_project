import datetime

class Interfaz():
    def __init__(self, app, componentes):
        self.app = app
        self.componentes = componentes

    def mostrar_menu(self):
        self.componentes.master.title("Menu Principal")
        menu_bar = self.componentes.crear_menu(self.componentes.master)
        self.componentes.master.config(menu=menu_bar)

        administracion_bar = self.componentes.crear_menu(menu_bar)
        self.componentes.agregar_sub_menu(administracion_bar, "Registrar Cliente", self.registrar_cliente)
        self.componentes.agregar_sub_menu(administracion_bar, "Registrar Empleado", self.registrar_empleado)

        paqueteria_bar = self.componentes.crear_menu(menu_bar)
        self.componentes.agregar_sub_menu(paqueteria_bar, "Registrar Paquete", self.registrar_paquete)
        self.componentes.agregar_sub_menu(paqueteria_bar, "Ver Paquete en transito", self.ver_paquetes_transito)

        transporte_bar = self.componentes.crear_menu(menu_bar)
        self.componentes.agregar_sub_menu(transporte_bar, "Registrar Transporte", self.registrar_transporte)
        self.componentes.agregar_sub_menu(transporte_bar, "Ver transportes", self.ver_transportes)

        menu_bar.add_cascade(label="Administracion", menu=administracion_bar)
        menu_bar.add_cascade(label="Paqueteria", menu=paqueteria_bar)
        menu_bar.add_cascade(label="Transporte", menu=transporte_bar)

    def registrar_cliente(self):
        self.componentes.limpiar_pantalla()
        self.componentes.master.title("Registrar Cliente")
        self.componentes.mostrar_texto("Nombre", 0, 0)
        nombre = self.componentes.crear_input(0, 1)
        self.componentes.mostrar_texto("Apellido", 1, 0)
        apellido = self.componentes.crear_input(1, 1)
        self.componentes.mostrar_texto("Cedula", 2, 0)
        cedula = self.componentes.crear_input(2, 1)
        self.componentes.mostrar_texto("RUC", 3, 0)
        ruc = self.componentes.crear_input(3, 1)
        self.componentes.crear_boton("Registrar", 4, 1, lambda: self.app.registrar_cliente(
            nombre.get(), apellido.get(), int(cedula.get()), int(ruc.get())))

        self.componentes.mostrar_datos(self.app.empresa.clientes, 5, 1)

    def registrar_empleado(self):
        self.componentes.limpiar_pantalla()
        self.componentes.master.title("Registrar Empleado")
        self.componentes.mostrar_texto("Nombre", 0, 0)
        nombre = self.componentes.crear_input(0, 1)
        self.componentes.mostrar_texto("Apellido", 1, 0)
        apellido = self.componentes.crear_input(1, 1)
        self.componentes.mostrar_texto("Cedula", 2, 0)
        cedula = self.componentes.crear_input(2, 1)
        self.componentes.crear_boton("Registrar", 4, 1, lambda: self.app.registrar_empleado(
            nombre.get(), apellido.get(), int(cedula.get())))

        self.componentes.mostrar_datos(self.app.empresa.empleados, 5, 1)

    def registrar_paquete(self):
        self.componentes.limpiar_pantalla()
        self.componentes.master.title("Registrar Paquete")
        self.componentes.mostrar_texto("Codigo", 0, 0)
        codigo = self.componentes.crear_input(0, 1)
        self.componentes.mostrar_texto("Peso", 1, 0)
        peso = self.componentes.crear_input(1, 1)
        self.componentes.mostrar_texto("Descripcion", 2, 0)
        descripcion = self.componentes.crear_input(2, 1)
        self.componentes.mostrar_texto("Valor Articulo*", 3, 0)
        valor_articulo = self.componentes.crear_input(3, 1)

        self.componentes.crear_boton("Registrar", 4, 1, lambda: self.app.registrar_paquete(
            int(codigo.get()), int(peso.get()), descripcion.get(), int(valor_articulo.get())))

        self.componentes.mostrar_texto("Paquetes Pendientes: ", 5, 0)
        self.componentes.mostrar_texto(self.app.empresa.paquetes_pendientes.qsize(), 5, 1)
        self.componentes.mostrar_texto("Paquetes en Transito:", 6, 0)
        self.componentes.mostrar_datos(self.app.empresa.paquetes_transito, 7, 1)

    def registrar_transporte(self):
        self.componentes.limpiar_pantalla()
        self.componentes.master.title("Registrar Transportes")
        self.componentes.mostrar_texto("Fecha de salida: YYYY-MM-DD: ", 0, 0)
        fecha_salida = self.componentes.crear_input(0, 1)
        self.componentes.mostrar_texto("Precio x Kg.", 1, 0)
        precio_por_kg = self.componentes.crear_input(1, 1)
        self.componentes.mostrar_texto("Capacidad en Kg.", 2, 0)
        capacidad = self.componentes.crear_input(2, 1)

        self.componentes.crear_boton("Registrar", 3, 1, lambda: self.app.registrar_transporte(
            Interfaz.formatear_fecha(fecha_salida.get()), int(precio_por_kg.get()), int(capacidad.get())))

        self.componentes.mostrar_texto("Transportes disponibles: ", 4, 0)
        self.componentes.mostrar_datos(self.app.empresa.transportes_disponibles, 5, 1)

    def ver_paquetes_transito(self):
        self.componentes.limpiar_pantalla()
        self.componentes.master.title("Paquetes en transito")
        self.componentes.mostrar_texto("Paquetes en transito: ", 0, 0)
        self.componentes.mostrar_datos(self.app.empresa.paquetes_transito, 1, 1)

    def ver_transportes(self):
        self.componentes.limpiar_pantalla()
        self.componentes.master.title("Transportes registrados")
        self.componentes.mostrar_texto("Transportes registrados: ", 0, 0)
        self.componentes.mostrar_datos(self.app.empresa.transportes_disponibles, 1, 1)

    def formatear_fecha(dato):
        year, month, day = map(int, dato.split('-'))
        return datetime.date(year, month, day)