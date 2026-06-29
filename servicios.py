from operaciones import agregar_venta

from calculos import (
    analizar_activo,
    validar_venta
)

def registrar_venta(operaciones,activo,cantidad,precio_venta):
    
    activo = activo.strip()
    activo = activo.upper()
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
    return True