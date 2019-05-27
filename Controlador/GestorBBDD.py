
import mysql.connector


"""
Conexion a la base de datos
"""
mydb = mysql.connector.connect(
  host="vtc.hopto.org",
  user="diego",
  passwd="Galicia96.",
    database="vtc"
)

"""
ControladorWebScrapperClasificador
"""
def seleccionarIDPaginaWeb(ID_Proyecto):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID_PaginaWeb FROM paginaweb WHERE ID_ProyectoClasificacion=%s", (ID_Proyecto,))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult

def seleccionarNombre(ID):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Nombre FROM paginaweb WHERE ID_PaginaWeb=%s", (ID[0],))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult

def seleccionarNotayTexto(ID):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Nota,Texto,ID_Unlabeled FROM unlabeled WHERE ID_PaginaWeb=%s", (ID[0],))
    mycursor.close()
    myresult = mycursor.fetchall()
    return myresult

def borrarArchivosWebScrapper(ID_Proyecto):
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM proyectoclasificacion WHERE ID_ProyectoClasificacion=%s", (ID_Proyecto,))
    mydb.commit()
    mycursor.close()


"""WebScrapper TripAdvisor, Booking y Amazon
Fusionar listas
"""
def insertarPaginaWeb(val):
    mycursor = mydb.cursor()
    sql = "INSERT INTO paginaweb (URL, Nombre,ID_ProyectoClasificacion) VALUES (%s, %s,%s)"
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def insertarPaginaWeb2(val):
    mycursor = mydb.cursor()
    sql = "INSERT INTO paginaweb (URL, Nombre,ID_Proyecto) VALUES (%s, %s,%s)"
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def seleccionarPaginaWeb(URL):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID_PaginaWeb FROM paginaweb WHERE URL=%s", (URL,))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult

def insertarBuenasyMalas(val):
    mycursor = mydb.cursor()
    sql = "INSERT INTO unlabeled (ID_PaginaWeb,Nota, Texto) VALUES (%s,%s,%s)"
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def insertarBuenasyMalas2(val):
    mycursor = mydb.cursor()
    sql = "INSERT INTO opinion (ID_PaginaWeb,Nota, Texto,Label) VALUES (%s,%s,%s,%s)"
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
"""
Metodo web en ControladorWebScrapperClasificador
"""
def insertarproyectoClasificacion(val):
    mycursor = mydb.cursor()
    sql = "INSERT INTO proyectoclasificacion (Nombre,ID_Usuario) VALUES (%s, %s)"
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def seleccionarID_ProyectoClasificacion(Nombrepro):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID_ProyectoClasificacion FROM proyectoclasificacion WHERE Nombre=%s", (Nombrepro,))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
"""
Metodo web en ControladorWebScrapper
"""
def insertarProyecto(val):
    mycursor = mydb.cursor()
    sql = "INSERT INTO proyecto (Nombre,ID_Usuario) VALUES (%s, %s)"
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def seleccionarID_Proyecto(Nombrepro):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID_Proyecto FROM proyecto WHERE Nombre=%s", (Nombrepro,))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult

"""
ControladorVentanaWebScrapper
"""
def seleccionarIDPaginaWeb2(ID_Proyecto):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID_PaginaWeb FROM paginaweb WHERE ID_Proyecto=%s", (ID_Proyecto,))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
def seleccionarNombre2(ID):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Nombre FROM paginaweb WHERE ID_PaginaWeb=%s", (ID[0],))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
def seleccionarNotayTextoBuenas2(ID):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Nota,Texto FROM opinion WHERE ID_PaginaWeb=%s and Label='Buenas'",
                     (ID[0],))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
def seleccionarNotayTextoMalas2(ID):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Nota,Texto FROM opinion WHERE ID_PaginaWeb=%s and Label='Malas'", (ID[0],))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
def borrarArchivosWebScrapper2(ID_Proyecto):
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM proyecto WHERE ID_Proyecto=%s", (ID_Proyecto,))
    mydb.commit()
    mycursor.close()
"""
ControladorVentanaRegistrar
"""
def agregarUsuario(val):
    mycursor = mydb.cursor()
    sql = "INSERT INTO usuario (Nombre,Apellidos,Usuario,Clave,Rol) VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
"""
ControladorVentanaLogin
"""
def seleccionarUsuario(usuarioBBDD):
    mycursor = mydb.cursor()
    sql = ("SELECT * FROM usuario WHERE Usuario = %s ")
    mycursor.execute(sql, usuarioBBDD)
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
"""
ControladorVentanaEntrenamientoSQL
"""
def entrenamientoSQL(comboBox):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID_Proyecto FROM proyecto WHERE Nombre=%s", (comboBox.currentText(),))
    myresult = mycursor.fetchall()
    return myresult
def nombreProyecto():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Nombre FROM proyecto")
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
"""
ControladorVentanaEntrenamiento
"""

def insertarNombreModelo(val):
    mycursor = mydb.cursor()
    sql = "INSERT INTO modelo (Nombre) VALUES (%s)"
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
"""
ControladorVentanaClasificadorSQL
"""

def nombreProyecto2():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Nombre FROM proyectoclasificacion")
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
def clasificadorSQL(comboBox):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID_ProyectoClasificacion FROM proyectoclasificacion WHERE Nombre=%s",
                     (comboBox.currentText(),))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
"""
ControladorVentanaClasificador
"""
def nombreModelo():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Nombre FROM modelo")
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
def updateAnalisisSentimiento(val):
    mycursor = mydb.cursor()
    sql = "UPDATE unlabeled SET Sentimiento = %s WHERE ID_Unlabeled = %s"
    mycursor.execute(sql, val)
    mydb.commit()
def updateLabel(val):
    mycursor = mydb.cursor()
    sql = "UPDATE unlabeled SET LabelAsignado = %s WHERE ID_Unlabeled = %s"
    mycursor.execute(sql, val)
    mydb.commit()
