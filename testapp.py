import json
import requests
def test_app_up():
    url = 'https://ci-cd-appservice.azurewebsites.net'
    response = requests.get(url)
    assert response.status_code == 200
    