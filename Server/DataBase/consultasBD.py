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
    query = "SELECT * FROM partida p where codigo = ?"
    c = conn.cursor()
    tofilter = []
    tofilter.append(codigo_partida)
    result = c.execute(query, tofilter).fetchone()[0]
    return result

def nueva_partida (conn):
    c = conn.cursor()
    codigo = random.randint(100000, 999999)
    try:
        nueva_partida = (codigo)
        query = '''INSERT INTO partida (codigo) 
        VALUES (?)'''
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
    query = ''' SELECT j.nick, j.puntos FROM jugador j WHERE j.partida = ?'''
    c = conn.cursor()
    tofilter = []
    tofilter.append(id_partida)
    result = c.execute(query, tofilter).fetchall()

    return result

def insertar_imagen_partida(conn, id_imagen, url, codigo_partida):
    c = conn.cursor()
    try:
        nueva_imagen = (id_imagen, url, codigo_partida)
        query = '''INSERT INTO imagen (id, url, partida) VALUES (?,?,?)'''
        c.execute(query, nueva_imagen)
        conn.commit()

    except Error as e:
        print(e)

def acabar_partida(conn, codigo_partida):
    c = conn.cursor()
    try:
        partida = (codigo_partida)
        query = '''DELETE FROM partida WHERE codigo = ?'''
        c.execute(query, partida)
        conn.commit()

    except Error as e:
        print(e)

def obtener_score_jugador(conn, nick):
    query = ''' SELECT j.puntos FROM jugador j WHERE j.nick = ?'''
    c = conn.cursor()
    tofilter = []
    tofilter.append(nick)
    result = c.execute(query, tofilter).fetchall()

def sumar_score(conn, nick, score):

    modificadores = (score, nick)

    try:
        query= ''' UPDATE jugador
                      SET puntos = ? ,
                      WHERE nombre = ?'''
        c = conn.cursor()
        c.execute(query, modificadores)
        conn.commit()
    except Error as e:
        print(e)