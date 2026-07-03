def mostrar_resumen_posicion(resumen):
    
    print("=================================================")
    print(f"Posición #: {resumen['posicion']}")
    print("=================================================")
    print(f"Activo: {resumen['activo']}")
    print(f"Estado: {resumen['estado']}")
    print("=================================================")
    print(f"Fecha de apertura: {resumen['fecha_apertura']}")
    if resumen['fecha_cierre'] is None:
        print("Fecha de cierre: -")
    else:
        print(f"Fecha de cierre: {resumen['fecha_cierre']}")
    print("=================================================")
    print(f"Capital histórico: {resumen['capital_historico']}")
    print(f"Capital recuperado: {resumen['capital_recuperado']}")
    print("=================================================")
    print(f"Cantidad total: {resumen['cantidad_total']}")
    print(f"Cantidad actual: {resumen['cantidad_actual']}")
    print("=================================================")
    print(f"Precio promedio: {resumen['precio_promedio']}")
    print(f"Ganancia realizada: {resumen['ganancia_realizada']}")
    print("=================================================")