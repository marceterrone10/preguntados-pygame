# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia

from datos_practica2 import lista_personajes
import json

mensaje = '''
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia
K. Salir
Ingrese: 
'''
def normalizar_dato(lista : list):
    for personaje in lista:
        personaje["peso"] = float(personaje["peso"])
        personaje["altura"] = float(personaje["altura"])
        personaje["fuerza"] =  float(personaje["fuerza"])
    return lista 

#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB

def recorrer_lista(lista:list, genero:str):
    for personaje in lista:
        if personaje['genero'] == genero:
            msj = print(f'Nombre: {personaje['nombre']} - Genero: {personaje['genero']}')
    return msj

#B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def encontrar_mas_alto(lista:list, genero:str):
    max_altura = None
    personaje_mas_alto = ''
    for personaje in lista:
        if personaje['genero'] == genero:
            if max_altura == None or max_altura < personaje['altura']:
                personaje_mas_alto = personaje['nombre']
                max_altura = personaje['altura']

    print(f'El personaje mas alto del genero {genero} es {personaje_mas_alto}')

# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB

def encontrar_mas_debil(lista:list, genero:str):
    pj_min_fuerza = None
    pj_mas_debil_nombre = ''
    for personaje in lista:
        if personaje['genero'] == genero:
            if pj_min_fuerza == None or pj_min_fuerza > personaje['fuerza']:
                pj_mas_debil_nombre = personaje['nombre']
                pj_min_fuerza = personaje['fuerza']

    print(f'El personaje mas debil del genero {genero} es {pj_mas_debil_nombre}')

#F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB

def calcular_fuerza_prom(lista:list, genero:str):  
    contador = 0
    acumulador = 0
    for personajes in lista:
        if personajes['genero'] == genero:
            contador += 1
            acumulador += personajes['fuerza']

    if contador != 0:
        promedio_fuerza = acumulador / contador
        mensaje = print(f'El promedio de fuerza del genero {genero} es {promedio_fuerza}')
    else:
        promedio_fuerza = 0

    return mensaje

# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

def calcular_contadores(lista:list, indicador:str):
    diccionario = {}
    for personaje in lista:
        valor = personaje.get(indicador)
        if valor not in diccionario:
            diccionario[valor] = 0
        diccionario[valor] += 1

    return diccionario

llamada = calcular_contadores(lista_personajes,"color_ojos")
#L. La lista resultante del punto H, guardarla como un archivo JSON.

def guardar_json(diccionario: dict, nombre_archivo: str):
    with open(f"C:/Users/user/Desktop/UTNFRA/Programacion 1/clase_12/{nombre_archivo}.json", "w") as archivo:
        json.dump(diccionario, archivo, indent=4, ensure_ascii=False)

    print("Guardado exitoso")


#M. La lista resultante del punto H, guardarla como un archivo CSV.
def guardar_csv (diccionario: dict, nombre_archivo: str):
    with open(f"C:/Users/user/Desktop/UTNFRA/Programacion 1/clase_12/{nombre_archivo}.csv1","w") as archivo:
        #for color, cantidad in diccionario.items():
            #archivo.write(f"{color}, {cantidad},\n")
        for clave in diccionario:
            archivo.write(f"{clave}, {diccionario[clave]},\n")
           

nombre_archivo = input("ayuda: ")
guardar_csv(llamada,nombre_archivo)



# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia 

def listar_superheroes(lista:list, indicador:str):
    for personajes in lista:
        if indicador == 'ojos':
            # if personajes['color_ojos'] == 'Red':
            #     print(f'Los pjs con color rojo son {personajes['nombre']}')
            # elif personajes['color_ojos'] == 'Blue':
            #     print(f'Los pjs con color blue son {personajes['nombre']}')
            # elif personajes['color_ojos'] == 'Green':
            #     print(f'Los pjs con color green son {personajes['nombre']}')
            # elif personajes['color_ojos'] == 'Brown':
            #     print(f'Los pjs con color brown son {personajes['nombre']}')
            # elif personajes['color_ojos'] == 'Yellow':
            #     print(f'Los pjs con color yellow son {personajes['nombre']}')
            pass             

normalizar_dato(lista_personajes)
continuar = True

while continuar:
    
    menu = input(mensaje)

    match menu:
        case 'A':
            recorrer_lista(lista_personajes, 'NB')
        case 'B':
            encontrar_mas_alto(lista_personajes, 'F')
        case 'C':
            encontrar_mas_alto(lista_personajes, 'M')
        case 'D':
            encontrar_mas_debil(lista_personajes, 'M')
        case 'E':
            encontrar_mas_debil(lista_personajes, 'NB')
        case 'F':
            calcular_fuerza_prom(lista_personajes, 'NB')
        case 'G':
            print(calcular_contadores(lista_personajes, 'color_ojos'))
        case 'H':
            print(calcular_contadores(lista_personajes, 'color_pelo'))
        case 'I':
            listar_superheroes(lista_personajes, 'ojos')
        case 'J':
            pass
        case 'K':
            continuar = False
        case _:
            print('Opcion no valida')
            