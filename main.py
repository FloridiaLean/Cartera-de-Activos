from operaciones import (
    agregar_compra,
    agregar_venta,
    obtener_activos
)

from calculos import (
    resumen_activo,
    resumen_cartera
)

operaciones = []

agregar_compra(operaciones, "BTC", 1000, 50000)
agregar_compra(operaciones, "ETH", 500, 2500)

print(resumen_cartera(operaciones))