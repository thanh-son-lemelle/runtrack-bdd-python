mysql> SELECT * FROM etudiant
    -> ORDER BY age ASC;
+----+-----------------+----------+-----+---------------------------------+
| id | nom             | prenom   | age | email                           |
+----+-----------------+----------+-----+---------------------------------+
|  4 | Binkie Barnes   | Binkie   |  16 | binkie.barnes@laplateforme.io   |
|  3 | John Doe        | John     |  18 | john.doe@laplateforme.io        |
|  5 | Gertrude Dupuis | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  1 | Betty Spaghetti | Betty    |  23 | betty.Spaghetti@laplateforme.io |
|  2 | Chuck Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     |
+----+-----------------+----------+-----+---------------------------------+
5 rows in set (0.00 sec)