import jwt
import datetime
from project_library_api.resources.user import User
from project_library_api.config import SECRET_KEY_JWT

class Authentication:
    def __init__(self):
        self.secret_key = SECRET_KEY_JWT
        
    def generate_token(self, username):
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload['username']
        except jwt.ExpiredSignatureError:
            return 'Token expirado. Faça login novamente.'
        except jwt.InvalidTokenError:
            return 'Token inválido. Faça login novamente.'

    def login(self, username, password):
        user = User(username, password)
        if user.check_credentials(username, password):
            token = self.generate_token(username)
            return {'message': 'Login bem-sucedido', 'token': token}
        else:
            return {'message': 'Credenciais inválidas'}

    def protected_route(self, token):
        username = self.verify_token(token)
        if username:
            return f'Bem-vindo, {username}! Esta é uma rota protegida.'
        else:
            return 'Token inválido ou expirado. Faça login novamente.'



