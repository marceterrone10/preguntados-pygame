import json

def importar_datos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos

