import random

class Persona():
    """
    Clase persona

    Parametros:
        argumento1(str): nombre
        argumento2(str): apellido
        argumento3(str): nro de documento
    """

    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        
    def __str__(self):
        return "nombre: {}, apellido: {}, ci: {}".format(self.nombre, self.apellido, self.ci)

class Cliente():
    """ 
    Clase Cliente

    Parametros:
        argumento1(Persona): objeto Persona
        argumento2(int): RUC del cliente
    """

    def __init__(self, persona, ruc=0):
        self.persona = persona
        self.ruc = ruc        
        self.identificador = (random.randint(0, 9) + persona.ci) if persona.ci != 0 else 0
        self.paquetes = []

    def __str__(self):
        return "{}, ruc: {}, identificador: {}".format(self.persona, self.ruc, self.identificador)


class Empleado():
    """
    Parametros:
    
        argumento1(Persona): objeto Persona
        argumento2(int): fecha de registro
    """

    def __init__(self, persona, fecha_inicio):
        self.persona = persona
        self.fecha_inicio = fecha_inicio

    def __str__(self):
        return "{}, fecha_inicio: {}".format(self.persona, self.fecha_inicio)
