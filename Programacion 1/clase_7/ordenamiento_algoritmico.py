# Ordenar la siguiente lista de manera ASCENDENTE, mediante Burbujeo/Bubble Sort
nombres = ["Sofia", "Pablo", "Ana", "David"]
edades = [23, 28, 30, 18]
sexos = ["F", "M", "F", "M"]
# Ordenar por sexo y si coinciden por nombre.


        #Iteramos hasta el penultimo porque no hay nada para comparar sino
for i in range(len(sexos)-1):
    for j in range(i+1, len(sexos)):
        if sexos[i] == sexos[j]:
            if nombres[i] > nombres[j]:
                #Swap
                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux
                aux = edades[i]
                edades[i] = edades[j]
                edades[j] = aux
                aux = sexos[i]
                sexos[i] = sexos[j]
                sexos[j] = aux
        else:
            if sexos[i] > sexos[j]:
                #Swap
                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux
                aux = edades[i]
                edades[i] = edades[j]
                edades[j] = aux
                aux = sexos[i]
                sexos[i] = sexos[j]
                sexos[j] = aux

print(nombres)
print(edades)
print(sexos)



# lista = ["c", "a", "B", "A"]
# for i in range(len(lista)-1):
#     for j in range(i+1, len(lista)):
#         if lista[i] > lista[j]:
#             # Swap
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux

# print(lista)

lista_practica = [3, 2, 10, 9, 5, 1, 0, 4, 11, 19, 17]


def ordenar(lista_practica):
    for i in range(len(lista_practica) - 1):
        #print(lista_practica[i])
        for j in range(i+1, len(lista_practica)):
            if lista_practica[i] > lista_practica[j]:
                aux = lista_practica[i]
                lista_practica[i] = lista_practica[j]
                lista_practica[j] = aux
    
    return lista_practica

print(ordenar(lista_practica))

# def ordenar(lista_practica):
#     for i in range(1, len(lista_practica)):
#         for j in range(0, len(lista_practica) - i):
#             if lista_practica[j+1] < lista_practica[j]:
#                 aux = lista_practica[j]
#                 lista_practica[j] = lista_practica[j+1]
#                 lista_practica[j+1] = aux

#     return lista_practica

# print(ordenar(lista_practica))




