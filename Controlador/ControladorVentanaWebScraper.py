from PyQt5.QtWidgets import QInputDialog, QMessageBox
from Vista.VistaVentanaWebScraper import *
import Controlador.ControladorVentanaEntrenamiento as ventanaEntrenamiento
import threading


import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
  host="vtc.hopto.org",
  user="diego",
  passwd="Galicia96.",
    database="vtc"
)


class NewApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(NewApp, self).__init__()
        self.setupUi(self)
        self.comboBox_paginas.addItem('https://www.booking.com')
        self.comboBox_paginas.addItem('https://www.amazon.es/')
        self.comboBox_paginas.addItem('no sabemos todavia')
        self.comboBox.addItem('Ingles')
        self.comboBox.addItem('Español')
        self.comboBox_2.addItem('75')
        self.comboBox_2.addItem('150')
        self.comboBox_2.addItem('225')
        self.comboBox_2.addItem('300')
        self.comboBox_2.addItem('375')
        self.comboBox_2.addItem('450')
        self.comboBox_2.addItem('525')
        self.comboBox_2.addItem('600')
        self.comboBox_2.addItem('675')
        self.comboBox_2.addItem('2700')
        self.comboBox_2.addItem('5400')
        self.btn_obtener.clicked.connect(self.iniciar)
        self.btn_atras.clicked.connect(self.volverAtras)
        self.btn_guardar.clicked.connect(self.guardar)

    def volverAtras(self):
        """
        Método encargado de volver al menu principal
        """
        self.Open = ventanaEntrenamiento.NewApp()
        self.Open.show()
        self.close()

    def mostrar(self,nota,positivas,contadorpos):
        self.listWidget.addItem(nota+' '+positivas)
        self.lineEdit_Buenas.setText(str(contadorpos))

    def mostrar2(self,nota,negativas,contadorneg):
        self.listWidget.addItem(nota+' '+negativas)
        self.lineEdit_Malas.setText(str(contadorneg))

    def iniciar(self):
        self.listWidget.clear()
        hilo2 = threading.Thread(target=self.web)
        hilo2.start()

    def guardar(self):
        mydb.commit()
        QMessageBox.about(self, "OK", "Se ha guardado correctamente")

    def web(self):
        idioma=self.comboBox.currentText()
        idiomareal=None
        if idioma =='Ingles':
            idiomareal='en'
        else:
            idiomareal='es'

        URL = self.URL.text()
        if URL.__contains__(self.comboBox_paginas.currentText()):
            if self.comboBox_paginas.currentText().__contains__('https://www.booking.com'):
                mycursor = mydb.cursor()
                flag = True
                i = 1
                Nombre = 'Booking'
                ID_PaginaWeb = 0
                ID_Opinion = 0
                sql = "INSERT INTO paginaweb (URL, Nombre) VALUES (%s, %s)"
                val = (URL, Nombre)
                mycursor.execute(sql, val)
                mydb.commit()
                mycursor.close()

                mycursor = mydb.cursor()
                mycursor.execute("SELECT ID_PaginaWeb FROM paginaweb WHERE URL=%s", (URL,))
                myresult = mycursor.fetchall()
                for x in myresult:
                    ID_PaginaWeb = x[0]
                mycursor.close()
                comodin=URL.replace('hotel','reviews',1)
                PAGINA = comodin[:34] + '/hotel' + comodin[34:]
                print(PAGINA)
                contador=0
                maximo=self.comboBox_2.currentText()
                maximo_int = int(maximo)
                maximo_pagina = (maximo_int / 75)
                while (flag == True and i<=maximo_pagina):

                    fijo = 'customer_type=total&hp_nav=0&lang='+idiomareal+'-us&order=featuredreviews&page=' + str(i) + '&r_lang='+idiomareal+'&rows=75&soz=1&lang_click=top;cdl=es;lang_changed=1'
                    req = requests.get(PAGINA,fijo)
                    soup = BeautifulSoup(req.content, "lxml")
                    contadorneg = 0
                    contadorpos = 0
                    print(fijo)
                    i += 1

                    for lab in soup.find_all(class_="review_item_review"):

                        self.lineEdit_Total.setText(str(contadorpos+contadorneg))
                        nota = lab.findAll(class_="review-score-badge", text=True)[0].text
                        for lab2 in lab.find_all(class_="review_pos"):
                            positivas = lab2.findAll(itemprop="reviewBody", text=True)[0].text
                            Nombre = 'Buenas'
                            contadorpos += 1
                            hilo1 = threading.Thread(target=self.mostrar,args=(nota,positivas,contadorpos))
                            hilo1.start()
                            #print(nota + positivas)

                            mycursor = mydb.cursor()
                            sql = "INSERT INTO opinion (ID_PaginaWeb,Nota, Texto) VALUES (%s,%s,%s)"
                            val = (ID_PaginaWeb, nota, positivas)
                            mycursor.execute(sql, val)
                            #mydb.commit()
                            mycursor.close()

                            mycursor = mydb.cursor()
                            mycursor.execute("SELECT ID_Opinion FROM opinion where ID_PaginaWeb=%s", (ID_PaginaWeb,))
                            myresult = mycursor.fetchall()
                            for id in myresult:
                                ID_Opinion = id[0]
                            mycursor.close()

                            mycursor = mydb.cursor()
                            sql = "INSERT INTO tipoopinion (ID_Opinion,Nombre) VALUES (%s,%s)"
                            val = (ID_Opinion, Nombre)
                            mycursor.execute(sql, val)
                            #mydb.commit()
                            mycursor.close()

                        for lab3 in lab.find_all(class_="review_neg"):
                            negativas = lab3.findAll(itemprop="reviewBody", text=True)[0].text
                            contadorneg += 1
                            hilo3 = threading.Thread(target=self.mostrar2, args=(nota, negativas,contadorneg))
                            hilo3.start()
                            # print(nota + negativas)
                            Nombre2 = 'Malas'

                            mycursor = mydb.cursor()
                            sql = "INSERT INTO opinion (ID_PaginaWeb,Nota, Texto) VALUES (%s,%s,%s)"
                            val = (ID_PaginaWeb, nota, negativas)
                            mycursor.execute(sql, val)
                            #mydb.commit()
                            mycursor.close()

                            mycursor = mydb.cursor()
                            mycursor.execute("SELECT ID_Opinion FROM opinion where ID_PaginaWeb=%s", (ID_PaginaWeb,))
                            myresult = mycursor.fetchall()
                            for id in myresult:
                                ID_Opinion = id[0]
                            mycursor.close()

                            mycursor = mydb.cursor()
                            sql = "INSERT INTO tipoopinion (ID_Opinion,Nombre) VALUES (%s,%s)"
                            val = (ID_Opinion, Nombre2)
                            mycursor.execute(sql, val)
                            #mydb.commit()
                            mycursor.close()

                    if positivas == None:
                        flag = False

            if self.comboBox_paginas.currentText().__contains__('https://www.amazon.es/'):
                print('amazon')
        else:
            QMessageBox.about(self, "Error", "URL introducido no coincide con la página seleccionada")