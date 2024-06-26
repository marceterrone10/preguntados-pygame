

def calcular_factorial(natural:int) -> int:
    resultado = 1
    for numero in range(1, natural + 1):
        resultado = resultado * numero
    
    return resultado


valor = int(input('Operando: '))
print(calcular_factorial(valor))
    
