mysql> USE LaPlateforme;
Database changed
mysql> SELECT *FROM etudiant
    -> WHERE age < 18;
+----+---------------+--------+-----+-------------------------------+
| id | nom           | prenom | age | email                         |
+----+---------------+--------+-----+-------------------------------+
|  4 | Binkie Barnes | Binkie |  16 | binkie.barnes@laplateforme.io |
+----+---------------+--------+-----+-------------------------------+
1 row in set (0.00 sec)