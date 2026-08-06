from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from servicios import (
    registrar_compra
)
from persistencia import (
    guardar_operaciones, 
    guardar_posiciones
)
from datos import (
    operaciones, 
    posiciones
)

compras_bp = Blueprint("compras",__name__)

@compras_bp.route("/compras",methods=["GET","POST"])
def compras():

    if request.method == "POST":

        activo = request.form["activo"]
        monto = float(request.form["monto"])
        precio = float(request.form["precio"])

        exito = registrar_compra(operaciones,posiciones,None,activo,monto,precio)

        if exito:
            guardar_operaciones(operaciones)
            guardar_posiciones(posiciones)

            flash("✅ Compra registrada correctamente.")

            return redirect(url_for("compras.compras"))

    return render_template("compras.html")