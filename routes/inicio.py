from flask import (
    Blueprint,
    render_template,
)
from datos import (
    posiciones,
    operaciones,
    configuracion
)
from posiciones import (
    obtener_posiciones_abiertas
)
from calculos import (
    generar_resumen_todas_posiciones,
    generar_resumen_dashboard,
    generar_tarjetas_activos
)
from utilidades import (
    formatear_dinero,
    formatear_cantidad,
    formatear_porcentaje,   
)

inicio_bp = Blueprint("inicio",__name__)

@inicio_bp.route("/")
def inicio():
    
    posiciones_abiertas = obtener_posiciones_abiertas(posiciones)
    
    resumenes_abiertas = generar_resumen_todas_posiciones(operaciones,posiciones_abiertas)
    resumenes_todas = generar_resumen_todas_posiciones(operaciones,posiciones)
    
    dashboard = generar_resumen_dashboard(resumenes_abiertas,resumenes_todas,configuracion)
    
    tarjetas = generar_tarjetas_activos(operaciones, posiciones)
    
    for tarjeta in tarjetas:
        
        tarjeta["ganancia_realizada"] = formatear_dinero(tarjeta["ganancia_realizada"])
        tarjeta["rentabilidad"] = formatear_porcentaje(tarjeta["rentabilidad"])
        
    return render_template("index.html",resumenes=resumenes_abiertas,dashboard=dashboard,tarjetas=tarjetas)