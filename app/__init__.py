from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # Configuración opcional desde `config.py`

    # Importa y registra las rutas
    from .routes import routes
    app.register_blueprint(routes)

    return app
