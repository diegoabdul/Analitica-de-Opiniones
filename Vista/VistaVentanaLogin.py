# -- coding: utf-8 --

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(366, 204)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setAutoFillBackground(True)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_usuario = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_usuario.sizePolicy().hasHeightForWidth())
        self.label_usuario.setSizePolicy(sizePolicy)
        self.label_usuario.setObjectName("label_usuario")
        self.verticalLayout_2.addWidget(self.label_usuario)
        self.textoUsuario = QtWidgets.QLineEdit(self.widget)
        self.textoUsuario.setObjectName("textoUsuario")
        self.verticalLayout_2.addWidget(self.textoUsuario)
        self.label_contrasena = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_contrasena.sizePolicy().hasHeightForWidth())
        self.label_contrasena.setSizePolicy(sizePolicy)
        self.label_contrasena.setObjectName("label_contrasena")
        self.verticalLayout_2.addWidget(self.label_contrasena)
        self.textoContrasena = QtWidgets.QLineEdit(self.widget)
        self.textoContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textoContrasena.setObjectName("textoContrasena")
        self.verticalLayout_2.addWidget(self.textoContrasena)
        self.btn_entrar = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_entrar.sizePolicy().hasHeightForWidth())
        self.btn_entrar.setSizePolicy(sizePolicy)
        self.btn_entrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_entrar.setObjectName("btn_entrar")
        self.verticalLayout_2.addWidget(self.btn_entrar, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Bienvenido"))
        self.label_usuario.setText(_translate("MainWindow", "Usuario"))
        self.label_contrasena.setText(_translate("MainWindow", "Contraseña"))
        self.btn_entrar.setText(_translate("MainWindow", "Entrar"))


