import json 

ARCHIVO_OPERACIONES = "operaciones.json"
ARCHIVO_POSICIONES = "posiciones.json"
ARCHIVO_CONFIGURACION = "configuracion.json"

def guardar_operaciones(operaciones):
    with open(ARCHIVO_OPERACIONES, "w") as archivo:
        json.dump(operaciones, archivo, indent=4)

def guardar_posiciones(posiciones):
    with open(ARCHIVO_POSICIONES, "w") as archivo:
        json.dump(posiciones, archivo, indent=4)

def guardar_configuracion(configuracion):
    with open(ARCHIVO_CONFIGURACION, "w") as archivo:
        json.dump(configuracion, archivo, indent=4)
        
def cargar_operaciones():
    try:
        with open(ARCHIVO_OPERACIONES, "r") as archivo:
            operaciones = json.load(archivo)
            return operaciones
    except FileNotFoundError:
        return []

def cargar_posiciones():
    try:
        with open(ARCHIVO_POSICIONES, "r") as archivo:
            posiciones = json.load(archivo)
        return posiciones
    except FileNotFoundError:
        return []

def cargar_configuracion():
    try:
        with open(ARCHIVO_CONFIGURACION, "r") as archivo:
            configuracion = json.load(archivo)
        return configuracion
    except FileNotFoundError:
        return {
            "capital_inicial": 0
        }