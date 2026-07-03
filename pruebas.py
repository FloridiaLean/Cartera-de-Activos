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
    guardar_operaciones,
    guardar_posiciones,
    cargar_posiciones,
    cargar_operaciones
)

#posiciones = []
operaciones = cargar_operaciones()

print("Antes:")
print(operaciones)

operaciones = []

print("Después de vaciar la lista:")
print(operaciones)

operaciones = cargar_operaciones()

print("Después de volver a cargar:")
print(operaciones)

# ========= PRUEBA 1 =========
# Crear posición y agregar compras

# ========= PRUEBA 2 =========
#registrar_venta(operaciones, posiciones, 1, "BTC", 0.00031531000333597984, 60000)

# ========= PRUEBA 3 =========
# Venta parcial
#registrar_venta(operaciones, posiciones, 1, "BTC", 0.002, 60000)

# ========= PRUEBA 4 =========
# Venta superior al saldo
#registrar_venta(operaciones, posiciones, 1, "BTC", 0.02, 60000)

# ========= PRUEBA 5 =========
# Activo incorrecto
#registrar_compra(operaciones, posiciones, 1, "ETH", 100, 2500)
#registrar_venta(operaciones, posiciones, 1, "ETH", 0.002, 2500)

# ========= PRUEBA 6 =========
# Posición inexistente
#registrar_compra(operaciones, posiciones, 3, "BTC", 100, 70000)



