from posiciones import (
    obtener_posicion_por_id
)
from calculos import (
    generar_resumen_posicion
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

def validar_edicion_venta(operaciones, posiciones, operacion, nueva_cantidad):
    
    posicion_id = operacion["posicion_id"]
    
    resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
    
    cantidad_disponible = (resumen["cantidad_actual"] + operacion["cantidad"])
    
    if nueva_cantidad > cantidad_disponible:
        print("No puede vender más de la cantidad disponible.")
        return False
    
    return True

def tiene_ventas_asociadas(operaciones, operacion):
    
    for operacion_actual in operaciones:   
        if operacion_actual["tipo"] == "venta" and operacion_actual["posicion_id"] == operacion["posicion_id"]:
            print("No se puede realizar esta acción porque existen ventas asociadas.")
            return False
    
    return True