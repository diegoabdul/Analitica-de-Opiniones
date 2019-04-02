from Vista.VistaVentanaPrincipal import *
import Controlador.ControladorVentanaEntrenamiento as ventanaEntrenamiento
import Controlador.ControladorVentanaClasificador as ventanaClasificador
import Controlador.ControladorVentanaRegistrar as ventanaRegistrar
import Controlador.ControladorVentanaLogin as ventanaLogin


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_entrenar.clicked.connect(self.entrenar)
        self.btn_atras.clicked.connect(self.volverAtras)
        self.btn_clasificar.clicked.connect(self.clasificar)
        self.btn_registrar.clicked.connect(self.registrar)

    def entrenar(self):
        """
        Método encargado de ejecutar la ventana entrenar
        """
        self.Open = ventanaEntrenamiento.NewApp()
        self.Open.show()
        self.cerraVentana()


    def clasificar(self):
        """
        Método encargado de ejecutar la ventana clasificar
        """
        self.Open = ventanaClasificador.NewApp()
        self.Open.show()
        self.cerraVentana()
        

    def registrar(self):
        """
        Método encargado de ejecutar la ventana registrar
        """
        self.Open = ventanaRegistrar.MainWindow()
        self.Open.show()
        self.cerraVentana()
        
        
    def volverAtras(self):
        self.Open = ventanaLogin.NewApp()
        self.Open.show()
        self.close()

    def cerraVentana(self):
        """
        Método encargado de cerrar la ventana actual
        """
        self.close()
