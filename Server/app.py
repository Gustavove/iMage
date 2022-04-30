import os

from flask import Flask, request, jsonify, abort, send_from_directory
from BaseDatos import consultasBD


app = Flask(__name__)

#@app.route('/', methods=['GET'])

#@app.route('/profesores/mensajes', methods=['POST'])
#def new_mensaje():  # put application's code here