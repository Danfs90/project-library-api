from flask import request
from flask.blueprints import Blueprint
from project_library_api.resources.auth import Authentication
from project_library_api import db

actions = Blueprint('auth', 'auth', url_prefix='/v1/auth')

@actions.route('/login', methods=['POST'])
def login():
    """Rota responsavel pelo login do usuario"""
    
    data = request.json
    
    username = data.get('username')
    password = data.get('password')
    
    auth_system = Authentication()
    login_response = auth_system.login(username, password, db.session) 

    return login_response, 200
