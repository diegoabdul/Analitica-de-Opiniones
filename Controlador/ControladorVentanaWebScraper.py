from PyQt5.QtWidgets import QMessageBox
from Vista.VistaVentanaWebScraper import *
import Controlador.ControladorVentanaEntrenamiento as ventanaEntrenamiento
import threading
import requests
from bs4 import BeautifulSoup
import mysql.connector
import re
import os

mydb = mysql.connector.connect(
  host="vtc.hopto.org",
  user="diego",
  passwd="Galicia96.",
    database="vtc"
)


class NewApp(QtWidgets.QMainWindow, Ui_MainWindow):
    flagDirectorio = False
    Directorio=os.getcwd() + '/Valoraciones'
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
        self.borraropinion = list()
        self.flagborrar=False
        self.btn_guardar.clicked.connect(self.guardar)


    def volverAtras(self):
        if self.flagborrar==False:
            """
            Método encargado de volver al menu principal
            """
            self.Open = ventanaEntrenamiento.NewApp()
            self.Open.show()
            self.close()
        else:
            QMessageBox.about(self, "Ok", "Ya hemos empezado el proceso porfavor guarde o borre en el botón correspondiente para poder salir")

    def mostrar(self,nota,positivas,contadorpos):
        self.listWidget.addItem(nota +positivas)
        self.lineEdit_Buenas.setText(str(contadorpos))

    def mostrar2(self,nota,negativas,contadorneg):
        self.listWidget.addItem(nota + negativas)
        self.lineEdit_Malas.setText(str(contadorneg))

    def iniciar(self):
        self.listWidget.clear()
        hilo2 = threading.Thread(target=self.web)
        hilo2.start()


    def guardar(self):
        if self.flagborrar == True:
            msgBox = QMessageBox()
            msgBox.setInformativeText("¿Desea guardar los cambios?")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec_()

            if (ret == QMessageBox.Save):

                path = os.getcwd() + '/Valoraciones'

                try:
                    os.makedirs(path)
                except OSError:
                    print("Creation of the directory %s failed" % path)
                else:
                    print("Successfully created the directory %s" % path)

                path = os.getcwd() + '/Valoraciones/Buenas'

                try:
                    os.makedirs(path)
                except OSError:
                    print("Creation of the directory %s failed" % path)
                else:
                    print("Successfully created the directory %s" % path)

                mycursor = mydb.cursor()
                mycursor.execute("SELECT Nombre FROM paginaweb WHERE ID_PaginaWeb=%s", (self.borrar,))
                myresult = mycursor.fetchall()
                for x in myresult:
                    NombreArchivo = x[0]
                mycursor.close()

                mycursor = mydb.cursor()
                mycursor.execute("SELECT Nota,Texto FROM opinion WHERE ID_PaginaWeb=%s and Label='Buenas'", (self.borrar,))
                myresult = mycursor.fetchall()
                i=0
                for x in myresult:
                    i+=1
                    Nota = x[0]
                    Texto = x[1]
                    NotaGuardar = str(Nota)
                    f = open(path + "/"+NombreArchivo+"_"+str(i)+".txt", "w+")
                    f.write(NotaGuardar+' '+Texto)
                    f.close()
                mycursor.close()


                path = os.getcwd() + '/Valoraciones/Malas'

                try:
                    os.makedirs(path)
                except OSError:
                    print("Creation of the directory %s failed" % path)
                else:
                    print("Successfully created the directory %s" % path)

                mycursor = mydb.cursor()
                mycursor.execute("SELECT Nombre FROM paginaweb WHERE ID_PaginaWeb=%s", (self.borrar,))
                myresult = mycursor.fetchall()
                for x in myresult:
                    NombreArchivoMalas = x[0]
                mycursor.close()

                mycursor = mydb.cursor()
                mycursor.execute("SELECT Nota,Texto FROM opinion WHERE ID_PaginaWeb=%s and Label='Malas'", (self.borrar,))
                myresult = mycursor.fetchall()
                for x in myresult:
                    i += 1
                    Nota2 = x[0]
                    Texto2 = x[1]
                    NotaGuardar2 = str(Nota2)
                    f = open(path + "/" + NombreArchivoMalas + "_" + str(i) + ".txt", "w+")
                    f.write(NotaGuardar2 + ' ' + Texto2)
                    f.close()
                mycursor.close()
                NewApp.flagDirectorio=True
                self.flagborrar=False
                QMessageBox.about(self, "Ok", "Se ha guardado correctamente")
                self.volverAtras()

            if (ret == QMessageBox.Discard):
                self.listWidget.clear()
                QMessageBox.about(self, "Ok", "Espere estamos borrando toda la información")
                mycursor = mydb.cursor()
                mycursor.execute("SELECT ID_Opinion FROM opinion where ID_PaginaWeb=%s", (self.borrar,))
                myresult = mycursor.fetchall()
                for id in myresult:
                    self.borraropinion = id[0]
                    mycursor.execute("DELETE FROM opinion WHERE ID_Opinion=%s", (self.borraropinion,))
                    mydb.commit()
                mycursor.execute("DELETE FROM paginaweb WHERE ID_PaginaWeb=%s", (self.borrar,))
                mydb.commit()
                QMessageBox.about(self, "Ok", "Eliminado Correctamente")
                self.flagborrar = False
                self.volverAtras()
            self.flagborrar=False
        else:
            QMessageBox.about(self, "Error", "No hay nada que guardar")

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
                self.borrar=ID_PaginaWeb

                comodin=URL.replace('hotel','reviews',1)
                PAGINA = comodin[:34] + '/hotel' + comodin[34:]
                #print(PAGINA)
                contador=0
                maximo=self.comboBox_2.currentText()
                maximo_int = int(maximo)
                maximo_pagina = (maximo_int / 75)
                contadorneg = 0
                contadorpos = 0
                self.flagborrar = True
                while (flag == True and i<=maximo_pagina):

                    fijo = 'customer_type=total&hp_nav=0&lang='+idiomareal+'-us&order=featuredreviews&page=' + str(i) + '&r_lang='+idiomareal+'&rows=75&soz=1&lang_click=top;cdl=es;lang_changed=1'
                    req = requests.get(PAGINA,fijo)
                    soup = BeautifulSoup(req.content, "lxml")
                    #print(fijo)
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
                            sql = "INSERT INTO opinion (ID_PaginaWeb,Nota, Texto,Label) VALUES (%s,%s,%s,%s)"
                            val = (ID_PaginaWeb, nota, positivas,Nombre)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            mycursor.close()

                        for lab3 in lab.find_all(class_="review_neg"):
                            negativas = lab3.findAll(itemprop="reviewBody", text=True)[0].text
                            contadorneg += 1
                            hilo3 = threading.Thread(target=self.mostrar2, args=(nota, negativas,contadorneg))
                            hilo3.start()
                            # print(nota + negativas)
                            Nombre2 = 'Malas'

                            mycursor = mydb.cursor()
                            sql = "INSERT INTO opinion (ID_PaginaWeb,Nota, Texto,Label) VALUES (%s,%s,%s,%s)"
                            val = (ID_PaginaWeb, nota, negativas,Nombre2)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            mycursor.close()

            if self.comboBox_paginas.currentText().__contains__('https://www.amazon.es/'):

                listaopiniones = list()
                listavaloraciones = list()
                listaopinionesneg = list()
                listavaloracionesneg =list()
                listafinal = list()
                listafinal2 =list()

                headers = requests.utils.default_headers()
                headers.update(
                    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0', })
                contador = 0
                maximo=self.comboBox_2.currentText()
                maximo_int = int(maximo)
                maximo_pagina = (maximo_int / 75)
                i = 1
                contadorneg = 0
                contadorpos = 0
                flag = True
                maximo_pagina2=maximo_pagina*7

                mycursor = mydb.cursor()
                Nombre = 'Amazon'
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
                self.borrar = ID_PaginaWeb
                self.flagborrar = True
                while (flag == True and i <= maximo_pagina2):
                    pagina = URL
                    comodin = pagina.replace('dp', 'product-reviews', 1)
                    url = re.sub('\/ref=*..*', '', comodin)

                    fijopositivas = '/ref=cm_cr_arp_d_viewpnt_lft?pf_rd_p=5edb1c0f-ae1f-4c50-bc68-529a8841cd34&pf_rd_r=HQ5MGXHVJZ6VZ1MMZ2RA&filterByStar=positive&pageNumber=' + str(
                        i)
                    fijonegativas = '/ref=cm_cr_arp_d_viewpnt_lft?pf_rd_p=5edb1c0f-ae1f-4c50-bc68-529a8841cd34&pf_rd_r=HQ5MGXHVJZ6VZ1MMZ2RA&filterByStar=critical&pageNumber=' + str(
                        i)
                    PAGINA_POSITIVAS = url + fijopositivas
                    PAGINA_NEGATIVAS = url + fijonegativas
                    #print(PAGINA_POSITIVAS)

                    i += 1
                    req = requests.get(PAGINA_POSITIVAS, headers)
                    soup = BeautifulSoup(req.content, "lxml")

                    for lab in soup.find_all('span', {'class': 'a-size-base review-text review-text-content'}):
                        comodin2 = re.sub(
                            '\/*<span class="a-size-base review-text review-text-content" data-hook="review-body"><span class="">',
                            '', str(lab))
                        comodin3 = re.sub('\/*<\/span>', '', comodin2)
                        comodin4 = re.sub('\/*<br\/>', '', comodin3)
                        opinionFinal = re.sub('\/*<div..*\/>', '', comodin4)
                        listaopiniones.append(opinionFinal)
                        contadorpos+=1
                    for lab1 in soup.find_all(class_="a-icon-alt"):
                        comodin5 = re.sub('\/*<span..*">', '', str(lab1))
                        valoracionFinal = re.sub('\/*de 5 estrellas<\/span>', '', comodin5)
                        listavaloraciones.append(valoracionFinal)

                    for final in range(len(listaopiniones)):
                        #print(listavaloraciones[final])
                        #print(listaopiniones[final])
                        hilo1 = threading.Thread(target=self.mostrar, args=( listavaloraciones[final],listaopiniones[final], contadorpos))
                        hilo1.start()
                        Nombre3 = 'Buenas'
                        if final == None:
                            flag = False
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO opinion (ID_PaginaWeb,Nota, Texto,Label) VALUES (%s,%s,%s,%s)"
                        val = (ID_PaginaWeb, listavaloraciones[final], listaopiniones[final],Nombre3)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        mycursor.close()

                    req2 = requests.get(PAGINA_NEGATIVAS, headers)
                    soup2 = BeautifulSoup(req2.content, "lxml")

                    for lab in soup2.find_all('span', {'class': 'a-size-base review-text review-text-content'}):
                        comodin2 = re.sub(
                            '\/*<span class="a-size-base review-text review-text-content" data-hook="review-body"><span class="">',
                            '', str(lab))
                        comodin3 = re.sub('\/*<\/span>', '', comodin2)
                        comodin4 = re.sub('\/*<br\/>', '', comodin3)
                        opinionFinal2 = re.sub('\/*<div..*\/>', '', comodin4)
                        listaopinionesneg.append(opinionFinal2)
                        contadorneg += 1

                    for lab1 in soup2.find_all(class_="a-icon-alt"):
                        comodin5 = re.sub('\/*<span..*">', '', str(lab1))
                        valoracionFinal = re.sub('\/*de 5 estrellas<\/span>', '', comodin5)
                        listavaloracionesneg.append(valoracionFinal)

                    for final in range(len(listaopinionesneg)):
                        # print(listavaloraciones[final])
                        # print(listaopiniones[final])
                        hilo3 = threading.Thread(target=self.mostrar2,
                                                 args=(listavaloracionesneg[final],listaopinionesneg[final], contadorneg))
                        hilo3.start()
                        Nombre4 = 'Malas'
                        if final == None:
                            flag = False
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO opinion (ID_PaginaWeb,Nota, Texto,Label) VALUES (%s,%s,%s,%s)"
                        val = (ID_PaginaWeb, listavaloracionesneg[final], listaopinionesneg[final],Nombre4)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        mycursor.close()
            #else:
                #QMessageBox.about(self, "Error", "URL introducido no coincide con la página seleccionada")
        else:
            print('URL incorrecta')

