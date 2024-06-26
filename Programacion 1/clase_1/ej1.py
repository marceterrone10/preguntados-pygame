# Una reconocida productora de contenidos audiovisuales está en busca de nuevas ideas
# para su próximo proyecto, que promete cautivar al público.
# Las posibles temáticas para explorar son las siguientes:
# • Comedia
# • Ciencia ficción
# • Drama
# Para ello, la empresa ha decidido realizar una encuesta entre sus empleados para
# recopilar información valiosa. Los datos para recopilar por cada empleado son los
# siguientes:
# A) Información a ingresar por cada empleado encuestado:
# • Nombre del empleado
# • Edad (debe ser mayor o igual a 18)
# • Género (Masculino - Femenino)
# • Temática de interés (Comedia, Ciencia ficción, Drama)
# B) Se deben cargar 10 encuestas a través de la terminal.
# C) Se requiere determinar:
# • La cantidad de empleados de género masculino que votaron por Ciencia ficción o
# Drama, cuya edad esté entre 25 y 50 años, inclusive.
# • El porcentaje de empleados que no votaron por Comedia, siempre y cuando su
# género no sea Femenino o su edad esté comprendida entre 30 y 40 años.
# • El nombre y la temática de interés votada por el empleado masculino de mayor
# edad.
contador_total_personas = 10
contador_punto_a = 0
contador_punto_b = 0
bandera_mayor_edad = True
nombre_mayor_edad = ''
tematica_mayor_edad = ''
edad_mayor = 0

for i in range(10):

    nombre_ingresado = input('Ingrese su nombre: ')
    
    edad_ingresada = int(input('Ingrese su edad: '))
    while edad_ingresada < 18:
        edad_ingresada = int(input('Re ingrese su edad: '))
    
    genero_ingresado = input('Ingrese su genero: ')
    while genero_ingresado != 'Masculino' and genero_ingresado != 'Femenino':
        genero_ingresado = input('Re ingrese su genero (Masculino/Femenino): ')
    
    tematica = input('Ingrese la tematica: ')
    while tematica != 'Comedia' and tematica != 'Ciencia Ficcion' and tematica != 'Drama':
        tematica = input('Re ingrese la tematica: ')


# C) Se requiere determinar:
# • La cantidad de empleados de género masculino que votaron por Ciencia ficción o
# Drama, cuya edad esté entre 25 y 50 años, inclusive.
# • El porcentaje de empleados que no votaron por Comedia, siempre y cuando su
# género no sea Femenino o su edad esté comprendida entre 30 y 40 años.
# • El nombre y la temática de interés votada por el empleado masculino de mayor
# edad.





if tematica != 'Comedia':
    if genero_ingresado == 'Masculino':
        if edad_ingresada >= 25 and edad_ingresada <= 50:
            contador_punto_a += 1
    if genero_ingresado == 'Masculino' or edad_ingresada > 30 and edad_ingresada < 40:
        contador_punto_b += 1

if genero_ingresado == 'Masculino':
    if bandera_mayor_edad == True or edad_ingresada > edad_mayor:
        edad_mayor = edad_ingresada
        tematica_mayor_edad = tematica
        nombre_mayor_edad = nombre_ingresado
        bandera_mayor_edad = False

print(f'La cantidad de empleados que estan entre los 25 y 50 anos que votaron por ciencia o drama y sean masculinos es de: {contador_punto_a}')


porcentaje = (contador_punto_b / contador_total_personas) * 100

print(f'El porcentaje es de {porcentaje}%')

print(f'El nombre y la tematica del empleado masculino con mayor edad es {edad_mayor}, {tematica_mayor_edad}')





