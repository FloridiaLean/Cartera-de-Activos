from datetime import datetime

def generar_id(operaciones):
    
    id_mayor = 0 
    
    for operacion in operaciones:
        id_operacion = operacion['id']
        
        if id_operacion > id_mayor:
            id_mayor = id_operacion 
    
    return id_mayor + 1

def obtener_fecha_actual():
    
    fecha = datetime.now()
    fecha_formateada = fecha.strftime("%d/%m/%Y %H:%M")

    return fecha_formateada

def agregar_compra(operaciones,activo,monto_invertido,precio_compra):
    
    cantidad = monto_invertido / precio_compra
    
    id_operacion = generar_id(operaciones)
    fecha = obtener_fecha_actual()
    
    nueva_operacion = {
        'id': id_operacion,
        'fecha': fecha,
        'tipo' : 'compra',
        'activo': activo,
        'monto_invertido' : float(monto_invertido),
        'precio_compra' : float(precio_compra),
        'cantidad' : float(cantidad)
    }
    operaciones.append(nueva_operacion)
    return True

def agregar_venta(operaciones,activo,cantidad,precio_venta):
    
    monto_recibido = cantidad * precio_venta
    
    id_operacion = generar_id(operaciones)
    fecha = obtener_fecha_actual()
    
    nueva_operacion = {
            'id': id_operacion,
            'fecha': fecha,
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

def obtener_activos(operaciones):
    
    activos = []
    
    for operacion in operaciones:
        if operacion['activo'] not in activos:
            activos.append(operacion['activo'])
    return activos