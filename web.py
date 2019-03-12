import os

import self as self
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect, secure_filename

import Controlador.ControladorVentanaClasificador as clasificador
import Controlador.ControladorVentanaEntrenamiento as entrenador

import itertools

import numpy as np
from PyQt5.QtWidgets import QInputDialog, QMessageBox
import pickle
from sklearn.metrics import confusion_matrix, accuracy_score
from Vista.VistaVentanaEntrenamiento import *
import Controlador.ControladorVentanaPrincipal as ventanaPrincipal
from os.path import isfile, join
from os import listdir
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

#class web():
    #def __init__(self):
        #self.prueba()

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('entrenar') == 'entrenar':
            # pass
            print("Entrenar")
        elif request.form.get('clasificar') == 'clasificar':
            # pass # do something else
            print("Decrypted")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
         return render_template("index.html")
         print("No Post Back Call")
    return render_template("index.html")

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=82)

