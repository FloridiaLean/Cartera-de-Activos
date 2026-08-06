from flask import (
    Blueprint,
    render_template,
)
from datos import (
    posiciones,
    operaciones
)

from posiciones import (
    obtener_posiciones_abiertas
)
from calculos import (
    generar_resumen_todas_posiciones
)

inicio_bp = Blueprint("inicio",__name__)

@inicio_bp.route("/")
def inicio():
    
    posiciones_abiertas = obtener_posiciones_abiertas(posiciones)
    
    resumenes =generar_resumen_todas_posiciones(operaciones,posiciones_abiertas)
    
    return render_template("index.html",resumenes=resumenes)