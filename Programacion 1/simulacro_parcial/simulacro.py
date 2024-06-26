#Apellido y nombre: Terrone Marcelo
#Division: 212
#Fecha: 11/06/2024
#Asignatura: Programacion 1
#Instancia: Primer examen parcial

import json
archivo = 'C:/Users/marce/Desktop/UTNFRA/Programacion 1/simulacro_parcial/data.json'

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
    return datos['juegos']

#lista = importar_data(archivo)

def validacion_datos(datos:dict, parametro:str):
    '''
    Valida los datos con sus respectivas normas

    Args:
    Datos: diccionario perteneciente a cada juego.
    Parametro: string dependiendo que se desea validar, nombre, empresa, genero, anio
    
    '''
    if parametro == 'nombre':
        nombre_nuevo = input('Escriba el nombre del juego: ')
        while len(nombre_nuevo) < 30 and nombre_nuevo.isalpha() == False:
            nombre_nuevo = input('Re escriba el nombre del juego (maximo 30 letras): ')
        datos['nombre'] = nombre_nuevo
    elif parametro == 'empresa':
        empresas_validas = ['Namco', 'Taito', 'Nintendo', 'Atari', 'Sega', 'Konami', 'Capcom', 'Epic Games']
        empresa_nueva = input('Escriba el nombre de la empresa: ')
        while empresa_nueva not in empresas_validas:
            empresa_nueva = input('Re escriba el nombre de la empresa: ')
        datos['empresa'] = empresa_nueva
    elif parametro == 'anio':
        anio_nuevo = input('Ingrese el año del juego: ')
        while not anio_nuevo.isdigit() or not (1978 <= int(anio_nuevo) <= 2024):
            anio_nuevo = input('Anio no valido (1978-2024): ')
        datos['anio'] = anio_nuevo
    elif parametro == 'genero':
        generos_validos = ['Laberinto', 'Puzzle', 'Plataformas', 'Peleas', 'Matamarcianos', 'Disparos', 'Carreras']
        genero_nuevo = input('Ingrese el genero de su juego: ')
        while genero_nuevo not in generos_validos:
            genero_nuevo = input('Re ingrese el genero de su juego: ')
        datos['genero'] = genero_nuevo

def alta_datos(lista:list):
    '''
    Permite agregar juegos a la lista importada
    La función empieza agregando un ID autoincremental a partir de la longitud de la lista y le suma de a uno, luego empieza a validar los nombres, años, empresas y generos permitidos, una vez cargado los datos crea un nuevo diccionario llamado "juego" con los datos del nuevo juego justamente y este lo agrega a la lista importada que contiene todos los demas diccionarios.

    Args:
    La lista importada desde el JSON

    Return:
    No debe de retornar nada
    '''

    #Empiezan las validaciones
    respuesta = True
    id_esperado = len(lista) + 1
    nuevo_juego = {'id': id_esperado}
    #print(id_esperado)
    while respuesta:
        validacion_datos(nuevo_juego, 'nombre')
        validacion_datos(nuevo_juego, 'empresa')
        validacion_datos(nuevo_juego, 'anio')
        validacion_datos(nuevo_juego, 'genero')
        print(nuevo_juego)

        lista.append(nuevo_juego)
        
        respuesta_seguir = input('¿Desea continuar agregando juegos? (si/no): ')
        if respuesta_seguir.lower() == 'no':
            break
        id_esperado += 1
    return lista
        
    

def listar_juegos(lista:list, argumento:str):
    '''
    La función imprime la lista de juegos dependiendo del argumento que se le atribuye, si necesitamos solo borrar o modificar solo listaria el ID y nombre del juego ya que no interesa los demas datos, en cambio si queremos imprimirla para ver que contiene la lista, imprimira todos los datos del diccionario.

    Args:
    Lista importada del JSON y argumento pasado por parametro.

    Return:
    Retorna el print de la lista que desee imprimir por pantalla
    '''
    retorno = False
    if len(lista) > 0:
        if argumento == 'modificar_borrar':
            claves = ['id', 'nombre'] #Defino solo las claves que quiero imprimir cuando se quiera borrar o modificar un juego
            encabezado = " | ".join(claves)
            print(encabezado)

            for juego in lista:
                mensaje = ""
                for clave in claves:
                    if clave in juego:
                        mensaje += f"{juego[clave]:2} | " # Ajusto el formato con dos espacios vacios de caracteres para la izquierda
                print(mensaje)

        elif argumento == 'listar_juegos':
            claves = lista[0].keys()
            encabezado = " | ".join(claves)
            print(encabezado)

            for heroes in lista:
                mensaje = ""
                for datos in heroes:
                    # para nombre 20, para identidad 25 y para el resto 15     
                    mensaje += f"{heroes[datos]:2} | "
                print(mensaje)
    return retorno


def manipular_datos_juegos(lista:list, argumento:str):

    '''
    La funcion pide un ID para luego validar si ese ID pertenece a un juego, y mediante el argumento se decide si se borra o modifica un juego, en la modificacion se valida el campo que se desea cambiar, si lo borra pide una confirmacion mediante input y reestablece los IDs

    Args:
    Lista importada del JSON y argumento pasado por parametro al llamar la funcion

    Return:
    No retorna nada   
    '''
    listar_juegos(lista, "modificar_borrar")
    
    id_juego_modificar = input(f'Escriba el ID del juego a {argumento}: ')

    while id_juego_modificar.isdigit() == False:
        print('ID inexistente')
        id_juego_modificar = input(f'Re escriba el ID del juego a {argumento}r: ')
    id_juego_modificar = int(id_juego_modificar)
    encontrar_id = False

    for juego in lista:
        if juego['id'] == id_juego_modificar:
            encontrar_id = True
            if argumento == 'modificar':
                    print(f'Usted va a modificar: {juego['nombre']} ')
                    respuesta = True
                    while respuesta:
                        opcion = int(input(f'Que desea modificar? ( 1)nombre/ 2)empresa/ 3)anio 4) salir)'))
                        match opcion:
                            case 1:
                                validacion_datos(juego, 'nombre')
                            case 2:
                                validacion_datos(juego, 'empresa')
                            case 3:
                                validacion_datos(juego, 'anio')
                            case 4:
                                respuesta = False
                                break
                            case _:
                                print('Opcion incorrecta')
                        print('juego modificado exitosamente!')
            elif argumento == 'borrar':
                confirmacion = input(f"Esta seguro que desea eliminar a {juego['nombre']}? S/N: ")
                if confirmacion.upper() == "S":
                    lista.remove(juego)
                    nuevo_id = 1
                    print(f'El juego {juego['nombre']} ha sido eliminado exitosamente!')
                    for juego in lista:
                        juego['id'] = nuevo_id
                        nuevo_id += 1
                elif confirmacion == "N":
                    print(f'No se ha borrado {juego['nombre']}')
    if encontrar_id == False:
        print('ID NO ENCONTRADO')

# 2 
# F – Hacer un submenú que realice lo siguiente:

#1) Listar por pantalla los juegos cuyo género sea Peleas.
def listar_genero(lista:list, argmt:str, parametro:str):
    '''
    La funcion se encarga de filtrar el genero especifico que se pase por parametro y agregarlo a la lista genero_de_tipo.

    Args: 
    lista: la lista con los juegos. 
    argmt: Es el genero del juego en especifico que se desea filtar.
    parametro: El parametro por si en un futuro se desea guardar o no la lista en un tipo de formato especifico.

    Return:
    Retorna la lista filtrada con el genero deseado   
    '''
    retorno = False
    genero_de_tipo = []
    for juego in lista:
        if juego['genero'] == argmt:
            genero_de_tipo.append(juego)
    if parametro == 'no_guardar':
        retorno = listar_juegos(genero_de_tipo, 'listar_juegos')
    elif parametro == 'guardar':
        retorno = genero_de_tipo

    return retorno


#2) Calcular  y  mostrar  la  cantidad  de  juegos  de  un  rango  de  años  determinado  (año  desde  y  año  hasta),  el mismo será ingresado por el usuario por consola.

# def hallar_rango_anios_desde():
#     desde = input('Desde que anio desea buscar? ')
#     while not desde.isdigit() or not (1978 <= int(desde) <= 2024):
#         desde = input('Re escriba desde que anio desea buscar? ')
#     desde = int(desde)
#     return desde

# def hallar_rango_anios_hasta():
#     hasta = input('Hasta que anio desea buscar? ')
#     while not hasta.isdigit() or not (1978 <= int(hasta) <= 2024):
#         hasta = input('Re escriba desde que anio desea buscar? ')
#     hasta = int(hasta)
#     return hasta

def calcular_contador(lista:list):
    '''
    La funcion calcula cuantos juegos existen en el rango de tiempo pedido por input, pregunta desde  y hasta que anio se desea consultar la cantidad validando que si o si sea un numero y se encuentre en el rango de anios correspondientes, recorre la lista y si en el rango pasado por input hay juegos suma uno al contador

    args: 
    lista: lista de juegos

    return: retorna un mensaje con el contador de juegos hallado
    '''

    desde = input('Desde que anio desea buscar? ')
    while not desde.isdigit() or not (1978 <= int(desde) <= 2024):
        desde = input('Re escriba desde que anio desea buscar? ')
    desde = int(desde)
    hasta = input('Hasta que anio desea buscar? ')
    while not hasta.isdigit() or not (1978 <= int(hasta) <= 2024):
        hasta = input('Re escriba desde que anio desea buscar? ')
    hasta = int(hasta)
    contador = 0 

    for juego in lista:
        if desde <= juego['anio'] <= hasta:
            contador += 1
    return(print(f'La cantidad de juegos en el rango {desde} - {hasta} es de: {contador}'))


# lista = importar_data(archivo)
# stark_normalizar_datos(lista)
# calcular_contador(lista)

# 3) Listar  todos  los  juegos  ordenados  por  Empresa.  Preguntar  al  usuario  si  lo  quiere  ordenar  de  manera ascendente (‘asc’)  o  descendente  (‘desc’). Este ítem debe ser realizado por el algoritmo de ordenamiento bubble sort (burbujeo).

def validar_sub_menu()-> str:
    '''
    La funcion valida que el input escrito sea si o si ASC o DESC para ordenar la lista luego

    return: 
    retorna en una variable el input pasado anteriormente
    '''
    argumento = input('Como desea ordenar la lista?')
    while argumento.upper() != 'ASC' and argumento.upper() != 'DESC':
        argumento = input('Como desea ordenar la lista? ASC o DESC')
    return argumento


def ordenar_lista_por_parametro(lista: list, criterio:str, parametro:str):
    """
    Ordena la lista recibida por parametro con el criterio "ASC" o "DESC" tambien recibido por parametro.

    args:
    lista: lista de juegos
    criterio: str con criterio ASC o DESC
    parametros: que se desea ordenar

    return:
    retorna la lista ordenada
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if (criterio == "ASC" and lista[i][parametro] > lista[j][parametro]) or (criterio == "DESC" and lista[i][parametro] < lista[j][parametro]):
                    # Swap
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista

def menu_ordenamiento(lista:list, parametro:str):
    '''
    La funcion es un menu para preguntar por argumento como se desea ordenar

    Args:
    lista: lista de juegos
    parametro: si se desea guardar o no el ordenamiento
    
    return 
    retorna la lista ordenada
    
    '''
    argumento = validar_sub_menu()
    ordenar_lista_por_parametro(lista, argumento.upper(), 'empresa')
    if parametro == 'no_guardar':
        retorno = listar_juegos(lista, 'listar_juegos')
    elif parametro == 'guardar':
        retorno = ordenar_lista_por_parametro(lista, argumento.upper(), 'empresa')
                       
    return retorno

#print(menu_ordenamiento(lista, 'guardar'))

#4) Exportar a JSON la lista de juegos de acuerdo a la opción F 1.

def guardar_json(lista:list, nombre_archivo: str):
    with open(f'C:/Users/marce/Desktop/UTNFRA/Programacion 1/simulacro_parcial/{nombre_archivo}.json', "w") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)
        print("Guardado exitoso")

#5) Exportar a CSV la lista de juegos de acuerdo a la opción F 3

def guardar_csv(lista:list, nombre_archivo:str):
    with open(f'C:/Users/marce/Desktop/UTNFRA/Programacion 1/simulacro_parcial/{nombre_archivo}.csv',"w") as archivo:
        archivo.write(f'Nombre, empresa, anio, genero,\n')
        for diccionario in lista:
            archivo.write(f'{diccionario['nombre']},{diccionario['empresa']},{diccionario['anio']},{diccionario['genero']}, \n')
        print("Guardado exitoso")



def imprimir_sub_menu():
    submenu = print("""
        ====SUBMENU====
Ingresar opcion:
1) Listar por pantalla los juegos cuyo género sea Peleas.
2) Calcular  y  mostrar  la  cantidad  de  juegos  de  un  rango  de  años  determinado  (año  desde  y  año  hasta),  el  mismo será ingresado por el usuario por consola.
3) Listar  todos  los  juegos  ordenados  por  Empresa.  Preguntar  al  usuario  si  lo  quiere  ordenar  de  manera ascendente (‘asc’)  o  descendente  (‘desc’). Este ítem debe ser realizado por el algoritmo de  ordenamiento bubble sort (burbujeo).
4) Exportar a JSON la lista de juegos de acuerdo a la opción F 1.
5) Exportar a CSV la lista de juegos de acuerdo a la opción F 3
6) Salir
        """)
    
def submenu_opcion():
    imprimir_sub_menu()
    opcion = int(input('Escriba su opcion: '))
    return opcion

def submenu_principal():
    lista = importar_data(archivo)
    continuar = True
    while continuar:
        submenu = submenu_opcion()
        match submenu:
            case 1:
                listar_genero(lista, 'Peleas', 'no_guardar')
            case 2:
                normalizar_datos(lista)
                calcular_contador(lista)
            case 3:
                menu_ordenamiento(lista, 'no_guardar')
            case 4:
                guardar_json(listar_genero(lista, 'Peleas', 'guardar'), 'lista_juegos_peleas')
            case 5:
                guardar_csv(menu_ordenamiento(lista, 'guardar'), 'lista_ordenada_empresas')
                pass
            case 6:
                print('Saliendo del submenu')
                continuar = False
                break
            case _:
                print('Opcion no valida')




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
F – Submenu
G - Salir
        """)
    return menu

def simulacro_menu_principal():
    imprimir_menu()
    opcion = input('Escriba su opcion: ')
    return opcion.upper()




