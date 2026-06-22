operaciones = []

def agregar_compra(operaciones,activo,inversion,precio_compra):
    
    cantidad = inversion / precio_compra
    
    nueva_operacion = {
        'activo': activo,
        'tipo' : 'compra',
        'inversion' : float(inversion),
        'precio_compra' : float(precio_compra),
        'cantidad' : float(cantidad)
    }
    operaciones.append(nueva_operacion)

def cantidad_monedas_actual(operaciones,activo):
    
    cantidad = 0 
    for operacion in operaciones:
        if operacion['activo'] != activo:
            continue
        if operacion['tipo'] == 'compra':
            cantidad += operacion['cantidad'] 
        else:
            cantidad -= operacion['cantidad'] 
    return cantidad

def agregar_venta(operaciones,activo,cantidad,precio_venta):
    
    if cantidad > cantidad_monedas_actual(operaciones,activo):
        return False
    else:
        nueva_operacion= {
            'activo': activo,
            'tipo': 'venta',
            'cantidad': float(cantidad),
            'precio_venta': float(precio_venta)
        }
        operaciones.append(nueva_operacion)
        return True

def obtener_operaciones_activo(operaciones,activo):
    
    resultado = []
    for operacion in operaciones:
        if activo == operacion['activo']:
            resultado.append(operacion)
    return resultado

def obtener_activos(operaciones):
    activos = []
    for operacion in operaciones:
        if operacion['activo'] not in activos:
            activos.append(operacion['activo'])
    return activos

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

agregar_compra(operaciones,'BTC',100,65000)
agregar_compra(operaciones,'BTC',50,62400)
agregar_compra(operaciones,'BTC',50,60000)
agregar_compra(operaciones,'BTC',100,67000)
agregar_venta(operaciones,'BTC',0.001,70000)
agregar_venta(operaciones,'BTC',0.001,70000)

agregar_compra(operaciones,'ETH',50,1400)
agregar_compra(operaciones,'ETH',100,1300)
agregar_compra(operaciones,'ETH',50,1600)
agregar_compra(operaciones,'ETH',70,1550)
agregar_venta(operaciones,'ETH',0.001,1800)

agregar_compra(operaciones,'SOL',50,120)
agregar_compra(operaciones,'SOL',50,110)
agregar_compra(operaciones,'SOL',50,100)
agregar_compra(operaciones,'SOL',50,90)
agregar_venta(operaciones,'BTC',0.5,130)


resumen_completo = resumen_cartera(operaciones)
print(resumen_completo)
