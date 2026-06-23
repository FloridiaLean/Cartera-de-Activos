from operaciones import (
    obtener_operaciones_por_activo,
    obtener_activos,
    obtener_cantidad_total,
    obtener_cantidad_actual
)

def calcular_capital_invertido(operaciones,activo):
    
    capital_invertido = 0
    for operacion in obtener_operaciones_por_activo(operaciones,activo):
        if operacion['tipo'] == 'compra': 
            capital_invertido += operacion['monto_invertido']
    return capital_invertido

def calcular_precio_promedio(operaciones,activo):
    
    capital = calcular_capital_invertido(operaciones,activo)
    cantidad = obtener_cantidad_total(operaciones,activo)
    return capital / cantidad

def calcular_capital_recuperado(operaciones,activo):
    
    capital_recuperado = 0
    for operacion in obtener_operaciones_por_activo(operaciones,activo):
        if operacion['tipo'] == 'venta':
            capital_recuperado += operacion['cantidad'] * operacion['precio_venta']
    return capital_recuperado

def calcular_ganancia_realizada(operaciones,activo):
    
    precio_promedio = calcular_precio_promedio(operaciones,activo)
    ganancia_realizada_total = 0
    
    for operacion in obtener_operaciones_por_activo(operaciones,activo):
        if operacion['tipo'] == 'venta':
            ganancia_realizada_total += (operacion['precio_venta'] - precio_promedio) * operacion['cantidad']
    return ganancia_realizada_total 

def generar_resumen_activo(operaciones,activo):
    
    cantidad_actual = obtener_cantidad_actual(operaciones,activo)
    monto_invertido = calcular_capital_invertido(operaciones,activo)
    precio_promedio = calcular_precio_promedio(operaciones,activo)
    capital_recuperado = calcular_capital_recuperado(operaciones,activo)
    ganancia_realizada = calcular_ganancia_realizada(operaciones,activo)
    
    resumen = {
        'activo': activo,
        'monto_invertido': monto_invertido,
        'cantidad_actual': cantidad_actual,
        'precio_promedio': precio_promedio,
        'capital_recuperado': capital_recuperado,
        'ganancia_realizada': ganancia_realizada
    }
    return resumen

def generar_resumen_cartera(operaciones):
    
    resumenes = []
    
    activos = obtener_activos(operaciones)
    
    for activo in activos:
        resumen = generar_resumen_activo(operaciones,activo)
        resumenes.append(resumen)
    return resumenes