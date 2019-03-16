from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut

from Vista.VistaVentanaRegistro import *
import Controlador.ControladorVentanaPrincipal as ventanaPrincipal
import mysql.connector


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_registrar.clicked.connect(self.prueba)
        #self.shortcut = QShortcut(QKeySequence("Return"), self)
        #self.shortcut.activated.connect(self.entrar)

    def prueba(self):

        nombre = self.plainTextEdit_Nombre.toPlainText()
        apellidos = self.plainTextEdit_Apellidos.toPlainText()
        usuario = self.plainTextEdit_Usuario.toPlainText()
        contrasena = self.plainTextEdit_Contrasena.toPlainText()
        rol = 1




        mydb = mysql.connector.connect(
            host="vtc.hopto.org",
            user="diego",
            passwd="Galicia96.",
            database="vtc"
        )

        if mydb.is_connected() == True:
            print("conectado")

        mycursor = mydb.cursor()
        sql = "INSERT INTO usuario (Nombre,Apellidos,Usuario,Clave,Rol) VALUES (%s,%s,%s,%s,%s)"
        val = (nombre, contrasena,usuario,apellidos,rol)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()

        print("el usuario ha sido añadido con exito")



    def cerraVentana(self):
        """
        Método encargado de cerrar la ventana actual
        """
        self.close()



