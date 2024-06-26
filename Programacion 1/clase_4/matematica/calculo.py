def calcular_potencia(num_uno:int, num_dos:int) -> int:
    '''
    Recibe dos numeros enteros y realiza una potencia.
    Retorna el resultado de la potencia.
    '''
    resultado = num_uno

    for i in range(1, num_dos):
        resultado = resultado * num_uno

    return resultado

def calcular_factorial(natural:int) -> int:
    resultado = 1
    for numero in range(1, natural + 1):
        resultado = resultado * numero
    
    return resultado