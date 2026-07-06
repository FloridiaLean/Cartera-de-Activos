from utilidades import (
    formatear_dinero,
    formatear_cantidad,
    formatear_precio
)

def mostrar_resumen_posicion(resumen):
    print("========= Resumen de Posicion =========")
    print("=================================================")
    print(f"Posición #: {resumen['posicion']}")
    print(f"Activo: {resumen['activo']}")
    print(f"Estado: {resumen['estado']}")
    print("=================================================")
    print(f"Fecha de apertura: {resumen['fecha_apertura']}")
    if resumen['fecha_cierre'] is None:
        print("Fecha de cierre: -")
    else:
        print(f"Fecha de cierre: {resumen['fecha_cierre']}")
    print("=================================================")
    print(f"Capital histórico: {formatear_dinero(resumen['capital_historico'])}")
    print(f"Capital recuperado: {formatear_dinero(resumen['capital_recuperado'])}")
    print("=================================================")
    print(f"Cantidad total: {formatear_cantidad(resumen['cantidad_total'], resumen['activo'])}")
    print(f"Cantidad actual: {formatear_cantidad(resumen['cantidad_actual'], resumen['activo'])}")
    print("=================================================")
    print(f"Precio promedio: {formatear_precio(resumen['precio_promedio'])}")
    print(f"Ganancia realizada: {formatear_dinero(resumen['ganancia_realizada'])}")
    print("=================================================")

def mostrar_resumen_activo(resumen):
    print("========= Resumen de Activo =========")
    print("=================================================")
    print(f"Activo: {resumen['activo']}")
    print("=================================================")
    print("=================================================")
    print(f"Capital histórico: {formatear_dinero(resumen['capital_historico'])}")
    print(f"Capital recuperado: {formatear_dinero(resumen['capital_recuperado'])}")
    print("=================================================")
    print(f"Cantidad actual: {formatear_cantidad(resumen['cantidad_actual'], resumen['activo'])}")
    print("=================================================")
    print(f"Precio promedio: {formatear_precio(resumen['precio_promedio'])}")
    print(f"Ganancia realizada: {formatear_dinero(resumen['ganancia_realizada'])}")
    print("=================================================")