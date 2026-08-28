from utilidades import (
    normalizar_activo
)

def generar_id_posicion(posiciones):
    
    id_mayor = 0 
    
    for posicion in posiciones:
        id_posicion = posicion['id']
        
        if id_posicion > id_mayor:
            id_mayor = id_posicion 
    
    return id_mayor + 1

def crear_posicion(posiciones,activo,fecha_apertura):
    
    posicion_id = generar_id_posicion(posiciones)
    
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

def obtener_posiciones_abiertas_por_activo(posiciones,activo):
    
    posiciones_abiertas = []
    
    for posicion in posiciones:
        if posicion['activo'] == activo and posicion['estado'] == 'ABIERTA':
            posiciones_abiertas.append(posicion)
            
    return posiciones_abiertas

def reabrir_posicion(posicion):
    
    posicion["estado"] = "ABIERTA"
    posicion["fecha_cierre"] = None

def cerrar_posicion(posicion,fecha_cierre):
    
    posicion['estado'] = 'CERRADA'
    posicion['fecha_cierre'] = fecha_cierre

def eliminar_posicion(posiciones,posicion):
    
    posiciones.remove(posicion)

def obtener_posiciones_abiertas(posiciones):

    posiciones_abiertas = []
    
    for posicion in posiciones:
        if posicion["estado"] == "ABIERTA":
            posiciones_abiertas.append(posicion)
    
    return posiciones_abiertas

def obtener_posiciones_cerradas(posiciones):
    
    posiciones_cerradas = []
    
    for posicion in posiciones:
        if posicion["estado"] == "CERRADA":
            posiciones_cerradas.append(posicion)
            
    return posiciones_cerradas

def obtener_posiciones_cerradas_por_activo(posiciones,activo):
    
    activo = normalizar_activo(activo)
    
    posiciones_cerradas = []
    
    for posicion in posiciones:
        if posicion["estado"] == "CERRADA" and posicion["activo"] == activo:
            posiciones_cerradas.append(posicion)
    
    return posiciones_cerradas