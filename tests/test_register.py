import pytest
from flask import json
from unittest.mock import patch, MagicMock
import logging


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
def test_register_user_success(client):
    """Teste para cenário de sucesso no registro de usuário"""
    # Arrange
    payload = {
        "email": "example@example.com.br",
        "first_name": "Lorem",
        "last_name": "Ipsum",
        "cellphone": "4199999999",
        "password": "password",
        "birth_date": "2021-01-01",
        "address": "Rua dos mercadores",
        "number": "100",
        "zip_code": "00000-000",
        "role": "user"
    }
    
    expected_response = {
        "data": None,
        "message": "Usuario criado com sucesso!",
        "status_code": 200
    }

    # Act
    with patch('project_library_api.routes.register.login') as mock_register:
        # Configura o mock para simular o registro bem-sucedido
        mock_user = MagicMock()
        mock_user.create_registration.return_value = None
        mock_register.return_value = mock_user
        
        response = client.post(
            '/v1/user/register',
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        # Assert
        response_data = json.loads(response.data.decode())

        LOGGER.info(response_data)

        assert response.status_code == 200
        assert response_data == expected_response


def test_register_user_missing_required_fields(client):
    """Teste para cenário de campos obrigatórios faltando"""
    # Arrange
    payload = {
        "last_name": "Ipsum",
        "cellphone": "4199999999",
        "address": "Rua dos mercadores",
        "number": "100",
        "zip_code": "00000-000"
    }
    
    expected_response = {
        "data": None,
        "message": "Parametros obrigatorios não enviados na requisição",
        "status_code": 400
    }

    # Act
    response = client.post(
        '/v1/user/register',
        data=json.dumps(payload),
        content_type='application/json'
    )
    
    # Assert
    response_data = json.loads(response.data.decode())

    LOGGER.info(response_data)

    assert response.status_code == 400
    assert response_data == expected_response

@pytest.fixture
def client():
    """Fixture para criar um cliente de teste"""
    from project_library_api.app import app
    
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client