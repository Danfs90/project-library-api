import jwt
import datetime
from project_library_api.util import hash_password
from project_library_api.config import SECRET_KEY_JWT

class Authentication():
    def __init__(self, email, password):
        self.secret_key = SECRET_KEY_JWT
        self.email = email
        self.password = password
        
    def generate_token(self):
        payload = {
            'email': self.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload['email']
        except jwt.ExpiredSignatureError:
            return 'Token expirado. Faça login novamente.'
        except jwt.InvalidTokenError:
            return 'Token inválido. Faça login novamente.'

    def login(self):

        if self.check_credentials():
            token = self.generate_token(self.email)
            return {'message': 'Login bem-sucedido', 'token': token}
        else:
            return {'message': 'Credenciais inválidas'}

    def protected_route(self, token):
        username = self.verify_token(token)
        if username:
            return f'Bem-vindo, {username}! Esta é uma rota protegida.'
        else:
            return 'Token inválido ou expirado. Faça login novamente.'

    def check_credentials(self):

        hashed_password = hash_password(self.email, self.password)
        if hashed_password:
            email = ''
            password = ''
            #TODO criar validação de banco aqui
        
        return self.email == email and self.password == password

