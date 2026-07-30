from datetime import datetime

def obtener_fecha_actual():
    
    fecha = datetime.now()
    fecha_formateada = fecha.strftime("%d/%m/%Y %H:%M")
    
    return fecha_formateada

def normalizar_activo(activo):
    
    activo_normalizado = activo.strip().upper()
    
    return activo_normalizado

def formatear_dinero(valor):
    
    valor_formateado = f"${valor:,.2f}"
    
    return valor_formateado

def formatear_cantidad(cantidad,activo):
    
    cantidad_formateada = f"{cantidad:.8f} {activo}"
    
    return cantidad_formateada

def leer_float(mensaje,permitir_cancelar=False):
    
    while True:
        try:
            numero = float(input(mensaje))
            
            if permitir_cancelar and numero == 0:
                return None 
            
            return numero
        
        except ValueError:
            print("Debe ingresar un número válido.")

def leer_int(mensaje,permitir_cancelar=False):
    
    while True:
        try:
            numero = int(input(mensaje))
            
            if permitir_cancelar and numero == 0:
                return None
            return numero
        
        except ValueError:
            print("Debe ingresar un número entero.")

def leer_texto(mensaje,permitir_cancelar=False):

    while True:

        texto = input(mensaje).strip()

        if permitir_cancelar and texto == "0":
            return None

        if texto == "":
            print("Debe ingresar un texto válido.")
            continue

        return texto

def pausar():
    input("\nPresione ENTER para continuar...")