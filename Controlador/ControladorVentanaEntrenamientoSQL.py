from Vista.VistaVentanaEntrenamientoSQL import *
import Controlador.ControladorVentanaEntrenamientoSQL as ventanaEntrenamientoSQL
import Controlador.ControladorVentanaEntrenamiento as ventanaEntrenamiento
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
import Controlador.GestorBBDD as BBDD
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    flagDirectorio = False
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_atras.clicked.connect(self.volverAtras)
        self.btn_obtener.clicked.connect(self.obtener)
        myresult=BBDD.nombreProyecto()
        for x in myresult:
            URL = x[0]
            self.comboBox.addItem(URL[0:50])

    def volverAtras(self):
        self.Open = ventanaEntrenamiento.NewApp()
        self.Open.show()
        self.close()

    def obtener(self):

        path = os.getcwd() + '/Valoraciones'
        if not os.path.isdir(path):

            try:
                os.makedirs(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s" % path)
        myresult=BBDD.entrenamientoSQL(self.comboBox)
        for x in myresult:
            ID_Proyecto = x[0]

        myresult=BBDD.seleccionarIDPaginaWeb2(ID_Proyecto)
        for ID in myresult:
            print(ID[0])

            myresult=BBDD.seleccionarNombre2(ID)
            for x in myresult:
                NombreArchivo = x[0]

            path = os.getcwd() + '/Valoraciones/Buenas'
            if not os.path.isdir(path):
                try:
                    os.makedirs(path)
                except OSError:
                    print("Creation of the directory %s failed" % path)
                else:
                    print("Successfully created the directory %s" % path)

            myresult=BBDD.seleccionarNotayTextoBuenas2(ID)
            i = 0
            for x in myresult:
                i += 1
                Nota = x[0]
                Texto = x[1]
                NotaGuardar = str(Nota)
                f = open(path + "/" + NombreArchivo + "_" + str(i) + ".txt", "w+")
                f.write(NotaGuardar + ' ' + Texto)
                f.close()
            path = os.getcwd() + '/Valoraciones/Malas'
            if not os.path.isdir(path):
                try:
                    os.makedirs(path)
                except OSError:
                    print("Creation of the directory %s failed" % path)
                else:
                    print("Successfully created the directory %s" % path)

            myresult=BBDD.seleccionarNombre2(ID)
            for x in myresult:
                NombreArchivoMalas = x[0]

            myresult=BBDD.seleccionarNotayTextoMalas2(ID)
            for x in myresult:
                i += 1
                Nota2 = x[0]
                Texto2 = x[1]
                NotaGuardar2 = str(Nota2)
                f = open(path + "/" + NombreArchivoMalas + "_" + str(i) + ".txt", "w+")
                f.write(NotaGuardar2 + ' ' + Texto2)
                f.close()
        self.flagborrar = False
        MainWindow.flagDirectorio = True
        QMessageBox.about(self, "Ok", "Se ha guardado correctamente")
        self.volverAtras()