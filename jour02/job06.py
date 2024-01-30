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
        resultat = tuple(sum(x) for x in zip(*data))
        print(f"la capcité de toutes les salles : {resultat} ")
    else: 
        print(f"la capcité de toutes les salles : {data} ")
        

        

cnx = connect()
query(cnx, "SELECT SUM(capacite) AS 'Capacité_total' FROM salle")
query(cnx, "SELECT capacite FROM salle")
cnx.close()