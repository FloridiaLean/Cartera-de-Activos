from utilidades import (
    formatear_dinero,
    formatear_cantidad
)

def mostrar_resumen_posicion(resumen):
    print("\n=======================================")
    print("          Resumen de Posición          ")
    print("=======================================")
    print(f"Posición ID: {resumen['posicion']}")
    print(f"Activo: {resumen['activo']}")
    print(f"Estado: {resumen['estado']}")
    print("=======================================")
    print(f"Fecha de apertura: {resumen['fecha_apertura']}")
    if resumen['fecha_cierre'] is None:
        print("Fecha de cierre: -")
    else:
        print(f"Fecha de cierre: {resumen['fecha_cierre']}")
    print("=======================================")
    print(f"Capital histórico: {formatear_dinero(resumen['capital_historico'])}")
    print(f"Capital recuperado: {formatear_dinero(resumen['capital_recuperado'])}")
    print("=======================================")
    print(f"Cantidad total: {formatear_cantidad(resumen['cantidad_total'], resumen['activo'])}")
    print(f"Cantidad actual: {formatear_cantidad(resumen['cantidad_actual'], resumen['activo'])}")
    print("=======================================")
    print(f"Precio promedio: {formatear_dinero(resumen['precio_promedio'])}")
    print(f"Ganancia realizada: {formatear_dinero(resumen['ganancia_realizada'])}")
    print("=======================================")

def mostrar_resumen_posiciones(resumenes):
    
    if len(resumenes) == 0:
        print("No existen posiciones registradas.")
        return
    
    for resumen in resumenes:
        mostrar_resumen_posicion(resumen)

def mostrar_resumen_activo(resumen):
    print("\n========= Resumen de Activo =========")
    print("=====================================")
    print(f"Activo: {resumen['activo']}")
    print("=====================================")
    print(f"Capital histórico invertido: {formatear_dinero(resumen['capital_historico'])}")
    print(f"Capital recuperado: {formatear_dinero(resumen['capital_recuperado'])}")
    print(f"Cantidad actual: {formatear_cantidad(resumen['cantidad_actual'], resumen['activo'])}")
    print(f"Ganancia realizada: {formatear_dinero(resumen['ganancia_realizada'])}")
    print("=====================================")

def mostrar_operacion(operacion):
    print("\n========= Operación =========")
    print(f"Operación ID: {operacion['id']}")
    print(f"Posición: {operacion['posicion_id']}")
    print(f"Tipo: {operacion['tipo'].upper()}")
    print(f"Activo: {operacion['activo']}")
    print(f"Fecha: {operacion['fecha']}")
    print("-----------------------------")

    if operacion['tipo'] == 'compra':
        print(f"Monto invertido: {formatear_dinero(operacion['monto_invertido'])}")
        print(f"Precio de compra: {formatear_dinero(operacion['precio_compra'])}")
        print(f"Cantidad: {formatear_cantidad(operacion['cantidad'], operacion['activo'])}")
        
    else:
        print(f"Cantidad: {formatear_cantidad(operacion['cantidad'], operacion['activo'])}")
        print(f"Precio de venta: {formatear_dinero(operacion['precio_venta'])}")
        print(f"Monto recibido: {formatear_dinero(operacion['monto_recibido'])}")
    print("============================")

def mostrar_operaciones(operaciones):

    if len(operaciones) == 0:
        print("No hay operaciones registradas.")
        return
    
    for operacion in operaciones:
        mostrar_operacion(operacion)

def mostrar_lista_posiciones(posiciones):
    
    print("============================")
    print("   Posiciones registradas   ")
    print("============================")
    
    for posicion in posiciones:
        print(f"ID Posicion #: {posicion['id']} | {posicion['activo']} | {posicion['estado']} ")

def mostrar_lista_activos(activos):

    print("=============================")
    print("     Activos registrados     ")
    print("=============================")

    for activo in activos:
        print(f"- {activo}")

def mostrar_posicion_seleccionada(resumen):
    
    print("\n=======================================")
    print("         Posición Seleccionada         ")
    print("=======================================")
    print(f"Posición ID: {resumen['posicion']}")
    print(f"Activo: {resumen['activo']}")
    print("=======================================")
    print(f"Capital histórico: {formatear_dinero(resumen['capital_historico'])}")
    print(f"Capital recuperado: {formatear_dinero(resumen['capital_recuperado'])}")
    print("=======================================")
    print(f"Cantidad actual: {formatear_cantidad(resumen['cantidad_actual'], resumen['activo'])}")
    print("=======================================")
    print(f"Precio promedio: {formatear_dinero(resumen['precio_promedio'])}")
    print(f"Ganancia realizada: {formatear_dinero(resumen['ganancia_realizada'])}")
    print("=======================================")