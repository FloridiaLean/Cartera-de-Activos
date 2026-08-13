from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
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
    formatear_resumen_posicion,
    formatear_operacion
)
from servicios import (
    eliminar_posicion_servicio
)

posiciones_bp = Blueprint("posiciones",__name__)

@posiciones_bp.route("/posiciones/<int:posicion_id>")

def detalle_posicion(posicion_id):
    
    posicion = obtener_posicion_por_id(posiciones,posicion_id)
    
    if posicion is None:
        return "Posición no encontrada", 404
    
    operaciones_posicion = obtener_operaciones_por_posicion(operaciones,posicion_id)
    
    for operacion in operaciones_posicion:
        operacion = formatear_operacion(operacion)
    
    resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
    
    resumen = formatear_resumen_posicion(resumen)
    
    return render_template("posicion.html",posicion=posicion,resumen=resumen,operaciones=operaciones_posicion)

@posiciones_bp.route("/posiciones/<int:posicion_id>/eliminar",methods=["POST"])

def eliminar_posicion(posicion_id):
    
    posicion = obtener_posicion_por_id(posiciones,posicion_id)
    
    if posicion is None:
        return "Posición no encontrada", 404
    
    eliminar_posicion_servicio(operaciones,posiciones,posicion)
    
    return redirect(url_for("inicio.inicio"))