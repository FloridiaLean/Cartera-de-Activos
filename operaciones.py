def agregar_compra(operaciones,activo,monto_invertido,precio_compra):
    
    cantidad = monto_invertido / precio_compra
    
    nueva_operacion = {
        'activo': activo,
        'tipo' : 'compra',
        'monto_invertido' : float(monto_invertido),
        'precio_compra' : float(precio_compra),
        'cantidad' : float(cantidad)
    }
    operaciones.append(nueva_operacion)

def agregar_venta(operaciones,activo,cantidad,precio_venta):
    
    if cantidad > obtener_cantidad_actual(operaciones,activo):
        return False
    else:
        nueva_operacion = {
            'activo': activo,
            'tipo': 'venta',
            'cantidad': float(cantidad),
            'precio_venta': float(precio_venta)
        }
        operaciones.append(nueva_operacion)
        return True

def obtener_operaciones_por_activo(operaciones,activo):
    
    operaciones_del_activo = []
    for operacion in operaciones:
        if activo == operacion['activo']:
            operaciones_del_activo.append(operacion)
    return operaciones_del_activo

def obtener_activos(operaciones):
    activos = []
    for operacion in operaciones:
        if operacion['activo'] not in activos:
            activos.append(operacion['activo'])
    return activos

def obtener_cantidad_actual(operaciones,activo):
    
    cantidad_actual = 0 
    for operacion in operaciones:
        if operacion['activo'] != activo:
            continue
        if operacion['tipo'] == 'compra':
            cantidad_actual += operacion['cantidad'] 
        else:
            cantidad_actual -= operacion['cantidad'] 
    return cantidad_actual

def obtener_cantidad_total(operaciones,activo):
    
    cantidad_total = 0 
    for operacion in operaciones:
        if operacion['activo'] != activo:
            continue
        if operacion['tipo'] == 'compra':
            cantidad_total += operacion['cantidad'] 
    return cantidad_total