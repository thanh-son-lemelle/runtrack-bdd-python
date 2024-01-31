import mysql.connector
import pandas

user = "root"
passwd = str(input("Enter your password: "))

cnx = mysql.connector.connect(host="localhost", 
                              user=user, 
                              passwd=passwd, 
                              database="zoo"
                              )
cursor = cnx.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS animal(
               id INT PRIMARY KEY AUTO_INCREMENT,
               nom VARCHAR(255),
               race VARCHAR(255),
               id_cage VARCHAR(255),
               date_de_naissance DATE,
               pays_d_origine VARCHAR(255)
               );
               """)
cursor.execute("""
                CREATE TABLE IF NOT EXISTS cage(
                id INT PRIMARY KEY AUTO_INCREMENT,
                superficie FLOAT,
                capacité_max INT
                );
               """)

def create_animal(nom, race, id_cage, date_de_naissance, pays_d_origine):
    cursor.execute("INSERT INTO animal (nom, race, id_cage, date_de_naissance, pays_d_origine) VALUES (%s, %s, %s, %s, %s)",
                   (nom, race, id_cage, date_de_naissance, pays_d_origine))
    cnx.commit()

def read_animal():
    cursor.execute("SELECT * FROM animal")
    data = cursor.fetchall()
    for row in data:
        print(row)

def update_animal(id, nom, race, cage_id, date_naissance, pays_origine):
    cursor.execute("UPDATE animal SET nom=%s, race=%s, id_cage=%s, date_de_naissance=%s, pays_d_origine=%s WHERE id=%s",
                   (nom, race, cage_id, date_naissance, pays_origine, id))
    cnx.commit()

def delete_animal(id):
    cursor.execute("DELETE FROM animal WHERE id = %s", (id,))
    cnx.commit()


def read_animaux_cage():
    cursor.execute("SELECT cage.id, cage.superficie, cage.capacité_max, animal.* FROM cage LEFT JOIN animal ON cage.id = animal.id_cage")
    data = cursor.fetchall()
    print(data)

def create_cage(superficie, capacité_max):
    cursor.execute("INSERT INTO cage (superficie, capacité_max) VALUES (%s, %s)", (superficie, capacité_max))
    cnx.commit()

def read_cage():
    cursor.execute("SELECT * FROM cage")
    data = cursor.fetchall()
    for row in data:
        print(row)

def Superficie_totale():
    cursor.execute("SELECT SUM(superficie) AS 'Superficie_totale' FROM cage")
    data = cursor.fetchall()
    print(data, "m2")


while True:
    print(
            """
            menu: 
            1. ajouter un animal 
            2. afficher les animaux 
            3. modifier un animal 
            4. supprimer un animal 
            5. afficher les animaux par cage 
            6. ajouter une cage 
            7. Afficher les cages 
            8. Afficher la superficie totale
            9. quitter
            """
          )
    
    choix = int(input("votre choix: "))

    if choix == 1:
        nom = input("nom: ")
        race = input("race: ")
        cage_id = input("id de la cage: ")
        date_naissance = input("date de naissance: ")
        pays_origine = input("pays d'origine: ")
        create_animal(nom, race, cage_id, date_naissance, pays_origine)
    elif choix == 2:
        read_animal()
    elif choix == 3:
        id = input("id de l'animal: ")
        nom = input("nom de l'animal: ")
        race = input("race: ")
        cage_id = input("id de la cage: ")
        date_naissance = input("date de naissance: ")
        pays_origine = input("pays d'origine: ")
        update_animal(id, nom, race, cage_id, date_naissance, pays_origine)
    elif choix == 4:
        id = input("id de l'animal: ")
        delete_animal(id)
    elif choix == 5:
        read_animaux_cage()
    elif choix == 6:
        superficie = input("superficie: ")
        capacité_max = input("capacité max: ")
        create_cage(superficie, capacité_max)
    elif choix == 7:
        read_cage()
    elif choix == 8:
        Superficie_totale()
    elif choix == 9:
        cursor.close()
        cnx.close()
        break

    else:
        print("choix invalide")

cursor.close()
cnx.close()