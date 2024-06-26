# Lista inicial de juegos
juegos = [
    {"id": 1, "nombre": "Juego 1"},
    {"id": 2, "nombre": "Juego 2"},
    {"id": 3, "nombre": "Juego 3"},
    {"id": 4, "nombre": "Juego 4"},
    {"id": 5, "nombre": "Juego 5"}
]

# Función para borrar un juego y reacomodar los IDs
def borrar_y_reacomodar_juegos(lista_juegos, id_juego):
    # Inicializar una nueva lista para los juegos con IDs reacomodados
    juegos_reacomodados = []
    nuevo_id = 1
    
    for juego in lista_juegos:
        if juego["id"] != id_juego:
            juego["id"] = nuevo_id
            juegos_reacomodados.append(juego)
            nuevo_id += 1

    return juegos_reacomodados

# Borrar el juego con ID 5
juegos_actualizados = borrar_y_reacomodar_juegos(juegos, 3)

# Imprimir la lista de juegos actualizada
print(juegos_actualizados)
