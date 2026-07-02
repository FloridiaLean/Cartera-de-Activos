from datetime import datetime

def generar_id_posicion(posiciones):
    
    id_mayor = 0 
    
    for posicion in posiciones:
        id_posicion = posicion['id']
        
        if id_posicion > id_mayor:
            id_mayor = id_posicion 
    
    return id_mayor + 1

def obtener_fecha_actual():
    
    fecha = datetime.now()
    fecha_formateada = fecha.strftime("%d/%m/%Y %H:%M")

    return fecha_formateada

def crear_posicion(posiciones,activo):
    
    posicion_id = generar_id_posicion(posiciones)
    fecha_apertura = obtener_fecha_actual()
    
    nueva_posicion = {
    'id': posicion_id,
    'activo': activo,
    'estado': 'ABIERTA',
    'fecha_apertura': fecha_apertura,
    'fecha_cierre': None
    }
    
    posiciones.append(nueva_posicion)
    
    return nueva_posicion

def obtener_posicion_por_id(posiciones, id_posicion): 
    
    for posicion in posiciones:
        if id_posicion == posicion['id']:
            return posicion
    return None