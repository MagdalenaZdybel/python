#Korzystając z API http://py.net/ po pobraniu klucza API (api_key)
# ustaw status swojego użytkownika (/user_status/set) i sprawdź status innych
# (/user_status) w szczególności koleżanki/kolegi obok.

import requests
url = 'http://py.net/auth'
dane = {"name": "Magdalena", "password": "ojojoj"}
resp = requests.post(url, json=dane)

print(resp.json())
