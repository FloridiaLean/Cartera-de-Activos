from flask import (
    Blueprint,
    render_template
)
from datos import (
    posiciones,
    operaciones
)
from posiciones import (
    obtener_posicion_por_id
)
from operaciones import (
    obtener_operaciones_por_posicion
)
from calculos import (
    generar_resumen_posicion
)
from utilidades import (
    formatear_dinero,
    formatear_cantidad,
    formatear_fecha
)

posiciones_bp = Blueprint("posiciones",__name__)

@posiciones_bp.route("/posiciones/<int:posicion_id>")

def detalle_posicion(posicion_id):

    posicion = obtener_posicion_por_id(posiciones,posicion_id)

    if posicion is None:
        return "Posición no encontrada", 404

    operaciones_posicion = obtener_operaciones_por_posicion(operaciones,posicion_id)
    
    for operacion in operaciones_posicion:
        
        operacion["cantidad_formateada"] = formatear_cantidad(operacion["cantidad"],operacion["activo"])
        operacion["fecha_formateada"] = formatear_fecha(operacion["fecha"])
        
        if operacion["tipo"] == "compra":
            operacion["precio_formateado"] = formatear_dinero(operacion["precio_compra"])
            operacion["monto_formateado"] = formatear_dinero(operacion["monto_invertido"])
        
        else: 
            operacion["precio_formateado"] = formatear_dinero(operacion["precio_venta"])
            operacion["monto_formateado"] = formatear_dinero(operacion["monto_recibido"])
    
    resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
    
    resumen["capital_historico_formateado"] = formatear_dinero(resumen["capital_historico"])
    resumen["capital_invertido_actual_formateado"] = formatear_dinero(resumen["capital_invertido_actual"])
    resumen["cantidad_formateada"] = formatear_cantidad(resumen["cantidad_actual"],resumen["activo"])
    resumen["ppc_formateado"] = formatear_dinero(resumen["precio_promedio"])
    resumen["capital_recuperado_formateado"] = formatear_dinero(resumen["capital_recuperado"])
    resumen["ganancia_realizada_formateada"] = formatear_dinero(resumen["ganancia_realizada"])
    
    return render_template("posicion.html",posicion=posicion,resumen=resumen,operaciones=operaciones_posicion)