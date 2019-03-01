from Vista.VistaVentanaPrincipal import *
import Controlador.ControladorVentanaPrincipal as ventanaPrincipal

def main():
    app = QtWidgets.QApplication([])
    window = ventanaPrincipal.MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()

