from simulacro_practica import *
#from os import system

archivo = 'C:/Users/marce/Desktop/UTNFRA/Programacion 1/para_practicar/data.json'

def simulacro_app_principal(lista:list):
    continuar = True
    juegos = []
    retorno_importar_data = False
    while continuar:
        menu = simulacro_menu_principal()
        match menu:
            case 'A':
                juegos = importar_data(archivo)
                normalizar_datos(juegos)
                retorno_importar_data = True
                print('Juegos cargados con exito!')
            case 'B':
                if retorno_importar_data == False:
                    print('Debes cargar los juegos primero')
                else:
                    alta_datos(archivo)
            case 'C':
                if retorno_importar_data == False:
                    print('Debes cargar los juegos primero')
                else:
                    manipular_datos_juegos(juegos, 'modificar')
            case 'D':
                if retorno_importar_data == False:
                    print('Debes cargar los juegos primero')
                else:
                    manipular_datos_juegos(juegos, 'borrar')
            case 'E':
                if retorno_importar_data == False:
                    print('Debes cargar los juegos primero')
                else:
                    listar_juegos(juegos, "listar_juegos")
            case 'F':
                if retorno_importar_data == False:
                    print('Debes cargar los juegos primero')
                else:
                    menu_ordenamiento(juegos)
            case 'G':
                if retorno_importar_data == False:
                    print('Debes cargar los juegos primero')
                else:
                    buscar_juego_titulo(juegos)
            case 'H':
                if retorno_importar_data == False:
                    print('Debes cargar los juegos primero')
                else:
                    mostrar_promedio_dato(lista, 'anio')
            case 'I':
                if retorno_importar_data == False:
                    print('Debes cargar los juegos primero')
                else:
                    calcular_porcentaje(juegos)
            case 'J':
                print('Saliendo del programa')
                continuar = False
                break
            case _:
                print('Opcion no valida')
        

simulacro_app_principal(archivo)
#system('cls')


