import sqlite3

conn = sqlite3.connect('iMageDB.sqlite')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS partida
          ([codigo] INTEGER KEY)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS jugador
          ([nick] TEXT PRIMARY KEY, 
          [puntos] INTEGER, 
          [codigo] INTEGER, 
          FOREIGN KEY(codigo) REFERENCES partida(codigo) ON DELETE CASCADE)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS imagen
          ([id] STRING PRIMARY KEY, 
          [url] STRING, 
          [partida] INTEGER, 
          FOREIGN KEY(partida) REFERENCES partida(codigo) ON DELETE CASCADE)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS imagen_partida
          ([id_partida] INTEGER,
          [id_imagen] INTEGER,
          FOREIGN KEY(id_partida) REFERENCES partida(codigo), 
          FOREIGN KEY(id_imagen) REFERENCES imagen(id))
          ''')

conn.commit()