from Vista.VistaVentanaRegistro import *



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_registrar.clicked.connect(self.registrar)

    def cerraVentana(self):
            """
            Método encargado de cerrar la ventana actual
            """
            self.close()