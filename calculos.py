from operaciones import (
    obtener_operaciones_activo,
    obtener_activos,
    cantidad_monedas,
    cantidad_monedas_actual
)

def cantidad_monedas(operaciones,activo):
    
    cantidad = 0 
    for operacion in operaciones:
        if operacion['activo'] != activo:
            continue
        if operacion['tipo'] == 'compra':
            cantidad += operacion['cantidad'] 
    return cantidad

def capital_invertido(operaciones,activo):
    
    capital = 0
    for operacion in obtener_operaciones_activo(operaciones,activo):
        if operacion['tipo'] == 'compra': 
            capital += operacion['inversion']
    return capital

def precio_promedio(operaciones,activo):
    capital = capital_invertido(operaciones,activo)
    cantidad = cantidad_monedas(operaciones,activo)
    return capital / cantidad

def capital_recuperado(operaciones,activo):
    
    capital = 0
    for operacion in obtener_operaciones_activo(operaciones,activo):
        if operacion['tipo'] == 'venta':
            capital += operacion['cantidad'] * operacion['precio_venta']
    return capital

def ganancia_realizada(operaciones,activo):
    
    precio_prom = precio_promedio(operaciones,activo)
    ganancia_venta = 0
    for operacion in obtener_operaciones_activo(operaciones,activo):
        if operacion['tipo'] == 'venta':
            ganancia_venta += (operacion['precio_venta'] - precio_prom) * operacion['cantidad']
    return ganancia_venta 

def resumen_activo(operaciones,activo):
    
    cantidad_actual = cantidad_monedas_actual(operaciones,activo)
    inversion = capital_invertido(operaciones,activo)
    promedio = precio_promedio(operaciones,activo)
    recuperado = capital_recuperado(operaciones,activo)
    ganancia = ganancia_realizada(operaciones,activo)
    
    resumen = {
        'activo': activo,
        'capital_invertido': inversion,
        'cantidad_actual': cantidad_actual,
        'precio_promedio': promedio,
        'capital_recuperado': recuperado,
        'ganancia_realizada': ganancia
    }
    return resumen

def resumen_cartera(operaciones):
    
    resumenes = []
    
    activos = obtener_activos(operaciones)
    
    for activo in activos:
        resumen = resumen_activo(operaciones,activo)
        resumenes.append(resumen)
    return resumenes