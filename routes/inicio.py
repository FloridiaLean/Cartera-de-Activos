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
    generar_tarjetas_activos,
    generar_resumen_activos_abiertos
)
from utilidades import (
    formatear_resumen_posicion,
    formatear_tarjeta_activo,
    formatear_resumen_activo,
    formatear_dashboard
)

inicio_bp = Blueprint("inicio",__name__)

@inicio_bp.route("/")
def inicio():
    
    posiciones_abiertas = obtener_posiciones_abiertas(posiciones)
    
    resumenes_abiertas = generar_resumen_todas_posiciones(operaciones,posiciones_abiertas)
    
    for resumen in resumenes_abiertas:
    
        formatear_resumen_posicion(resumen)
    
    resumenes_todas = generar_resumen_todas_posiciones(operaciones,posiciones)
    resumenes_activos = generar_resumen_activos_abiertos(resumenes_abiertas)
    
    for resumen in resumenes_activos:
    
        formatear_resumen_activo(resumen)
    
    dashboard = generar_resumen_dashboard(resumenes_abiertas,resumenes_todas,configuracion)
    
    formatear_dashboard(dashboard)
    
    tarjetas = generar_tarjetas_activos(operaciones,posiciones)
    
    for tarjeta in tarjetas:
    
        formatear_tarjeta_activo(tarjeta)
    
    return render_template("index.html",resumenes=resumenes_abiertas,dashboard=dashboard,tarjetas=tarjetas,resumenes_activos=resumenes_activos)