from servicios import (
    registrar_compra,
    registrar_venta,
    editar_compra_servicio,
    editar_venta_servicio,
    eliminar_operacion_servicio,
    eliminar_posicion_servicio
)
from visualizacion import (
    mostrar_resumen_posicion,
    mostrar_resumen_posiciones,
    mostrar_operaciones,
    mostrar_operacion,
    mostrar_resumen_activo,
    mostrar_lista_posiciones,
    mostrar_lista_activos,
    mostrar_posicion_seleccionada
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
    formatear_cantidad,
    leer_texto
)
from posiciones import (
    obtener_posicion_abierta_por_activo,
    obtener_posiciones_abiertas_por_activo,
    obtener_posicion_por_id,
    obtener_posiciones_abiertas
)
from operaciones import (
    obtener_operacion_por_id,
    obtener_activos
)

def menu_registrar_compra(operaciones,posiciones):
    
    activo = leer_texto("Ingrese el nombre del activo (0 para volver): ",permitir_cancelar=True)
    
    if activo is None:
        return
    
    activo = normalizar_activo(activo)
    
    posiciones_abiertas = obtener_posiciones_abiertas_por_activo(posiciones,activo)
    
    exito = False
    id_posicion = None
    
    if len(posiciones_abiertas) == 0:
        id_posicion = None
    else:
        print("\n=================================================")
        print("Se encontraron las siguientes posiciones abiertas:")
        print("=================================================")
        
        for posicion in posiciones_abiertas:
            posicion_id = posicion["id"]
            resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
            mostrar_resumen_posicion(resumen)
            
        print("\nIngrese 0 para crear una nueva posición.") 
        print("Ingrese Posición ID para agregar a una existente.\n") 
        
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
    
    monto_invertido = leer_float("Ingrese el monto de la inversión (0 para volver): ",permitir_cancelar=True)
    
    if monto_invertido is None:
        return
    
    precio_compra = leer_float("Ingrese el precio de compra del activo (0 para volver): ",permitir_cancelar=True)
    
    if precio_compra is None:
        return
    
    exito = registrar_compra(operaciones,posiciones,id_posicion,activo,monto_invertido,precio_compra)    
    
    if exito:
        print("Compra registrada correctamente.")
    
    pausar()

def menu_registrar_venta(operaciones,posiciones):
    
    posiciones_abiertas = obtener_posiciones_abiertas(posiciones)
    
    posicion = seleccionar_posicion(posiciones_abiertas)
    
    if posicion is None:
        return
    
    posicion_id = posicion["id"]
    activo = posicion["activo"]
    
    resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
    mostrar_posicion_seleccionada(resumen)
    
    cantidad = leer_float("Ingrese la cantidad a vender (0 para volver): ",permitir_cancelar=True)
    
    if cantidad is None:
        return
    
    precio_venta = leer_float("Ingrese el precio al que vendio (0 para volver): ",permitir_cancelar=True)
    
    if precio_venta is None:
        return
    
    exito = registrar_venta(operaciones,posiciones,posicion_id,activo,cantidad,precio_venta)
    
    if exito:
        print("Venta registrada correctamente.")
    
    pausar()

def menu_mostrar_posicion(operaciones,posiciones):
    
    posicion = seleccionar_posicion(posiciones)
    
    if posicion is None:
        return
    
    resumen = generar_resumen_posicion(operaciones,posiciones,posicion['id'])
    mostrar_resumen_posicion(resumen)
    
    pausar()

def menu_mostrar_posiciones(operaciones,posiciones):
    
    resumenes = generar_resumen_todas_posiciones(operaciones,posiciones)
    mostrar_resumen_posiciones(resumenes)
    
    pausar()

def menu_mostrar_resumen_activo(operaciones):
    
    if not operaciones:
        print("No existen operaciones registradas.")
        pausar()
        return
    
    activos = obtener_activos(operaciones)
    mostrar_lista_activos(activos)
    
    while True:
        
        activo = leer_texto("Ingrese el nombre del activo (0 para volver): ",permitir_cancelar=True)
            
        if activo is None:
            return
            
        activo = normalizar_activo(activo)
        
        if activo in activos:
            break
        
        print("El activo seleccionado no es válido. Intente nuevamente.")
    
    resumen = generar_resumen_activo(operaciones,activo)
    mostrar_resumen_activo(resumen)
    
    pausar()

def menu_mostrar_operaciones(operaciones):
    
    mostrar_operaciones(operaciones)
        
    pausar()

def seleccionar_operacion(operaciones):
    
    if not operaciones:
        print("No hay operaciones registradas.")
        return None
    
    mostrar_operaciones(operaciones)
    
    while True:
        
        operacion_id = leer_int("Ingrese el ID de la operación (0 para volver): ",permitir_cancelar=True)
        
        if operacion_id is None:
            return None
        
        operacion = obtener_operacion_por_id(operaciones,operacion_id)
        
        if operacion is not None:
            mostrar_operacion(operacion)
            return operacion
        
        print("La operación seleccionada no existe. Intente nuevamente.")

def seleccionar_posicion(posiciones):
    
    if not posiciones:
        print("No hay posiciones registradas.")
        return None
    
    mostrar_lista_posiciones(posiciones)
    
    while True:
        
        posicion_id = leer_int("\nIngrese el ID de la posición (0 para volver): ",permitir_cancelar=True)
            
        if posicion_id is None:
            return None
            
        posicion = obtener_posicion_por_id(posiciones,posicion_id)
                
        if posicion is not None:
            return posicion
            
        print("La posición seleccionada no es válida. Intente nuevamente.")

def menu_editar_operaciones(operaciones,posiciones):
    
    operacion = seleccionar_operacion(operaciones)
    
    if operacion is None:
        pausar()
        return
    
    if operacion["tipo"] == "compra":
        
        print("\n========= Editar Compra =========")
        print(f"Monto actual: {formatear_dinero(operacion['monto_invertido'])}")
        print(f"Precio actual: {formatear_dinero(operacion['precio_compra'])}")
        print("Ingrese los nuevos valores.\n")
        
        monto_invertido = leer_float("Ingrese el monto de la inversión (0 para volver): ",permitir_cancelar=True)
        
        if monto_invertido is None:
            return
        
        precio_compra = leer_float("Ingrese el precio de compra del activo (0 para volver): ",permitir_cancelar=True)
        
        if precio_compra is None:
            return
        
        exito = editar_compra_servicio(operaciones,operacion,monto_invertido,precio_compra)
        
        if exito:
            print("\nCompra editada correctamente.\n")
            mostrar_operacion(operacion)
    else:
        
        print("\n========= Editar Venta =========")
        print(f"Cantidad: {formatear_cantidad(operacion['cantidad'],operacion['activo'])}")
        print(f"Precio de venta: {formatear_dinero(operacion['precio_venta'])}")
        print("Ingrese los nuevos valores.\n")
        
        cantidad = leer_float("Ingrese la cantidad a vender (0 para volver): ",permitir_cancelar=True)
            
        if cantidad is None:
            return
            
        precio_venta = leer_float("Ingrese el precio al que vendio (0 para volver): ",permitir_cancelar=True)
            
        if precio_venta is None:
            return
        
        exito = editar_venta_servicio(operaciones,posiciones,operacion,cantidad,precio_venta)
        
        if exito:
            print("\nVenta editada correctamente.\n")
            mostrar_operacion(operacion)
        
    pausar()        

def menu_eliminar_operacion(operaciones,posiciones):
    
    operacion = seleccionar_operacion(operaciones)
    
    if operacion is None:
        pausar()
        return
    
    while True:
        
        print("\n=================================")
        print("¿Desea eliminar esta operación?")
        print("=================================\n")
        print("1. Sí")
        print("2. Cancelar")
        
        opcion = leer_texto("Seleccione una opción: ")  
        
        if opcion == "1": 
            
            exito = eliminar_operacion_servicio(operaciones,posiciones,operacion)
            
            if exito:
                print("\nOperación eliminada correctamente.\n")
                pausar()
                return
            
        elif opcion == "2":
            
            print("\nOperación cancelada.\n")
            pausar()
            return
        else:
            print("Opción Inválida.")

def menu_eliminar_posicion(operaciones,posiciones):
    
    posicion = seleccionar_posicion(posiciones)
    
    if posicion is None:
        pausar()
        return
    
    resumen = generar_resumen_posicion(operaciones,posiciones,posicion["id"])
    
    mostrar_resumen_posicion(resumen)
    
    while True:
    
        print("\n=================================")
        print("¿Desea eliminar esta posición?")
        print("=================================")
        print("1. Sí")
        print("2. Cancelar")
        
        opcion = leer_texto("Seleccione una opción: ")
        
        if opcion == "1":
        
            exito = eliminar_posicion_servicio(operaciones,posiciones,posicion)
            
            if exito:
                print("\nPosición eliminada correctamente.\n")
                pausar()
                return

        elif opcion == "2":
            print("\nOperación cancelada.\n")
            pausar()
            return
        else:
            print("Opción inválida.")

def menu_principal(operaciones,posiciones):
    
    while True:
    
        print('''       
=======================================
        CARTERA DE ACTIVOS
=======================================

1. Registrar una compra
2. Registrar una venta
3. Mostrar resumen de posición
4. Mostrar todas las posiciones
5. Mostrar resumen del activo
6. Mostrar todas las operaciones
7. Editar una operacion
8. Eliminar una operacion
9. Eliminar una posición
10. Salir
''')
        opcion = leer_texto("Seleccione una opción: ")
        
        if opcion == "1": menu_registrar_compra(operaciones,posiciones)
        elif opcion == "2": menu_registrar_venta(operaciones,posiciones)
        elif opcion == "3": menu_mostrar_posicion(operaciones,posiciones)
        elif opcion == "4": menu_mostrar_posiciones(operaciones,posiciones)
        elif opcion == "5": menu_mostrar_resumen_activo(operaciones)
        elif opcion == "6": menu_mostrar_operaciones(operaciones)
        elif opcion == "7": menu_editar_operaciones(operaciones,posiciones)
        elif opcion == "8": menu_eliminar_operacion(operaciones,posiciones)
        elif opcion == "9": menu_eliminar_posicion(operaciones,posiciones)
        elif opcion == "10": break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
