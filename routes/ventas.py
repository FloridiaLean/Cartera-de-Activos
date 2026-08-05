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

ventas_bp = Blueprint("ventas",__name__)

@ventas_bp.route("/ventas",methods=["GET","POST"])
def ventas():
    
    if request.method == "POST":
        
        posicion_id = int(request.form["posicion_id"])
        cantidad = float(request.form["cantidad"])
        precio_venta = float(request.form["precio_venta"])
        
        exito = registrar_venta(operaciones,posiciones,posicion_id,cantidad,precio_venta)
        
        if exito:
            flash("Venta registrada correctamente.")
        else:
            flash("No fue posible registrar la venta.")
        
        return redirect(url_for("ventas.ventas"))
    
    posiciones_abiertas = obtener_posiciones_abiertas(posiciones)
    
    return render_template("ventas.html",posiciones_abiertas=posiciones_abiertas)

