import requests

URL = "http://127.0.0.1:2224/whosthatpokemon/"

print(requests.get(URL).json())
