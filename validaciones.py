from posiciones import (
    obtener_posicion_por_id
)

def validar_activo(activo):
    if activo == "":
        print("El nombre del activo no es válido")
        return False
    return True

def validar_monto(monto):
    if monto <= 0:
        print("El monto invertido debe ser mayor a 0")
        return False
    return True

def validar_precio(precio):
    
    if precio <= 0:
        print("El precio debe ser mayor a 0")
        return False
    return True

def validar_cantidad(cantidad):
    if cantidad <= 0:
        print("La cantidad ingresada tiene que ser mayor a 0")
        return False
    return True

def validar_posicion(posiciones,posicion_id,activo):
    
    posicion = obtener_posicion_por_id(posiciones,posicion_id)
        
    if posicion is None:
        print("La posición con el ID proporcionado no existe.")
        return None
        
    if posicion['estado'] != 'ABIERTA':
        print("La posición no se encuentra abierta.")
        return None
        
    if posicion['activo'] != activo:
        print(f"El activo {activo} no coincide con el activo de la posición ({posicion['activo']}).")
        return None
    
    return posicion

def validar_venta(analisis,cantidad):
    
    cantidad_actual = analisis['cantidad_actual']
    
    if cantidad > cantidad_actual:
        return False
    return True