def calcular_valor_iva(valor_sin_iva, iva=21):
    resultado = valor_sin_iva * (1 + (iva/100))
    return resultado

valor = 1000
valor_con_iva = calcular_valor_iva(1000)
print(valor_con_iva)

#=============================================================

#Desarrollo de la funcion
def sumar(varible_1, variable_2): #Parametros formales
    '''Sumatoria de dos variables recibidos por parametro'''
    return varible_1 + variable_2

#Llamada de la funcion
resultado = sumar(1, 2) #Paramtros actuales
print(resultado)


#=============================================================

variable_valor = 3
variable_ref = 2

def get_variable_uno(variable_valor):
    variable_valor = 7
    print(variable_valor)

get_variable_uno(variable_valor)

#=============================================================

def agregar_dato_lista(lista:list): #Pasar por referencia
    lista.append(5)

mi_lista = [1,2,3,4]

print(mi_lista)

agregar_dato_lista(mi_lista)

print(mi_lista)
#Se modifica la lista ORIGINAL ya que se pasa el valor por refencia 

#Un numero, cadena str, booleano, bytes, tuplas inmutables
#Listas, diccionarios, sets por referencia, mutables

#Que sea mutable quiere decir que se cambia, modifica la lista, diccionario, etc pero no se cambia la direccion de memoria

