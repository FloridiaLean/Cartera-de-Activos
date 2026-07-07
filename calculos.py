from operaciones import (
    obtener_operaciones_por_activo,
    obtener_operaciones_por_posicion,
    obtener_activos,
)
from posiciones import (
    obtener_posicion_por_id
)

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
    
    ganancia_realizada = 0
    for venta in ventas:
            ganancia_realizada += (venta['precio_venta'] - precio_promedio) * venta['cantidad']
    
    return {
    "capital_historico": float(capital_historico),
    "cantidad_total": float(cantidad_total),
    "cantidad_actual": float(cantidad_actual),
    "capital_recuperado": float(capital_recuperado),
    "precio_promedio": float(precio_promedio),
    'ganancia_realizada': float(ganancia_realizada),
}

def analizar_posicion(operaciones,posicion_id):
    
    operaciones_posicion = obtener_operaciones_por_posicion(operaciones,posicion_id)
    return analizar_operaciones(operaciones_posicion)

def analizar_activo(operaciones,activo):
    
    operaciones_activo = obtener_operaciones_por_activo(operaciones,activo)
    
    return analizar_operaciones(operaciones_activo)

def generar_resumen_activo(operaciones,activo):
    
    operaciones_activo = obtener_operaciones_por_activo(operaciones, activo)
    if len(operaciones_activo) == 0:
        return None
    
    analisis = analizar_operaciones(operaciones)
    
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
    
    if posicion is None:
        return None
    
    resumen = {
        'posicion': posicion_id,
        'activo': posicion['activo'],
        'estado': posicion['estado'],
        'fecha_apertura': posicion['fecha_apertura'],
        'fecha_cierre': posicion['fecha_cierre'],
        'capital_historico': analisis['capital_historico'],
        'cantidad_actual': analisis['cantidad_actual'],
        'cantidad_total': analisis['cantidad_total'],
        'precio_promedio': analisis['precio_promedio'],
        'capital_recuperado': analisis['capital_recuperado'],
        'ganancia_realizada': analisis['ganancia_realizada']
    }
    return resumen

def generar_resumen_todas_posiciones(operaciones,posiciones):
    
    resumenes = []
    
    for posicion in posiciones:
        resumen = generar_resumen_posicion(operaciones,posiciones,posicion['id'])
        resumenes.append(resumen)
    
    return resumenes
