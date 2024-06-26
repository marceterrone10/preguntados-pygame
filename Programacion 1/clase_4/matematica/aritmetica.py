def sumar(num_uno: int, num_dos: int) -> int:
    '''Esta funcion suma dos numeros y retorna el resultado'''
    suma = num_uno + num_dos
    return suma

def restar(num_uno: int, num_dos:int) -> int:
    '''Esta funcion resta dos numeros y retorna el resultado'''
    resta = num_uno - num_dos
    return resta

def dividir(dividendo: int, divisor:int) -> int:
    '''Esta funcion divide dos numeros y retorna el resultado'''
    if divisor == 0:
        print('Error, no se puede dividir por cero. La funcion retorna cero.')
        division = divisor
    else:
        division = dividendo / divisor
    return division

def multiplicacion(num_uno: int, num_dos:int) -> int:
    '''Esta funcion multiplica dos numeros y retorna el resultado'''
    operacion = num_uno * num_dos
    return operacion


#Ejemplo de documentacion 
def nombre_de_la_funcion(parametro1, parametro2):
    """
    Descripción de la función
    
    Args:
    parametro1 (tipo): Descripción del primer parámetro
    parametro2 (tipo): Descripción del segundo parámetro
    
    Returns:
    tipo_de_retorno: Descripción del valor de retorno
    """
    # Cuerpo de la función
    pass

#Este es un ejemplo
def suma(a, b):
    '''Esta función suma dos números y devuelve el resultado.
    
    Args:
    a (int o float): El primer número a sumar.
    b (int o float): El segundo número a sumar.
    
    Returns:
    int o float: La suma de a y b.'''

    pass
    
    


