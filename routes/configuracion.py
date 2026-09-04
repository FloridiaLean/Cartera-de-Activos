from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from datos import (
    configuracion,
    posiciones,
    operaciones
)
from posiciones import (
    obtener_posiciones_abiertas
)
from calculos import (
    generar_resumen_todas_posiciones,
    generar_resumen_dashboard
)
from persistencia import (
    guardar_configuracion_sql
)
from utilidades import (
    formatear_dashboard
)
from servicios import (
    ajustar_liquidez
)

configuracion_bp = Blueprint("configuracion",__name__)

@configuracion_bp.route("/configuracion",methods=["GET","POST"])

def mostrar_configuracion():
    
    posiciones_abiertas = obtener_posiciones_abiertas(posiciones)
    
    resumenes_abiertas = generar_resumen_todas_posiciones(operaciones,posiciones_abiertas)
    
    resumenes_todas = generar_resumen_todas_posiciones(operaciones,posiciones)
    
    dashboard = generar_resumen_dashboard(resumenes_abiertas,resumenes_todas,configuracion)
    
    formatear_dashboard(dashboard)
    
    if request.method == "POST":
        
        accion = request.form.get("accion")
        
        if accion == "agregar" or accion == "restar":
            
            monto = float(request.form["monto_liquidez"])
            
            valido, mensaje = ajustar_liquidez(configuracion,monto,accion,dashboard["liquidez"])
            
            if valido:
                flash("✅ " + mensaje)
            else:
                flash("❌ " + mensaje)
        else:
            capital_inicial = float(request.form["capital_inicial"])
            
            configuracion["capital_inicial"] = capital_inicial 
            
            guardar_configuracion_sql(configuracion)
            
            flash("✅ Configuración guardada correctamente.")
            
        return redirect(url_for("configuracion.mostrar_configuracion"))
    
    return render_template("configuracion.html",configuracion=configuracion,dashboard=dashboard)