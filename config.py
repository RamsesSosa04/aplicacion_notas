import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta_para_formularios'
    DATABASE = os.path.join(BASE_DIR, 'app.db')
