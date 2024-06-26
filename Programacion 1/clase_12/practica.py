from datos import lista_personajes

mensaje = '''
A. Mostrar todos
B. Mostrar el mas fuerte
C. Mostrar el mas bajo
D. Mostrar peso promedio de masculinos
E. Mostrar nombre y peso promedio mayor a los que superen el promedio femenino
F. Salir
Ingrese: 

'''
    
#B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
def recorrer_max(lista: list):
    personaje_actual = ""
    max_fuerza = None
    for personaje in lista:
        #fuerza_actual = personaje['fuerza']
        if max_fuerza == None or max_fuerza < personaje['fuerza']:
            personaje_actual = personaje
            max_fuerza = personaje['fuerza']
    print(f"El personaje mas fuerte es {personaje_actual['identidad']} y su peso es: {personaje_actual['peso']}")
    
#C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)

def recorrer_min(lista:list):
    personaje_actual = ''
    min_altura = None

    for personaje in lista:
        if min_altura == None or min_altura > personaje['altura']:
            personaje_actual = personaje
            min_altura = personaje['altura']
    print(f'El nombre del personaje con menor altura es {personaje_actual['nombre']} y su identidad es {personaje_actual['identidad']}')

# D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)

# def hallar_promedios(lista:list):
#     acumulador = 0
#     contador = 0

#     for personaje in lista:
#         if personaje['genero'] == 'M':
#             contador += 1
#             acumulador += personaje['peso']
#     promedio_peso = acumulador / contador

#     if promedio_peso != 0:
#         print(f'El promedio del peso de los masculinos es de {promedio_peso}')
#     else:
#         print('No hay personajes del genero masculino')

#     return promedio_peso

def calcular_promedios(lista:list, clave:str, genero:str):
    acumulador = 0
    contador = 0

    for personaje in lista:
        if personaje['genero'] == genero:
            contador += 1
            acumulador += personaje[clave]

    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = 0

    return promedio

# E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino

def calcular_promedio_fuerza(lista:list, clave:str, genero:str):
    acumulador = 0
    contador = 0
    fuerza_max = None
    # nombre_pj_max = ''
    # peso_pj_max = ''

    for personaje in lista:
        if personaje['genero'] == genero:
            contador += 1
            acumulador += personaje[clave]

    if contador != 0:
        promedio_fem = acumulador / contador
    else:
        promedio_fem = 0
    #print(promedio_fem)

    for personaje in lista:
        if personaje['genero'] == 'M':
            if fuerza_max == None or fuerza_max < promedio_fem:
                nombre_pj_max = personaje['nombre']
                peso_max = personaje['peso']
                fuerza_max = personaje['fuerza']

    mensaje_e = print(f'El nombre del personaje con mayor fuerza que el promedio de fuerza femenino es {nombre_pj_max} y su peso es {peso_max}')

    return mensaje_e

def normalizar_dato(lista : list):
    for personaje in lista:
        personaje["peso"] = float(personaje["peso"])
        personaje["altura"] = float(personaje["altura"])
        personaje["fuerza"] =  float(personaje["fuerza"])
    return lista 



continuar = True

normalizar_dato(lista_personajes)

while continuar:

    menu = input(mensaje)

    match menu:
        case 'A':
            # titulos = (lista_personajes[0].keys())
            # titulo = ""
            # for i in titulos:
            #     titulo += i.upper() + "\t"
            # print(titulo)

            claves = lista_personajes[0].keys()
            encabezado = " | ".join(claves)
            print(encabezado)

            for heroes in lista_personajes:
                mensaje = ''
                for datos in heroes:
                    mensaje += f'{heroes[datos]:20}'
                print(mensaje)
        case 'B':
            recorrer_max(lista_personajes)
        case 'C':
            recorrer_min(lista_personajes)
        case 'D':
            #promedios = encontrar_promedios(lista_personajes)
            print(f'El promedio del peso masculino es {calcular_promedios(lista_personajes, 'peso', 'M')}')
        case 'E':
            #E. Mostrar nombre y peso promedio mayor a los que superen el promedio femenino
            #promedio = encontrar_promedios(lista_personajes, 'fuerza', 'F' )
            calcular_promedio_fuerza(lista_personajes, 'fuerza', 'F')
        case 'F':
            continuar = False
        case _:
            print('No existe esa opcion')
