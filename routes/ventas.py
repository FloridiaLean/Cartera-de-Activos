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
    formatear_resumen_posicion
)

ventas_bp = Blueprint("ventas",__name__)

@ventas_bp.route("/ventas",methods=["GET","POST"])

def ventas():
    
    posiciones_abiertas = obtener_posiciones_abiertas(posiciones)
    
    posicion_id = request.args.get("posicion_id")
    
    if posicion_id is not None:
        posicion_id = int(posicion_id)
        
        resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
        
        resumen = formatear_resumen_posicion(resumen)
        
        return render_template("ventas.html",posiciones=None,resumen=resumen,posicion_id=posicion_id)
    
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
        
        resumen = formatear_resumen_posicion(resumen)
        
        return render_template("ventas.html",posiciones=None,resumen=resumen,posicion_id=posicion_id)
    
    resumenes = []
    
    for posicion in posiciones_abiertas:
        
        resumen = generar_resumen_posicion(operaciones,posiciones,posicion["id"])
        
        resumen = formatear_resumen_posicion(resumen)
        
        resumenes.append(resumen)
        
    return render_template("ventas.html",posiciones=resumenes,resumen=None,posicion_id=None)

