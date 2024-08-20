import pytest
import requests
from lesson8.constants import X_client_URL

@pytest.fixture()
def get_token():
    creds = {'username': 'ivan', 'password': 'sunshine123'}
    resp = requests.post(f"{X_client_URL}/auth/login", json=creds)
    return resp.json()['userToken']
