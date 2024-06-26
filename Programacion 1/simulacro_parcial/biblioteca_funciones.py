import json
lista_nueva = []

def importar_data(nombre_archivo):
    
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
        lista_nueva.append(datos)
        #print(lista_nueva)
    return datos

def encontrar_ultimo_id(datos):
    ultimo_id = 0
    for juego in datos:
        if type(juego) == dict and 'id' in juego:
            if juego['id'] > ultimo_id:
                ultimo_id = juego['id']
    return ultimo_id

def simulacro_alta_juegos(datos:list):
    lista = []
    ultimo_id = encontrar_ultimo_id(datos)
    id_juego = ultimo_id + 1
    lista.append(id_juego)
    print(f"ID asignado: {id_juego}")

    nombre = input('Escriba su nombre: ')
    while not nombre.isalpha() or len(nombre) > 30:
        nombre = input('Reescriba su nombre (maximo 30 caracteres): ')
    lista.append(nombre)

    empresa = input('Escriba su empresa: ')
    empresas_validas = ["Namco", "Taito", "Nintendo", "Atari", "Sega", "Konami", "Capcom", "Epic Games"]
    while empresa not in empresas_validas:
        empresa = input(f"Reescriba su empresa (validas: {', '.join(empresas_validas)}): ")
    lista.append(empresa)

    anio = input('Escriba el año: ')
    while not anio.isdigit() or not (1978 <= int(anio) <= 2024):
        anio = input('Reescriba el año (entre 1978 y 2024): ')
    lista.append(int(anio))

    genero = input('Escriba el genero del juego: ')
    generos_validos = ["Laberinto", "Puzzle", "Plataformas", "Peleas", "Matamarcianos", "Disparos", "Carreras"]
    while genero not in generos_validos:
        genero = input(f"Reescriba el genero (validos: {', '.join(generos_validos)}): ")
    lista.append(genero)

    nuevo_juego = {
        "id": lista[0],
        "nombre": lista[1],
        "empresa": lista[2],
        "anio": lista[3],
        "genero": lista[4]
    }

    datos.append(nuevo_juego)
    print("Juego agregado correctamente.")
    return datos

def listar_id(datos:list):
    ids = [juego['id'] for juego in datos['juegos']]
    nombres = [juego['nombre'] for juego in datos['juegos']]

    for i in range(len(ids)):
        print(f'ID: {ids[i]}, nombre: {nombres[i]}')

def modificar_lista(datos:list):
    listar_id(datos)

    id_juego_modificar = input('Ingrese el ID del juego a modificar: ')
    juego_encontrado = None

    for juego in datos:
        if juego['id'] == int(id_juego_modificar):
            juego_encontrado = juego
            break
    
    if juego_encontrado:
        print(f'El juego seleccionado es {juego_encontrado['nombre']}')
        print(f'Seleccionar la opcion numerica que desea cambiar')
        print(f'1. Nombre')
        print(f'2. Empresa')
        print(f'3. Anio')
        print(f'4. Genero')
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            while not nuevo_nombre.isalpha() or len(nuevo_nombre) > 30:
                nuevo_nombre = input('Nombre invalido. Reescriba su nombre: ')
            juego_encontrado['nombre'] = nuevo_nombre
        elif opcion == '2':
            nueva_empresa = input("Ingrese la nueva empresa: ")
            empresas_validas = ["Namco", "Taito", "Nintendo", "Atari", "Sega", "Konami", "Capcom", "Epic Games"]
            while nueva_empresa not in empresas_validas:
                nueva_empresa = input(f"Reescriba su empresa (válidas: {', '.join(empresas_validas)}): ")
            juego_encontrado['empresa'] = nueva_empresa
        elif opcion == '3':
            nuevo_anio = input("Ingrese el nuevo año: ")
            while not nuevo_anio.isdigit() or not (1978 <= int(nuevo_anio) <= 2024):
                nuevo_anio = input('Reescriba el año (entre 1978 y 2024): ')
            juego_encontrado['anio'] = int(nuevo_anio)
        elif opcion == '4':
            nuevo_genero = input("Ingrese el nuevo genero: ")
            generos_validos = ["Laberinto", "Puzzle", "Plataformas", "Peleas", "Matamarcianos", "Disparos", "Carreras"]
            while nuevo_genero not in generos_validos:
                nuevo_genero = input(f"Reescriba el genero (válidos: {', '.join(generos_validos)}): ")
            juego_encontrado['genero'] = nuevo_genero

        print("Juego modificado.")
    else:
        print("ID de juego no encontrado.")

# archivo = 'C:/Users/marce/Desktop/UTNFRA/Programacion 1/simulacro_parcial/data.json'   
# datos = importar_data(archivo)
# listar_id(datos)      

def imprimir_menu():
    print("""
        ====MENU====
Ingresar opción:
A – Cargar el archivo data.json.
B – Alta de datos con sus respectivas validaciones
C – Modificar datos: Listar id y nombre de todos los juegos, luego buscarlo por id y realizar la
modificación del nombre, la empresa o el año del juego (Realizar un submenú).
D – Borrar datos: Listar id y nombre de todos los juegos, luego buscarlo por id y realizar la baja
correspondiente.
E – Listar todos los datos, formateados de la siguiente manera:
Nombre | Género | Año | Empresa
F – Salir
    """)

def simulacro_menu_principal():
    imprimir_menu()
    opcion = input('Escriba su opción: ')

    while not opcion.isalpha():
        opcion = input('Re-escriba su opción: ')

    return opcion

def app_simulacro(archivo):
    continuar = True
    carga_datos = False
    datos = []
    
    while continuar:
        opcion = simulacro_menu_principal()
        match opcion.upper():
            case 'A':
                datos = importar_data(archivo)
                carga_datos = True
                print('Carga hecha')
            case 'B':
                if not carga_datos:
                    print('Primero debes cargar los datos')
                else:
                    datos = simulacro_alta_juegos(datos)
            case 'C':
                if not carga_datos:
                    print('Primero debes cargar los datos')
                else:
                    modificar_lista(datos)
            case 'D':
                if not carga_datos:
                    print('Primero debes cargar los datos')
                else:
                    pass
            case 'E':
                if not carga_datos:
                    print('Primero debes cargar los datos')
                else:
                    pass
            case 'F':
                print('Saliendo del programa')
                continuar = False
            case _:
                print('Opción no válida')


archivo = 'C:/Users/marce/Desktop/UTNFRA/Programacion 1/simulacro_parcial/data.json'
app_simulacro(archivo)