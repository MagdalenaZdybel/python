import requests
url = 'http://py.net/register'
dane = {"name": "Magdalena",
        "password": "ojojoj"}
resp = requests.post(url, json=dane)
print(resp.json())
