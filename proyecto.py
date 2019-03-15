import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
  host="vtc.hopto.org",
  user="diego",
  passwd="Galicia96.",
    database="vtc"
)

mycursor = mydb.cursor()
flag=True
i=1
while flag==True:

    fijo = 'customer_type=total&hp_nav=0&lang=en-us&order=featuredreviews&page='+str(i)+'&r_lang=en&rows=75&soz=1&lang_click=top;cdl=es;lang_changed=1'
    req = requests.get('https://www.booking.com/reviews/ae/hotel/atlantis-the-palm.html?label=gen173nr-1DCA0oAkIRYXRsYW50aXMtdGhlLXBhbG1IClgEaKkBiAEBmAEKuAEXyAEP2AED6AEB-AECiAIBqAIDuALkt6PkBcACAQ&sid=e0fc479b2a8428c6e64b32ee71056cf7&',fijo)
    soup = BeautifulSoup(req.content, "lxml")
    contadorneg = 0
    contadorpos = 0

    for lab in soup.find_all(class_="review_item_review"):
        nota = lab.findAll(class_="review-score-badge", text=True)[0].text
        for lab2 in lab.find_all(class_="review_pos"):
            positivas = lab2.findAll(itemprop="reviewBody", text=True)[0].text
            #print(nota + positivas )

            sql = "INSERT INTO opinion (Nota, Texto) VALUES (%s, %s)"
            val = (nota, positivas)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")

            contadorpos += 1
        for lab3 in lab.find_all(class_="review_neg"):
            negativas = lab3.findAll(itemprop="reviewBody", text=True)[0].text
           # print(nota + negativas)
            contadorneg += 1
    i+=1
    if positivas == None:
        flag=False

print('TOTAL DE VALORACIONES POSITIVAS', contadorpos)
print('TOTAL DE VALORACIONES NEGATIVAS', contadorneg)



