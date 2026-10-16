import requests
from flask import Blueprint, render_template, session, redirect, url_for

# Definimos el Blueprint para agrupar las rutas relacionadas al perfil
perfil_bp = Blueprint('perfil', __name__, template_folder='templates')

# Ruta que renderiza el perfil del usuario (localhost:5000/perfil)
@perfil_bp.route('/perfil', methods=['GET'])
def mostrar_perfil():
    
    #Si el usuario no esta logeado: Redirigimos de inmediato al Login.
    if 'token' not in session:
        return redirect(url_for('auth.login')) # Ajusta 'auth.login' según tu Blueprint de Login
    
    # 2 HEADER DE AUTENTICACIÓN: Preparamos el "pase de entrada" en los headers.
    # .NET espera estrictamente el formato "Bearer [Token]" para poder validar el JWT.
    headers = {
        'Authorization': f"Bearer {session['token']}"
    }
    
    try:
        # LLAMAMOS A LA API CON 'GET' Y ALMACENAMOS SU RESPUESTA ( status_code, JSON's, etc )
        url_api_perfil = "http://localhost:5055/api/perfil"
        respuesta_api = requests.get(url_api_perfil, headers=headers, timeout=5)
        
        # 3 VERIFICACIÓN DE RESPUESTA:
        if respuesta_api.status_code == 200:
            # .json() transforma el string de respuesta de .NET en un diccionario de Python
            datos_usuario = respuesta_api.json()
            
            # SIMULACIÓN DE TICKETS (Temporal): 
            # Como aún no creamos el TicketsController, enviamos una lista de prueba 
            # para verificar que el carrusel horizontal de Jinja2 pinte de forma dinámica.
            tickets_prueba = [
                {
                    "id": 101, 
                    "titulo": "Error crítico en login de usuarios", 
                    "descripcion": "El botón rompe la sesión al hacer clic repetidas veces.", 
                    "estado": "En Proceso"
                },
                {
                    "id": 102, 
                    "titulo": "Ajustar sombras neubrutalistas en CSS", 
                    "descripcion": "La sombra del contenedor principal debe ser sólida y de 8px.", 
                    "estado": "Sin Iniciar"
                },
                {
                    "id": 103, 
                    "titulo": "Validar contraseñas vacías en API", 
                    "descripcion": "PostgreSQL arroja error si el campo hash llega nulo.", 
                    "estado": "Terminado"
                }
            ]
            
            # 4 RENDERIZADO EXITOSO: Enviamos los datos reales del usuario y los tickets de prueba al HTML
            return render_template('perfil/perfil.html', usuario=datos_usuario, tickets=tickets_prueba)
        
        # Si la API responde 401 (Token inválido o expirado), limpiamos la sesión (.pop) y mandamos al login
        elif respuesta_api.status_code == 401:
            session.pop('token', None)
            return redirect(url_for('auth.login'))
            
        else:
            # Si hay otro error de la API (ej. 500), pintamos el template mostrando el error brutalista
            return render_template('perfil/perfil.html', ERROR=f"La API respondió con código: {respuesta_api.status_code}")
            
    except requests.exceptions.RequestException:
        # CAPTURA DE CAÍDAS: Si la API de .NET está apagada, evitamos que Flask tire un pantallazo de error
        return render_template('perfil/perfil.html', ERROR="No se pudo establecer conexión con el servidor backend (.NET)")