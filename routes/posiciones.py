from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)
from datos import (
    posiciones,
    operaciones
)
from posiciones import (
    obtener_posicion_por_id,
    obtener_posiciones_cerradas
)
from operaciones import (
    obtener_operaciones_por_posicion
)
from calculos import (
    generar_resumen_posicion,
    generar_resumen_todas_posiciones
)
from utilidades import (
    formatear_resumen_posicion,
    formatear_operacion
)
from servicios import (
    eliminar_posicion_servicio,
    eliminar_operacion_servicio
)

posiciones_bp = Blueprint("posiciones",__name__)

@posiciones_bp.route("/posiciones")

def todas_las_posiciones():

    resumenes = generar_resumen_todas_posiciones(operaciones,posiciones)
    
    for resumen in resumenes:
        formatear_resumen_posicion(resumen)
    
    return render_template("posiciones.html",posiciones=resumenes)

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

@posiciones_bp.route("/posiciones/operaciones/<int:operacion_id>/eliminar",methods=["POST"])

def eliminar_operacion(operacion_id):

    operacion = next((operacion for operacion in operaciones if operacion["id"] == operacion_id),None)
    
    if operacion is None:
        flash("❌ Operación no encontrada.")
        return redirect(url_for("inicio.inicio"))
    
    posicion_id = operacion["posicion_id"]
    
    exito, mensaje = eliminar_operacion_servicio(operaciones,posiciones,operacion)
    
    if exito:
        flash(f"✅ {mensaje}")
    else:
        flash(f"❌ {mensaje}")
        return redirect(url_for("posiciones.detalle_posicion",posicion_id=posicion_id))
    
    posicion = obtener_posicion_por_id(posiciones,posicion_id)
    
    if posicion is None:
        return redirect(url_for("inicio.inicio"))
    
    return redirect(url_for("posiciones.detalle_posicion",posicion_id=posicion_id))

@posiciones_bp.route("/historial")

def historial_posiciones():
    
    posiciones_cerradas = obtener_posiciones_cerradas(posiciones)
    
    resumenes = []
    
    for posicion in posiciones_cerradas:
    
        resumen = generar_resumen_posicion(operaciones,posiciones,posicion["id"])
        
        resumen = formatear_resumen_posicion(resumen)
        
        resumenes.append(resumen)
        
    return render_template("posiciones_cerradas.html",posiciones=resumenes)