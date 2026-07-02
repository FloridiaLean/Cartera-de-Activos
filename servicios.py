from operaciones import (
    agregar_venta,
    agregar_compra,
    obtener_operaciones_por_activo,
    obtener_operaciones_por_posicion
)

from calculos import (
    analizar_activo,
    analizar_posicion,
    validar_venta
)

from posiciones import (
    crear_posicion,
    obtener_posicion_por_id
)

def registrar_compra(operaciones,posiciones,posicion_id,activo,monto_invertido,precio_compra):
    
    activo = activo.strip()
    activo = activo.upper()
        
    if activo == "":
        print("El nombre del activo no es valido")
        return False
    
    if monto_invertido <= 0:
        print("El monto invertido debe ser mayor a 0")
        return False
    
    if precio_compra <= 0:
        print("El precio de compra del activo tiene que ser mayor a 0")
        return False
    
    if posicion_id is None:
        nueva_posicion = crear_posicion(posiciones,activo)
        id_posicion = nueva_posicion['id']
    else:
        posicion = obtener_posicion_por_id(posiciones,posicion_id)
        if posicion is None:
            print("La posición con el ID proporcionado no existe.")
            return False
        id_posicion = posicion['id']
        
        if posicion['activo'] != activo:
            print(f"No puede agregar una compra de {activo} a una posición de {posicion['activo']}.")
            return False
            
    agregar_compra(operaciones,id_posicion,activo,monto_invertido,precio_compra)
    
    return True
    
def registrar_venta(operaciones,posiciones,posicion_id,activo,cantidad,precio_venta):
    
    activo = activo.strip()
    activo = activo.upper()
    
    if activo == "":
        print("El nombre del activo no es valido")
        return False
    
    posicion = obtener_posicion_por_id(posiciones,posicion_id)
    if posicion is None:
        print("La posición con el ID proporcionado no existe.")
        return False
    posicion_id = posicion['id']
        
    if posicion['activo'] != activo:
        print(f"No puede agregar una venta de {activo} a una posición de {posicion['activo']}.")
        return False
    
    analisis = analizar_posicion(operaciones,posicion_id)
    
    if cantidad <= 0:
        print("La cantidad ingresada tiene que ser mayor a 0")
        return False
    
    if precio_venta <= 0:
        print("El precio de venta del activo tiene que ser mayor a 0")
        return False
    
    if not validar_venta(analisis,cantidad):
        print("No tiene la cantidad suficiente para realizar esta venta")
        return False
    
    agregar_venta(operaciones,posicion_id,activo,cantidad,precio_venta)
    
    return True



