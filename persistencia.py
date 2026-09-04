from database import obtener_conexion

def guardar_operaciones_sql(operaciones):

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    for operacion in operaciones:
    
        cursor.execute("""
            INSERT OR REPLACE INTO operaciones (
                id,
                fecha,
                posicion_id,
                tipo,
                activo,
                monto_invertido,
                precio_compra,
                cantidad,
                precio_venta,
                monto_recibido
            )
            VALUES (?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(id) DO UPDATE SET
                fecha = excluded.fecha,
                posicion_id = excluded.posicion_id,
                tipo = excluded.tipo,
                activo = excluded.activo,
                monto_invertido = excluded.monto_invertido,
                precio_compra = excluded.precio_compra,
                cantidad = excluded.cantidad,
                precio_venta = excluded.precio_venta,
                monto_recibido = excluded.monto_recibido
        """,(
            operacion["id"],
            operacion["fecha"],
            operacion["posicion_id"],
            operacion["tipo"],
            operacion["activo"],
            operacion.get("monto_invertido"),
            operacion.get("precio_compra"),
            operacion["cantidad"],
            operacion.get("precio_venta"),
            operacion.get("monto_recibido")
        ))
    
    conexion.commit()
    conexion.close()

def guardar_posiciones_sql(posiciones):

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    for posicion in posiciones:
    
        cursor.execute("""
            INSERT OR REPLACE INTO posiciones (
                id,
                activo,
                estado,
                fecha_apertura,
                fecha_cierre
            )
            VALUES (?,?,?,?,?)
            ON CONFLICT(id) DO UPDATE SET
                activo = excluded.activo,
                estado = excluded.estado,
                fecha_apertura = excluded.fecha_apertura,
                fecha_cierre = excluded.fecha_cierre
        """, (
            posicion["id"],
            posicion["activo"],
            posicion["estado"],
            posicion["fecha_apertura"],
            posicion.get("fecha_cierre")
        ))
    
    conexion.commit()
    conexion.close()

def guardar_configuracion_sql(configuracion):

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
        INSERT OR REPLACE INTO configuracion (
            id,
            capital_inicial,
            ajuste_liquidez
        )
        VALUES (?,?,?)
    """, (
        1,
        configuracion["capital_inicial"],
        configuracion["ajuste_liquidez"]
    ))
    
    conexion.commit()
    conexion.close()

def cargar_operaciones_sql():

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
        SELECT
            id,
            fecha,
            posicion_id,
            tipo,
            activo,
            monto_invertido,
            precio_compra,
            cantidad,
            precio_venta,
            monto_recibido
        FROM operaciones
    """)
    
    filas = cursor.fetchall()
    columnas = [descripcion[0] for descripcion in cursor.description]
    
    operaciones = []
    
    for fila in filas:
        operacion = dict(zip(columnas,fila))
        operaciones.append(operacion)
    
    conexion.close()
    
    return operaciones

def cargar_posiciones_sql():

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
        SELECT
            id,
            activo,
            estado,
            fecha_apertura,
            fecha_cierre
        FROM posiciones
    """)
    
    filas = cursor.fetchall()
    columnas = [descripcion[0] for descripcion in cursor.description]
    
    posiciones = []
    
    for fila in filas:
        posicion = dict(zip(columnas,fila))
        posiciones.append(posicion)
    
    conexion.close()
    
    return posiciones

def cargar_configuracion_sql():

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
        SELECT capital_inicial,
                ajuste_liquidez
        FROM configuracion
        WHERE id = 1
    """)
    
    fila = cursor.fetchone()
    
    conexion.close()
    
    if fila is None:
        return {
            "capital_inicial": 0,
            "ajuste_liquidez": 0
        }
    
    return {
        "capital_inicial": fila[0],
        "ajuste_liquidez": fila[1]
    }

def eliminar_operacion_sql(operacion_id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
        DELETE FROM operaciones
        WHERE id = ?
    """,(operacion_id,))
    
    conexion.commit()
    conexion.close()

def eliminar_operaciones_por_posicion_sql(posicion_id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
        DELETE FROM operaciones
        WHERE posicion_id = ?
    """,(posicion_id,))
    
    conexion.commit()
    conexion.close()

def eliminar_posicion_sql(posicion_id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
        DELETE FROM posiciones
        WHERE id = ?
    """,(posicion_id,))
    
    conexion.commit()
    conexion.close()

def sincronizar_operaciones_sql(operaciones):

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("DELETE FROM operaciones")
    
    for operacion in operaciones:
    
        cursor.execute("""
            INSERT INTO operaciones (
                id,
                fecha,
                posicion_id,
                tipo,
                activo,
                monto_invertido,
                precio_compra,
                cantidad,
                precio_venta,
                monto_recibido
            )
            VALUES (?,?,?,?,?,?,?,?,?,?)
        """,(
            operacion["id"],
            operacion["fecha"],
            operacion["posicion_id"],
            operacion["tipo"],
            operacion["activo"],
            operacion.get("monto_invertido"),
            operacion.get("precio_compra"),
            operacion["cantidad"],
            operacion.get("precio_venta"),
            operacion.get("monto_recibido")
        ))
    
    conexion.commit()
    conexion.close()