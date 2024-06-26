#Apellido y nombre: Terrone Marcelo
#Division: 212
#Fecha: 11/06/2024
#Asignatura: Programacion 1
#Instancia: Primer examen parcial
from simulacro import *
archivo = 'C:/Users/marce/Desktop/UTNFRA/Programacion 1/simulacro_parcial/data.json' 

def simulacro_app_principal(archivo:str):
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
                    alta_datos(juegos)
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
                    submenu_principal()
            case 'G':
                print('Saliendo del programa')
                continuar = False
                break                
            case _:
                print('Opcion no valida')


simulacro_app_principal(archivo)


