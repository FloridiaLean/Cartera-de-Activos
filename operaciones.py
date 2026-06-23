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

def cantidad_monedas(operaciones,activo):
    
    cantidad = 0 
    for operacion in operaciones:
        if operacion['activo'] != activo:
            continue
        if operacion['tipo'] == 'compra':
            cantidad += operacion['cantidad'] 
    return cantidad