from servicios import (
    registrar_compra,
    registrar_venta,
    editar_compra_servicio,
    editar_venta_servicio
)
from visualizacion import (
    mostrar_resumen_posicion,
    mostrar_resumen_posiciones,
    mostrar_operaciones,
    mostrar_operacion,
    mostrar_resumen_activo
)
from calculos import (
    generar_resumen_posicion,
    generar_resumen_todas_posiciones,
    generar_resumen_activo
)
from utilidades import (
    leer_float,
    leer_int,
    pausar,
    normalizar_activo,
    formatear_dinero,
    formatear_cantidad
)
from posiciones import (
    obtener_posicion_abierta_por_activo,
    obtener_posiciones_abiertas_por_activo,
    obtener_posicion_por_id
)
from operaciones import (
    obtener_operacion_por_id
)

def menu_registrar_compra(operaciones,posiciones):
    
    activo = normalizar_activo(input("Ingrese el activo que desea comprar: "))
    
    posiciones_abiertas = obtener_posiciones_abiertas_por_activo(posiciones,activo)
    
    exito = False
    id_posicion = None
    
    if  len(posiciones_abiertas) == 0:
        id_posicion = None
    else:
        print("\n=================================================")
        print("Se encontraron las siguientes posiciones abiertas:")
        print("=================================================\n")
        
        for posicion in posiciones_abiertas:
            posicion_id = posicion["id"]
            resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
            mostrar_resumen_posicion(resumen)
            
        print("\n0. Para crear una nueva posición.") 
        print("Ingrese la Posición # para agregar a una existente.\n") 
        
        while True:
            
            id_posicion = leer_int("Ingrese el ID de la posición: ")
            
            if id_posicion == 0:    
                id_posicion = None
                break
            else:
                posicion = obtener_posicion_por_id(posiciones_abiertas,id_posicion)
                
                if posicion is not None:
                    break
                print("La posición seleccionada no existe.")
    
    monto_invertido = leer_float("Ingrese el monto de inversión: ")
    precio_compra = leer_float("Ingrese el precio de compra: ")
    
    exito = registrar_compra(operaciones,posiciones,id_posicion,activo,monto_invertido,precio_compra)    
    
    if exito:
        print(f"Compra registrada correctamente.")
    
    pausar()

def menu_registrar_venta(operaciones,posiciones):
    
    posicion_id = leer_int("Ingrese el ID de la posicion: ")
    activo = input("Ingrese el activo que desea vender: ")
    cantidad = leer_float("Ingrese la cantidad a vender: ")
    precio_venta = leer_float("Ingrese el precio al que vendio: ")
    
    exito = registrar_venta(operaciones,posiciones,posicion_id,activo,cantidad,precio_venta)
    
    if exito:
        print(f"Venta registrada correctamente.")
    
    pausar()

def menu_mostrar_posicion(operaciones,posiciones):
    
    posicion_id = leer_int("Ingrese el ID de la posicion: ")
    
    resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
    
    if resumen is None:
        print("La posicion no existe")
    else:
        mostrar_resumen_posicion(resumen)
    
    pausar()

def menu_mostrar_posiciones(operaciones,posiciones):
    
    resumenes = generar_resumen_todas_posiciones(operaciones,posiciones)
    mostrar_resumen_posiciones(resumenes)
    
    pausar()

def menu_mostrar_resumen_activo(operaciones):
    
    activo = input("Ingrese el nombre del activo: ")
    activo = normalizar_activo(activo)
    
    resumen = generar_resumen_activo(operaciones,activo)
    
    if resumen is None:
        print(f"No existen operaciones para el activo {activo}.")
    else:
        mostrar_resumen_activo(resumen)
    
    pausar()

def menu_mostrar_operaciones(operaciones):
    
    mostrar_operaciones(operaciones)
        
    pausar()

def seleccionar_operacion(operaciones):
    
    mostrar_operaciones(operaciones)
    
    while True:
        
        operacion_id = leer_int("Ingrese el ID de la operacion: ")
        operacion = obtener_operacion_por_id(operaciones,operacion_id)
        
        if operacion is not None:
            mostrar_operacion(operacion)
            return operacion
        print("La operación seleccionada no existe. Intente nuevamente.")
        
def menu_editar_operaciones(operaciones,posiciones):
    
    operacion = seleccionar_operacion(operaciones)
    
    if operacion["tipo"] == "compra":
        
        print("\n========= Editar Compra =========")
        print(f"Monto actual: {formatear_dinero(operacion['monto_invertido'])}")
        print(f"Precio actual: {formatear_dinero(operacion['precio_compra'])}")
        print("Ingrese los nuevos valores.\n")
        
        monto_invertido = leer_float("Nuevo monto de inversión: ")
        precio_compra = leer_float("Nuevo precio de compra: ")
        
        exito = editar_compra_servicio(operaciones,operacion,monto_invertido,precio_compra)
        
        if exito:
            print("\nCompra editada correctamente.\n")
            mostrar_operacion(operacion)
    else:
        
        print("\n========= Editar Venta =========")
        print(f"Cantidad: {formatear_cantidad(operacion['cantidad'],operacion['activo'])}")
        print(f"Precio de venta: {formatear_dinero(operacion['precio_venta'])}")
        print("Ingrese los nuevos valores.\n")
        
        cantidad = leer_float("Nueva cantidad: ")
        precio_venta = leer_float("Nuevo precio de venta: ")
        
        exito = editar_venta_servicio(operaciones,posiciones,operacion,cantidad,precio_venta)
        
        if exito:
            print("\nVenta editada correctamente.\n")
            mostrar_operacion(operacion)
        
    pausar()        

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
    6. Mostrar operaciones
    7. Editar operaciones
    8. Salir
''')
        opcion = input("Seleccione la opción: ")
        
        if opcion == "1": menu_registrar_compra(operaciones,posiciones)
        elif opcion == "2": menu_registrar_venta(operaciones,posiciones)
        elif opcion == "3": menu_mostrar_posicion(operaciones,posiciones)
        elif opcion == "4": menu_mostrar_posiciones(operaciones,posiciones)
        elif opcion == "5": menu_mostrar_resumen_activo(operaciones)
        elif opcion == "6": menu_mostrar_operaciones(operaciones)
        elif opcion == "7": menu_editar_operaciones(operaciones,posiciones)
        elif opcion == "8": break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
