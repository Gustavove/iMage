import sqlite3
import random
from sqlite3 import Error
import os
import sys
absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)

def connectDB():
    conn = None
    try:
        conn = sqlite3.connect(os.path.join(fileDirectory, "iMageDB"))
    except Error as e:
        print(e)
    return conn

def closeBD(conn):
    if conn:
        conn.close()

def consultar_información_partida(conn, codigo_partida):
    query = "SELECT * FROM partida p"
    c = conn.cursor()
    tofilter = []
    tofilter.append(codigo_partida)
    result = c.execute(query, tofilter).fetchone()[0]
    return result

def nueva_partida (conn, rondas_totales):
    c = conn.cursor()
    codigo = random.randint(100000, 999999)
    try:
        nueva_partida = (codigo, 0, rondas_totales)
        query = '''INSERT INTO partida (codigo, ronda_actual, rondas_actuales) 
        VALUES (?,?,?)'''
        c.execute(query, nueva_partida)
        conn.commit()

    except Error as e:
        print(e)

    return codigo

def nuevo_jugador(conn, nick, id_partida):
    c = conn.cursor()
    try:
        nuevo_jugador = (nick, 0, id_partida)
        query = '''INSERT INTO jugador (nick, puntos, codigo) 
        VALUES (?,?,?)'''
        c.execute(query, nuevo_jugador)
        conn.commit()

    except Error as e:
        print(e)

def obtener_puntuaciones_totales_partida(conn, id_partida):
    c = conn.cursor()
    try:
        datos = (id_partida)
        query = ''' SELECT j.nick, j.puntos FROM jugador j WHERE j.partida = ?'''
        c.execute(query, datos)
        conn.commit()

    except Error as e:
        print(e)

