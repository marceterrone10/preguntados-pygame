'''import aritmetica

num_uno = int(input('Numero uno: '))
num_dos = int(input('Numero dos: '))

print(aritmetica.sumar(num_uno, num_dos))'''



# from aritmetica import sumar, restar

# num_uno = int(input('Numero uno: '))
# num_dos = int(input('Numero dos: '))

# resultado = sumar(num_uno, num_dos)
# print(resultado)

# resultado = restar(num_uno, num_dos)
# print(resultado)


# from Clase_4.matematica.aritmetica import *

# num_uno = int(input('Numero uno: '))
# num_dos = int(input('Numero dos: '))

# resultado = sumar(num_uno, num_dos)
# print(resultado)

# resultado = restar(num_uno, num_dos)
# print(resultado)

# import matematica.aritmetica


# num_uno = int(input('Numero uno: '))
# num_dos = int(input('Numero dos: '))

# resultado = matematica.aritmetica.sumar(num_uno, num_dos)
# print(resultado)

# from matematica.aritmetica import sumar, restar


# num_uno = int(input('Numero uno: '))
# num_dos = int(input('Numero dos: '))

# print(sumar(num_uno, num_dos))

# print(restar(num_uno, num_dos))


from matematica.aritmetica import *
from matematica.calculo import calcular_factorial


num_uno = int(input('Numero uno: '))
num_dos = int(input('Numero dos: '))

print(sumar(num_uno, num_dos))

print(restar(num_uno, num_dos))

print(calcular_factorial(num_uno))


'''
def factorial(n):
    #n=3
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def factorial(n):
    #n=2
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def factorial(n):
    #n=1
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def factorial(n):
    #n=0
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(4))

