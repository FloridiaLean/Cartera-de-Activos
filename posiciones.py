from utilidades import obtener_fecha_actual

def generar_id_posicion(posiciones):
    
    id_mayor = 0 
    
    for posicion in posiciones:
        id_posicion = posicion['id']
        
        if id_posicion > id_mayor:
            id_mayor = id_posicion 
    
    return id_mayor + 1

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

def obtener_posicion_por_id(posiciones,posicion_id): 
    
    for posicion in posiciones:
        if posicion_id == posicion['id']:
            return posicion
    return None

def cerrar_posicion(posiciones,posicion_id):
    
    posicion = obtener_posicion_por_id(posiciones,posicion_id)
    
    if  posicion is None:
        print("Posición no encontrada")
        return None
    
    posicion['estado'] = 'CERRADA'
    posicion['fecha_cierre'] = obtener_fecha_actual()
    
    return posicion

def obtener_posicion_abierta_por_activo(posiciones,activo):
    
    for posicion in posiciones:
        if posicion['activo'] == activo and posicion['estado'] == 'ABIERTA':
            return posicion
    return None

def obtener_posiciones_abiertas_por_activo(posiciones,activo):
    
    posiciones_abiertas = []
    
    for posicion in posiciones:
        if posicion['activo'] == activo and posicion['estado'] == 'ABIERTA':
            posiciones_abiertas.append(posicion)
    return posiciones_abiertas