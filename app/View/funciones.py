def mostrar_lista(lista, titulo=" ", mostrarNro=True):
    """
    Mostrar una lista

    Parametros:
        argumento1(Objeto[]): lista a mostrar por terminal
        argumento2(str): Titulo a mostrar
        argumento3(bool): Bandera para indicar si se muestran los numeros a un costado
    """

    print("\n--------------------------------")
    print("{}".format(titulo))
    item = 1
    for element in lista:
        print("{}- {}".format(item if mostrarNro == True else " ", element))
        item += 1

    print("--------------------------------\n")


def sub_menu(items, titulo=" ", mostrarNro=True):
    ''' Permite el input de datos '''
    print("\n--------------")
    mostrar_lista(items, titulo, mostrarNro)
    print("--------------")
    return int(input("Seleccionar: "))


def main(funcion):
    """
    Funcion que ejecuta otras funciones y atrapa las posibles excepciones
    que puedan suceder durante la ejecución

    Parametros:
        argumento1(funcion): Funcion a ejecutar
    """
    try:
        exit_menu = funcion()
    except:
        print("Error de input")
        exit_menu = False
    finally:
        return 0 if exit_menu == True else main(funcion)
