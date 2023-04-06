import requests

api_url = 'http://localhost:8000'

def test_healthcheck():
    response = requests.get(f'{api_url}/__health')
    assert response.status_code == 200

class TestBooks():
    def test_get_empty_books(self):
        response = requests.get(f'{api_url}/books')
        assert response.status_code == 200
        #assert len(response.json()) == 0
