import os

from flask import Flask, request, jsonify, abort
from DataBase import consultasBD
import requests
import json
import random
from pyunsplash import PyUnsplash

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

app = Flask(__name__)

@app.route('/crea_partida', methods=['POST'])
def crea_partida():
    nick = request.form["nick"]
    conn = consultasBD.connectDB()

    codigo = consultasBD.nueva_partida(conn)
    consultasBD.nueva_jugador(conn, nick, codigo)

    consultasBD.closeBD(conn)

    result = []
    result.append({"Code": codigo})

    return jsonify(result)

@app.route('/unir_jugadores', methods=['POST'])
def unir_jugadores():
    nick = request.form["nick"]
    codigo_partida = request.form["codigo_partida"]
    conn = consultasBD.connectDB()

    consultasBD.nueva_jugador(conn, nick, codigo_partida)

    consultasBD.closeBD(conn)

    resp = jsonify(success=True)
    return resp

@app.route('/obtener_puntuacion_total', methods=['GET'])
def obtener_puntuacion_total():
    query_parameters = request.args
    codigo_partida= query_parameters.get('codigo_partida')
    conn = consultasBD.connectDB()

    bd_result = consultasBD.obtener_puntuaciones_totales_partida(conn, codigo_partida)
    consultasBD.acabar_partida(conn, codigo_partida)

    consultasBD.closeBD(conn)

    result = []
    for i in bd_result:
        result.append({"Nick": i[0], "Puntuacion": i[1]})

    return jsonify(result)

@app.route('/obtener_imagen', methods=['GET'])
def obtener_imagen():
    query_parameters = request.args
    codigo_partida = query_parameters.get('codigo_partida')

    ### OBTENER FOTO RANDOM

    UNSPLASH_ACCESS_KEY = 'V5QCNGe1Ips6O2bWF_ZFczvHTvBKBoFHsxHRNYJb23M'

    pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)

    photos = pu.photos(type_='random', count=1, featured=True)
    [photo] = photos.entries

    ##Guardamos la imagen
    consultasBD.insertar_imagen_partida(conn, photo.id, photo.link_download, codigo_partida)

    result = []
    result.append({"id_foto": photo.id, "url": photo.link_download})
    return result

@app.route('/descricion_jugador', methods=['POST'])
def obtener_score():
    nick = request.form["nick"]
    codigo_partida = request.form["codigo_partida"]
    url_imagen = request.form["url_imagen"]
    descripcion = request.form["descripcion"]

    IMAGA_URL = "https://api.imagga.com/v2/tags"
    querystring = {"image_url": url_imagen, "version": "2"}

    headers = {
        'accept': "application/json",
        'authorization': "Basic YWNjXzNiOGUwOWYxOWNhMjU4ZDo3N2FhZGM3NGNkZjA0ZjBjZWQyNzM0YjM3MWU3ZDllYQ=="
    }

    response = requests.request("GET", IMAGA_URL, headers=headers, params=querystring)

    score = obtener_score(descripcion, response.json())


    #Obtener score actual jugador
    conn = consultasBD.connectDB()

    puntos_totales = 0
    bd_result = consultasBD.obtener_score_jugador(conn, nick)

    #Sumar actual score con el nuevo
    for i in bd_result:
        puntos_totales = i[0] + score

    #Insertar nuevos datos
    consultasBD.sumar_score(conn, nick, score)

    consultasBD.closeBD(conn)

    result = []
    result.append({"Score": score})
    return result

if __name__ == '__main__':
    app.run(debug=True)