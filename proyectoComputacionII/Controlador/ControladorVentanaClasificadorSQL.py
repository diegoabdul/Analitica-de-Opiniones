from Vista.VistaVentanaEntrenamientoSQL import *
import Controlador.ControladorVentanaClasificadorSQL as ventanaEntrenamientoSQL
import Controlador.ControladorVentanaClasificador as ventanaEntrenamiento
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
import os

mydb = mysql.connector.connect(
  host="vtc.hopto.org",
  user="diego",
  passwd="Galicia96.",
    database="vtc"
)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    flagDirectorio = False
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_atras.clicked.connect(self.volverAtras)
        self.btn_obtener.clicked.connect(self.obtener)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT Nombre FROM proyectoclasificacion")
        myresult = mycursor.fetchall()
        for x in myresult:
            URL = x[0]
            self.comboBox.addItem(URL[0:50])
        mycursor.close()

    def volverAtras(self):
        self.Open = ventanaEntrenamiento.NewApp()
        self.Open.show()
        self.close()

    def obtener(self):

        mycursor = mydb.cursor()
        mycursor.execute("SELECT ID_ProyectoClasificacion FROM proyectoclasificacion WHERE Nombre=%s", (self.comboBox.currentText(),))
        myresult = mycursor.fetchall()
        for x in myresult:
            self.ID_Proyecto = x[0]
        mycursor.close()

        path = os.getcwd() + '/UNLABELED'
        if not os.path.isdir(path):

            try:
                os.makedirs(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s" % path)

        mycursor = mydb.cursor()
        mycursor.execute("SELECT ID_PaginaWeb FROM paginaweb WHERE ID_ProyectoClasificacion=%s", (self.ID_Proyecto,))
        myresult = mycursor.fetchall()
        mycursor.close()
        for ID in myresult:
            print(ID[0])
            mycursor = mydb.cursor()
            mycursor.execute("SELECT Nombre FROM paginaweb WHERE ID_PaginaWeb=%s", (ID[0],))
            myresult = mycursor.fetchall()
            for x in myresult:
                NombreArchivo = x[0]
            mycursor.close()
            mycursor = mydb.cursor()
            mycursor.execute("SELECT Nota,Texto,ID_Unlabeled FROM unlabeled WHERE ID_PaginaWeb=%s", (ID[0],))
            myresult = mycursor.fetchall()
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
            mycursor.close()
        self.flagborrar = False
        MainWindow.flagDirectorio = True
        QMessageBox.about(self, "Ok", "Se ha guardado correctamente")
        self.volverAtras()
