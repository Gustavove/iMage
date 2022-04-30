import os

from flask import Flask, request, jsonify, abort
from DataBase import consultasBD


app = Flask(__name__)

@app.route('/crea_partida', methods=['POST'])
def crea_partida():
    nick = request.form["nick"]
    rondas_totales = request.form["rondas_totales"]
    conn = consultasBD.connectDB()

    codigo = consultasBD.nueva_patida(conn, rondas_totales)
    consultasBD.nueva_jugador(conn, nick, codigo)

    consultasBD.closeBD(conn)

    return codigo

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
    consultasBD.closeBD(conn)

    result = []
    for i in bd_result:
        result.append({"Nick": i[0], "Puntuacion": i[1]})

    return jsonify(result)
