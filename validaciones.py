from posiciones import (
    obtener_posicion_por_id
)
from calculos import (
    generar_resumen_posicion
)

def validar_activo(activo):
    if activo == "":
        return False,"El nombre del activo no es válido"
    return True,None

def validar_monto(monto):
    if monto <= 0:
        return False,"El monto debe ser mayor a 0"
    return True,None

def validar_precio(precio):
    
    if precio <= 0:
        return False,"El precio unitario debe ser mayor a 0"
    return True,None

def validar_cantidad(cantidad):
    if cantidad <= 0:
        return False,"La cantidad ingresada tiene que ser mayor a 0"
    return True,None

def validar_posicion(posiciones,posicion_id):
    
    posicion = obtener_posicion_por_id(posiciones,posicion_id)
    
    if posicion is None:
        
        return False, "La posición seleccionada no existe."
    
    if posicion['estado'] != 'ABIERTA':
        
        return False, "La posición no se encuentra abierta."
    
    return True, posicion

def validar_venta(analisis,cantidad):
    
    cantidad_actual = analisis['cantidad_actual']
    
    if cantidad > cantidad_actual:
        return False, "No tienes la cantidad suficiente para realizar esta venta."
    return True, None

def validar_edicion_venta(operaciones,posiciones,operacion,nueva_cantidad):
    
    posicion_id = operacion["posicion_id"]
    
    resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
    
    cantidad_disponible = (resumen["cantidad_actual"] + operacion["cantidad"])
    
    if nueva_cantidad > cantidad_disponible:
        return False, "No puede vender más de la cantidad disponible."
    
    return True, None

def tiene_ventas_asociadas(operaciones,operacion):
    
    posicion_id = operacion["posicion_id"]
    
    for otra_operacion in operaciones: 
        
        if otra_operacion["posicion_id"] != posicion_id:
            continue
        
        if otra_operacion["tipo"] == "venta":
            return True
        
    return False

def validar_fecha(fecha_anterior,fecha):
    
    if fecha < fecha_anterior:
        return False, "La fecha ingresada no puede ser anterior a una operación ya registrada."
    return True, None

def validar_retiro_liquidez(liquidez,monto):
    
    if monto > liquidez:
        return False, "No puedes retirar más dinero del disponible."
    return True, None