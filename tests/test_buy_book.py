import pytest
from flask import json
import logging


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

def test_add_book_success(client, mocker):
    """
    Test successful book payment creation
    """
    # Test data
    payload = {
        "id_user": 5,
        "id_book": 4
    }
    
    # Make the POST request
    response = client.post(
        '/v1/my_books/payment',
        data=json.dumps(payload),
        content_type='application/json'
    )
    data = json.loads(response.data.decode())

    LOGGER.info(data)

    assert response.status_code == 200
    
    assert data['status_code'] == 200
    assert data['message'] == 'Livro adicionado com sucesso!'
    assert len(data['data']) == 1
    assert data['data'][0]['book_id'] == payload['id_book']
    

def test_add_book_failure(client, mocker):
    """
    Test book payment creation failure
    """
    # Test data
    payload = {
        "id_user": 5,
        "id_books": 0
    }
    
    # Make the POST request
    response = client.post(
        '/v1/my_books/payment',
        data=json.dumps(payload),
        content_type='application/json'
    )

    data = json.loads(response.data.decode())
    
    LOGGER.info(data)    
    # Assert the response
    assert response.status_code == 500
    assert data['status_code'] == 500
    assert data['message'] == 'Erro ao criar o pagamento do novo livro!'
    assert data['data'] is False

# Fixtures necessários para os testes
@pytest.fixture
def client():
    """Fixture para criar um cliente de teste"""
    from project_library_api.app import app
    
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client
