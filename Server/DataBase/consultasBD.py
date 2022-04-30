import sqlite3
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






