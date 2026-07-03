from calculos import (
    generar_resumen_activo,
    generar_resumen_cartera,
    generar_resumen_posicion
)
from servicios import (
    registrar_venta,
    registrar_compra
)
from posiciones import (
    cerrar_posicion
)
from visualizacion import (
    mostrar_resumen_posicion
)
from persistencia import (
    cargar_posiciones,
    cargar_operaciones
)

operaciones = cargar_operaciones()
posiciones = cargar_posiciones()

# Crear posición y agregar compras

#registrar_compra(operaciones,posiciones,None,"BTC",25,79287.05)
#registrar_compra(operaciones,posiciones,1,"BTC",25,77243.94)
#registrar_compra(operaciones,posiciones,1,"BTC",100,76311.99)
#registrar_compra(operaciones,posiciones,1,"BTC",25,74464.30)
#registrar_compra(operaciones,posiciones,1,"BTC",25,71837)
#registrar_compra(operaciones,posiciones,1,"BTC",25,68830.50)
#registrar_compra(operaciones,posiciones,1,"BTC",25,59714.33)



resumen = generar_resumen_posicion(operaciones,posiciones,1)
resumen_posicion = mostrar_resumen_posicion(resumen)


