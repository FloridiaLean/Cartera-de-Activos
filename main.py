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
from menu import (
    menu_principal
)

operaciones = cargar_operaciones()
posiciones = cargar_posiciones()


menu_principal(operaciones,posiciones)


