# Utilizar For
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# mostrar el mayor.

lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

def obtener_maximo(lista_numeros:list) -> int:
    bandera_max = True
    numero_maximo = None

    for numero in lista_numeros:
        if bandera_max == True or numero > numero_maximo:
            numero_maximo = numero
            bandera_max = False
    
    return(numero_maximo)


print(obtener_maximo(lista_numeros))
