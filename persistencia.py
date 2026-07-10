import json 

ARCHIVO_OPERACIONES = "operaciones.json"
ARCHIVO_POSICIONES = "posiciones.json"

def guardar_operaciones(operaciones):
    with open(ARCHIVO_OPERACIONES, "w") as archivo:
        json.dump(operaciones, archivo, indent=4)

def guardar_posiciones(posiciones):
    with open(ARCHIVO_POSICIONES, "w") as archivo:
        json.dump(posiciones, archivo, indent=4)
    
def cargar_operaciones():
    try :
        with open(ARCHIVO_OPERACIONES, "r") as archivo:
            operaciones =json.load(archivo)
            return operaciones
    except FileNotFoundError:
        return []

def cargar_posiciones():
    try:
        with open(ARCHIVO_POSICIONES, "r") as archivo:
            posiciones =json.load(archivo)
        return posiciones
    except FileNotFoundError:
        return []