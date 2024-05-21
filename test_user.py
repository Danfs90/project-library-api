import pytest
import hashlib
from flask import Flask
from project_library_api.resources.user import User
from project_library_api.util import hash_password, api_response
from unittest.mock import MagicMock


# faz o teste se o banco foi chamado e o usuario foi inserido corretamente no banco.
def test_create_registration(monkeypatch):
    mock_db = MagicMock()
    user = User(first_name='username', last_name='teste', cellphone='315432566', email='teste@gmail.com', password='password', db=mock_db, 
                birth_date='2023-01-01T00:00:00.000Z', address='123 Street', 
                zip_code='12345', role='user', number='1234567890')

    monkeypatch.setattr('project_library_api.models.Users', MagicMock())
    user.create_registration()

    assert mock_db.add.called
    assert mock_db.commit.called


# testa se o hash da senha foi gerado corretamente.
def test_hash_password():
    email = "user@example.com"
    password = "securepassword"
    expected_hash = hashlib.sha256((email + password).encode()).hexdigest()

    assert hash_password(email, password) == expected_hash


# Chama a API e testa se a função api_response retorna o status code correto
@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app

def test_api_response(app):
    with app.test_request_context():
        response, status_code = api_response(200, "Success", {"key": "value"})
        assert status_code == 200
        json_data = response.get_json()
        assert json_data['status_code'] == 200
        assert json_data['message'] == "Success"
        assert json_data['data'] == {"key": "value"}

