from flask import Blueprint, render_template

# Crea un blueprint para las rutas
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')  # Asegúrate de que index.html existe en templates/
