from operaciones import (
    agregar_compra,
    agregar_venta,
    obtener_activos
)
from calculos import (
    generar_resumen_activo,
    generar_resumen_cartera
)
from servicios import (
    registrar_venta,
    registrar_compra
)

operaciones = []
posiciones = []

registrar_compra(operaciones,posiciones,None,"BTC",250,50000)
registrar_compra(operaciones,posiciones,1,"BTC",100,70000)
registrar_compra(operaciones,posiciones,3,"BTC",100,70000)

print(posiciones)
print(operaciones)