from operaciones import (
    agregar_venta,
    agregar_compra,
)

from calculos import (
    analizar_activo,
    analizar_posicion
)

from posiciones import (
    crear_posicion,
    cerrar_posicion,
    obtener_posicion_por_id
)

from utilidades import (
    normalizar_activo
)

from validaciones import (
    validar_activo,
    validar_precio,
    validar_monto,
    validar_cantidad,
    validar_posicion,
    validar_venta
)

def registrar_compra(operaciones,posiciones,posicion_id,activo,monto_invertido,precio_compra):
    
    activo = normalizar_activo(activo)
        
    if not validar_activo(activo):
        return False
    
    if not validar_monto(monto_invertido):
        return False

    if not validar_precio(precio_compra):
        return False
    
    if posicion_id is None:
        nueva_posicion = crear_posicion(posiciones,activo)
        id_posicion = nueva_posicion['id']
    else:
        posicion = validar_posicion(posiciones, posicion_id, activo)
        
        if posicion is None:
            return False
        id_posicion = posicion['id']
            
    agregar_compra(operaciones,id_posicion,activo,monto_invertido,precio_compra)
    
    return True
    
def registrar_venta(operaciones,posiciones,posicion_id,activo,cantidad,precio_venta):
    
    activo = normalizar_activo(activo)
    
    if not validar_activo(activo):
        return False
    
    posicion = validar_posicion(posiciones, posicion_id, activo)
    
    if posicion is None:
        return False
    id_posicion = posicion['id']
    
    analisis = analizar_posicion(operaciones,id_posicion)
    
    if not validar_cantidad(cantidad):
        return False
    
    if not validar_precio(precio_venta):
        return False
    
    if not validar_venta(analisis,cantidad):
        print("No tiene la cantidad suficiente para realizar esta venta")
        return False
    
    agregar_venta(operaciones,id_posicion,activo,cantidad,precio_venta)
    
    analisis_actualizado = analizar_posicion(operaciones,id_posicion)
    if analisis_actualizado['cantidad_actual'] == 0:
        cerrar_posicion(posiciones,id_posicion)
    
    return True



