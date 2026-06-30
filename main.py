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

registrar_compra(operaciones, "BTC", 250, 50000 )
registrar_venta(operaciones, "BTC", 0.004, 60000)

print(generar_resumen_cartera(operaciones))