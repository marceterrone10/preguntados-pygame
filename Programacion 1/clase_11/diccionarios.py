from copy import deepcopy

# Diccionario   -> Clave: "nombre": Valor: "Marty".

# if mi_diccionario["esta_casado"] == True:
#     casado = " estoy casado."
# else:
#     casado = " no estoy casado."
# mensaje = f'Hola, mi nombre es {mi_diccionario["nombre"]}, tengo {mi_diccionario["edad"]} años y{casado}'
# print(mensaje)
#print(mi_diccionario["direccion"])

# mensaje = f'Vivo en la calle {mi_diccionario["direccion"]["calle"]} y la altura {mi_diccionario["direccion"]["altura"]}.'
# print(mensaje)


# for clave in mi_diccionario:
#     print(clave)
#     print(mi_diccionario[clave])

# copia_del_diccionario = mi_diccionario # Referencia
# copia_del_diccionario = mi_diccionario.copy() # Shallow Copy, hace una copia.
# copia_del_diccionario = deepcopy(mi_diccionario) # Deep Copy, hace una copia.
# print(f"Antes original: {mi_diccionario}")
# print(f"Antes copia: {copia_del_diccionario}")

# # print(id(mi_diccionario))
# # print(id(copia_del_diccionario))

# print("Cambio valor del original")
# # mi_diccionario["direccion"]["calle"] = "Callao" 
# # mi_diccionario["nombre"] = "Pepe" 
# copia_del_diccionario["nombre"] = "Jose"
# copia_del_diccionario["direccion"]["calle"] = "Rivadavia"

# print(f"Despues original: {mi_diccionario}")
# print(f"Despues copia: {copia_del_diccionario}")


mi_diccionario = {"nombre": "Marty", "edad": 35, "direccion": {"calle": "Belgrano", "altura": 2350}}
mi_otro_diccionario = {}
print(mi_otro_diccionario)
mi_otro_diccionario.update({"nombre": "Pepe"})
print(mi_otro_diccionario)
mi_otro_diccionario.update({"nombre2": "Jose"})
print(mi_otro_diccionario)
mi_otro_diccionario.clear()
print(mi_otro_diccionario)

# print(mi_diccionario["nombre"])
# print(mi_diccionario.get("genero", "No existe esa clave"))

# print(mi_diccionario.keys())
# print(mi_diccionario.values())
# print(mi_diccionario.items())

# print(f"Antes: {mi_diccionario}")
# mi_diccionario.pop("edad", "no se encontro la clave")
# print(f"Despues: {mi_diccionario}")
