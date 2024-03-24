from flask.blueprints import Blueprint

actions = Blueprint('auth', 'auth', url_prefix='/v1/auth')

@actions.route('/login', methods=['GET'])
def auth_get():
    pass
