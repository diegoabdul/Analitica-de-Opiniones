from Vista.VistaVentanaPrincipal import *
import Controlador.ControladorVentanaEntrenamiento as ventanaEntrenamiento
import Controlador.ControladorVentanaClasificador as ventanaClasificador
import Controlador.ControladorVentanaRegistro as ventanaRegistro


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_entrenar.clicked.connect(self.entrenar)
        self.btn_clasificar.clicked.connect(self.clasificar)
        self.btn_registrar.clicked.connect(self.registrar)

    def entrenar(self):
        """
        Método encargado de ejecutar la ventana entrenar
        """
        self.Open = ventanaEntrenamiento.NewApp()
        self.Open.show()
        self.cerraVentana()

    def registrar(self):
        """
        Método encargado de ejecutar la ventana entrenar
        """
        self.Open = ventanaRegistro.NewApp()
        self.Open.show()
        self.cerraVentana()


    def clasificar(self):
        """
        Método encargado de ejecutar la ventana clasificar
        """
        self.Open = ventanaClasificador.NewApp()
        self.Open.show()
        self.cerraVentana()

    def cerraVentana(self):
        """
        Método encargado de cerrar la ventana actual
        """
        self.close()
