from calculos import (
    generar_resumen_activo,
    generar_resumen_cartera
)
from servicios import (
    registrar_venta,
    registrar_compra
)
from posiciones import (
    cerrar_posicion
)

operaciones = []
posiciones = []

# ========= PRUEBA 1 =========
# Crear posición y agregar compras
registrar_compra(operaciones,posiciones,None,"BTC",25,79287.05)
#registrar_compra(operaciones,posiciones,1,"BTC",25,77243.94)
#registrar_compra(operaciones,posiciones,1,"BTC",100,76311.99)
#registrar_compra(operaciones,posiciones,1,"BTC",25,74464.30)
#registrar_compra(operaciones,posiciones,1,"BTC",25,71837)
#registrar_compra(operaciones,posiciones,1,"BTC",25,68830.50)
#registrar_compra(operaciones,posiciones,1,"BTC",25,59714.33)

# ========= PRUEBA 2 =========
registrar_venta(operaciones, posiciones, 1, "BTC", 0.00031531000333597984, 60000)

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

#cerrada = cerrar_posicion(posiciones,1)

print('========= Posiciones =========')
print(posiciones)
print('========= Resumen Operaciones =========')
print(operaciones)
print('========= Resumen de Cartera =========')
print(generar_resumen_cartera(operaciones))
#print(cerrada)