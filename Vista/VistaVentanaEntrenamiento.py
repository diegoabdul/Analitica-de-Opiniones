# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrenamiento.ui'
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
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.valoraciones_tab = QtWidgets.QTabWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valoraciones_tab.sizePolicy().hasHeightForWidth())
        self.valoraciones_tab.setSizePolicy(sizePolicy)
        self.valoraciones_tab.setObjectName("valoraciones_tab")
        self.widget1 = QtWidgets.QWidget()
        self.widget1.setObjectName("widget1")
        self.valoraciones_tab.addTab(self.widget1, "")
        self.gridLayout_13.addWidget(self.valoraciones_tab, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_13, 3, 0, 1, 1)
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
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 2, 4, 1)
        self.btn_directorio = QtWidgets.QPushButton(self.widget)
        self.btn_directorio.setObjectName("btn_directorio")
        self.gridLayout_6.addWidget(self.btn_directorio, 0, 1, 1, 1)
        self.directorio_text = QtWidgets.QLabel(self.widget)
        self.directorio_text.setObjectName("directorio_text")
        self.gridLayout_6.addWidget(self.directorio_text, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 0, 4, 1)
        self.btn_entrenarSQL = QtWidgets.QPushButton(self.widget)
        self.btn_entrenarSQL.setObjectName("btn_entrenarSQL")
        self.gridLayout_6.addWidget(self.btn_entrenarSQL, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_entrenar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_entrenar.setFont(font)
        self.btn_entrenar.setObjectName("btn_entrenar")
        self.gridLayout_3.addWidget(self.btn_entrenar, 0, 0, 1, 1)
        self.btn_guardar = QtWidgets.QPushButton(self.widget)
        self.btn_guardar.setEnabled(False)
        self.btn_guardar.setObjectName("btn_guardar")
        self.gridLayout_3.addWidget(self.btn_guardar, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 4, 1, 3, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.idioma_text = QtWidgets.QLabel(self.widget)
        self.idioma_text.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idioma_text.sizePolicy().hasHeightForWidth())
        self.idioma_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.idioma_text.setFont(font)
        self.idioma_text.setObjectName("idioma_text")
        self.gridLayout_5.addWidget(self.idioma_text, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 1, 0, 5, 1)
        self.comboBox_algoritmo = QtWidgets.QComboBox(self.widget)
        self.comboBox_algoritmo.setObjectName("comboBox_algoritmo")
        self.comboBox_algoritmo.addItem("")
        self.comboBox_algoritmo.addItem("")
        self.comboBox_algoritmo.addItem("")
        self.comboBox_algoritmo.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_algoritmo, 1, 1, 1, 1)
        self.comboBox_idioma = QtWidgets.QComboBox(self.widget)
        self.comboBox_idioma.setEnabled(False)
        self.comboBox_idioma.setObjectName("comboBox_idioma")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.comboBox_idioma.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_idioma, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 1, 2, 5, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 6, 1, 1, 1)
        self.checkBox_detectarIdioma = QtWidgets.QCheckBox(self.widget)
        self.checkBox_detectarIdioma.setChecked(True)
        self.checkBox_detectarIdioma.setObjectName("checkBox_detectarIdioma")
        self.gridLayout_5.addWidget(self.checkBox_detectarIdioma, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.panelEstadistica = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panelEstadistica.sizePolicy().hasHeightForWidth())
        self.panelEstadistica.setSizePolicy(sizePolicy)
        self.panelEstadistica.setObjectName("panelEstadistica")
        self.gridLayout_2.addWidget(self.panelEstadistica, 0, 1, 4, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.widget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.valoraciones_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fase de entrenamiento"))
        self.valoraciones_tab.setTabText(self.valoraciones_tab.indexOf(self.widget1), _translate("MainWindow", "Valoraciones"))
        self.btn_atras.setText(_translate("MainWindow", "Atrás"))
        self.btn_directorio.setText(_translate("MainWindow", "WebScraper"))
        self.directorio_text.setText(_translate("MainWindow", "Directorio:"))
        self.btn_entrenarSQL.setText(_translate("MainWindow", "Entrenar desde Opiniones en la Base de Datos"))
        self.btn_entrenar.setText(_translate("MainWindow", "ENTRENAR"))
        self.btn_guardar.setText(_translate("MainWindow", "Guardar entrenamiento"))
        self.idioma_text.setText(_translate("MainWindow", "Idioma de valoraciones:"))
        self.comboBox_algoritmo.setItemText(0, _translate("MainWindow", "Naive Bayes"))
        self.comboBox_algoritmo.setItemText(1, _translate("MainWindow", "Random Forest"))
        self.comboBox_algoritmo.setItemText(2, _translate("MainWindow", "Regresión Logistica"))
        self.comboBox_algoritmo.setItemText(3, _translate("MainWindow", "Árbol de decisión"))
        self.comboBox_idioma.setItemText(0, _translate("MainWindow", "spanish"))
        self.comboBox_idioma.setItemText(1, _translate("MainWindow", "english"))
        self.comboBox_idioma.setItemText(2, _translate("MainWindow", "french"))
        self.comboBox_idioma.setItemText(3, _translate("MainWindow", "german"))
        self.comboBox_idioma.setItemText(4, _translate("MainWindow", "italian"))
        self.comboBox_idioma.setItemText(5, _translate("MainWindow", "portuguese"))
        self.comboBox_idioma.setItemText(6, _translate("MainWindow", "russian"))
        self.comboBox_idioma.setItemText(7, _translate("MainWindow", "swedish"))
        self.comboBox_idioma.setItemText(8, _translate("MainWindow", "hungarian"))
        self.comboBox_idioma.setItemText(9, _translate("MainWindow", "danish"))
        self.comboBox_idioma.setItemText(10, _translate("MainWindow", "dutch"))
        self.comboBox_idioma.setItemText(11, _translate("MainWindow", "finnish"))
        self.label_2.setText(_translate("MainWindow", "Algoritmo:"))
        self.checkBox_detectarIdioma.setText(_translate("MainWindow", "Auto detectar idioma"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

