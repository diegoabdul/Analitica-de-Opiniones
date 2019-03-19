import itertools
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from Vista.VistaVentanaWebScraper import *
from os.path import isfile, join
from os import listdir
import os
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
        self.btn_clasificar.clicked.connect(self.mostrar)
        self.show()

    def mostrar(self):
        contador = 30
        for a in contador:
            self.listWidget_WebScraper.addItem(a)

    def web(self):
        URL = self.URL.text()
        if URL.__contains__(self.comboBox_paginas.currentText()):
            if self.comboBox_paginas.currentText().__contains__('https://www.booking.com'):
                mycursor = mydb.cursor()
                flag = True
                i = 1
                Nombre = 'Atlantis'
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
                while (flag == True):

                    fijo = 'customer_type=total&hp_nav=0&lang=es-us&order=featuredreviews&page=' + str(i) + '&r_lang=es&rows=75&soz=1&lang_click=top;cdl=es;lang_changed=1'
                    req = requests.get(PAGINA,fijo)
                    soup = BeautifulSoup(req.content, "lxml")
                    contadorneg = 0
                    contadorpos = 0

                    for lab in soup.find_all(class_="review_item_review"):
                        nota = lab.findAll(class_="review-score-badge", text=True)[0].text
                        for lab2 in lab.find_all(class_="review_pos"):
                            positivas = lab2.findAll(itemprop="reviewBody", text=True)[0].text
                            Nombre = 'Buenas'

                            #print(nota + positivas)

                            mycursor = mydb.cursor()
                            sql = "INSERT INTO opinion (ID_PaginaWeb,Nota, Texto) VALUES (%s,%s,%s)"
                            val = (ID_PaginaWeb, nota, positivas)
                            mycursor.execute(sql, val)
                            mydb.commit()
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
                            mydb.commit()
                            mycursor.close()
                            contadorpos += 1

                        for lab3 in lab.find_all(class_="review_neg"):
                            negativas = lab3.findAll(itemprop="reviewBody", text=True)[0].text
                            # print(nota + negativas)
                            Nombre2 = 'Malas'

                            mycursor = mydb.cursor()
                            sql = "INSERT INTO opinion (ID_PaginaWeb,Nota, Texto) VALUES (%s,%s,%s)"
                            val = (ID_PaginaWeb, nota, negativas)
                            mycursor.execute(sql, val)
                            mydb.commit()
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
                            mydb.commit()
                            mycursor.close()

                            contadorneg += 1

                        i += 1
                        print(i)
                        self.listWidget_WebScraper.addItem(str(i))
                    if positivas == None:
                        flag = False
                print('TOTAL DE VALORACIONES POSITIVAS', contadorpos)
                print('TOTAL DE VALORACIONES NEGATIVAS', contadorneg)
            if self.comboBox_paginas.currentText().__contains__('https://www.amazon.es/'):
                print('amazon')
        else:
            QMessageBox.about(self, "Error", "URL introducido no coincide con la página seleccionada")