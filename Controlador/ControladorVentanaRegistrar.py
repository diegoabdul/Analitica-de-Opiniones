import hashlib

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QMessageBox

from Vista.VistaVentanaRegistro import *
import Controlador.ControladorVentanaPrincipal as ventanaPrincipal
import mysql.connector


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_registrar.clicked.connect(self.prueba)
        self.btn_atras.clicked.connect(self.volverAtras)

    def encriptarContrasena(self, contrasena):
        codificiacionContrasena = hashlib.md5()
        codificiacionContrasena.update(contrasena.encode('utf-8'))
        return codificiacionContrasena.hexdigest()

    def volverAtras(self):
        """
        Método encargado de volver al menu principal
        """
        self.Open = ventanaPrincipal.MainWindow()
        self.Open.show()
        self.cerraVentana()

    def prueba(self):

        nombre = self.lineEdit_nombre.text()
        apellidos = self.lineEdit_apellidos.text()
        usuario = self.lineEdit_usuario.text()
        contrasena = self.lineEdit_contrasena.text()
        rolcomodin = self.comboBox.currentText()
        if rolcomodin=="Cliente":
            rol=1
        else:
            rol=0


        mydb = mysql.connector.connect(
            host="vtc.hopto.org",
            user="diego",
            passwd="Galicia96.",
            database="vtc"
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO usuario (Nombre,Apellidos,Usuario,Clave,Rol) VALUES (%s,%s,%s,%s,%s)"
        val = (nombre, apellidos,usuario,self.encriptarContrasena(contrasena),rol)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()

        QMessageBox.about(self, "Ok", "Se ha añadido el usuario correctamente")
        self.volverAtras()


    def cerraVentana(self):
        """
        Método encargado de cerrar la ventana actual
        """
        self.close()



