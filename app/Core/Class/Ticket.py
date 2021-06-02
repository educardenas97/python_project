from abc import ABCMeta, abstractmethod

class Ticket(metaclass=ABCMeta):
    '''Abstracción de la clase Ticket'''

    def __init__(self, peso, fecha, costo):
        self.peso = peso
        self.fecha = fecha
        self.costo = costo
    
    @abstractmethod
    def imprimir_ticket():
        pass

    def __str__(self):
        return "peso: {}, fecha: {}, costo:{} \n".format(self.peso, self.fecha, self.costo)

class TicketRecepcion(Ticket):
    """ 
    Especialización de la clase Ticket
    Parametros:
        argumento1(Date): fecha de salida
        argumento2(int): Precio del paquete

    """

    def __init__(self, fecha_embarque, costo, paquete, cliente):
        super().__init__(paquete.peso, fecha_embarque, costo)
        self.paquete = paquete
        self.fecha_embarque = fecha_embarque
        self.cliente = cliente

    def imprimir_ticket(self):
        return {
            "peso": self.peso,
            "fecha": self.fecha,
            "precio": self.costo,
            "paquete": {
                "codigo": self.paquete.codigo, 
                "peso": self.paquete.peso,
            },
            "fecha_embarque": self.fecha_embarque,
            "cliente": {
                "nombre": self.cliente.persona.nombre,
                "apellido": self.cliente.persona.apellido
            }
        }
    
    def __str__(self):
        return " {} {} \n fecha_embarque: {}, cliente: {} \n".format(super().__str__(), self.paquete, self.fecha_embarque, self.cliente)

class TicketEmbarque(Ticket):
    """
    Especialización de la clase Ticket
    Parametros:
        argumento1(Date): fecha de salida del transporte
        argumento2(int): Costo de transportar los paquetes
        argumento3(Transporte): objeto del tipo Transporte
    """

    def __init__(self, fecha, costo, transporte):
        super().__init__(transporte.capacidad_utilizada, fecha, costo)
        self.transporte = transporte

    def imprimir_ticket(self):
        return{
            "peso": self.peso,
            "fecha_salida": self.fecha,
            "costo": self.costo,
            "transporte": self.transporte
        }

    def __str__(self):
        return " {}, transporte: {}".format(super().__str__(), self.transporte)
