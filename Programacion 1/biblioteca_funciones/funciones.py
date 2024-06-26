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



#########################################################################################

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

