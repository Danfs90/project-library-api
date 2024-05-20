import hashlib
from project_library_api.resources.user import User
from unittest.mock import MagicMock


# faz o teste se o usuario foi inserido no banco.
def test_create_registration(monkeypatch):
    mock_db = MagicMock()
    user = User(username='test_user', password='password', db=mock_db, 
                birth_date='2023-01-01T00:00:00.000Z', address='123 Street', 
                zip_code='12345', role='user', number='1234567890')

    monkeypatch.setattr('project_library_api.models.Users', MagicMock())
    user.create_registration()
    assert mock_db.add.called
    assert mock_db.commit.called


# testa se o hash da senha foi gerado corretamente.
def test_hash_password():
    user = User(username='test_user', password='password')
    hashed_password = user._hash_password('password')
    expected_hash = hashlib.sha256('test_userpassword'.encode()).hexdigest()
    assert hashed_password == expected_hash


#
def test_check_credentials(monkeypatch):
    mock_user = User(username='test_user', password='password')

    def mock_hash_password(password):
        return 'hashed_password'

    monkeypatch.setattr(mock_user, '_hash_password', mock_hash_password)
    result = mock_user.check_credentials('test_user', 'password')
    assert result == True

    result = mock_user.check_credentials('wrong_user', 'password')
    assert result == False
