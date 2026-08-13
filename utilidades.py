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
    resumen["ppc_formateado"] = formatear_dinero(resumen["precio_promedio"])
    resumen["ganancia_realizada_formateada"] = formatear_dinero(resumen["ganancia_realizada"])
    resumen["capital_recuperado_formateado"] = formatear_dinero(resumen["capital_recuperado"])
    
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
    resumen["precio_promedio_formateado"] = formatear_dinero(resumen["precio_promedio"])
    resumen["capital_invertido_formateado"] = formatear_dinero(resumen["capital_invertido_actual"])
    
    return resumen

def formatear_tarjeta_activo(tarjeta):
    
    tarjeta["ganancia_realizada"] = formatear_dinero(tarjeta["ganancia_realizada"])
    tarjeta["rentabilidad"] = formatear_porcentaje(tarjeta["rentabilidad"])
    
    return tarjeta

def formatear_dashboard(dashboard):

    dashboard["capital_invertido_formateado"] = formatear_dinero(dashboard["capital_invertido"])
    dashboard["ganancia_realizada_formateada"] = formatear_dinero(dashboard["ganancia_realizada"])
    dashboard["liquidez_formateada"] = formatear_dinero(dashboard["liquidez"])
    
    return dashboard

def leer_float(mensaje,permitir_cancelar=False):
    
    while True:
        try:
            numero = float(input(mensaje))
            
            if permitir_cancelar and numero == 0:
                return None 
            
            return numero
        
        except ValueError:
            print("Debe ingresar un número válido.")

def leer_int(mensaje,permitir_cancelar=False):
    
    while True:
        try:
            numero = int(input(mensaje))
            
            if permitir_cancelar and numero == 0:
                return None
            return numero
        
        except ValueError:
            print("Debe ingresar un número entero.")

def leer_texto(mensaje,permitir_cancelar=False):

    while True:

        texto = input(mensaje).strip()

        if permitir_cancelar and texto == "0":
            return None

        if texto == "":
            print("Debe ingresar un texto válido.")
            continue

        return texto

def pausar():
    input("\nPresione ENTER para continuar...")