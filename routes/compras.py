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
from posiciones import (
    obtener_posiciones_abiertas_por_activo
)
from utilidades import (
    normalizar_activo
)
from calculos import (
    generar_resumen_posicion
)

compras_bp = Blueprint("compras",__name__)

@compras_bp.route("/compras",methods=["GET","POST"])
def compras():

    if request.method == "POST":

        activo = normalizar_activo(request.form["activo"]) 
        monto = request.form.get("monto")
        precio = request.form.get("precio")
        
        posicion_id = request.form.get("posicion_id")
        
        if posicion_id is not None:

            if posicion_id == "":
                posicion_id = None
            elif posicion_id is not None:
                posicion_id = int(posicion_id)
            
            if monto is not None and precio is not None:

                monto = float(monto)
                precio = float(precio)

                exito = registrar_compra(operaciones,posiciones,posicion_id,activo,monto,precio)

                if exito:
                    flash("✅ Compra registrada correctamente.")

                    return redirect(url_for("compras.compras"))
    
        posiciones_abiertas = obtener_posiciones_abiertas_por_activo(posiciones,activo)
        
        resumenes = []
        
        for posicion in posiciones_abiertas:
            
            resumen = generar_resumen_posicion(operaciones,posiciones,posicion["id"])
            resumenes.append(resumen)

        return render_template("compras.html",activo=activo,posiciones=resumenes,posicion_id=posicion_id,mostrar_formulario_compra=True
            if "posicion_id" in request.form
            else False)
    
    return render_template("compras.html",mostrar_formulario_compra=False)