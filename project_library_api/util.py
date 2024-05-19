import hashlib
from flask import jsonify

def api_response(status_code, message=None, data=None):
    """
    Função para padronizar os retornos de API.
    
    Args:
        status_code (int): Código de status HTTP.
        message (str): Mensagem de erro (opcional).
        data (dict): Dados a serem retornados (opcional).

    Returns:
        response (json): Resposta JSON padronizada.
    """
    response = {
        'status_code': status_code,
        'message': message,
        'data': data
    }
    return jsonify(response), status_code

def hash_password(email, password):
    """
    Função para hashear uma senha.
    
    Args:
        password (int): senha do usuario.

    Returns:
        response (string): Hash da concatenacao email + password.
    """ 
    hash_string = email + password
    hashed_password = hashlib.sha256(hash_string.encode()).hexdigest()
    return hashed_password