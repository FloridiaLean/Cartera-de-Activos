from persistencia import (
    cargar_operaciones_sql,
    cargar_posiciones_sql,
    cargar_configuracion_sql
)

operaciones = cargar_operaciones_sql()
posiciones = cargar_posiciones_sql()
configuracion = cargar_configuracion_sql()