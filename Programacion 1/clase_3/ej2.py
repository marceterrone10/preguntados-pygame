# def ingresar_numero() -> int:
#     '''Pido un dato al usuario y lo retorno en consola'''
#     numero = int(input('Ingrese un numero: '))
#     return numero

# resultado = ingresar_numero()
# # print(resultado)

def verif_num_par(numero:int):
    '''
    Funcion que recibe un numero y analiza si es par o no, si es par devuelve True y si no lo es devuelve False
    Recibe un numero que se le restara 2 hasta que quede 0 o 1.
    Si es 1 devuelve False, es impar, si es 0 devuelve True, es par.
    '''
    retorno = None
    # if numero % 2 == 0:
    #     retorno = True
    # else:
    #     retorno = False

    if numero < 0:
        numero = numero * -1

    while(numero > 1):
        numero = numero - 2
    
    if numero == 1:
        retorno = False
    else:
        retorno = True

    return retorno

verif_num_par(3)

for i in range(5):
    numero = int(input('Ingresar un numero: '))

    while verif_num_par(numero) == False:
        numero = int(input('Re ingresar un numero: '))

    print('El numero fue bien ingresado')

    