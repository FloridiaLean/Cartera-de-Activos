from utilidades import obtener_fecha_actual

def generar_id(operaciones):
    
    id_mayor = 0 
    
    for operacion in operaciones:
        id_operacion = operacion['id']
        
        if id_operacion > id_mayor:
            id_mayor = id_operacion 
    
    return id_mayor + 1

def agregar_compra(operaciones,posicion_id,activo,monto_invertido,precio_compra):
    
    cantidad = monto_invertido / precio_compra
    
    id_operacion = generar_id(operaciones)
    fecha = obtener_fecha_actual()
    
    nueva_operacion = {
        'id': id_operacion,
        'fecha': fecha,
        'posicion_id': posicion_id,
        'tipo' : 'compra',
        'activo': activo,
        'monto_invertido' : float(monto_invertido),
        'precio_compra' : float(precio_compra),
        'cantidad' : float(cantidad)
    }
    operaciones.append(nueva_operacion)
    return True

def agregar_venta(operaciones,posicion_id,activo,cantidad,precio_venta):
    
    monto_recibido = cantidad * precio_venta
    
    id_operacion = generar_id(operaciones)
    fecha = obtener_fecha_actual()
    
    nueva_operacion = {
            'id': id_operacion,
            'fecha': fecha,
            'posicion_id': posicion_id,
            'tipo': 'venta',
            'activo': activo,
            'cantidad': float(cantidad),
            'precio_venta': float(precio_venta),
            'monto_recibido' : float(monto_recibido)
        }
    operaciones.append(nueva_operacion)
    return True

def obtener_operaciones_por_activo(operaciones,activo):
    
    operaciones_del_activo = []
    
    for operacion in operaciones:
        if activo == operacion['activo']:
            operaciones_del_activo.append(operacion)
    
    return operaciones_del_activo

def obtener_operaciones_por_posicion(operaciones,posicion_id):
    
    operaciones_de_posicion = []
    
    for operacion in operaciones:
        if operacion['posicion_id'] == posicion_id:
            operaciones_de_posicion.append(operacion)
    return operaciones_de_posicion

def obtener_activos(operaciones):
    
    activos = []
    
    for operacion in operaciones:
        if operacion['activo'] not in activos:
            activos.append(operacion['activo'])
    return activos

def obtener_operacion_por_id(operaciones,operacion_id):
    
    for operacion in operaciones:
        if operacion_id == operacion['id']:
            return operacion
    return None

def editar_compra(operacion,monto_invertido,precio_compra):
    
    operacion["monto_invertido"] = monto_invertido  
    operacion["precio_compra"] = precio_compra 
    operacion["cantidad"] = monto_invertido / precio_compra

def editar_venta(operacion, cantidad, precio_venta):
    
    operacion["cantidad"] = cantidad
    operacion["precio_venta"] = precio_venta
    operacion["monto_recibido"] = cantidad * precio_venta