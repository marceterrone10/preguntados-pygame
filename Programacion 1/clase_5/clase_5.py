acumulador = 0
edades = []
bandera_min = False
bandera_max = False

for i in range(4):
    edad = int(input("Ingrese su edad: "))
    while edad < 0:
        edad = int(input("Ingrese una edad válida"))
    acumulador += edad
    edades.append(edad)
    if bandera_max == False or edades[i] > edad_maxima:
        edad_maxima = edades[i]
        bandera_max = True
    if bandera_min == False or edades[i] < edad_minima:
        edad_minima = edades[i]
        bandera_min = True

for i in range(len(edades)):
    if bandera_max == False or edades[i] > edad_maxima:
        edad_maxima = edades[i]
        bandera_max = True
    if bandera_min == False or edades[i] < edad_minima:
        edad_minima = edades[i]
        bandera_min = True

print(edad_maxima)
print(edad_minima)
# promedio = acumulador / (i + 1)
# print(promedio)
# print(edades)
# print(edades[0])
# print(edades)

# palabra = input("Ingrese palabra: ")
# for i in range(len(palabra)):
#     print(palabra[i])

# for letra in palabra:
#     print(letra)

#CARGA SECUENCIAL
# nombres = ["A","A","A","A","A","A","A"]
# for i in range(len(nombres)):
#     nombre = input("Ingrese un nombre: ")
#     nombres[i] = nombre

# for i in range(len(nombres)):
#     print(nombres[i])

#CARGA ALEATORIA
nombres = ["A","A","A","A","A","A","A"]
for i in range(len(nombres)):
    nombre = input("Ingrese un nombre: ")
    indice = int(input("Ingrese el índice: "))
    while indice < 0 or indice > len(nombres) or nombres[indice] != "A":
        indice = int(input("Error, reingrese índice: "))
    nombres[indice] = nombre

for i in range(len(nombres)):
    print(nombres[i])