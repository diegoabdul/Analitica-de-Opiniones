from Vista.VistaVentanaEntrenamientoSQL import *
import Controlador.ControladorVentanaClasificador as ventanaEntrenamiento
from PyQt5.QtWidgets import QMessageBox
import Controlador.GestorBBDD as BBDD
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    flagDirectorio = False
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_atras.clicked.connect(self.volverAtras)
        self.btn_obtener.clicked.connect(self.obtener)
        myresult=BBDD.nombreProyecto2()
        for x in myresult:
            URL = x[0]
            self.comboBox.addItem(URL[0:50])


    def volverAtras(self):
        self.Open = ventanaEntrenamiento.NewApp()
        self.Open.show()
        self.close()

    def obtener(self):

        myresult=BBDD.clasificadorSQL(self.comboBox)
        for x in myresult:
            self.ID_Proyecto = x[0]

        path = os.getcwd() + '/UNLABELED'
        if not os.path.isdir(path):

            try:
                os.makedirs(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s" % path)

        myresult=BBDD.seleccionarIDPaginaWeb(self.ID_Proyecto)
        for ID in myresult:
            print(ID[0])

            myresult = BBDD.seleccionarNombre(ID)
            for x in myresult:
                NombreArchivo = x[0]

            myresult=BBDD.seleccionarNotayTexto(ID)
            i = 0
            for x in myresult:
                i += 1
                Nota = x[0]
                Texto = x[1]
                ID_Unlabeled = x[2]
                NotaGuardar = str(Nota)
                f = open(path + "/" + NombreArchivo + "_" + str(ID_Unlabeled) + ".txt", "w+")
                f.write(NotaGuardar + ' ' + Texto)
                f.close()
        self.flagborrar = False
        MainWindow.flagDirectorio = True
        QMessageBox.about(self, "Ok", "Se ha guardado correctamente")
        self.volverAtras()
