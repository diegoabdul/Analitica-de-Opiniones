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
import Controlador.ControladorVentanaWebScraper as ventanaWebScraper


class NewApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(NewApp, self).__init__()
        self.setupUi(self)
        self.btn_atras.clicked.connect(self.volverAtras)
        self.btn_directorio.clicked.connect(self.filechooser)
        self.btn_entrenar.clicked.connect(self.entrenamiento)
        self.btn_guardar.clicked.connect(self.guardar)
        self.checkBox_detectarIdioma.stateChanged.connect(self.habilitarOpcionesCheckBox)
        self.rutaDirectorio = ""
        self.existenArchivos = False
        self.modeloAlgoritmo = None
        self.diccionarioEntrenamiento = None
        self.titulosGrafico = None
        self.figure = plt.figure()
        self.grafico = self.figure.add_subplot(111)
        self.canvas = FigureCanvasQTAgg(self.figure)
        lay = QtWidgets.QVBoxLayout(self.panelEstadistica)
        lay.addWidget(self.canvas)
        self.show()

    def volverAtras(self):
        """
        Método encargado de volver al menu principal
        """
        self.Open = ventanaPrincipal.MainWindow()
        self.Open.show()
        self.cerraVentana()

    def cerraVentana(self):
        """
        Método encargado de cerrar la ventana actual
        """
        self.close()

    def filechooser(self):
        """
        Método para introducir la ruta donde se encuentran las carpetas con  las valoraciones a entrenar.
        Recorre esa ruta en búsqueda de tales archivos y genera una tab por cada carpeta con archivos que encuentre
        """
        self.Open = ventanaWebScraper.NewApp()
        self.Open.show()
        self.cerraVentana()


    def entrenamiento(self):
        """
        Método para entrenar las valoraciones
        Manda y recoge lo referente al proceso entrenarDatos de la clase algoritmo
        """
        if(self.rutaDirectorio and self.existenArchivos):
            print("Ruta valoraciones: ", self.rutaDirectorio)
            self.btn_guardar.setEnabled(True)
            from Utilidades.Algoritmia import algoritmo
            claseAlgoritmo = algoritmo()
            datosMatriz = claseAlgoritmo.entrenarDatos(self.rutaDirectorio,self.comboBox_algoritmo.currentText(),
                                                       self.comboBox_idioma.currentText(), self.checkBox_detectarIdioma.isChecked())
            self.configurarFiguraGrafico(datosMatriz)
            self.modeloAlgoritmo = datosMatriz[3]
            self.diccionarioEntrenamiento = datosMatriz[4]

        else:
            self.dialogo("No has seleccionado uno o más directorios", "Debe seleccionar el directorio de las valoraciones antes de entrenar",
                              QMessageBox.Warning)


    def guardar(self):
        """
        Método que solicita al usuario asignar un nombre al entrenamiento realizado, y donde con ese nombre
        guardamos el modelo, el diccionario y los titulos de cada sección
        """
        nombreArchivo, ok = QInputDialog.getText(self, 'Guardar', 'Introduzca el nombre del modelo a guardar:')
        if ok:
            nombreArchivo = str(nombreArchivo)
            if nombreArchivo:
                with open('../ModelosGuardados/' + nombreArchivo + ".model", 'wb') as archivo:
                    pickle.dump(self.modeloAlgoritmo, archivo)

                with open('../ModelosGuardados/' + nombreArchivo + ".vocabulary", 'wb') as archivo:
                    pickle.dump(self.diccionarioEntrenamiento, archivo)

                with open('../ModelosGuardados/' + nombreArchivo + ".target", 'wb') as archivo:
                    pickle.dump(self.titulosGrafico, archivo)

                self.dialogo("Modelo Guardado", "El entrenamiento se ha guradado satisfactoriamente.", QMessageBox.Information)

            else:
                self.dialogo("Imposible guardar", "Para guardar debe especificar un nombre para el entrenamiento.", QMessageBox.Warning)



    def configurarFiguraGrafico(self, datosMatriz):
        """
        Método encargado de dibujar las gráficas con los datos obtenidos del entrenamiento en tiempo real
        :param datosMatriz: recibe una lista con el total de datos importantes para representar la matriz de confusión
        """
        self.figure.clear()
        y_test = datosMatriz[0]
        y_pred = datosMatriz[1]
        self.titulosGrafico = datosMatriz[2]
        matriz = confusion_matrix(y_test, y_pred)
        porcentajeAcierto = accuracy_score(y_test, y_pred)
        self.grafico = self.figure.add_subplot(111)
        plt.ylabel('\nValoraciones reales')
        barraLateral = self.grafico.matshow(matriz, cmap="YlGn", interpolation='bicubic')
        plt.colorbar(barraLateral,fraction=0.046, pad=0.04) #los dos ultimos argumentos son para hacer la barra igual de grande que la matriz
        tick_marks = np.arange(len(self.titulosGrafico))
        plt.xticks(tick_marks, self.titulosGrafico)
        plt.yticks(tick_marks, self.titulosGrafico, rotation=90)
        plt.xlabel('\nPrecisión algoritmo '+ self.comboBox_algoritmo.currentText() +': {:0.2f}%'.format(porcentajeAcierto*100))

        puntosAltos = matriz.max() / 2. #añadir label en el interior de la matriz
        for i, j in itertools.product(range(matriz.shape[0]), range(matriz.shape[1])):
            plt.text(j, i, format(matriz[i, j], '.0f'), horizontalalignment="center",
                     color="white" if matriz[i, j] > puntosAltos else "black")

        plt.draw()
        self.canvas.draw()
        self.panelEstadistica.repaint()  # linea necesaria para refrescar en Mac OS X el gráfico


    def habilitarOpcionesCheckBox(self):
        """
        Método encargado de habilitar o deshabilitar en tiempo real el combobox de idiomas en función
        el checkbox de detección de idiomas cambie
        """
        if (self.checkBox_detectarIdioma.isChecked()):
            self.idioma_text.setDisabled(True)
            self.comboBox_idioma.setDisabled(True)
        else:
            self.idioma_text.setEnabled(True)
            self.comboBox_idioma.setEnabled(True)



    def dialogo(self, titulo, texto, icono):
        """
        Método que se encarga de crear un dialogo de tipo informativo
        :param titulo: recibe un string con el titulo del dialogo
        :param texto: recibe un string con el texto que va a contener el dialogo
        :param icono: recibe un icono para mostrar en el dialogo
        """
        mensaje = QMessageBox()
        mensaje.setIcon(icono)
        mensaje.setWindowTitle(titulo)
        mensaje.setText(texto)
        mensaje.exec_()

