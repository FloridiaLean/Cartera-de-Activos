from .inicio import inicio_bp
from .compras import compras_bp
from .ventas import ventas_bp

def registrar_blueprints(app):

    app.register_blueprint(inicio_bp)
    app.register_blueprint(compras_bp)
    app.register_blueprint(ventas_bp)