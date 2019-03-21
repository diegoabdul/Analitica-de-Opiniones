from wsgiref import headers

import requests
from bs4 import BeautifulSoup
import mysql.connector
from itertools import zip_longest
import re
listaopiniones=list()
listavaloraciones=list()
listafinal=list()
headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',})
contador=0
#maximo=self.comboBox_2.currentText()
#maximo_int = int(maximo)
#maximo_pagina = (maximo_int / 75)
i=1
contadorneg = 0
contadorpos = 0
flag = True

while (flag == True and i <= 5):
    URL='https://www.amazon.es/dp/B079PFKDZC/ref=gw_es_desk_h1_aucc_Rd_shlv_alx?pf_rd_p=5edb1c0f-ae1f-4c50-bc68-529a8841cd34&pf_rd_r=HQ5MGXHVJZ6VZ1MMZ2RA'
    comodin= URL.replace('dp','product-reviews',1)
    url = re.sub('\/ref=*..*', '', comodin)

    fijopositivas='/ref=cm_cr_arp_d_viewpnt_lft?pf_rd_p=5edb1c0f-ae1f-4c50-bc68-529a8841cd34&pf_rd_r=HQ5MGXHVJZ6VZ1MMZ2RA&filterByStar=positive&pageNumber=' + str(i)
    fijonegativas='/ref=cm_cr_arp_d_viewpnt_lft?pf_rd_p=5edb1c0f-ae1f-4c50-bc68-529a8841cd34&pf_rd_r=HQ5MGXHVJZ6VZ1MMZ2RA&filterByStar=critical&pageNumber=' + str(i)
    PAGINA_POSITIVAS=url+fijopositivas
    PAGINA_NEGATIVAS=url+fijonegativas
    print(PAGINA_POSITIVAS)
    #print(PAGINA_NEGATIVAS)
    i+=1
    req = requests.get(PAGINA_POSITIVAS,headers)
    soup = BeautifulSoup(req.content, "lxml")

    for lab in soup.find_all('span', {'class': 'a-size-base review-text review-text-content'}):
            comodin2 = re.sub('\/*<span class="a-size-base review-text review-text-content" data-hook="review-body"><span class="">', '',str(lab))
            comodin3 = re.sub('\/*<\/span>', '',comodin2)
            comodin4 = re.sub('\/*<br\/>', '', comodin3)
            opinionFinal = re.sub('\/*<div..*\/>', '', comodin4)
            listaopiniones.append(opinionFinal)

    for lab1 in soup.find_all(class_="a-icon-alt"):
        comodin5 = re.sub('\/*<span..*">', '',str(lab1))
        valoracionFinal = re.sub('\/*de 5 estrellas<\/span>', '', comodin5)
        listavaloraciones.append(valoracionFinal)


    for final in range(len(listaopiniones)):
        print(listavaloraciones[final])
        print(listaopiniones[final])

