from operaciones import (
    agregar_venta,
    agregar_compra,
    editar_compra,
    editar_venta,
    eliminar_operacion,
    obtener_operaciones_por_posicion
)
from calculos import (
    analizar_activo,
    analizar_posicion,
    generar_resumen_posicion
)
from posiciones import (
    crear_posicion,
    cerrar_posicion,
    reabrir_posicion,
    obtener_posicion_por_id,
    eliminar_posicion
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
    validar_venta,
    validar_edicion_venta,
    tiene_ventas_asociadas
)
from persistencia import (
    guardar_operaciones,
    guardar_posiciones
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
    
    guardar_operaciones(operaciones)
    guardar_posiciones(posiciones)
    
    return True
    
def registrar_venta(operaciones,posiciones,posicion_id,activo,cantidad,precio_venta):
    
    activo = normalizar_activo(activo)
    
    if not validar_activo(activo):
        return False
    
    if not validar_cantidad(cantidad):
        return False
    
    if not validar_precio(precio_venta):
        return False
    
    posicion = validar_posicion(posiciones, posicion_id, activo)
    
    if posicion is None:
        return False
    id_posicion = posicion['id']
    
    analisis = analizar_posicion(operaciones,id_posicion)
    
    if not validar_venta(analisis,cantidad):
        print("No tiene la cantidad suficiente para realizar esta venta")
        return False
    
    agregar_venta(operaciones,id_posicion,activo,cantidad,precio_venta)
    
    actualizar_estado_posicion(operaciones,posiciones,posicion_id)
    
    guardar_operaciones(operaciones)
    guardar_posiciones(posiciones)
    
    return True

def editar_compra_servicio(operaciones,operacion,monto_invertido,precio_compra):
    
    if not validar_monto(monto_invertido):
        return False

    if not validar_precio(precio_compra):
        return False
    
    if not tiene_ventas_asociadas(operaciones, operacion):
            return False
    
    editar_compra(operacion,monto_invertido,precio_compra)
    
    guardar_operaciones(operaciones)
    
    return True

def editar_venta_servicio(operaciones,posiciones,operacion,cantidad,precio_venta):
    
    posicion_id = operacion["posicion_id"]
    
    if not validar_cantidad(cantidad):
        return False
    
    if not validar_precio(precio_venta):
        return False
    
    if not validar_edicion_venta(operaciones,posiciones,operacion,cantidad):
        return False
    
    editar_venta(operacion,cantidad,precio_venta)
    actualizar_estado_posicion(operaciones,posiciones,posicion_id)
    guardar_operaciones(operaciones)
    
    return True

def eliminar_operacion_servicio(operaciones,posiciones,operacion):
    
    posicion_id = operacion["posicion_id"]
    
    if operacion["tipo"] == "compra":
        
        if not tiene_ventas_asociadas(operaciones, operacion):
            return False
    
    eliminar_operacion(operaciones,operacion)
    
    operaciones_posicion = obtener_operaciones_por_posicion(operaciones,posicion_id)
    
    if not operaciones_posicion:
        posicion = obtener_posicion_por_id(posiciones, posicion_id)
        eliminar_posicion(posiciones,posicion)
    else:
        actualizar_estado_posicion(operaciones,posiciones,posicion_id)
    
    guardar_operaciones(operaciones)
    guardar_posiciones(posiciones)
    
    return True

def actualizar_estado_posicion(operaciones,posiciones,posicion_id):
    
    resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
    posicion = obtener_posicion_por_id(posiciones, posicion_id)
    
    if resumen["cantidad_actual"] <= 1e-8:
        cerrar_posicion(posicion)
    else:
        reabrir_posicion(posicion)