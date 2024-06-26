# Array Multidimensional (Matriz)
matriz = [[1, 23, 15],  # 2x3
          [30, 2, 13]
          ]

#vector = [1, 23, 30, 2]
# Como ordenar una matriz?

# Matriz completamente ordenada [[1, 2, 13], [15, 23, 30]]
# Matriz parcialemente ordenada [[1, 15, 23], [2, 13, 30]]
print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])-1):
        for k in range(j+1, len(matriz[i])):
            print(f"I:{i} -- J:{j} -- K:{k}")
            if matriz[i][j] > matriz[i][k]:
            # swap
                aux = matriz[i][j]
                matriz[i][j] = matriz[i][k]
                matriz[i][k] = aux


print(len(matriz))
print(matriz)

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j])


# numero_max = None
# for combinacion in matriz:
#     for numero in combinacion:
#         if numero_max == None or numero_max < numero:
#             numero_max = numero

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if numero_max == None or numero_max < matriz[i][j]:
#             numero_max = matriz[i][j]

# print(f"Numeros {matriz}")
# print(f"Listas anidadas {matriz[0]}")
# print(f"Valor numerico {matriz[0][1]}")

# print(f"El numero maximo es {numero_max}")


# nombres_ = [["Juan", "Perez"],
#           ["Pepe", "Gomez"]]
# # indices [ 0,        1]
# nombres = ["Ana", "David"]
# # Filas y Columnas
# # print(nombres_[0][0] + " " + nombres[0][1])
# # nombre = "Sofia" # ["S", "o", "f", "i", "a"]

# for i in range(len(nombres)):
#     for j in range(len(nombres[i])):
#         print(nombres[i][j])

# #print(nombres[1][0])

# # for nombre in nombres:
# #     for letra in nombre:
# #         print(letra)
