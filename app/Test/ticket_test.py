import datetime
from app.Core.main import *

app = App.App('Front', 'direct')

#Empleados
app.registrar_empleado('pepe', 'gallo', 783)
app.registrar_empleado('Ed', 'Gomez', 4659580)
app.registrar_empleado('pepae', 'gallo', 783234)

#clientes
app.registrar_cliente('Yo', 'Merengues', 4659580, 11290633)
identificador = app.empresa.clientes[0].identificador

#Paquetes
#En este punto no se encuentran los transportes, y quedan encolados como pendientes
app.registrar_paquete(2, 43, 'ttt')
app.registrar_paquete(234, 43, 'GGG')

#Transportes
#El transporte no tiene capacidad suficiente, más paquetes quedan pendientes
app.registrar_transporte(datetime.datetime.now(), 23, 0.1)
app.registrar_paquete(int(identificador), 43, 'GGG')
app.registrar_paquete(2, 43, 'ttt')
app.registrar_paquete(234, 43, 'GGG')
app.registrar_paquete(2, 43, 'ttt')


#Transportes
#Todos los paquetes pendientes son cargados
app.registrar_transporte(datetime.datetime.now(), 23, 100)

#Paquetes
app.registrar_paquete(2, 43, 'ttt')
app.registrar_paquete(2, 43, 'ttt')
app.registrar_paquete(2, 43, 'ttt')


#Se muestran los tickets
if len(app.empresa.paquetes_transito) == 9:
    print("Test passed")

#for ticket in app.empresa.paquetes_transito:
#    print(ticket.imprimir_ticket())