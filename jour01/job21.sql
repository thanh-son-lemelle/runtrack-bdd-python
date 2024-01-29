mysql> SELECT COUNT(*) AS nombre_etudiants_entre_18_et_25 FROM etudiant
    -> WHERE age BETWEEN 18 AND 25;
+---------------------------------+
| nombre_etudiants_entre_18_et_25 |
+---------------------------------+
|                               3 |
+---------------------------------+
1 row in set (0.00 sec)