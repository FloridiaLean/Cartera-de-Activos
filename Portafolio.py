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

agregar_compra(operaciones,'ETH',50,1000)
agregar_compra(operaciones,'BTC',50,50000)
agregar_compra(operaciones,'BTC',50,65000)
agregar_compra(operaciones,'BTC',50,67000)
agregar_venta(operaciones,'BTC',0.001,70000)

activos = obtener_activos(operaciones)
operaciones_btc = obtener_operaciones_activo(operaciones,'BTC')
cantidad_activo = cantidad_monedas_actual(operaciones,'BTC')
cantidad_total = cantidad_monedas(operaciones,'BTC')
inversion = capital_invertido(operaciones,'BTC')
promedio = precio_promedio(operaciones,'BTC')


print("----- Activos Invertidos -----")
print(activos)
print("----- Operaciones Realizadas -----")
print(operaciones_btc)
print("----- Cantidad de Activo -----")
print(cantidad_activo)
print("----- Cantidad Dinero Invertido -----")
print(inversion)
print("-----Precio Promedio de Compra -----")
print(promedio)