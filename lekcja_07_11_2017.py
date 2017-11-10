import requests
resp = requests.get('http://py.net/health')
print(resp.json()['health'])

import requests
resp = requests.get('http://py.net/status')
print(resp.json())
resp = requests.post(
    'http://py.net/status/set',
    json={
        "status": "testowy klocek"
    }
)
print(resp.json())
resp = requests.get('http://py.net/status')
print(resp.json())