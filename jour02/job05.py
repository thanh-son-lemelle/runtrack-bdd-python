import mysql.connector
import getpass
import pandas

host = "localhost"
user = "root"
passwd = str(input("Enter your password: "))
database = "LaPlateforme"

def connect():

    try:
        cnx = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
        return cnx
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return None
def query(cnx, query):
    data = []
    cursor = cnx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    if len(data) != 1:
        
        data = data[0] + data[1]
        data = data[0] + data[1]

    print(f"la superficie de la Plateforme est de {data} m2")

        

cnx = connect()
query(cnx, "SELECT SUM(superficie) AS 'Superficie_totale' FROM etage")
query(cnx, "SELECT superficie FROM etage")
cnx.close()