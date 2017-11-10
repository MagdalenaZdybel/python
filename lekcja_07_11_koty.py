import requests
resp = requests.get('http://py.net/cat')
with open('cat','wb') as file:
    file.write(resp.content)

