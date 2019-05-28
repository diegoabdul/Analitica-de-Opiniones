# -- coding: utf-8 --

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(418, 215)
        Form.setFixedSize(418, 215)
        self.textoUsuario = QtWidgets.QLineEdit(Form)
        self.textoUsuario.setGeometry(QtCore.QRect(70, 70, 291, 20))
        self.textoUsuario.setObjectName("textoUsuario")
        self.textoContrasena = QtWidgets.QLineEdit(Form)
        self.textoContrasena.setGeometry(QtCore.QRect(70, 130, 291, 20))
        self.textoContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textoContrasena.setObjectName("textoContrasena")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 20, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 81, 16))
        self.label_3.setObjectName("label_3")
        self.btn_entrar = QtWidgets.QPushButton(Form)
        self.btn_entrar.setGeometry(QtCore.QRect(160, 180, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setObjectName("btn_entrar")
        self.labelIncorrectos = QtWidgets.QLabel(Form)
        self.labelIncorrectos.setGeometry(QtCore.QRect(105, 160, 291, 16))
        self.labelIncorrectos.setText("")
        self.labelIncorrectos.setObjectName("labelIncorrectos")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "Usuario"))
        self.label.setText(_translate("Form", "¡Bienvenido!"))
        self.label_3.setText(_translate("Form", "Contraseña"))
        self.labelIncorrectos.setText(_translate("Form", ""))
        self.btn_entrar.setText(_translate("Form", "Entrar"))