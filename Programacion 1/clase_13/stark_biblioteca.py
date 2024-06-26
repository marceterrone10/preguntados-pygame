# 0. Crear la función 'stark_normalizar_datos()' la cual recibirá por parámetro la
# lista de héroes. La función deberá:
# ● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
# las keys que representan datos numéricos) por ejemplo fuerza (int),
# altura (float), etc
# ● Validar primero que el tipo de dato no sea del tipo al cual será
# casteado. Por ejemplo si una key debería ser entero (ejemplo fuerza)
# verificar antes que no se encuentre ya en ese tipo de dato.
# ● Si al menos un dato fue modificado, la función deberá retornar el valor
# booleano True
# ● En caso de que la lista esté vacía o ya se hayan normalizado
# anteriormente los datos se deberá retornar el valor booleano False
# ● Crear una opción en el menú que me permita normalizar los datos (No
# se debería poder acceder a ninguna otra opción del menú hasta que
# los datos esten normalizados)
# ● En caso de que la llamada a la función retorne True mostrar un
# mensaje diciendo “Datos Normalizados” sino mostrar el mensaje
# “Hubo un error al normalizar los datos. Verifique que la lista no este
# vacía o que los datos ya no se hayan normalizado anteriormente”
from data_stark import lista_personajes


def stark_normalizar_datos(lista:list) -> bool:
    """
    Recibe una lista de personajes, modifica los datos numericos a su respectivo tipo de dato y luego retorna un booleano.
    Recibe una lista de tipo lista
    Retorna un booleano "True" si el dato pudo ser modificado, de lo contrario retornara "False"
    """
    retorno = False
    if len(lista) > 0:
        for heroe in lista:
            if type(heroe['peso']) != float:
                heroe['peso'] = float(heroe['peso'])
                retorno = True
            if type(heroe['fuerza']) != int:    
                heroe['fuerza'] = int(heroe['fuerza'])
                retorno = True
            if type(heroe['altura']) != float:    
                heroe['altura'] = float(heroe['altura'])
                retorno = True
            heroe['color_ojos'] = heroe['color_ojos'].capitalize()
            heroe['color_pelo'] = heroe['color_pelo'].capitalize()
    return retorno

# 1.1. Crear la función ”obtener_dato()” la cual recibirá por parámetro un
# diccionario el cual representara a un héroe y también recibirá un string que
# hace referencia a una “clave” del mismo
# Validar siempre que el diccionario no esté vacío y que el mismo tenga una key
# llamada “nombre”. Caso contrario la función retornara un False


def obtener_dato(personaje:dict, clave:str):
    retorno = False
    if len(personaje) > 0 and 'nombre' in personaje:
        retorno = personaje[clave]
    return retorno

def obtener_nombre(personaje:dict) -> str:
    nombre_nuevo = obtener_dato(personaje, 'nombre')

    if nombre_nuevo == False:
        mensaje = 'Error'
    else:
        mensaje = f'Nombre: {nombre_nuevo}'

    return mensaje


# Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
# diccionario el cual representara a un héroe y una key (string) la cual
# representará el dato que se desea obtener.
# ● La función deberá devolver un string el cual contenga el nombre y dato
# (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O
# CUALQUIER OTRO DATO.
# ● El string resultante debe estar formateado de la siguiente manera:
# (suponiendo que la key es fuerza)
# Nombre: Venom | fuerza: 500
# ● Validar siempre que la lista no este vacía. Caso contrario la función
# retornara un False

def obtener_nombre_y_dato(personaje: dict, key: str):

    retorno = False

    datos = obtener_dato(personaje, key)

    nombre = obtener_nombre(personaje)

    if datos != False and nombre != False: #
        retorno = f"{nombre} | {key}: {datos}"
        
    return retorno 

print(obtener_nombre_y_dato(lista_personajes[1], "altura"))

# 3.1 Crear la función “obtener_maximo()” la cual recibirá como parámetro una lista y
# una key (string) la cual representará el dato al cual se le debe calcular su cantidad
# MÁXIMA.
# ● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
# un int o un float. Caso contrario la función retornara un False
# ● En caso de que el dato que se está buscando en el diccionario es de tipo int o
# float retornar el mayor que haya encontrado en la búsqueda.

def obtener_maximo(lista:list, clave: str):
    '''
    Obtendra el valor de la clave especifica mas grande.
    Primero la funcion se fijara si el valor del primer diccionario es numerico, si es asi 
    se revisara toda la lista en busca del valor mas grande.

    Args
    lista (list) : Lista a revisar.
    clave (str) : Clave de la cual se buscara el maximo.

    Return
    Retornara FALSE si la lista esta vacia o el tipo de dato de clave no es numerica.
    Retornara el dato de clave maximo encontrado si todo sale correctamente.
    '''
    retorno = False
    #Verificar que la lista no este vacia
    if len(lista) > 0:
        #verificar que en el indice, la primera clave sea un int o un float
        if type(lista[0][clave]) == int or type(lista[0][clave]) == float:
            maxima_clave = None

            for heroe in lista:
                dato = heroe[clave] #atrapamos clave en la variable dato
                if maxima_clave == None or dato > maxima_clave[clave]:
                    maxima_clave = heroe

            retorno = maxima_clave
    
    return retorno

# def obtener_maximo_genero(lista:list, genero:str, clave:str):
#     lista_filtrada = []
#     for heroe in lista:
#         if heroe['genero'] == genero:
#             lista_filtrada.append(heroe)

#     maximo_heroe = obtener_maximo(lista_filtrada, clave)

#     return print(f'La {clave} maxima del genero {genero} la tiene {maximo_heroe['nombre']}')

# 3.2 Crear la función “obtener_minimo()” la cual recibirá como parámetro una lista y
# una key (string) la cual representará el dato al cual se le debe calcular su cantidad
# MÍNIMA.
# ● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
# un int o un float. Caso contrario la función retornara un False
# ● En caso de que el dato que se está buscando en el diccionario es de tipo int o
# float retornar el menor que haya encontrado en la búsqueda.


def obtener_minimo(lista:list, clave: str):
    '''
        Obtendra el valor de la clave especifica mas pequeño.
        Primero la funcion se fijara si el valor del primer diccionario es numerico, si es asi 
        se revisara toda la lista en busca del valor mas pequeño.

        Args
        lista (list) : Lista a revisar.
        clave (str) : Clave de la cual se buscara el minimo.

        Return
        Retornara FALSE si la lista esta vacia o el tipo de dato de clave no es numerica.
        Retornara el dato de clave minimo encontrado si todo sale correctamente.
    '''
    retorno = False
    #Verificar que la lista no este vacia
    if len(lista) > 0:
        #verificar que en el indice, la primera clave sea un int o un float
        if type(lista[0][clave]) == int or type(lista[0][clave]) == float:
            minimo_clave = None

            for heroe in lista:
                dato = heroe[clave] #atrapamos clave en la variable dato
                if minimo_clave == None or dato < minimo_clave[clave]:
                    minimo_clave = heroe

            retorno = minimo_clave
    
    return retorno

# def obtener_minimo_genero(lista:list, genero:str, clave:str):
#     lista_filtrada = []
#     for heroe in lista:
#         if heroe['genero'] == genero:
#             lista_filtrada.append(heroe)

#     minimo_heroe = obtener_minimo(lista_filtrada, clave)

#     return print(f'La {clave} minima del genero {genero} la tiene {minimo_heroe['nombre']}')


def obtener_x_cosa(lista:list, genero:str, clave:str, argumento:str):
    lista_filtrada_maximo = []
    lista_filtrada_minimo = []
    
    if argumento == 'maximo':
        for heroe in lista:
            if heroe['genero'] == genero:
                lista_filtrada_maximo.append(heroe)
        maximo_heroe = obtener_maximo(lista_filtrada_maximo, clave)
        retorno = print(f'La {clave} maxima del genero {genero} la tiene {maximo_heroe['nombre']}')
    elif argumento == 'minimo':
        for heroe in lista:
            if heroe['genero'] == genero:
                lista_filtrada_minimo.append(heroe)
        minimo_heroe = obtener_minimo(lista_filtrada_minimo, clave)
        retorno = print(f'La {clave} minima del genero {genero} la tiene {minimo_heroe['nombre']}')

    return retorno
           

# 3.3 Crear la función 'obtener_dato_cantidad()' la cual recibira tres parámetros:
# ● La lista de héroes
# ● Un número que me indique el valor a buscar (puede ser la altura
# máxima, la altura mínima o cualquier otro dato)
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
# ‘peso’, ‘edad’, etc.
# La función deberá retornar una lista con el héroe o los heroes que cumplan
# con la condición pedida. Reutilizar las funciones hechas en los puntos 3.1 y
# 3.2
# Ejemplo de llamada:
# mayor_altura = obtener_maximo(lista_heroes,”altura”)
# lista_heroes_max_altura = 'obtener_dato_cantidad(lista_heroes,mayor_altura,”altura”)
# El objetivo de estás llamadas es obtener todos los superhéroes que tengan la altura
# correspondiente a la altura máxima, y la misma función me podria servir tanto como
# para altura menor, como la mayor o alguna altura que yo le especifique también.

#lista de personajes, el valor va a ser 5, clave sera "fuerza"
def obtener_dato_cantidad(heroes:list, valor:int, clave:str) -> list:
    lista_heroes = []
    for heroe in heroes:
        if valor == heroe[clave]:
            lista_heroes.append(heroe)

    return lista_heroes

# 3.4 Crear la función 'stark_imprimir_heroes' la cual recibirá un parametro:
# ● La lista de héroes
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
# contrario no hará nada y retornara False
# En caso de que la lista no este vacia imprimir la información completa de
# todos los heroes de la lista que se le pase
# Ejemplo de llamada:
# mas_pesado = obtener_maximo(lista_heroes,”peso”)
# lista_mas_pesados = 'obtener_dato_cantidad(lista_heroes,mas_pesado ,”peso”)
# stark_imprimir_heroes(lista_mas_pesados) -> Imprimo sólo los héroes más pesados
# stark_imprimir_heroes(lista_heroes) -> Imprimo todos los héroes

def stark_imprimir_heroes(lista: list):
    retorno = False
    if len(lista) > 0:
        claves = lista[0].keys()
        encabezado = " | ".join(claves)
        print(encabezado)

        for heroes in lista:
            mensaje = ""
            for datos in heroes:
                # para nombre 20, para identidad 25 y para el resto 15     
                mensaje += f"{heroes[datos]:15}"
            print(mensaje)
    return retorno

def stark_imprimir_x_heroe(lista:list, argmt:str):
    heroes_de_tipo = []
    for heroe in lista:
        if heroe['genero'] == argmt:
            heroes_de_tipo.append(heroe)

    return stark_imprimir_heroes(heroes_de_tipo)

# 4.1 Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de
# héroes y un string que representara el dato/key de los héroes que se requiere sumar.
# Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes
# de hacer la suma. La función deberá retorna la suma de todos los datos según la key
# pasada por parámetro


def sumar_dato_heroe(lista:list, key:str):
    acumulador = 0
    for heroe in lista: #se recorre la lista para acceder a cada diccionario de los heroes
        if type(heroe) == dict and len(heroe) > 0: #se valida que el tipo heroe sea un diccionario y que este no este vacio
            valor = heroe[key]
            if type(valor) == float or type(valor) == int:
                acumulador += valor
    return acumulador

'''4.2 Crear la función ‘dividir’ la cual recibirá como parámetro dos números (dividendo
y divisor). Se debe verificar si el divisor es 0, en caso de serlo, retornar False, caso
contrario realizar la división entre los parámetros y retornar el resultado'''

def dividir(dividendo, divisor):
    if divisor == 0:
        retorno = False
    else:
        retorno = dividendo / divisor

    return retorno

'''4.3 Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de
héroes y un string que representa el dato del héroe que se requiere calcular el
promedio. La función debe retornar el promedio del dato pasado por parámetro
IMPORTANTE: hacer uso de las las funciones creadas en los puntos 4.1 y 4.2'''

def calcular_promedio(lista:list, key:str):

    if len(lista) < 0:
        promedio = print('No se pudo calcular el promedio')
    
    sumatoria_total = sumar_dato_heroe(lista,key)

    cantidad_heroes = len(lista) #hallar el divisor, la cantidad de diccionarios totales(heroes) en la lista

    promedio = dividir(sumatoria_total, cantidad_heroes)

    return promedio

'''4.4 Crear la función ‘mostrar_promedio_dato’ la cual recibirá como parámetro una
lista de héroes y un string que representa la clave del dato
● Se debe validar que el dato que se encuentra en esa clave sea de tipo int o
float. Caso contrario retornaria False
● Se debe validar que la lista a manipular no esté vacía , en caso de que esté
vacía se retornaria también False'''

def mostrar_promedio_dato(lista:list, key:str):

    if (type(key) != int or type(key) != float) and (len(lista) < 0):
        resultado = False
    else:
        resultado = calcular_promedio(lista, key)

    return print(resultado)

def filtrar_por_genero(lista:list, genero:str):
    lista_filtrada = []
    for heroe in lista:
        if heroe['genero'] == genero:
            lista_filtrada.append(heroe)
    
    return lista_filtrada

def mostrar_promedio_genero(lista:list, genero:str, key:str):
    promedio_genero_filtrado = filtrar_por_genero(lista, genero) #atajo con una variable el retorno de la funcion que filtra los heroes por genero
    mostrar_promedio_dato(promedio_genero_filtrado, key)

'''5.1 Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla,
el cual permite utilizar toda la funcionalidad ya programada.'''

def imprimir_menu():
    menu = print("""
        ====MENU====
Ingresar opcion:
1. Normalizar datos (No se debe poder acceder a los otros puntos)
2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
10. Listar todos los superhéroes agrupados por color de ojos.
11. Listar todos los superhéroes agrupados por tipo de inteligencia
12. Salir
        """)
    return menu

'''5.2 Crear la función “validar_entero” la cual recibirá por parámetro un string de
número el cual deberá verificar que sea sea un string conformado únicamente por
dígitos. Retornara True en caso de serlo, False caso contrario'''

def validar_entero(numero:str):
    retorno = False

    if numero.isdigit():
        retorno = True
    else:
        retorno = False
    
    return retorno

'''5.3 Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú
de opciones y le pedirá al usuario que ingrese el número de una de las opciones
elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara
casteado a int , caso contrario retorna False. Reutilizar las funciones del ejercicio 5.1
y 5.2'''

def stark_menu_principal():
    imprimir_menu()
    retorno = False
    opcion = input('Escriba un numero: ')

    if validar_entero(opcion):
        retorno = int(opcion)
    else:
        retorno = False

    return retorno

def calcular_contadores(lista:list, key:str):
    diccionario = {}
    for personaje in lista:
        valor = personaje.get(key)
        if valor not in diccionario:
            diccionario[valor] = 0
        diccionario[valor] +=1

    return diccionario

#10. Listar todos los superhéroes agrupados por color de ojos.
#11. Listar todos los superhéroes agrupados por tipo de inteligencia

def listar_heroes(lista:list, key:str):
    diccionario = {}
    for personaje in lista:
        valor = personaje.get(key)
        if type(valor) != str:
            valor = str(valor)
        if valor not in diccionario:
            diccionario[valor] = []
        diccionario[valor].append(personaje['nombre'])

    for valor in diccionario:
        nombres = diccionario[valor]
        print(f"{valor}: {nombres}")

'''6.Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes
y se encargará de la ejecución principal de nuestro programa.
Utilizar if/elif o match según prefiera. Debe informar por consola en caso de
seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las
funciones con prefijo 'stark_' donde crea correspondiente.'''

def stark_marvel_app(lista:list):
    continuar = True
    normalizado = False
    while continuar:
        menu = stark_menu_principal()
        match menu:
            case 1:
                retorno_normalizacion = stark_normalizar_datos(lista_personajes)
                if retorno_normalizacion == True:
                    print('Datos normalizados')
                    normalizado = True
                else:
                    print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
            case 2:
                if normalizado == False:
                    print('Se deben normalizar los datos para poder seleccionar esta opción.')
                    pass
                else:
                    print(stark_imprimir_x_heroe(lista_personajes, 'NB'))

            case 3:
                if normalizado == False:
                    print('Se deben normalizar los datos para poder seleccionar esta opción.')
                    pass
                else:
                    obtener_x_cosa(lista_personajes, 'F', 'altura', 'maximo')
            case 4:
                if normalizado == False:
                    print('Se deben normalizar los datos para poder seleccionar esta opción.')
                    pass
                else:
                    obtener_x_cosa(lista_personajes, 'M', 'altura', 'maximo')
            case 5:
                if normalizado == False:
                    print('Se deben normalizar los datos para poder seleccionar esta opción.')
                    pass
                else:
                    obtener_x_cosa(lista_personajes, 'M', 'fuerza', 'minimo')
            case 6:
                if normalizado == False:
                    print('Se deben normalizar los datos para poder seleccionar esta opción.')
                    pass
                else:
                    obtener_x_cosa(lista_personajes, 'NB', 'fuerza', 'minimo')
            case 7:
                if normalizado == False:
                    print('Se deben normalizar los datos para poder seleccionar esta opción.')
                    pass
                else:
                    mostrar_promedio_genero(lista_personajes, 'NB', 'fuerza')         
            case 8:
                if normalizado == False:
                    print('Se deben normalizar los datos para poder seleccionar esta opción.')
                    pass
                else:
                    print(calcular_contadores(lista_personajes, "color_ojos"))
            case 9:
                if normalizado == False:
                    print('Se deben normalizar los datos para poder seleccionar esta opción.')
                    pass
                else:
                    print(calcular_contadores(lista_personajes, "color_pelo"))
            case 10:
                if normalizado == False:
                    print('Se deben normalizar los datos para poder seleccionar esta opción.')
                    pass
                else:
                    listar_heroes(lista_personajes, "color_pelo")
            case 11:
                if normalizado == False:
                    print('Se deben normalizar los datos para poder seleccionar esta opción.')
                    pass
                else:
                    listar_heroes(lista_personajes, "inteligencia")
            case 12:
                print("Saliendo del programa")
                continuar = False
            case _:
                print("Opcion invalida")






# stark_normalizar_datos(lista_personajes)
# resultado = round(sumar_dato_heroe(lista_personajes, 'peso'),2)
# print(resultado)
# resultado = mostrar_promedio_dato(lista_personajes, 'peso')
# print(resultado)
# print(validar_entero("12345"))  
# print(validar_entero("123a5"))  
# print(validar_entero("01234")) 
# print(validar_entero("")) 
# # menu = imprimir_menu()

#stark_menu_principal()
# opcion_seleccionada = stark_menu_principal()
# if opcion_seleccionada:
#     print(f"Opción seleccionada: {opcion_seleccionada}")
# else:
#     print("Opción inválida. Por favor, ingrese un número del menú.")

stark_marvel_app(lista_personajes)
    

