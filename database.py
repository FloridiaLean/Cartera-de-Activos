import sqlite3

ARCHIVO_BASE_DATOS = "cartera.db"

def obtener_conexion():
    
    conexion = sqlite3.connect(ARCHIVO_BASE_DATOS)
    
    conexion.execute("PRAGMA foreign_keys = ON")
    
    return conexion

def crear_tablas():
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posiciones (
            id INTEGER PRIMARY KEY,
            activo TEXT NOT NULL,
            estado TEXT NOT NULL,
            fecha_apertura TEXT NOT NULL,
            fecha_cierre TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operaciones (
            id INTEGER PRIMARY KEY,
            fecha TEXT NOT NULL,
            posicion_id INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            activo TEXT NOT NULL,
            monto_invertido REAL,
            precio_compra REAL,
            cantidad REAL NOT NULL,
            precio_venta REAL,
            monto_recibido REAL,
            
            FOREIGN KEY (posicion_id)
                REFERENCES posiciones(id)
                ON DELETE CASCADE
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS configuracion (
            id INTEGER PRIMARY KEY,
            capital_inicial REAL NOT NULL
        )
    """)
    
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tablas()
