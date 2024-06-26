# Array Multidimensional (Matriz)
matriz = [[1, 5, 10, 7],  # 4x4
          [2, 6, 4, 8], 
          [1, 3, 11, 9],
          [14, 13, 16, 15]]
print(matriz)



def ordenar_matriz(matriz):
    """Documentacion"""
    # 1er paso
    for i in range(len(matriz)): # 2
        for j in range(len(matriz[i])): # 3
            for k in range(len(matriz[i])): # 3
                if k == len(matriz[i]) - 1: # 3
                    for l in range(i + 1, len(matriz)): # 1, 2
                        for m in range(len(matriz[i])): # 3
                            if matriz[i][j] > matriz[l][m]: 
                                # Swap
                                aux = matriz[i][j]
                                matriz[i][j] = matriz[l][m]
                                matriz[l][m] = aux
    # 2do paso
    for i in range(len(matriz)):
        for j in range(len(matriz[i])-1):
            for k in range(j+1, len(matriz[i])):
                #print(f"I:{i} -- J:{j} -- K:{k}")
                if matriz[i][j] > matriz[i][k]:
                    # Swap
                    aux = matriz[i][j]
                    matriz[i][j] = matriz[i][k]
                    matriz[i][k] = aux

ordenar_matriz(matriz)
print(matriz)