import mysql.connector
import getpass
import pandas

host = "localhost"
user = "root"
passwd = str(input("Enter your password: "))
database = "job07"

def connect():

    try:
        cnx = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
        return cnx
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return None
    
def query(cnx, query):
    try:
        data = []
        cursor = cnx.cursor()
        cursor.execute(query)
        columns = [columns[0] for columns in cursor.description]

        

        data = cursor.fetchall()

        data = pandas.DataFrame(data, columns=columns)
        cursor.close()
        print(data)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    finally:
        cursor.close()


cnx = connect()
query(cnx, "SELECT * FROM employe WHERE salaire > 3000")
print ("=====================================================================================================")

cnx.close()

cnx = connect()
query(cnx, "SELECT employe. *, service.nom AS service_nom FROM employe LEFT JOIN service ON employe.id_service = service.id;")

print("=====================================================================================================")


class Employe:
    def __init__(self, cnx):
        self.cnx = cnx

    def create(self, nom, prenom, salaire, id_service):
        cursor = self.cnx.cursor()
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        cursor.execute(query, values)
        self.cnx.commit()
        cursor.close()

    def read_all(self):
        cursor = self.cnx.cursor(dictionary=True)
        query = "SELECT employe.*, service.nom AS service_nom FROM employe LEFT JOIN service ON employe.id_service = service.id"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def update(self, employee_id, new_salaire):
        cursor = self.cnx.cursor()
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salaire, employee_id)
        cursor.execute(query, values)
        self.cnx.commit()
        cursor.close()

    def delete(self, employee_id):
        cursor = self.cnx.cursor()
        query = "DELETE FROM employe WHERE id = %s"
        cursor.execute(query, (employee_id,))
        self.cnx.commit()
        cursor.close()

# Usage example:
cnx = connect()
salarie_manager = Employe(cnx)

# Create
salarie_manager.create("Doe", "John", 5000.00, 1)

# Read all
employees_with_services = salarie_manager.read_all()
print("=====================================================================================================")
print(employees_with_services)
print("=====================================================================================================")

# Update
salarie_manager.update(employee_id=1, new_salaire=6000.00)

# Delete
salarie_manager.delete(employee_id=1)

cnx.close()