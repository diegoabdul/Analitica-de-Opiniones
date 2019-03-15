from Vista.VistaVentanaLogin import *
import Controlador.ControladorVentanaPrincipal as ventanaPrincipal
import Controlador.ControladorVentanaClasificador as ventanaClasificador


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_entrar.clicked.connect(self.entrar)



    def entrar(self):
        """
        Método encargado de ejecutar la ventana entrenar
        """
        print("hola")

        usuario = self.textoUsuario.text()
        contrasena = self.textoContrasena.text()

        print(usuario)
        print(contrasena)

        adminCorrecto = "admin"
        contrasenaAdminCorrecta = "123"

        usuarioCorrecto = "usuario"
        contrasenaUsuarioCorrecta = "123"


        if (usuario == adminCorrecto) and (contrasena == contrasenaAdminCorrecta):
            self.Open = ventanaPrincipal.MainWindow()
            self.Open.show()
            self.cerraVentana()

        if (usuario == usuarioCorrecto) and (contrasena==contrasenaUsuarioCorrecta):
            self.Open = ventanaClasificador.NewApp()
            self.Open.show()
            self.cerraVentana()


    def cerraVentana(self):
        """
        Método encargado de cerrar la ventana actual
        """
        self.close()
