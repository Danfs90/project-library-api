from flask import request
from flask.blueprints import Blueprint
import logging
from project_library_api.resources.auth import Authentication
from project_library_api import db

LOGGER = logging.getLogger(__name__)

actions = Blueprint('auth', 'auth', url_prefix='/v1/auth')

@actions.route('/login', methods=['POST'])
def login():
    """Rota responsavel pelo login do usuario"""
    try:
        
        LOGGER.info("Iniciando autenticação do usuario")

        data = request.json
        
        username = data.get('email')
        password = data.get('password')
        
        auth_system = Authentication()
        login_response = auth_system.login(username, password, db.session) 

        return login_response, 200
    except Exception as e:
        LOGGER.info("Erro na autenticação do usuario: ".format(e))
        return "Erro no servidor", 500