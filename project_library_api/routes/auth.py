from flask.blueprints import Blueprint
from project_library_api.resources.auth import Authentication
actions = Blueprint('auth', 'auth', url_prefix='/v1/auth')

@actions.route('/login', methods=['GET'])
def login():
    """Rota responsavel pelo login do usuario"""
    auth_system = Authentication()

    login_response = auth_system.login('user', 'password') 
    #TODO necessario finalizar rota
    print("OK")
    return "200"
