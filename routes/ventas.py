from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from datos import (
    operaciones, 
    posiciones
)
from posiciones import (
    obtener_posiciones_abiertas
)
from servicios import (
    registrar_venta 
)
from calculos import (
    generar_resumen_posicion
)
from utilidades import (
    formatear_dinero,
    formatear_cantidad
)

ventas_bp = Blueprint("ventas",__name__)

@ventas_bp.route("/ventas",methods=["GET","POST"])
def ventas():
    
    posiciones_abiertas = obtener_posiciones_abiertas(posiciones)
    
    if request.method == "POST":
        
        posicion_id = int(request.form["posicion_id"])
        cantidad = request.form.get("cantidad")
        precio = request.form.get("precio")
        
        if cantidad is not None and precio is not None:

            cantidad = float(cantidad)
            precio = float(precio)

            exito, mensaje = registrar_venta(operaciones,posiciones,posicion_id,cantidad,precio)
            
            if exito:
                flash("✅ Venta registrada correctamente.")
                return redirect(url_for("ventas.ventas"))
            flash(f"❌ {mensaje}")
            
        resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
        
        resumen["capital_historico_formateado"] = formatear_dinero(resumen["capital_historico"])
        resumen["capital_invertido_formateado"] = formatear_dinero(resumen["capital_invertido_actual"])
        resumen["cantidad_formateada"] = formatear_cantidad(resumen["cantidad_actual"],resumen["activo"])
        resumen["ppc_formateado"] = formatear_dinero(resumen["precio_promedio"])
        resumen["capital_recuperado_formateado"] = formatear_dinero(resumen["capital_recuperado"])
        resumen["ganancia_realizada_formateada"] = formatear_dinero(resumen["ganancia_realizada"])
        
        return render_template("ventas.html",posiciones=None,resumen=resumen,posicion_id=posicion_id)
    
    resumenes = []
    
    for posicion in posiciones_abiertas:
        
        resumen = generar_resumen_posicion(operaciones,posiciones,posicion["id"])
        resumen["capital_historico_formateado"] = formatear_dinero(resumen["capital_historico"])
        resumen["capital_invertido_formateado"] = formatear_dinero(resumen["capital_invertido_actual"])
        resumen["cantidad_formateada"] = formatear_cantidad(resumen["cantidad_actual"],resumen["activo"])
        resumen["ppc_formateado"] = formatear_dinero(resumen["precio_promedio"])
        resumen["capital_recuperado_formateado"] = formatear_dinero(resumen["capital_recuperado"])
        resumen["ganancia_realizada_formateada"] = formatear_dinero(resumen["ganancia_realizada"])
        resumenes.append(resumen)
        
    return render_template("ventas.html",posiciones=resumenes,resumen=None,posicion_id=None)

