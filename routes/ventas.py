from flask import (
    Blueprint,
    render_template,
    request
)
from datos import (
    operaciones, 
    posiciones
)
from posiciones import (
    obtener_posiciones_abiertas
)

ventas_bp = Blueprint("ventas",__name__)

@ventas_bp.route("/ventas",methods=["GET","POST"])
def ventas():
    
    if request.method == "POST":
        
        #posicion_id = int(request.form["posicion_id"])
        #cantidad = float(request.form["cantidad"])
        #precio_venta = float(request.form["precio_venta"])
        #
        #print(posicion_id)
        #print(cantidad)
        #print(precio_venta)
        print(request.form)
        
    posiciones_abiertas = obtener_posiciones_abiertas(posiciones)
    
    return render_template("ventas.html",posiciones_abiertas=posiciones_abiertas)

