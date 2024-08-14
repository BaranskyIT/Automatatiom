import pytest
import requests
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

X_client_URL = "http://example.com"
DATABASE_URL = "postgresql+psycopg2://user:password@localhost/testdb"

@pytest.fixture
def get_valid_token():
    response = requests.post(X_client_URL + '/auth/login', json={'username': 'roxy', 'password': 'animal-fairy'})
    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.text}")
    assert response.status_code == 201
    return response.json().get('token')

@pytest.fixture(scope='module')
def db():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    engine.dispose()

@pytest.fixture
def get_valid_token():
    response = requests.post(X_client_URL + '/auth/login', json={'username': 'roxy', 'password': 'animal-fairy'})
    assert response.status_code == 201
    return response.json().get('token')

@pytest.fixture
def test_employee(db):
    employee_data = {
        "first_name": "Test",
        "last_name": "User",
        "middle_name": "Middle",
        "phone": "1234567890",
        "email": "test.user@example.com",
        "avatar_url": "http://example.com/avatar.jpg",
        "company_id": 1
    }
    company_data = {
        "id": 1,
        "name": "Test Company"
    }
    
    # Удаляем существующие записи для предотвращения конфликтов
    db.execute(text("DELETE FROM company WHERE id = :id"), {'id': company_data['id']})
    db.execute(text("INSERT INTO company (id, name) VALUES (:id, :name)"), company_data)