from Vista.VistaVentanaPrincipal import *
from Vista.VistaVentanaLogin import *
import Controlador.ControladorVentanaPrincipal as ventanaPrincipal
import Controlador.ControladorVentanaLogin as ventanaLogin



def main():
    app = QtWidgets.QApplication([])
    window = ventanaLogin.MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()

