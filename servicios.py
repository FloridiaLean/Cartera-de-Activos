from operaciones import (
    agregar_venta,
    agregar_compra,
    obtener_operaciones_por_activo
)

from calculos import (
    analizar_activo,
    validar_venta
)

def registrar_compra(operaciones,activo,monto_invertido,precio_compra):
    
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
    
    agregar_compra(operaciones,activo,monto_invertido,precio_compra)
    
    return True
    
def registrar_venta(operaciones,activo,cantidad,precio_venta):
    
    activo = activo.strip()
    activo = activo.upper()
    
    if activo == "":
        print("El nombre del activo no es valido")
        return False
    
    operaciones_activo = obtener_operaciones_por_activo(operaciones,activo)
    if not operaciones_activo:
        print("El activo no existe en la cartera.")
        return False
    
    analisis = analizar_activo(operaciones,activo)
    
    if cantidad <= 0:
        print("La cantidad ingresada tiene que ser mayor a 0")
        return False
    
    if precio_venta <= 0:
        print("El precio de venta del activo tiene que ser mayor a 0")
        return False
    
    if not validar_venta(analisis,cantidad):
        print("No tiene la cantidad suficiente para realizar esta venta")
        return False
    
    agregar_venta(operaciones,activo,cantidad,precio_venta)
    
    return True



