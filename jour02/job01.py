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
def query(cnx):
    data = []
    cursor = cnx.cursor()
    query = ("SELECT * FROM etudiant")
    cursor.execute(query)
    for (id, nom, prenom, age, email) in cursor:
        data.append([id, nom, prenom, age, email])
    cursor.close()
    columns = ["id", "nom", "prenom", "age", "email"]
    data = pandas.DataFrame(data, columns=columns, index = None)
    print(data)

    cnx.close()    

cnx = connect()
query(cnx)
