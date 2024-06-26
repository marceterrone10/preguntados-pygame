'''
Hacer 2 funciones, que una haga shallow copy y otra que haga deep copy. (Sin usar .copy())
Por el momento solo con diccionarios.
'''

#Datos: Nombre, Legajo, Direccion
diccionario_alumno = {"Nombre": "Maria", "Legajo": 9999,
"Direccion": {"Calle": "Moreno", "Altura": 88, "Localidad": "Quilmes"}}

#diccionario_alumno_copia = diccionario_alumno
#diccionario_alumno_copia = diccionario_alumno.copy()
#print(diccionario_alumno)

#Funciones
#Equivalente manual de Shallow Copy.
def copiar_diccionario_shallow(diccionario) -> dict:
    mi_otro_diccionario = {}

    for clave in diccionario:
        mi_otro_diccionario.update({clave: diccionario[clave]})

    return mi_otro_diccionario

#Equivalente manual de Deep Copy.
def copiar_diccionario_deep(diccionario) -> dict:
    mi_otro_diccionario = {}
    
    #Recorre las claves principales (Nombre, Legajo, Direccion)
    for clave in diccionario:
        if (type(diccionario[clave]) == dict):
            #Llamamos a esta misma funcion (Recursividad)
            mi_otro_diccionario_2 = copiar_diccionario_deep(diccionario[clave])
            mi_otro_diccionario.update({clave: mi_otro_diccionario_2})
        else:
            mi_otro_diccionario.update({clave: diccionario[clave]})

    return mi_otro_diccionario

#Prints
#Shallow
diccionario_alumno_copia = copiar_diccionario_shallow(diccionario_alumno)
print(f"Original: {diccionario_alumno}")
print(f"Copia: {diccionario_alumno_copia}")
diccionario_alumno_copia["Nombre"] = "Julian"
diccionario_alumno_copia["Direccion"]["Localidad"] = "Banfield"
print(f"Original (Post-Modificacion): {diccionario_alumno}")
print(f"Copia (Post-Modificacion): {diccionario_alumno_copia}")

#Deep
diccionario_alumno_copia = copiar_diccionario_deep(diccionario_alumno)
print(f"Original: {diccionario_alumno}")
print(f"Copia: {diccionario_alumno_copia}")
diccionario_alumno_copia["Nombre"] = "Julian"
diccionario_alumno_copia["Direccion"]["EntreCalles"]["Calle1"] = "Mitre"
print(f"Original (Post-Modificacion): {diccionario_alumno}")
print(f"Copia (Post-Modificacion): {diccionario_alumno_copia}")
