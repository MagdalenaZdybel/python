#Korzystając z API http://py.net/ po pobraniu klucza API (api_key)
# ustaw status swojego użytkownika (/user_status/set) i sprawdź status innych
# (/user_status) w szczególności koleżanki/kolegi obok.

import requests
url = 'http://py.net/auth'
dane = {"name": "Magdalena", "password": "ojojoj"}
resp = requests.post(url, json=dane)

print(resp.json())

dane_logowania = resp.json()
api = dane_logowania['api_key']
print(api)

url = 'http://py.net/user_status'
resp = requests.get(url, json=dane)

print(resp.json())

sasiad = resp.json()
status_sasiada = sasiad['JakubWedrowycz2']
print("ststus mojego sąsiada: ", status_sasiada)

url = 'http://py.net/user_status/set'
dane = {"api_key": api, "status": "jest czy nie jest"}
resp = requests.post(url, json=dane)

print(resp.json())
