from datetime import datetime

def obtener_fecha_actual():
    
    fecha = datetime.now()
    fecha_formateada = fecha.strftime("%d/%m/%Y %H:%M")
    
    return fecha_formateada

def normalizar_activo(activo):
    
    activo_normalizado = activo.strip().upper()
    
    return activo_normalizado

def formatear_dinero(valor):
    
    valor_formateado = f"${valor:,.2f}"
    
    return valor_formateado

def formatear_por_magnitud(valor):
    
    decimales = 2 if abs(valor) >= 10 else 8
    
    return f"${valor:,.{decimales}f}"

def formatear_cantidad(cantidad,activo):
    
    cantidad_formateada = f"{cantidad:.8f} {activo}"
    
    return cantidad_formateada

def formatear_porcentaje(porcentaje):

    porcentaje_formateado = f"{porcentaje:.2f}%"
    
    return porcentaje_formateado

def formatear_fecha(fecha):

    if fecha is None:
        return "-"
    
    return fecha

def formatear_resumen_posicion(resumen):
    
    resumen["capital_historico_formateado"] = formatear_dinero(resumen["capital_historico"])
    resumen["capital_invertido_formateado"] = formatear_dinero(resumen["capital_invertido_actual"])
    resumen["cantidad_formateada"] = formatear_cantidad(resumen["cantidad_actual"],resumen["activo"])
    resumen["ppc_formateado"] = formatear_por_magnitud(resumen["precio_promedio"])
    resumen["ganancia_realizada_formateada"] = formatear_dinero(resumen["ganancia_realizada"])
    resumen["capital_recuperado_formateado"] = formatear_dinero(resumen["capital_recuperado"])
    resumen["break_even_formateado"] = formatear_por_magnitud(resumen["precio_break_even"])
    resumen["rentabilidad_formateada"] = formatear_porcentaje(resumen["rentabilidad"])
    if resumen["estado"] == "ABIERTA":
        resumen["duracion_formateada"] = f"En curso hace: {resumen['duracion']} días"
    else:
        resumen["duracion_formateada"] = f"Duración: {resumen['duracion']} días"
    
    return resumen

def formatear_operacion(operacion):
    
    operacion["cantidad_formateada"] = formatear_cantidad(operacion["cantidad"],operacion["activo"])
    operacion["fecha_formateada"] = formatear_fecha(operacion["fecha"])
    
    if operacion["tipo"] == "compra":
        operacion["precio_formateado"] = formatear_dinero(operacion["precio_compra"])
        operacion["monto_formateado"] = formatear_dinero(operacion["monto_invertido"])
    
    else: 
        operacion["precio_formateado"] = formatear_dinero(operacion["precio_venta"])
        operacion["monto_formateado"] = formatear_dinero(operacion["monto_recibido"])
    
    return operacion

def formatear_resumen_activo(resumen):
    
    resumen["cantidad_formateada"] = formatear_cantidad(resumen["cantidad_actual"],resumen["activo"])
    resumen["precio_promedio_formateado"] = formatear_por_magnitud(resumen["precio_promedio"])
    resumen["capital_invertido_formateado"] = formatear_dinero(resumen["capital_invertido_actual"])
    resumen["asignacion_formateada"] = formatear_porcentaje(resumen["asignacion"])
    
    return resumen

def formatear_tarjeta_activo(tarjeta):
    
    tarjeta["ganancia_realizada_formateada"] = formatear_dinero(tarjeta["ganancia_realizada"])
    tarjeta["rentabilidad_formateada"] = formatear_porcentaje(tarjeta["rentabilidad"])
    
    return tarjeta

def formatear_dashboard(dashboard):

    dashboard["capital_invertido_formateado"] = formatear_dinero(dashboard["capital_invertido"])
    dashboard["ganancia_realizada_formateada"] = formatear_dinero(dashboard["ganancia_realizada"])
    dashboard["liquidez_formateada"] = formatear_dinero(dashboard["liquidez"])
    
    return dashboard