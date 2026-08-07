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
    generar_resumen_dashboard
)

inicio_bp = Blueprint("inicio",__name__)

@inicio_bp.route("/")
def inicio():
    
    posiciones_abiertas = obtener_posiciones_abiertas(posiciones)
    
    resumenes_abiertas = generar_resumen_todas_posiciones(operaciones,posiciones_abiertas)
    resumenes_todas = generar_resumen_todas_posiciones(operaciones,posiciones)
    
    dashboard = generar_resumen_dashboard(resumenes_abiertas,resumenes_todas,configuracion)
    
    return render_template("index.html",resumenes=resumenes_abiertas,dashboard=dashboard)