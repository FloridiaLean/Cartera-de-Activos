from operaciones import (
    obtener_operaciones_por_activo,
    obtener_operaciones_por_posicion,
    obtener_activos
)
from posiciones import (
    obtener_posicion_por_id,
    obtener_posiciones_cerradas_por_activo
)
from datetime import date

def calcular_duracion_posicion(posicion):
    
    fecha_apertura = date.fromisoformat(posicion["fecha_apertura"])
    
    if posicion["fecha_cierre"] is None:
        fecha_fin = date.today()
    else:
        fecha_fin = date.fromisoformat(posicion["fecha_cierre"])
    
    return (fecha_fin - fecha_apertura).days

def calcular_capital_invertido(resumenes):
    
    capital_invertido = 0 
    
    for resumen in resumenes:
        capital_invertido += resumen['capital_invertido_actual']
    
    return capital_invertido

def calcular_capital_historico(resumenes):
    
    capital = 0
    
    for resumen in resumenes:
        capital += resumen["capital_historico"]
    
    return capital

def calcular_ganancia_realizada(resumenes):
    
    ganancia_realizada = 0 
    
    for resumen in resumenes:
        ganancia_realizada += resumen['ganancia_realizada']
    
    return ganancia_realizada

def calcular_cantidad_posiciones(resumenes):
    
    return len(resumenes)

def calcular_liquidez(configuracion,dashboard):
    
    capital_inicial = configuracion["capital_inicial"]
    capital_invertido = dashboard["capital_invertido"]
    ganancia_realizada = dashboard["ganancia_realizada"]
    
    liquidez = (capital_inicial - capital_invertido + ganancia_realizada)
    
    return liquidez

def calcular_rentabilidad(ganancia_realizada,capital_historico):
    
    if capital_historico == 0:
        rentabilidad = 0
    else:
        rentabilidad = (ganancia_realizada / capital_historico) * 100
    return rentabilidad

def analizar_operaciones(operaciones):
    
    capital_historico = 0
    cantidad_total = 0
    cantidad_actual = 0
    capital_recuperado = 0
    
    ventas = []
    
    for operacion in operaciones:
        if operacion['tipo'] == 'compra':
            capital_historico += operacion['monto_invertido']
            cantidad_total += operacion['cantidad']
            cantidad_actual += operacion['cantidad']
        else:
            cantidad_actual -= operacion['cantidad']
            capital_recuperado += operacion['monto_recibido']
            ventas.append(operacion)
            
    if cantidad_total == 0:
        precio_promedio = 0 
    else:
        precio_promedio = capital_historico / cantidad_total   
    
    capital_invertido_actual = cantidad_actual * precio_promedio
    ganancia_realizada = 0
    
    for venta in ventas:
            ganancia_realizada += (venta['precio_venta'] - precio_promedio) * venta['cantidad']
    
    rentabilidad = calcular_rentabilidad(ganancia_realizada,capital_historico)
    
    return {
    "capital_historico": float(capital_historico),
    "capital_invertido_actual": float(capital_invertido_actual),
    "cantidad_total": float(cantidad_total),
    "cantidad_actual": float(cantidad_actual),
    "capital_recuperado": float(capital_recuperado),
    "precio_promedio": float(precio_promedio),
    'ganancia_realizada': float(ganancia_realizada),
    "rentabilidad": float(rentabilidad)
}

def analizar_posicion(operaciones,posicion_id):
    
    operaciones_posicion = obtener_operaciones_por_posicion(operaciones,posicion_id)
    return analizar_operaciones(operaciones_posicion)

def analizar_activo(operaciones,activo):
    
    operaciones_activo = obtener_operaciones_por_activo(operaciones,activo)
    return analizar_operaciones(operaciones_activo)

def generar_resumen_activo(operaciones,activo):
    
    operaciones_activo = obtener_operaciones_por_activo(operaciones,activo)
    if len(operaciones_activo) == 0:
        return None
    
    analisis = analizar_operaciones(operaciones_activo)
    
    resumen = {
        'activo': activo,
        'capital_historico': analisis['capital_historico'],
        'cantidad_actual': analisis['cantidad_actual'],
        'precio_promedio': analisis['precio_promedio'],
        'capital_recuperado': analisis['capital_recuperado'],
        'ganancia_realizada': analisis['ganancia_realizada']
    }
    return resumen

def generar_resumen_cartera(operaciones):
    
    resumenes = []
    
    activos = obtener_activos(operaciones)
    
    for activo in activos:
        resumen = generar_resumen_activo(operaciones,activo)
        resumenes.append(resumen)
    
    return resumenes

def generar_resumen_posicion(operaciones,posiciones,posicion_id):
    
    posicion = obtener_posicion_por_id(posiciones,posicion_id)
    
    if posicion is None:
        return None
    
    analisis = analizar_posicion(operaciones,posicion_id)
    
    duracion = calcular_duracion_posicion(posicion)
    
    resumen = {
        'posicion': posicion_id,
        'activo': posicion['activo'],
        'estado': posicion['estado'],
        'fecha_apertura': posicion['fecha_apertura'],
        'fecha_cierre': posicion['fecha_cierre'],
        'duracion': duracion,
        'capital_historico': analisis['capital_historico'],
        'capital_invertido_actual': analisis['capital_invertido_actual'],
        'cantidad_actual': analisis['cantidad_actual'],
        'cantidad_total': analisis['cantidad_total'],
        'precio_promedio': analisis['precio_promedio'],
        'capital_recuperado': analisis['capital_recuperado'],
        'ganancia_realizada': analisis['ganancia_realizada'],
        'rentabilidad': analisis['rentabilidad']
    }
    return resumen

def generar_resumen_todas_posiciones(operaciones,posiciones):
    
    resumenes = []
    
    for posicion in posiciones:
        resumen = generar_resumen_posicion(operaciones,posiciones,posicion['id'])
        resumenes.append(resumen)
    
    return resumenes

def generar_resumen_dashboard(resumenes_abiertas,resumenes_todas,configuracion):

    dashboard = {
        
        "capital_invertido": calcular_capital_invertido(resumenes_abiertas),
        "ganancia_realizada": calcular_ganancia_realizada(resumenes_todas),
        "cantidad_posiciones": calcular_cantidad_posiciones(resumenes_todas),
        "cantidad_posiciones_abiertas": calcular_cantidad_posiciones(resumenes_abiertas)
    }
    
    dashboard["liquidez"] = calcular_liquidez(configuracion, dashboard)
    
    return dashboard

def generar_tarjeta_activo(activo,operaciones,posiciones):
    
    posiciones_cerradas = obtener_posiciones_cerradas_por_activo(posiciones,activo)
    
    if len(posiciones_cerradas) == 0:
        return None
    
    resumenes = generar_resumen_todas_posiciones(operaciones,posiciones_cerradas)
    
    ganancia_realizada = calcular_ganancia_realizada(resumenes)
    capital_historico = calcular_capital_historico(resumenes)
    rentabilidad = calcular_rentabilidad(ganancia_realizada,capital_historico)
        
    return {
    "activo": activo,
    "ganancia_realizada": ganancia_realizada,
    "rentabilidad": rentabilidad
}

def generar_tarjetas_activos(operaciones,posiciones):

    tarjetas = []
    
    activos = obtener_activos(operaciones)
    
    for activo in activos:
    
        tarjeta = generar_tarjeta_activo(activo,operaciones,posiciones)
        
        if tarjeta is not None:
            tarjetas.append(tarjeta)
    
    return tarjetas

def generar_resumen_activos_abiertos(resumenes_abiertas):

    activos = []
    resumenes = []
    
    for resumen in resumenes_abiertas:
    
        activo = resumen["activo"]
        
        if activo not in activos:
            activos.append(activo)
    
    for activo in activos:
    
        cantidad_actual = 0
        capital_invertido = 0
        
        for resumen in resumenes_abiertas:
        
            if resumen["activo"] == activo:
            
                cantidad_actual += resumen["cantidad_actual"]
                capital_invertido += resumen["capital_invertido_actual"]
        
        if cantidad_actual == 0:
            precio_promedio = 0
        else:
            precio_promedio = capital_invertido / cantidad_actual
        
        resumen = {
            "activo": activo,
            "cantidad_actual": cantidad_actual,
            "capital_invertido_actual": capital_invertido,
            "precio_promedio": precio_promedio
        }
        
        resumenes.append(resumen)
    
    return resumenes