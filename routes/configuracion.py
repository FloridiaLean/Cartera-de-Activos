from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from datos import (
    configuracion
)
from persistencia import (
    guardar_configuracion
)

configuracion_bp = Blueprint("configuracion",__name__)

@configuracion_bp.route("/configuracion",methods=["GET","POST"])

def mostrar_configuracion():
    
    if request.method == "POST":
        
        capital_inicial = float(request.form["capital_inicial"])
        
        configuracion["capital_inicial"] = capital_inicial 
        
        guardar_configuracion(configuracion)
        
        flash("Configuración guardada correctamente.")
        
        return redirect(url_for("configuracion.mostrar_configuracion"))
    
    return render_template("configuracion.html",configuracion=configuracion)