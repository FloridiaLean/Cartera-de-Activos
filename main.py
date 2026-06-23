from operaciones import (
    agregar_compra,
    agregar_venta,
    obtener_activos
)

from calculos import (
    generar_resumen_activo,
    generar_resumen_cartera
)

operaciones = []

agregar_compra(operaciones, "BTC", 1000, 50000)
agregar_compra(operaciones, "ETH", 500, 2500)

print(generar_resumen_cartera(operaciones))