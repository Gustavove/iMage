import requests
import json
import random
from pyunsplash import PyUnsplash

### OBTENER FOTO RANDOM

UNSPLASH_ACCESS_KEY='V5QCNGe1Ips6O2bWF_ZFczvHTvBKBoFHsxHRNYJb23M'

pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)

photos = pu.photos(type_='random', count=1, featured=True)
[photo] = photos.entries
print(photo.id, photo.link_download)

### OBTENER TAGS DE IMMAGA


UNSPLASH_URL = ""


IMAGA_URL = "https://api.imagga.com/v2/tags"
querystring = {"image_url":photo.link_download,"version":"2"}

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjXzNiOGUwOWYxOWNhMjU4ZDo3N2FhZGM3NGNkZjA0ZjBjZWQyNzM0YjM3MWU3ZDllYQ=="
    }

response = requests.request("GET", IMAGA_URL, headers=headers, params=querystring)

print("Respuestas: ", response.json())


def obtener_score(palabras, tags):
    tags = tags.get('result')
    tags = tags.get('tags')
    score = 0
    acertadas = []
    for tag in tags:
        tagname = tag.get('tag')
        # print(type(tagname))
        # print(f'Tag: {tagname.get("en")} - Score: {tag.get("confidence")}')
        if tagname.get('en') in palabras:
            score += tag.get('confidence') * 10
            acertadas.append(tagname.get('en'))
    return (score, acertadas)

words = 4
i = 0
palabras = []
while i < words:
    palabra = input("Ingresa una palabra: ")
    palabras.append(palabra)
    i+=1


score = obtener_score(palabras, response.json())

print("Resutlado obenitdo: ", score)

# correcta = palabra_correcta(palabras, response.text)

