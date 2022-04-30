import requests
import json
from pexels_api import API
import random

### OBTENER TAGS DE IMMAGA

IMAGA_URL = "https://api.imagga.com/v2/tags"
UNSPLASH_URL = ""


querystring = {"image_url":"https://source.unsplash.com/random","version":"2"}

print(querystring)

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjXzNiOGUwOWYxOWNhMjU4ZDo3N2FhZGM3NGNkZjA0ZjBjZWQyNzM0YjM3MWU3ZDllYQ=="
    }

response = requests.request("GET", IMAGA_URL, headers=headers, params=querystring)

print("Respuestas: ", response.text)

palabra = input("Ingresa una palabra: ")

if palabra in response.text:
    print("SI")