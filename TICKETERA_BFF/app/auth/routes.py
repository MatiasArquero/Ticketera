from flask import redirect, render_template, request, session, url_for
from flask import Blueprint
import requests

auth_bp = Blueprint('auth', __name__, template_folder='templates')
API_BASE_URL = "http://localhost:5055/api/auth"


def _usuario_con_sesion_activa():
    """FASE 0: si ya hay JWT en sesión, no volver a mostrar login/registro."""
    return 'token' in session and session.get('token')


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    # FASE 0: limpiar sesión BFF y volver al login
    session.pop('token', None)
    return redirect(url_for('auth.login'))


@auth_bp.route('/registrate', methods=['GET', 'POST'])
def registrate():
    if _usuario_con_sesion_activa():
        return redirect(url_for('perfil.mostrar_perfil'))

    MENSAJE_ERROR = None

    if request.method == 'POST':
        username = request.form.get('username')
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        password = request.form.get('password')

        Usuario = {
            "Username": username,
            "UsuarioNombre": nombre,
            "UsuarioApellido": apellido,
            "Email": email,
            "Password": password
        }
        try:
            url_destino = f"{API_BASE_URL}/registrar"
            respuesta_api = requests.post(url_destino, json=Usuario, timeout=5)

            if respuesta_api.status_code in [200, 201]:
                return redirect(url_for('auth.login'))
            else:
                try:
                    datos_error = respuesta_api.json()
                    MENSAJE_ERROR = datos_error.get("mensaje", "LA API NO POSEE MSJ")
                except ValueError:
                    MENSAJE_ERROR = f"ERROR EN EL REGISTRO ( CODIGO: {respuesta_api.status_code} )"

        except requests.exceptions.ConnectionError:
            MENSAJE_ERROR = "No se pudo establecer comunicación con el servidor(.NET apagado)"
        except requests.exceptions.Timeout:
            MENSAJE_ERROR = "El servidor de registro tardó demasiado en responder. Intenta más tarde."

    return render_template("auth/registrate.html", ERROR=MENSAJE_ERROR)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if _usuario_con_sesion_activa():
        return redirect(url_for('perfil.mostrar_perfil'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        payload = {
            "Email": email,
            "Password": password
        }

        try:
            respuesta_api = requests.post(f"{API_BASE_URL}/login", json=payload, timeout=5)

            if respuesta_api.status_code == 200:
                datos_api = respuesta_api.json()
                # FASE 0: la API devuelve la propiedad "token" (no tokenString)
                token = datos_api.get('token')
                if not token:
                    return render_template(
                        'auth/login.html',
                        ERROR="La API no devolvió un token de sesión válido."
                    )
                session['token'] = token
                return redirect(url_for('perfil.mostrar_perfil'))

            else:
                error_msg = respuesta_api.json().get('mensaje', 'Credenciales inválidas')
                return render_template('auth/login.html', ERROR=error_msg)

        except requests.exceptions.RequestException:
            return render_template('auth/login.html', ERROR="La API de .NET está apagada")

    return render_template('auth/login.html')
