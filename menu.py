from servicios import (
    registrar_compra,
    registrar_venta
)
from visualizacion import (
    mostrar_resumen_posicion,
    mostrar_resumen_activo
)
from calculos import (
    generar_resumen_posicion,
    generar_resumen_todas_posiciones,
    generar_resumen_activo
)

def menu_registrar_compra(operaciones,posiciones):
    
    activo = input("Ingrese el activo que desea comprar: ")
    monto_inversion = float(input("Ingrese el monto de inversión: "))
    precio_compra = float(input("Ingrese el precio de compra: "))
    
    exito = registrar_compra(operaciones,posiciones,None,activo,monto_inversion,precio_compra)
    
    if exito:
        print(f"Compra registrada correctamente.")

    input("\nPresione ENTER para volver al menú...")

def menu_registrar_venta(operaciones,posiciones):
    
    posicion_id = int(input("Ingrese el ID de la posicion: "))
    activo = input("Ingrese el activo que desea vender: ")
    cantidad = float(input("Ingrese la cantidad a vender: "))
    precio_venta = float(input("Ingrese el precio al que vendio: "))
    
    exito = registrar_venta(operaciones,posiciones,posicion_id,activo,cantidad,precio_venta)
    
    if exito:
        print(f"Venta registrada correctamente.")

    input("\nPresione ENTER para volver al menú...")

def menu_mostrar_posicion(operaciones,posiciones):
    
    posicion_id = int(input("Ingrese el ID de la posicion: "))

    resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
    mostrar_resumen_posicion(resumen)
    
    input("\nPresione ENTER para volver al menú...")

def menu_mostrar_posiciones(operaciones,posiciones):
    
    resumen = generar_resumen_todas_posiciones
    
    input("\nPresione ENTER para volver al menú...")
    pass


def menu_mostrar_resumen_activo(operaciones,activo):
    
    activo = input("Ingrese el nombre del activo: ")
    
    resumen = generar_resumen_activo(operaciones,activo)
    mostrar_resumen_activo(resumen)
    
    input("\nPresione ENTER para volver al menú...")

def menu_principal(operaciones,posiciones):
    
    while True:
        
        print('''       
    =====================================
            CARTERA DE ACTIVOS
    =====================================

    1. Registrar compra
    2. Registrar venta
    3. Mostrar posición
    4. Mostrar todas las posiciones
    5. Mostrar resumen por activo
    6. Salir
''')
        opcion = input("Seleccione la opción: ")
        
        if opcion == "1": menu_registrar_compra(operaciones,posiciones)
        elif opcion == "2": menu_registrar_venta(operaciones,posiciones)
        elif opcion == "3": menu_mostrar_posicion(operaciones,posiciones)
        elif opcion == "4": print("Mostrar todas las posiciones")
        elif opcion == "5": menu_mostrar_resumen_activo(operaciones,posiciones)
        elif opcion == "6": break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
