import errno
import pickle
from itertools import groupby
import numpy as np
from PyQt5.QtWidgets import QMessageBox
from Vista.VistaVentanaClasificador import *
import Controlador.ControladorVentanaPrincipal as ventanaPrincipal
from os.path import isfile, join
from os import listdir
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from shutil import copyfile
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class NewApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(NewApp, self).__init__()
        self.setupUi(self)
        self.btn_atras.clicked.connect(self.volverAtras)
        self.btn_directorio.clicked.connect(self.filechooser)
        self.btn_clasificar.clicked.connect(self.AnalisisSentimiento)
        self.btn_clasificar.clicked.connect(self.clasificar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.checkBox_detectarIdioma.stateChanged.connect(self.habilitarOpcionesCheckBox)
        self.rutaDirectorio = ""
        self.listaDeFicheros = list()
        self.listaAnalisis = list()
        self.prediccion = list()
        self.titulosGrafico = list()
        self.figure = plt.figure(figsize=(8, 6))
        self.grafico = self.figure.add_subplot(111)
        self.canvas = FigureCanvasQTAgg(self.figure)
        lay = QtWidgets.QVBoxLayout(self.panelEstadistica)
        lay.addWidget(self.canvas)
        self.rellenarModelo()
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
        Método para introducir la ruta con la carpeta de archivos si clasificar, y recorrer esa misma ruta en busca de textos
        """
        rutaDirectorio = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecciona carpeta de valoraciones')
        if rutaDirectorio:
            self.textosValorar_text.setText("Directorio: "+ os.path.basename(rutaDirectorio))
            self.rutaDirectorio = rutaDirectorio
            self.listaDeFicheros.clear()
            self.listWidget_valoraciones.clear()

            for file in listdir(rutaDirectorio):
                if isfile(join(rutaDirectorio, file)):
                    if file.endswith('.txt'):
                        self.listaDeFicheros.append(join(rutaDirectorio,file))
                        self.listWidget_valoraciones.addItem(file)


    def rellenarModelo(self):
        """
        Método encargado de rellenar el combobox de modelos guardados,
        recorre el directorio donde se encuentran los modelos y los agrega
        al combobox
        """
        algoritmoSeleccionado = list()
        rutaDirectorio = "../ModelosGuardados"
        for fichero in listdir(rutaDirectorio):
            if isfile(join(rutaDirectorio, fichero)):
                if fichero.endswith('.model'):
                    algoritmoSeleccionado.append(os.path.splitext(fichero)[0])
        self.comboBox_modelo.addItems(algoritmoSeleccionado)

    def AnalisisSentimiento(self):
        for i in self.listaDeFicheros:
            f = open(i, "r")
            #print(f.readlines())
            #analizer = SentimentIntensityAnalyzer()
            #sentimiento = analizer.polarity_scores(f.read())
            #print(sentimiento)
            texto = f.read()
            #analysis = TextBlob(texto)
            #textotraducido=analysis.translate(to="english")
            traductor = TextBlob(texto)
            textotraducido=traductor.translate(to="en")
            #print(textotraducido)
            analysis = TextBlob(textotraducido.stripped)
            print(analysis.sentiment.polarity)
            #print(analysis.words)
            f.close()


    def clasificar(self):
        """
        Método para clasificar las valoraciones
        Manda y recoge lo referente al proceso clasificarDatos de la clase algoritmo
        """
        if(self.rutaDirectorio and self.listaDeFicheros):
            print("En proceso.....")
            with open('../ModelosGuardados/'+self.comboBox_modelo.currentText()+".model", 'rb') as fichero:
                modelo = pickle.load(fichero)
                print(modelo)

            with open('../ModelosGuardados/'+self.comboBox_modelo.currentText()+".target", 'rb') as fichero:
                self.titulosGrafico = pickle.load(fichero)

            with open('../ModelosGuardados/'+self.comboBox_modelo.currentText()+".vocabulary", 'rb') as fichero:
                diccionario = pickle.load(fichero)

            from Utilidades.Algoritmia import algoritmo
            claseAlgoritmo = algoritmo()
            self.prediccion = claseAlgoritmo.clasificarDatos(self.listaDeFicheros, modelo, diccionario,
                                                             self.comboBox_idioma.currentText(), self.checkBox_detectarIdioma.isChecked())
            self.btn_guardar.setEnabled(True)
            listaParaGrafico = self.configurarListaParaGrafico()
            self.configurarGrafico(listaParaGrafico)
        else:
            self.dialogo("No has seleccionado directorio entrada", "Debe seleccionar el directorio de las valoraciones a clasificar",
                              QMessageBox.Warning)


    def configurarListaParaGrafico(self):
        """
        Método para generar los datos necesarios para representar en las gráficas los datos
        obtenidos en la clasificación de textos
        :return: devuelve una lista con la suma del total de valoraciones de cada caso
        """
        listaDeListas = list() #creamos lista que contendrá listas dividas segun su contenido
        listaDeListas.append([list(j) for i, j in groupby(sorted(self.prediccion, key=int))]) #Dividimos las listas en listas de mismo numero. Para dividir, primero hay qie ordenador, por ello el sorted
        listaDatosTamaño = list()
        for datos in listaDeListas[0]:
            listaDatosTamaño.append(len(datos)) #miramos el tamaño de las sublistas
        return listaDatosTamaño


    def guardar(self):
        """
        Método encargado de guardar los textos ya clasificados en la carpeta seleccionada por el usuario
        """
        rutaDirectorioGuardar = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecciona carpeta de valoraciones')
        if rutaDirectorioGuardar: #comprobamos que el usuario ha introducido una ruta para guardar
            if(len(self.listaDeFicheros) == len(self.prediccion)): #comprobamos que efectivamente la longitud de la lista de ficheros es igual al de la predicción
                for indice, datosEntrenamiento in enumerate(self.prediccion):
                    encontrado = False
                    contador = 0
                    while(not encontrado and len(self.titulosGrafico) > contador):
                        rutaDestino = rutaDirectorioGuardar + "/" + self.titulosGrafico[contador]
                        if not os.path.exists(rutaDestino):
                            try:
                                os.makedirs(rutaDestino)
                            except OSError as exc:
                                if exc.errno != errno.EEXIST:
                                    raise
                        if(datosEntrenamiento == contador):
                            rutaOrigen = self.listaDeFicheros[indice]
                            archivo = os.path.basename(rutaOrigen)
                            rutaDestino = join(rutaDestino, archivo)
                            copyfile(rutaOrigen, rutaDestino)
                            encontrado = True

                        contador += 1

                self.dialogo("Guardado con éxito", "Se guardo con éxito las clasificaciones", QMessageBox.Information)
            else:
                self.dialogo("Error desconocido", "Debe seleccionar la ruta de salida", QMessageBox.Warning)
        else:
            self.dialogo("No has seleccionado ruta", "Debe seleccionar la ruta de salida", QMessageBox.Warning)


    def configurarGrafico(self, listaDatosTamaño):
        """
        Método encargado de dibujar las gráficas con los datos obtenidos de la clasificación en tiempo real
        :param listaDatosTamaño: recibe una lista con el total de textos clasificados por secciones
        """
        self.grafico.clear()
        self.grafico.set_facecolor(("#E6E6E6")) #cambiar el color de fondo del grafico a gris en este caso
        self.grafico.set_axisbelow(True)#añadimos lineas por debajo de las gráficas para indicar eje x, y
        self.grafico.yaxis.grid(color='white')
        self.grafico.xaxis.grid(color='white')

        x_pos = np.arange(len(listaDatosTamaño))
        print(listaDatosTamaño)
        self.grafico.bar(x_pos, listaDatosTamaño, color = "#58FA82")
        plt.title('Número de valoraciones')
        plt.xticks(x_pos, self.titulosGrafico)
        for x, i in enumerate(listaDatosTamaño):
            plt.text(x-.05, i*2/3, str(round(i, 2)), fontsize=10,color='black')

        plt.draw()
        self.canvas.draw()
        self.panelEstadistica.repaint() #linea necesaria para refrescar en Mac OS X el gráfico

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

