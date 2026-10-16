import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Llave secreta obligatoria para cifrar las cookies de sesión (donde guardaremos el JWT de .NET)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'TuLlaveSecretaSuperSeguraParaLasCookies2026')

    from app.auth.routes import auth_bp
    from app.home.routes import home_bp
    from app.perfil.routes import perfil_bp  # FASE 0: /perfil con Bearer hacia la API

    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(perfil_bp)

    #INICIAR APP
    return app





