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

