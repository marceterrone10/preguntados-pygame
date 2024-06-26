from practica import *

def simulacro_app_principal(lista:list):
    continuar = True
    #personas = []
    retorno_importar_data = False
    while continuar:
        menu = simulacro_menu_principal()
        match menu:
            case 'A':
                personas = cargar_info(nombre_archivo)
                normalizar_datos(personas)
                retorno_importar_data = True
                print('Informacion cargada!')
            case 'B':
                if retorno_importar_data == False:
                    print('Cargar datos para continuar.')
                else:
                    alta_datos(cargar_info(nombre_archivo))
            case 'C':
                if retorno_importar_data == False:
                    print('Cargar datos para continuar.')
                else:
                    modificar_datos(cargar_info(nombre_archivo), 'modificar')
            case 'D':
                if retorno_importar_data == False:
                    print('Cargar datos para continuar.')
                else:
                    modificar_datos(personas, 'borrar')
            case 'E':
                if retorno_importar_data == False:
                    print('Cargar datos para continuar.')
                else:
                    listar_juegos(personas, 'listar_juegos')
            case 'F':
                if retorno_importar_data == False:
                    print('Cargar datos para continuar.')
                else:
                    menu_ordenamiento(personas)                   
            case 'J':
                print('Saliendo del programa')
                continuar = False
                break
            case _:
                print('Opcion no valida')

simulacro_app_principal(nombre_archivo)