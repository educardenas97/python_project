from queue import Queue


class Empresa:
    """
    Clase: Empresa
    
    Parametros:
        argumento1(str): Razon Social de la Empresa
        argumento2(str): Direccion fisica        
    """

    def __init__(self, razon_social, direccion):
        self.razon_social = razon_social
        self.direccion = direccion
        #Cola de paquetes_pendientes
        self.paquetes_pendientes = Queue()
        self.paquetes_entregados = []
        self.paquetes_transito = []
        self.transportes_disponibles = []
        self.embarques_realizados = []
        self.empleados = []
        self.clientes = []
    
    def agregar_transporte(self, transporte):
        """
        Se agrega un nuevo transporte a los ya disponibles

        Parametros:
            argumento1 (Transporte): transporte a agregar

        """
        self.transportes_disponibles.append(transporte)
        self.transportes_disponibles.sort(key=lambda transporte: transporte.fecha_salida)
    
    def calcular_rentabilidad():
        ''' Funcion que calcula la rentabilidad actual de la empresa '''
        pass

    def __str__(self):
        return "razon_social: {}, direccion: {},\n paquetes_pendientes: {},\n paquetes_transito: {} ,\n paquetes_entregados: {},\n transportes_disponibles: {},\n embarques_realizados: {},\n empleados: {},\n clientes: {}".format(self.razon_social,
        self.direccion, self.paquetes_pendientes.qsize(), self.paquetes_transito, self.paquetes_entregados, self.transportes_disponibles, self.embarques_realizados, self.empleados, self.clientes)
