import hashlib

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QMessageBox

from Vista.VistaVentanaLogin import *
import Controlador.ControladorVentanaPrincipal as ventanaPrincipal
import Controlador.ControladorVentanaClasificador as ventanaClasificador
import mysql.connector
from Crypto.Cipher import AES
import base64

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_entrar.clicked.connect(self.entrar)
        self.shortcut = QShortcut(QKeySequence("Return"), self)
        self.shortcut.activated.connect(self.entrar)


    def entrar(self):

        mydb = mysql.connector.connect(
            host="vtc.hopto.org",
            user="diego",
            passwd="Galicia96.",
            database="vtc"
        )

        cipher = AES.new(secret_key, AES.MODE_ECB)  # never use ECB in strong systems obviously




        mycursor = mydb.cursor()

        sql = ("SELECT * FROM usuario WHERE Usuario = %s ")
        usuarioBBDD = (self.textoUsuario.text(), )
        mycursor.execute(sql, usuarioBBDD)




        myresult = mycursor.fetchall()

        if (mycursor.rowcount == 0):

            self.labelIncorrectos.setText("usuario y contraseña incorrectos")
        else:

            for x in myresult:
                usuarioCorrecto = x[3]
                contrasenaCorrecta = x[4]
                rolUsuario = x[5]
                nombreUsuario = x[1]

            if (self.textoUsuario.text() == usuarioCorrecto) and (self.textoContrasena.text() == (cipher.decrypt(baes64.b64decode(contrasenaCorrecta)))):

                if (rolUsuario==0):
                    self.Open = ventanaPrincipal.MainWindow()
                    self.Open.show()
                    self.cerraVentana()

                else:
                    self.Open = ventanaClasificador.NewApp()
                    self.Open.show()
                    self.cerraVentana()

            else:
                self.labelIncorrectos.setText("usuario y contraseña incorrectos")




    def cerraVentana(self):
        """
        Método encargado de cerrar la ventana actual
        """
        self.close()







