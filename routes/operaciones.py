from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
    request
)
from datos import (
    operaciones,
    posiciones
)
from utilidades import (
    formatear_operacion,
    formatear_cantidad
)
from servicios import (
    editar_compra_servicio,
    editar_venta_servicio
)
from calculos import (
    generar_resumen_posicion
)

operaciones_bp = Blueprint("operaciones",__name__)

@operaciones_bp.route("/operaciones")

def historial_operaciones():
    
    activo = request.args.get("activo","").strip().upper()
    tipo = request.args.get("tipo","").strip().lower()
    
    operaciones_filtradas = operaciones
    
    if activo:
        operaciones_filtradas = [operacion for operacion in operaciones if operacion["activo"] == activo]
    
    if tipo:
        operaciones_filtradas = [operacion for operacion in operaciones_filtradas if operacion["tipo"] == tipo]
    
    operaciones_formateadas = []
    
    for operacion in operaciones_filtradas:
        operacion_formateada = formatear_operacion(operacion)
        operaciones_formateadas.append(operacion_formateada)
    
    return render_template("operaciones.html",operaciones=operaciones_formateadas,activo=activo,tipo=tipo)

@operaciones_bp.route("/operaciones/<int:operacion_id>/editar",methods=["GET","POST"])

def editar_operacion(operacion_id):

    operacion = next((operacion for operacion in operaciones if operacion["id"] == operacion_id),None)
    
    if operacion is None:
        flash("❌ Operación no encontrada.")
        return redirect(url_for("inicio.inicio"))
    
    posicion_id = operacion["posicion_id"]
    
    if request.method == "POST":
        
        if operacion["tipo"] == "compra":
            
            monto_invertido = float(request.form["monto_invertido"])
            precio_compra = float(request.form["precio_compra"])
            
            exito, mensaje = editar_compra_servicio(operaciones,posiciones,operacion,monto_invertido,precio_compra)
            
            if exito:
                flash("✅ Compra editada correctamente.")
            else:
                flash(f"❌ {mensaje}")
        else: 
            
            cantidad = float(request.form["cantidad"])
            precio_venta = float(request.form["precio_venta"])
            
            exito, mensaje = editar_venta_servicio(operaciones,posiciones,operacion,cantidad,precio_venta)
            
            if exito:
                flash("✅ Venta editada correctamente.")
            else:
                flash(f"❌ {mensaje}")
            
        return redirect(
            url_for("posiciones.detalle_posicion",posicion_id=posicion_id))
    
    operacion = formatear_operacion(operacion)
    
    cantidad_disponible = None
    
    if operacion["tipo"] == "venta":
    
        resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
        
        cantidad_disponible = (resumen["cantidad_actual"] + operacion["cantidad"])
        
        cantidad_disponible_formateada = formatear_cantidad(cantidad_disponible,operacion["activo"])
        
        return render_template("editar_operacion.html",operacion=operacion,cantidad_disponible=cantidad_disponible, cantidad_disponible_formateada=cantidad_disponible_formateada)
    
    return render_template("editar_operacion.html",operacion=operacion)