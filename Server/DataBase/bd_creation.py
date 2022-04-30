import sqlite3

conn = sqlite3.connect('iMageDB')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS partida
          ([codigo] INTEGER KEY)
          ''')


c.execute('''
          CREATE TABLE IF NOT EXISTS jugador
          ([nick] TEXT PRIMARY KEY, [puntos] INTEGER, [codigo] INTEGER REFERENCES partida(codigo))
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS imagenes
          ([id] INTEGER PRIMARY KEY)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS imagenesPartida
          ([id_partida] INTEGER REFERENCES partida(codigo), [id_imagen] INTEGER REFERENCES imagenes(id))
          ''')

conn.commit()