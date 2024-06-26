from os import system

# Crear una funcion propia, que mida cadenas de caracteres o listas
# Recibe string/lista.
# Retorna la cantidad de caracteres de una cadena o la cantidad de elementos de una lista.

def contar_elementos(elementos) -> int:
    '''
        Cuenta la cantidad de elementos dentro de un objeto iterable.
        Recibe string/lista.
        Retorna la cantidad de caracteres de una cadena o la cantidad de elementos de una lista.
    '''

    contador = 0
    for i in elementos:
        contador += 1

    return contador

mi_lista = [0, 1, 80, -4]
mi_string = "Sopa de verdura"

print(f"Elementos de lista: {contar_elementos(mi_lista)}")
print(f"Elementos de la string: {contar_elementos(mi_string)}")

#A 65
#a 97
#Diferencia 32
#Letras Mayusculas: 65-90
#Letras Minusculas: 97-122
print(ord("A"))
print(ord("a"))
print(chr(65))
print(chr(97))

#hola -> Hola
#HOLA -> Hola
def capitalizar(cadena: str) -> str:
    #Convierte la primera letra (si es minuscula) en mayuscula.
    #Comprueba si es una letra con su valor ASCII.
    if (ord(cadena[0]) >= 97 and ord(cadena[0]) <= 122):
        resultado = chr(ord(cadena[0])-32)
    else:
        resultado = cadena[0]

    #Recorremos desde el 2do caracter de la cadena hasta el final.
    for i in range(1, contar_elementos(cadena)):
        #Preguntamos si el caracter del indice es una letra mayuscula.
        if (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90):
            resultado += chr(ord(cadena[i])+32)
        else:
            resultado += cadena[i]
    
    return resultado

system("cls")

'''
Crear una funcion que convierta el String pasado por parametro a mayuscula.
'''

#Letras Mayusculas: 65-90
#Letras Minusculas: 97-122

def convertir_mayuscula(cadena: str) -> str:
    resultado = "" #Variable a devolver

    #Recorremos toda la cadena
    for i in range(contar_elementos(cadena)):
        #Preguntamos si el caracter del indice es una Minuscula.
        if (ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122):
            resultado += chr(ord(cadena[i])-32)
        else:
            #resultado = resultado + cadena[i] (Es lo mismo)
            resultado += cadena[i]
    
    return resultado

def convertir_minuscula(cadena: str) -> str:
    resultado = "" #Variable a devolver

    #Recorremos toda la cadena
    for i in range(contar_elementos(cadena)):
        #Preguntamos si el caracter del indice es una Mayuscula.
        if (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90):
            resultado += chr(ord(cadena[i])+32)
        else:
            #resultado = resultado + cadena[i] (Es lo mismo)
            resultado += cadena[i]
    
    return resultado

mi_cadena = "HoLa mUnDo"
print(convertir_minuscula(mi_cadena))