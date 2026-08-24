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
from datos import (
    operaciones, 
    posiciones
)
from posiciones import (
    obtener_posiciones_abiertas_por_activo,
    obtener_posicion_por_id
)
from calculos import (
    generar_resumen_posicion
)
from utilidades import (
    normalizar_activo,
    formatear_resumen_posicion
)

compras_bp = Blueprint("compras",__name__)

@compras_bp.route("/compras",methods=["GET","POST"])

def compras():
    
    posicion_id = request.args.get("posicion_id")
    
    if posicion_id is not None:
        posicion_id = int(posicion_id)
        
        posicion = obtener_posicion_por_id(posiciones,posicion_id)
        
        if posicion is None:
            return "Posición no encontrada", 404
        
        resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
        
        resumen = formatear_resumen_posicion(resumen)
        
        return render_template("compras.html",activo=posicion["activo"],posiciones=None,posicion_id=posicion_id,resumen=resumen,mostrar_formulario_compra=True)
        
    if request.method == "POST":
        
        activo = normalizar_activo(request.form["activo"]) 
        monto = request.form.get("monto")
        precio = request.form.get("precio")
        fecha = request.form.get("fecha")
        
        posicion_id = request.form.get("posicion_id")
        
        if posicion_id is not None:
            
            if posicion_id == "":
                posicion_id = None
            elif posicion_id is not None:
                posicion_id = int(posicion_id)
            
            if monto is not None and precio is not None:
            
                monto = float(monto)
                precio = float(precio)
                
                exito, mensaje = registrar_compra(operaciones,posiciones,posicion_id,activo,monto,precio,fecha)
                
                if exito:
                    flash("✅ Compra registrada correctamente.")
                    return redirect(url_for("compras.compras"))
                
                flash(f"❌ {mensaje}")
                
                if posicion_id is not None:
                    
                    resumen = generar_resumen_posicion(operaciones,posiciones,posicion_id)
                    
                    resumen = formatear_resumen_posicion(resumen)
                    
                    return render_template("compras.html",activo=activo,posiciones=None,posicion_id=posicion_id,resumen=resumen,mostrar_formulario_compra=True)
                    
        posiciones_abiertas = obtener_posiciones_abiertas_por_activo(posiciones,activo)
        
        resumenes = []
        
        for posicion in posiciones_abiertas:
            
            resumen = generar_resumen_posicion(operaciones,posiciones,posicion["id"])
            
            resumen = formatear_resumen_posicion(resumen)
            
            resumenes.append(resumen)
        
        return render_template("compras.html",activo=activo,posiciones=resumenes,posicion_id=posicion_id,mostrar_formulario_compra=True
            if "posicion_id" in request.form
            else False)
    
    return render_template("compras.html",mostrar_formulario_compra=False)