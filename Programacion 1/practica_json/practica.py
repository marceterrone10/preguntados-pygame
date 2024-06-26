import json
nombre_archivo = 'C:/Users/marce/Desktop/UTNFRA/Programacion 1/practica_json/data.json'


def cargar_info(nombre_archivo:str):
    with open(nombre_archivo, 'r') as file:
        datos = json.load(file)
    
    return datos['Personas']

# print(cargar_info(nombre_archivo))

def modificar_json(nombre_archivo:str, lista:list):
    with open(nombre_archivo, 'w') as file:
        json.dump({'Personas': lista}, file, indent=4, ensure_ascii=False)


def normalizar_datos(lista:list) -> bool:
    """
    Recibe una lista de personajes, modifica los datos numericos a su respectivo tipo de dato y luego retorna un booleano.
    Recibe una lista de tipo lista
    Retorna un booleano "True" si el dato pudo ser modificado, de lo contrario retornara "False"
    """
    retorno = False
    if len(lista) > 0:
        for persona in lista:
            if type(persona['anio']) != int:
                persona['anio'] = int(persona['anio'])
                retorno = True
            if type(persona['legajo']) != int:
                persona['legajo'] = int(persona['legajo'])
                retorno = True
        modificar_json(nombre_archivo, lista)
    return retorno

def validacion_datos(datos:dict, campo:str):
    if campo == 'nombre':
        nombre_nuevo = input('Ingrese un nuevo nombre: ')
        while nombre_nuevo.isalpha() == False and len(nombre_nuevo) < 30:
            nombre_nuevo = input('Re ingrese un nuevo nombre: ')
        datos['nombre'] = nombre_nuevo
    elif campo == 'genero':
        genero_nuevo = input('Ingrese un genero nuevo: ')
        while genero_nuevo != 'NB' and genero_nuevo != 'F' and genero_nuevo != 'M':
            genero_nuevo = input('Re ingrese un genero nuevo: ')
        datos['genero'] = genero_nuevo
    elif campo == 'legajo':
        legajo_nuevo = input('Ingrese un legajo nuevo: ')
        while not legajo_nuevo.isdigit() or not (1000 <= int(legajo_nuevo) <= 1999):
            legajo_nuevo = input('Reingrese un legajo válido (1000-1999): ')
        legajo_nuevo = int(legajo_nuevo)
        datos['legajo'] = legajo_nuevo
    elif campo == 'anio':
        nacimiento_nuevo = input('Ingrese un nacimiento nuevo: ')
        while not nacimiento_nuevo.isdigit() or not (1978 <= int(nacimiento_nuevo) <= 2005):
            nacimiento_nuevo = input('Re ingrese un nacimiento nuevo: ')
        nacimiento_nuevo = int(nacimiento_nuevo)
        datos['anio'] = nacimiento_nuevo
    
    
def alta_datos(lista:list):
    id_nuevo = len(lista) + 1
    nueva_persona = {'id': id_nuevo}
    
    validacion_datos(nueva_persona, 'nombre')
    validacion_datos(nueva_persona, 'genero')
    validacion_datos(nueva_persona, 'anio')
    validacion_datos(nueva_persona, 'legajo')

    lista.append(nueva_persona)
    id_nuevo += 1
    modificar_json(nombre_archivo, lista)
    return print(lista)

def listar_juegos(lista:list, argumento:str):
    '''
    La función imprime la lista de juegos dependiendo del argumento que se le atribuye, si necesitamos solo borrar o modificar solo listaria el ID y nombre del juego ya que no interesa los demas datos, en cambio si queremos imprimirla para ver que contiene la lista, imprimira todos los datos del diccionario.

    Args:
    Lista importada del JSON y argumento pasado por parametro.

    Return:
    Retorna el print de la lista que desee imprimir por pantalla
    '''
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


def modificar_datos(lista:list, argumento:str):
    listar_juegos(lista, 'modificar_borrar')

    persona_a_modificar = input(f'Escriba el id de la persona a {argumento}: ')
    while persona_a_modificar.isalpha() == True:
        persona_a_modificar = input(f'Re escriba el id de la persona a {argumento}: ')
    persona_a_modificar = int(persona_a_modificar)


    encontrar_persona = False
    for persona in lista:
        if persona['id'] == persona_a_modificar:
            encontrar_persona = True
            if argumento == 'modificar':
                print(f'Usted va a modificar a {persona['nombre']}')
                respuesta = True
                while respuesta:
                    opcion = int(input('Ingrese que desea cambiar: 1) nombre, 2) anio nacimiento, 3) legajo, 4) genero, 5) Salir'))
                    match opcion:
                        case 1:
                            validacion_datos(persona, 'nombre')
                        case 2:
                            validacion_datos(persona, 'anio')
                        case 3:
                            validacion_datos(persona, 'legajo')
                        case 4:
                            validacion_datos(persona, 'genero')
                        case 5:
                            respuesta = False
                            break
                        case _:
                            print('Opcion incorrecta')
                    modificar_json(nombre_archivo, lista)
            elif argumento == 'borrar':
                confirmacion = int(input(f'Desea borrar a {persona['nombre']}? 1) Si 2) No '))
                if confirmacion == 1:
                    lista.remove(persona)
                    nuevo_id = 1
                    print(f'{persona['nombre']} ha sido borrado de la lista')
                    for persona in lista:
                        persona['id'] = nuevo_id
                        nuevo_id += 1
                elif confirmacion == 2:
                    print(f'No se ha borrado a {persona['nombre']}')
                modificar_json(nombre_archivo, lista)

    if encontrar_persona == False:
        print('Persona INEXISTENTE')
        
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

    sub_menu = print('Como desea ordenar los juegos:\n 1. Nombre\n 2. Genero\n 3. Anio\n 4. Legajo')
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
            modificar_json(nombre_archivo, lista)
        case 2:
            encontrar_opcion == True
            argumento = validar_sub_menu()
            ordenar_lista_por_parametro(lista, argumento, 'genero')
            retorno = listar_juegos(lista, 'listar_juegos')
            modificar_json(nombre_archivo, lista)
        case 3:
            encontrar_opcion == True
            argumento = validar_sub_menu()
            ordenar_lista_por_parametro(lista, argumento, 'anio')
            retorno = listar_juegos(lista, 'listar_juegos')
            modificar_json(nombre_archivo, lista)
        case 4:
            encontrar_opcion == True
            argumento = validar_sub_menu()
            ordenar_lista_por_parametro(lista, argumento, 'legajo')
            retorno = listar_juegos(lista, 'listar_juegos')
            modificar_json(nombre_archivo, lista)
        case _:
            retorno = print('Opcion invalida')                           
    return retorno

def validacion_genero():
    genero = input('Ingrese el genero que desea calcular el promedio: ')
    while genero != 'NB' and genero != 'M' and genero != 'F':
        genero = input('Re ingrese el genero que desea calcular el promedio: ')
    
    return genero

def sumar_dato(lista:list):
    genero = validacion_genero()
    acumulador = 0
    for persona in lista:
        if type(persona) == dict and len(persona) > 0 and genero == persona['genero']:
            acumulador += 1
    
    return acumulador

def dividir(dividendo, divisor):
    if divisor == 0:
        retorno = False
    else:
        retorno = dividendo / divisor
    return retorno

def calcular_porcentaje(lista:list):
    if len(lista) < 0:
        print('No se pudo calcular el promedio')
    
    sumatoria_total = sumar_dato(lista)
    cantidad_juegos = len(lista)

    promedio = dividir(sumatoria_total, cantidad_juegos) * 100

    return print(f'El promedio es de {promedio} %')


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
C – Modificar datos: Listar nombre de las personas, luego buscarlo por nombre y realizar la modificación del nombre, genero o legajo (Realizar un submenú).
D – Borrar datos: Listar nombre de todas las personas, luego buscarlo por nombre y realizar la baja correspondiente.
E – Listar todos los datos, formateados de la siguiente manera: Nombre | Género | Año | Legajo
F - Usar ordenamiento burbuja ASC O DESC como quiera el usuario y preguntar que quiere ordenar
H - calcular promedio de anio de nacimiento de las personas
I - calcular porcentaje de los generos de personas, pedir el genero por input al usuario
J – Salir
        """)
    return menu

def simulacro_menu_principal():
    imprimir_menu()
    opcion = input('Escriba su opcion: ')
    return opcion.upper()


def simulacro_app_principal(lista:list):
    continuar = True
    personas = []
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
                    alta_datos(personas)
            case 'C':
                if retorno_importar_data == False:
                    print('Cargar datos para continuar.')
                else:
                    modificar_datos(personas, 'modificar')
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
            case 'H':
                if retorno_importar_data == False:
                    print('Cargar datos para continuar.')
                else:
                    calcular_porcentaje(personas)                 
            case 'J':
                print('Saliendo del programa')
                continuar = False
                break
            case _:
                print('Opcion no valida')
        

simulacro_app_principal(nombre_archivo)
