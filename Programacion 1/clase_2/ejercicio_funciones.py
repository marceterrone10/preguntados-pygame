# Funciones Parte I

# 1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

# 2. Crear una función que verifique si un número dado por argumento es par o impar. 
#    La función debe imprimir un mensaje indicando si el número es par o impar.
   
# 3. Define una función que encuentre el máximo de tres números. 
#    La función debe aceptar tres argumentos y devolver el número más grande.
   
# 4. Diseña una función que calcule la potencia de un número. 
#    La función debe recibir la base y el exponente como argumentos y devolver el resultado.


def ingresar_numero() -> int:
    '''Pido un dato al usuario y lo retorno en consola'''
    numero = int(input('Ingrese un numero: '))
    return numero

resultado = ingresar_numero()
# print(resultado)

def verif_num_par(numero):
    ''''''
    if numero % 2 == 0:
        print(f'{numero} es numero par')
    else:
        print(f'{numero} es numero inpar')


numero_dos = ingresar_numero()

verif_num_par(numero_dos)


# 3. Define una función que encuentre el máximo de tres números. 
#    La función debe aceptar tres argumentos y devolver el número más grande.

def encontrar_mayor(num_uno:int, num_dos:int, num_tres:int) -> int:
    ''''''

    if num_uno == num_dos and num_tres == num_dos:
        resultado = num_uno
    else:
        # if num_uno == num_dos and num_uno > num_tres:
        #     resultado = num_uno
        if num_uno == num_tres and num_uno > num_dos:
            resultado == num_uno
        # elif num_dos == num_tres and num_dos > num_uno:
        #     resultado == num_dos
        elif num_uno >= num_dos and num_uno > num_tres:
            resultado = num_uno
        elif num_dos >= num_tres:
            resultado = num_dos
        else:
            resultado = num_tres
    
    return resultado

numero1 = ingresar_numero()
numero2 = ingresar_numero()
numero3 = ingresar_numero()

respuesta = encontrar_mayor(numero1, numero2, numero3)
print(respuesta)

# 4. Diseña una función que calcule la potencia de un número. 
#    La función debe recibir la base y el exponente como argumentos y devolver el resultado.


def calcular_potencia(base:int, exponente:int) -> int:
    '''
    Recibe dos numeros enteros y realiza una potencia.
    Retorna el resultado de la potencia.
    '''
    resultado = base

    for i in range(1, exponente):
        resultado = resultado * base

    return resultado

base = ingresar_numero()
exponente = ingresar_numero()
print(calcular_potencia(base, exponente))




