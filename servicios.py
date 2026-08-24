from operaciones import (
    agregar_venta,
    agregar_compra,
    editar_compra,
    editar_venta,
    eliminar_operacion,
    obtener_operaciones_por_posicion,
    eliminar_operaciones_por_posicion,
    obtener_ultima_operacion_por_posicion,
    obtener_fecha_apertura_posicion
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
    tiene_ventas_asociadas,
    validar_fecha_cierre,
    validar_fecha
)
from persistencia import (
    guardar_operaciones_sql,
    guardar_posiciones_sql,
    eliminar_operacion_sql,
    eliminar_operaciones_por_posicion_sql,
    eliminar_posicion_sql,
    sincronizar_operaciones_sql
)

def registrar_compra(operaciones,posiciones,posicion_id,activo,monto_invertido,precio_compra,fecha):
    
    activo = normalizar_activo(activo)
    
    valido, mensaje = validar_activo(activo)
    if not valido:
        return False, mensaje
    
    valido, mensaje = validar_monto(monto_invertido)
    if not valido:
        return False, mensaje
    
    valido, mensaje = validar_precio(precio_compra)
    if not valido:
        return False, mensaje
    
    if posicion_id is None:
        nueva_posicion = crear_posicion(posiciones,activo,fecha)
        id_posicion = nueva_posicion['id']
        
    else:
        posicion = validar_posicion(posiciones,posicion_id)
        
        if posicion is None:
            return False, "La posición seleccionada no existe."
        
        id_posicion = posicion['id']
        
        ultima_operacion = obtener_ultima_operacion_por_posicion(operaciones,id_posicion) 
        
        if ultima_operacion is not None:
            valido, mensaje = validar_fecha(ultima_operacion["fecha"],fecha)
        
        if not valido:
            return False, mensaje
    
    agregar_compra(operaciones,id_posicion,activo,monto_invertido,precio_compra,fecha)
    
    guardar_posiciones_sql(posiciones)
    guardar_operaciones_sql(operaciones)
    
    return True, None
    
def registrar_venta(operaciones,posiciones,posicion_id,cantidad,precio_venta,fecha):
    
    posicion = validar_posicion(posiciones,posicion_id)
    
    if posicion is None:
        return False, "La posición seleccionada no existe."
    
    activo = posicion["activo"]
    
    valido, mensaje = validar_cantidad(cantidad)
    if not valido:
        return False, mensaje
    
    valido, mensaje = validar_precio(precio_venta)
    if not valido:
        return False, mensaje
    
    id_posicion = posicion['id']
    
    ultima_operacion = obtener_ultima_operacion_por_posicion(operaciones,id_posicion)
    
    if ultima_operacion is not None:
        valido, mensaje = validar_fecha(ultima_operacion["fecha"],fecha)
    
    if not valido:
        return False, mensaje
    
    analisis = analizar_posicion(operaciones,id_posicion)
    
    valido, mensaje = validar_venta(analisis,cantidad)
    if not valido:
        return False, mensaje
    
    agregar_venta(operaciones,id_posicion,activo,cantidad,precio_venta,fecha)
    
    actualizar_estado_posicion(operaciones,posiciones,posicion_id,fecha)
    
    guardar_operaciones_sql(operaciones)
    guardar_posiciones_sql(posiciones)
    
    return True, None

def editar_compra_servicio(operaciones,posiciones,operacion,monto_invertido,precio_compra):
    
    valido, mensaje = validar_monto(monto_invertido)
    
    if not valido:
        return False, mensaje
    
    valido, mensaje = validar_precio(precio_compra)
    
    if not valido:
        return False, mensaje
    
    if tiene_ventas_asociadas(operaciones,operacion):
            return False, "La compra tiene ventas asociadas."
    
    editar_compra(operacion,monto_invertido,precio_compra)
    
    guardar_operaciones_sql(operaciones)
    guardar_posiciones_sql(posiciones)
    
    return True, "Compra editada correctamente."

def editar_venta_servicio(operaciones,posiciones,operacion,cantidad,precio_venta):
    
    posicion_id = operacion["posicion_id"]
    
    valido, mensaje = validar_cantidad(cantidad)
    
    if not valido:
        return False, mensaje
    
    valido, mensaje = validar_precio(precio_venta)
    
    if not valido:
        return False, mensaje
    
    valido, mensaje = validar_edicion_venta(operaciones,posiciones,operacion,cantidad)
    
    if not valido:
        return False, mensaje
    
    editar_venta(operacion,cantidad,precio_venta)
    actualizar_estado_posicion(operaciones,posiciones,posicion_id)
    
    guardar_operaciones_sql(operaciones)
    guardar_posiciones_sql(posiciones)
    
    return True, "Venta editada correctamente."

def eliminar_operacion_servicio(operaciones,posiciones,operacion):
    
    posicion_id = operacion["posicion_id"]
    
    if operacion["tipo"] == "compra":
        
        if tiene_ventas_asociadas(operaciones,operacion):
            return False, "No se puede eliminar una compra que tiene ventas asociadas."
    
    eliminar_operacion(operaciones,operacion)
    
    operaciones_posicion = obtener_operaciones_por_posicion(operaciones,posicion_id)
    
    if not operaciones_posicion:
        posicion = obtener_posicion_por_id(posiciones,posicion_id)
        
        eliminar_posicion(posiciones,posicion)
        eliminar_operaciones_por_posicion_sql(posicion_id)
        eliminar_posicion_sql(posicion_id)
        
    else:
        posicion = obtener_posicion_por_id(posiciones,posicion_id)
        
        fecha_apertura = obtener_fecha_apertura_posicion(operaciones,posicion_id)
        
        posicion["fecha_apertura"] = fecha_apertura 
        
        actualizar_estado_posicion(operaciones,posiciones,posicion_id)
    
    sincronizar_operaciones_sql(operaciones)
    guardar_posiciones_sql(posiciones)
    
    return True, "Operación eliminada correctamente."

def actualizar_estado_posicion(operaciones,posiciones,posicion_id):
    
    resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
    posicion = obtener_posicion_por_id(posiciones,posicion_id)
    operaciones_posicion = obtener_operaciones_por_posicion(operaciones,posicion_id)
    
    if not operaciones_posicion:
        return
    
    compras = [operacion for operacion in operaciones_posicion if operacion["tipo"] == "compra"]
    
    if compras:
        fecha_apertura = min(compra["fecha"] for compra in compras)
        
        posicion["fecha_apertura"] = fecha_apertura
        
    if resumen["cantidad_actual"] <= 1e-8:
        
        ventas = [operacion for operacion in operaciones_posicion if operacion["tipo"] == "venta"]
        
        if ventas:
            fecha_cierre = max(venta["fecha"] for venta in ventas)
            
            cerrar_posicion(posicion,fecha_cierre)
    else:
        reabrir_posicion(posicion)

def eliminar_posicion_servicio(operaciones,posiciones,posicion):
    
    posicion_id = posicion["id"]
    
    eliminar_operaciones_por_posicion(operaciones,posicion_id)
    
    eliminar_posicion(posiciones,posicion)
    
    eliminar_operaciones_por_posicion_sql(posicion_id)
    eliminar_posicion_sql(posicion_id)
    
    return True