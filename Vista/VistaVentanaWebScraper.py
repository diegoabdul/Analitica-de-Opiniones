# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webScraper.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(894, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(720, 500))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_atras = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_atras.sizePolicy().hasHeightForWidth())
        self.btn_atras.setSizePolicy(sizePolicy)
        self.btn_atras.setObjectName("btn_atras")
        self.gridLayout_4.addWidget(self.btn_atras, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 4, 0, 3, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_obtener = QtWidgets.QPushButton(self.widget)
        self.btn_obtener.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_obtener.sizePolicy().hasHeightForWidth())
        self.btn_obtener.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_obtener.setFont(font)
        self.btn_obtener.setObjectName("btn_obtener")
        self.gridLayout_3.addWidget(self.btn_obtener, 0, 0, 1, 1)
        self.btn_guardar = QtWidgets.QPushButton(self.widget)
        self.btn_guardar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_guardar.sizePolicy().hasHeightForWidth())
        self.btn_guardar.setSizePolicy(sizePolicy)
        self.btn_guardar.setObjectName("btn_guardar")
        self.gridLayout_3.addWidget(self.btn_guardar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 4, 1, 3, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox_paginas = QtWidgets.QComboBox(self.widget)
        self.comboBox_paginas.setObjectName("comboBox_paginas")
        self.gridLayout_5.addWidget(self.comboBox_paginas, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 1, 0, 3, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 7, 1, 1, 1)
        self.idioma_text = QtWidgets.QLabel(self.widget)
        self.idioma_text.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.idioma_text.setFont(font)
        self.idioma_text.setObjectName("idioma_text")
        self.gridLayout_5.addWidget(self.idioma_text, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 11, 1, 1, 1)
        self.URL = QtWidgets.QLineEdit(self.widget)
        self.URL.setObjectName("URL")
        self.gridLayout_5.addWidget(self.URL, 6, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_5.addWidget(self.comboBox, 8, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 1, 2, 3, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 9, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_5.addWidget(self.comboBox_2, 10, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_Total = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Total.setObjectName("lineEdit_Total")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Total)
        self.lineEdit_Malas = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Malas.setObjectName("lineEdit_Malas")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Malas)
        self.lineEdit_Buenas = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Buenas.setObjectName("lineEdit_Buenas")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Buenas)
        self.gridLayout_2.addLayout(self.formLayout, 2, 1, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.textosValorar_tab = QtWidgets.QTabWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textosValorar_tab.sizePolicy().hasHeightForWidth())
        self.textosValorar_tab.setSizePolicy(sizePolicy)
        self.textosValorar_tab.setObjectName("textosValorar_tab")
        self.widget1 = QtWidgets.QWidget()
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget1)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)
        self.textosValorar_tab.addTab(self.widget1, "")
        self.gridLayout_13.addWidget(self.textosValorar_tab, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_13, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.widget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.textosValorar_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fase de clasificación"))
        self.btn_atras.setText(_translate("MainWindow", "Atrás"))
        self.btn_obtener.setText(_translate("MainWindow", "OBTENER"))
        self.btn_guardar.setText(_translate("MainWindow", "Guardar/Borrar"))
        self.label.setText(_translate("MainWindow", "Seleccione el idioma en que desea recuperar las opiniones:"))
        self.idioma_text.setText(_translate("MainWindow", "URL: "))
        self.label_2.setText(_translate("MainWindow", "Seleccione una página para obtener opiniones:"))
        self.label_3.setText(_translate("MainWindow", "Ingrese el maximo de opiniones que desee:"))
        self.label_4.setText(_translate("MainWindow", "Número de opiniones Buenas"))
        self.label_5.setText(_translate("MainWindow", "Número de opiniones Malas"))
        self.label_6.setText(_translate("MainWindow", "Número de opiniones Total"))
        self.textosValorar_tab.setTabText(self.textosValorar_tab.indexOf(self.widget1), _translate("MainWindow", "WebScrapper"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

