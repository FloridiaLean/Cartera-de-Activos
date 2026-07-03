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

def formatear_precio(valor):
    
    precio_formateado = f"${valor:,.2f}"
    
    return precio_formateado