import itertools
import numpy as np
from PyQt5.QtWidgets import QInputDialog, QMessageBox
import pickle
from sklearn.metrics import confusion_matrix, accuracy_score
from Vista.VistaVentanaEntrenamiento import *
import Controlador.ControladorVentanaPrincipal as ventanaPrincipal
from shutil import rmtree
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import Controlador.ControladorVentanaWebScraper as ventanaWebScraper
import Controlador.ControladorVentanaEntrenamientoSQL as ventanaSQL
from os.path import isfile, join
from os import listdir
import Utilidades.gestionBBDD as BBDD
import boto3
import os


class NewApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(NewApp, self).__init__()
        self.setupUi(self)
        self.btn_atras.clicked.connect(self.volverAtras)
        self.btn_directorio.clicked.connect(self.filechooser)
        self.btn_entrenar.clicked.connect(self.entrenamiento)
        self.btn_guardar.clicked.connect(self.guardar)
        self.checkBox_detectarIdioma.stateChanged.connect(self.habilitarOpcionesCheckBox)
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
        self.valoraciones(ventanaWebScraper.NewApp.flagDirectorio)
        self.valoraciones(ventanaSQL.MainWindow.flagDirectorio)
        self.btn_entrenarSQL.clicked.connect(self.SQL)

    def SQL(self):
        self.Open = ventanaSQL.MainWindow()
        self.Open.show()
        self.cerraVentana()

    def volverAtras(self):
        """
        Método encargado de volver al menu principal
        """
        self.Open = ventanaPrincipal.MainWindow()
        self.Open.show()
        self.cerraVentana()

    def valoraciones(self,flag):
        if flag:
            rutaDirectorio = ventanaWebScraper.NewApp.Directorio
            if rutaDirectorio:
                self.directorio_text.setText("Directorio: " + os.path.basename(rutaDirectorio))
                print(rutaDirectorio)
                self.rutaDirectorio = rutaDirectorio
                self.valoraciones_tab.clear()
                self.existenArchivos = False
                for dirname, dirnames, filenames in os.walk(rutaDirectorio):
                    for subdirname in dirnames:
                        ruta = os.path.join(dirname, subdirname)
                        self.tab = QtWidgets.QWidget()
                        self.tab.setObjectName((subdirname))
                        self.valoraciones_tab.addTab(self.tab, subdirname)
                        lista = list()
                        for file in listdir(ruta):
                            if isfile(join(ruta, file)):
                                if file.endswith('.txt'):
                                    lista.append(file)
                                    self.existenArchivos = True

                        if self.existenArchivos:
                            self.gridContenedor = QtWidgets.QGridLayout(self.tab)
                            self.listaValoraciones = QtWidgets.QListWidget(self.tab)
                            self.listaValoraciones.addItems(lista)
                            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                                               QtWidgets.QSizePolicy.Preferred)
                            self.listaValoraciones.setSizePolicy(sizePolicy)
                            self.gridContenedor.addWidget(self.listaValoraciones)


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
        path=os.getcwd() + '/Valoraciones'
        if os.path.isdir(path):
            rmtree(path)
        self.Open = ventanaWebScraper.NewApp()
        self.Open.show()
        self.cerraVentana()


    def entrenamiento(self):
        """
        Método para entrenar las valoraciones
        Manda y recoge lo referente al proceso entrenarDatos de la clase algoritmo
        """
        if((ventanaWebScraper.NewApp.flagDirectorio==True)or(ventanaSQL.MainWindow.flagDirectorio==True)):
            self.rutaDirectorio = ventanaWebScraper.NewApp.Directorio
            self.btn_guardar.setEnabled(True)
            from Utilidades.Algoritmia import algoritmo
            claseAlgoritmo = algoritmo()

            datosMatriz = claseAlgoritmo.entrenarDatos(self.rutaDirectorio,self.comboBox_algoritmo.currentText(),
                                                       self.comboBox_idioma.currentText(), self.checkBox_detectarIdioma.isChecked())

            self.configurarFiguraGrafico(datosMatriz)
            self.modeloAlgoritmo = datosMatriz[3]
            self.diccionarioEntrenamiento = datosMatriz[4]

        else:
            self.dialogo("Error", "No has realizado el WebScraper,Debe hacerlo correctamente para continuar con el Entrenamiento del Modelo",
                             QMessageBox.Warning)


    def guardar(self):
        """
        Método que solicita al usuario asignar un nombre al entrenamiento realizado, y donde con ese nombre
        guardamos el modelo, el diccionario y los titulos de cada sección
        """
        path = '../ModelosGuardados'

        try:
            os.makedirs(path)
        except OSError:
            print("Creation of the directory %s failed" % path)

        nombreArchivo, ok = QInputDialog.getText(self, 'Guardar', 'Introduzca el nombre del modelo a guardar:')
        if ok:
            nombreArchivo = str(nombreArchivo.lower())
            if nombreArchivo:

                with open('../ModelosGuardados/' + nombreArchivo + ".model", 'wb') as archivo:
                    pickle.dump(self.modeloAlgoritmo, archivo)

                with open('../ModelosGuardados/' + nombreArchivo + ".vocabulary", 'wb') as archivo:
                    pickle.dump(self.diccionarioEntrenamiento, archivo)

                with open('../ModelosGuardados/' + nombreArchivo + ".target", 'wb') as archivo:
                    pickle.dump(self.titulosGrafico, archivo)

                s3 = boto3.resource('s3',
                                    aws_access_key_id='AKIAIHNNODXALBFXU2SQ',
                                    aws_secret_access_key='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')

                boto3.setup_default_session(region_name='eu-west-3')

                bucketName = "modelosopinionesuem"
                Key = "../ModelosGuardados/" + nombreArchivo + ".model"
                outPutname = nombreArchivo + ".model"

                Key2 = "../ModelosGuardados/" + nombreArchivo + ".target"
                outPutname2 = nombreArchivo + ".target"

                Key3 = "../ModelosGuardados/" + nombreArchivo + ".vocabulary"
                outPutname3 = nombreArchivo + ".vocabulary"

                s3 = boto3.client('s3',
                                  aws_access_key_id='AKIAIHNNODXALBFXU2SQ',
                                  aws_secret_access_key='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')
                s3.upload_file(Key, bucketName, outPutname)
                s3.upload_file(Key2, bucketName, outPutname2)
                s3.upload_file(Key3, bucketName, outPutname3)


                val = (nombreArchivo,)
                BBDD.insertarNombreModelo(val)

                self.dialogo("Modelo Guardado", "El entrenamiento se ha guradado satisfactoriamente.", QMessageBox.Information)
                rmtree(os.getcwd() + '/Valoraciones')
                rmtree('../ModelosGuardados')

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