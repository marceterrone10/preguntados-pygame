import json
archivo = 'C:/Users/marce/Desktop/UTNFRA/Programacion 1/para_practicar/data.json'

def importar_data(nombre_archivo:str):
    '''
    Importa los datos del archivo externo al programa de salida .json
    Primero la funcion abre el archivo a partir del parametro pasado, lo lee y carga los datos a la variable datos
    
    Arg:
    El nombre del archivo, en este caso puede ser utilizado como una variable que contiene la ruta del archivo .json o mismo pasar la ruta de ese archivo como parametro ya que esta en modo str

    Return:
    Retornara la lista que contiene el archivo .json
    '''

    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
        datos_juegos= datos['juegos']
    return datos_juegos


def alta_datos(lista:list):
    '''
    Permite agregar juegos a la lista importada
    La función empieza agregando un ID autoincremental a partir de la longitud de la lista y le suma de a uno, luego empieza a validar los nombres, años, empresas y generos permitidos, una vez cargado los datos crea un nuevo diccionario llamado "juego" con los datos del nuevo juego justamente y este lo agrega a la lista importada que contiene todos los demas diccionarios.

    Args:
    La lista importada desde el JSON

    Return:
    No debe de retornar nada
    '''


    empresas_validas = ['Namco', 'Taito', 'Nintendo', 'Atari', 'Sega', 'Konami', 'Capcom', 'Epic Games']
    generos_validos = ['Laberinto', 'Puzzle', 'Plataformas', 'Peleas', 'Matamarcianos', 'Disparos', 'Carreras']

    #Empiezan las validaciones
    respuesta = True
    id_esperado = len(lista) + 1
    #print(id_esperado)
    while respuesta:
        nombre = input('Escriba el nombre del juego: ')
        while len(nombre) < 30 and nombre.isalpha() == False:
            nombre = input('Re escriba el nombre del juego (maximo 30 letras): ')

        empresa = input('Escriba el nombre de la empresa: ')
        while empresa not in empresas_validas:
            empresa = input('Re escriba el nombre de la empresa: ')
        
        anio = input('Ingrese el año del juego: ')
        while not anio.isdigit() or not (1978 <= int(anio) <= 2024):
            anio = input('Anio no valido (1978-2024): ')

        genero = input('Ingrese el genero de su juego: ')
        while genero not in generos_validos:
            genero = input('Re ingrese el genero de su juego: ')

        
        juego = {
            "id": id_esperado,
            "nombre": nombre,
            "empresa": empresa,
            "anio": anio,
            "genero": genero
        }

        lista.append(juego)

        respuesta_seguir = input('¿Desea continuar agregando juegos? (si/no): ')
        if respuesta_seguir.lower() == 'no':
            break
        id_esperado += 1
    

def listar_juegos(lista:list, argumento:str):
    '''
    La función imprime la lista de juegos dependiendo del argumento que se le atribuye, si necesitamos solo borrar o modificar solo listaria el ID y nombre del juego ya que no interesa los demas datos, en cambio si queremos imprimirla para ver que contiene la lista, imprimira todos los datos del diccionario.

    Args:
    Lista importada del JSON y argumento pasado por parametro.

    Return:
    Retorna el print de la lista que desee imprimir por pantalla
    '''
    # for juego in lista:
    #     if argumento == 'modificar_borrar':
    #         listado_juegos = print(f"{juego['id']} | {juego['nombre']}")
    #     elif argumento == 'listar_juegos':
    #         listado_juegos = print(f"{juego['id']} | {juego['nombre']} | {juego['empresa']} | {juego['anio']} | {juego['genero']}")

    # return listado_juegos
    retorno = False
    if argumento == 'modificar_borrar':
        if len(lista) > 0:
            # Definir las claves que deseas imprimir
            claves = ['id', 'nombre']
            encabezado = " | ".join(claves)
            print(encabezado)

            for juego in lista:
                mensaje = ""
                for clave in claves:
                    # Ajustar el formato para id y nombre
                    if clave in juego:
                        mensaje += f"{juego[clave]:<2} | " 
                print(mensaje)

    elif argumento == 'listar_juegos':
        claves = lista[0].keys()
        encabezado = " | ".join(claves)
        print(encabezado)

        for heroes in lista:
            mensaje = ""
            for datos in heroes:
                # para nombre 20, para identidad 25 y para el resto 15     
                mensaje += f"{heroes[datos]:<2} | "
            print(mensaje)
        
    
    return retorno


def manipular_datos_juegos(lista:list, argumento:str):
    listar_juegos(lista, "modificar_borrar")
    
    id_juego_modificar = input(f'Escriba el ID del juego a {argumento}: ')

    while id_juego_modificar.isdigit() == False:
        print('ID inexistente')
        id_juego_modificar = input(f'Re escriba el ID del juego a {argumento}r: ')
    id_juego_modificar = int(id_juego_modificar)
    encontrar_id = False

    for juego in lista:
        empresas_validas = ['Namco', 'Taito', 'Nintendo', 'Atari', 'Sega', 'Konami', 'Capcom', 'Epic Games']
        if argumento == 'modificar':
            if juego['id'] == id_juego_modificar:
                print(f'Usted va a modificar: {juego['nombre']} ')
                encontrar_id = True
                respuesta = True
                while respuesta:
                    opcion = int(input(f'Que desea modificar? ( 1)nombre/ 2)empresa/ 3)anio 4) salir)'))
                    match opcion:
                        case 1:
                            nuevo_nombre = input('Ingrese el nuevo nombre: ')
                            while len(nuevo_nombre) < 30 and nuevo_nombre.isalpha() == False:
                                nuevo_nombre = input('Re ingrese el nuevo nombre(maximo 30 letras): ') 
                            juego['nombre'] = nuevo_nombre
                        case 2:
                            nueva_empresa = input('Ingrese el nombre de la empresa: ')
                            while not nueva_empresa in empresas_validas:
                                nueva_empresa = input('Re ingrese el nombre de la empresa: ')
                            juego['empresa'] = nueva_empresa
                        case 3:
                            nuevo_anio = input('Ingrese el anio del juego: ')
                            while not nuevo_anio.isdigit() or not (1978 <= int(nuevo_anio) <= 2024):
                                nuevo_anio = input('Anio no valido (1978-2024): ')
                            juego['anio'] = nuevo_anio
                        case 4:
                            respuesta = False
                            break
                        case _:
                            print('Opcion incorrecta')

                    print('juego modificado exitosamente!')
        elif argumento == 'borrar':
            if juego['id'] == id_juego_modificar:
                confirmacion = input(f"Esta seguro que desea eliminar a {juego['nombre']}? S/N: ")
                if confirmacion == "S":
                    encontrar_id = True
                    lista.remove(juego)
                    nuevo_id = 1
                    for juego in lista:
                        juego['id'] = nuevo_id
                        nuevo_id += 1 #recorre los IDS de juego y los reemplaza por nuevo_id que es 1 y va sumando de a uno
                    break
                elif confirmacion == "N":
                        print(f'No se ha borrado {juego['nombre']}')
    if encontrar_id == False:
        print('ID NO ENCONTRADO')


def ordenar_lista_por_parametro(lista: list, criterio:str, parametro:str):
    """
    Ordena la lista recibida por parametro con el criterio "ASC" o "DESC" tambien recibido por parametro.
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if (criterio == "ASC" and lista[i][parametro] > lista[j][parametro]) or (criterio == "DESC" and lista[i][parametro] < lista[j][parametro]):
                    # Swap
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

    return lista


def validar_sub_menu()-> str:
    argumento = input('Como desea ordenar la lista?')
    while argumento.upper() != 'ASC' and argumento.upper() != 'DESC':
        argumento = input('Como desea ordenar la lista? ASC o DESC')
    return argumento

def menu_ordenamiento(lista:list):

    sub_menu = print('Como desea ordenar los juegos:\n 1. Nombre\n 2. Empresa\n 3. Anio de lanzamiento\n 4. Genero')
    opcion_ordenar = input('Escriba su opcion: ')

    while opcion_ordenar.isdigit() == False:
        print('Opcion invalida')
        opcion_ordenar = input('Re escriba su opcion: ')
    opcion_ordenar = int(opcion_ordenar)
    encontrar_opcion = False
    match opcion_ordenar:
        case 1:
            encontrar_opcion == True
            argumento = validar_sub_menu()
            ordenar_lista_por_parametro(lista, argumento, 'nombre')
            retorno = listar_juegos(lista, 'listar_juegos')
        case 2:
            encontrar_opcion == True
            argumento = validar_sub_menu()
            ordenar_lista_por_parametro(lista, argumento, 'empresa')
            retorno = listar_juegos(lista, 'listar_juegos')
        case 3:
            encontrar_opcion == True
            argumento = validar_sub_menu()
            ordenar_lista_por_parametro(lista, argumento, 'anio')
            retorno = listar_juegos(lista, 'listar_juegos')
        case 4:
            encontrar_opcion == True
            argumento = validar_sub_menu()
            ordenar_lista_por_parametro(lista, argumento, 'genero')
            retorno = listar_juegos(lista, 'listar_juegos')
        case _:
            retorno = print('Opcion invalida')                           
    return retorno

def buscar_juego_titulo(lista:list):
    while True:
        buscador = input('Escriba el juego que desea encontrar: ')
        encontrar_juego = False
        for juego in lista:
            if buscador == juego['nombre']:
                mensaje = print(f'ID: {juego['id']}, Nombre: {juego['nombre']}, Empresa: {juego['empresa']}, Anio de lanzamiento: {juego['anio']}, Genero: {juego['genero']}')
                encontrar_juego = True
                break
        if encontrar_juego == False:
            mensaje = print('Juego no encontrado')
    
        return mensaje
    

def normalizar_datos(lista:list) -> bool:
    """
    Recibe una lista de personajes, modifica los datos numericos a su respectivo tipo de dato y luego retorna un booleano.
    Recibe una lista de tipo lista
    Retorna un booleano "True" si el dato pudo ser modificado, de lo contrario retornara "False"
    """
    retorno = False
    if len(lista) > 0:
        for juego in lista:
            if type(juego['anio']) != int:
                juego['anio'] = int(juego['anio'])
                retorno = True
    return retorno

def sumar_dato(lista:list, key:str):
    acumulador = 0
    for juego in lista: #se recorre la lista para acceder a cada diccionario de los heroes
        if type(juego) == dict and len(juego) > 0: #se valida que el tipo heroe sea un diccionario y que este no este vacio
            valor = juego[key]
            if type(valor) == float or type(valor) == int:
                acumulador += valor
    return acumulador



def dividir(dividendo, divisor):
    if divisor == 0:
        retorno = False
    else:
        retorno = dividendo / divisor
    return retorno


def calcular_promedio(lista:list, key:str):

    if len(lista) == 0:
        promedio = print('No se pudo calcular el promedio')
    
    sumatoria_total = sumar_dato(lista,key)

    cantidad_juegos = len(lista) #hallar el divisor, la cantidad de diccionarios totales(heroes) en la lista

    promedio = dividir(sumatoria_total, cantidad_juegos)
    

    return promedio


def mostrar_promedio_dato(lista:list, key:str):

    if (type(key) != int or type(key) != float) and (len(lista) == 0):
        resultado = False
    else:
        resultado = calcular_promedio(lista, key)

    return print(resultado)

def calcular_contador_genero(lista: list):
    generos_validos = ['Laberinto', 'Puzzle', 'Plataformas', 'Peleas', 'Matamarcianos', 'Disparos', 'Carreras']
    genero_pedido = input('Ingrese el genero que desea calcular el porcentaje: ')
    while genero_pedido not in generos_validos:
        genero_pedido = input('Re ingrese el genero que desea calcular el porcentaje: ')
    
    contador = 0

    for juego in lista:
        if 'genero' in juego and genero_pedido == juego['genero']:
            contador += 1
    
    print(f'Cantidad de juegos del género {genero_pedido}: {contador}')
    return contador

def calcular_porcentaje(lista: list):
    contador_total_lista = len(lista)
    contador_genero = calcular_contador_genero(lista)
    division = dividir(contador_genero, contador_total_lista)

    if division is False:
        mensaje = print('Error')
    else:
        porcentaje = division * 100
        mensaje = print(f'El porcentaje es de {porcentaje}%')

    return mensaje



def imprimir_menu():
    '''
    La función imprime el MENU de opciones del ejercicio
    Return:
    Retornara el print del MENU
    '''
    menu = print("""
        ====MENU====
Ingresar opcion:
A – Cargar el archivo data.json.
B – Alta de datos con sus respectivas validaciones.
C – Modificar datos: Listar id y nombre de todos los juegos, luego buscarlo por id y realizar la modificación del nombre, la empresa o el año del juego (Realizar un submenú).
D – Borrar datos: Listar id y nombre de todos los juegos, luego buscarlo por id y realizar la baja correspondiente.
E – Listar todos los datos, formateados de la siguiente manera: Nombre | Género | Año | Empresa
F - Usar ordenamiento burbuja para ordenar los juegos ASC o DESC depende como lo quiera el usuario, hacer un submenu numerico que pregunte que desea ordenar
    1. Nombre.
    2. Empresa.
    3. Año de lanzamiento.
    4. Genero
G - pedir al usuario que ingrese un juego, localizarlo y imprimir la info de ese juego
H - calcular promedio de anio de lanzamiento de los juegos
I - calcular porcentaje de los generos de juegos, pedir el genero por input al usuario
J – Salir
        """)
    return menu

def simulacro_menu_principal():
    imprimir_menu()
    opcion = input('Escriba su opcion: ')
    return opcion.upper()




#print(importar_data(archivo))

