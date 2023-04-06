import requests

api_url = 'http://localhost:8000'


class TestBooks():
    def test_get_empty_books(self):
        response = requests.get(f'{api_url}/books')
        assert response.status_code == 200
        #assert len(response.json()) == 0
