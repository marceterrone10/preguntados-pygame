# Ejercicios Cadenas:

# 1) Crear una función que reciba como parámetro una cadena y determine la cantidad 
# de vocales que hay de cada una (individualmente). La función retornará una matriz 
# indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.

# Por ej:
# cadena = “murcielaguito”

# “a” -> 1
# “e” -> 1 
# “i” -> 2
# “o” -> 1
# “u” -> 2

# lista_vocales = ['a','e','i','o','u']
# contador_vocales = [0,0,0,0,0]

# def contar_vocales(cadena, contador_vocales):

#     resultado = []

#     for letra in cadena:
#         for i in range(len(lista_vocales)):
#             if letra == lista_vocales[i]:
#                 contador_vocales[i] += 1

# contar_vocales(cadena, contador_vocales)
# print(contador_vocales)


def contar_vocales(cadena: str):
    cont_a = 0
    cont_e = 0
    cont_i = 0
    cont_o = 0
    cont_u = 0
    
    for vocal in cadena.lower():
        if vocal == 'a':
            cont_a += 1
        elif vocal == 'e':
            cont_e += 1
        elif vocal == 'i':
            cont_i += 1
        elif vocal == 'o':
            cont_o += 1
        elif vocal == 'u':
            cont_u += 1

        matriz = [
            ['a', cont_a],
            ['e', cont_e],
            ['i', cont_i],
            ['o', cont_o],
            ['u', cont_u]
        ]

    return matriz
cadena = 'murcielaguito'
resultado = contar_vocales(cadena)
print(resultado)


# 2) Crear una función que reciba una cadena y un caracter. 
# La función deberá devolver el índice en el que se encuentre la primera 
# incidencia de dicho caracter, o -1 en caso de que no esté.

def indice_caracter(cadena_2:str, caracter:str) -> int:
    for letras in range(len(cadena_2)):
        if cadena_2[letras] == caracter:
            return letras
        else:
            resultado = -1
    
    return resultado

cadena_2 = "marcelo"
caracter = "a"
final = indice_caracter(cadena_2, caracter)
print(final)

# 3) Crear una función que reciba como parámetro una cadena y determine si la misma 
# es o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.

def palindromo(cadena_3:str) -> bool:
    for i in range(len(cadena_3)):
        if cadena_3[i] != cadena_3[-i-1]:
            resultado = False
        else:
            resultado = True

    return resultado
        

cadena_3 = "neuquen"

ejercicio_3 = palindromo(cadena_3)
print(ejercicio_3)


# 4) Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
# 	Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

cadena_cuatro = "Hoooooooooooola"

def eliminar_caracter_rep(cadena_cuatro:str) -> str:
    caracteres_no_repetidos = ""
    for i in cadena_cuatro:
        if i not in caracteres_no_repetidos:
            caracteres_no_repetidos += i
    return caracteres_no_repetidos


resultado_4 = eliminar_caracter_rep(cadena_cuatro)
print(resultado_4)


# 5) Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
#     Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.


cadena_4 = "marcelo"

def eliminar_vocales(cadena_4:str) -> str:
    """Funcion que elimina vocales de una cadena de texto por medio de un bucle for el cual recorre la cadena_4
    y por medio del if se analiza si esa letra esta en la lista vocales, de no ser asi se suman a la variable texto_vacio
    """
    vocales = ["a","e","i","o","u"]
    texto_vacio = ""
    for i in cadena_4.lower():
        if i not in vocales: #preguntamos si los caracteres de la cadena no estan en la lista, si no estan se agregan a la variable texto_vacio.
            texto_vacio += i

    return texto_vacio

resultado_5 = eliminar_vocales(cadena_4)
print(resultado_5)

# 6) Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
#     Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.


# 7) CASO INVESTIGACIÓN CRIMINAL: CSI UTN 

# Se ha encontrado una muestra de ADN en el lugar del crimen que contiene la siguiente 
# secuencia de bases nitrogenadas: “CGTTTAATG”. La investigación ha revelado tres 
# posibles sospechosos, cada uno con su propia muestra de ADN:
# Juan Pérez
# Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"
# María Rodríguez
# Muestra de ADN: "AACGTTTAATGTTCTAAGCTGCG"
# Carlos Sánchez
# Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"

# Para resolver el caso, nos piden que desarrollemos un programa que compare las combinaciones 
# de bases nitrogenadas de la muestra encontrada con las muestras de los sospechosos. 
# Mostrar el nombre por pantalla en caso de encontrar al asesino, o la leyenda “SON TODOS INOCENTES”. 
