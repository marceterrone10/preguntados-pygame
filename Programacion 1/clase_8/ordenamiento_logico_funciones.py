lista_numeros = [5, 7, 4, 6]
lista_nombres = ["Pepe", "Ana", "Juan", "Sofia", "Pablo"]
# Ordenamiento Asc  /  Desc        
#   criterio = "ASC", criterio = "DESC"           
def ordenar_lista(lista: list, criterio: str = "ASC"):
    """
    Ordena la lista recibida por parametro con el criterio "ASC" o "DESC" tambien recibido por parametro.
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if (criterio == "ASC" and lista[i] > lista[j]) or (criterio == "DESC" and lista[i] < lista[j]):
                    # Swap
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

print(lista_nombres)
ordenar_lista(lista_nombres)
print(lista_nombres)

