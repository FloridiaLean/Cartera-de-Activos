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
    resumenes_activos = generar_resumen_activos_abiertos(resumenes_abiertas)
    dashboard = generar_resumen_dashboard(resumenes_abiertas,resumenes_todas,configuracion)
    
    tarjetas = generar_tarjetas_activos(operaciones,posiciones)
    
    for tarjeta in tarjetas:
        
        tarjeta["ganancia_realizada"] = formatear_dinero(tarjeta["ganancia_realizada"])
        tarjeta["rentabilidad"] = formatear_porcentaje(tarjeta["rentabilidad"])
    
    for resumen in resumenes_activos:

        resumen["cantidad_formateada"] = formatear_cantidad(resumen["cantidad_actual"],resumen["activo"])
        resumen["precio_promedio_formateado"] = formatear_dinero(resumen["precio_promedio"])
        resumen["capital_invertido_formateado"] = formatear_dinero(resumen["capital_invertido_actual"])
    
    return render_template("index.html",resumenes=resumenes_abiertas,dashboard=dashboard,tarjetas=tarjetas,resumenes_activos=resumenes_activos)