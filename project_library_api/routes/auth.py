import logging

from flask import request
from flask.blueprints import Blueprint
from project_library_api import db
from project_library_api.factory import new_login
from project_library_api.util import api_response

LOGGER = logging.getLogger(__name__)

actions = Blueprint('auth', 'auth', url_prefix='/v1/auth')

@actions.route('/login', methods=['POST'])
def login():
    """Rota responsavel pelo login do usuario"""
    try:
        
        LOGGER.info("Iniciando autenticação do usuario")

        data = request.json
        
        hash = data.get('hash')
        
        auth_system = new_login(hash, db.session)
        login_response, status= auth_system.login() 

        return api_response(data=login_response['data'], message=login_response['message'], status_code=status)
    except Exception as e:
        LOGGER.info("Erro na autenticação do usuario: ".format(e))
        return "Erro no servidor", 500