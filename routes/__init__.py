from .inicio import inicio_bp
from .compras import compras_bp
from .ventas import ventas_bp
from .configuracion import configuracion_bp 
from .posiciones import posiciones_bp

def registrar_blueprints(app):

    app.register_blueprint(inicio_bp)
    app.register_blueprint(compras_bp)
    app.register_blueprint(ventas_bp)
    app.register_blueprint(configuracion_bp)
    app.register_blueprint(posiciones_bp)