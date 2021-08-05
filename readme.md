Création de conteneurs docker :

        . mysql : base de donnée  

        . adminer : gestion de la base de donnée (interface graphique)

        . flask : gestion de la base de donnée (interface web)

MySQL :  

paramètres de connexion:  
        . user: root  
        . password: root  
        . ports: 3306:3306  
        . nom du service: db  

Adminer peut être interrogé sur le localhost:8080

Flask est sur le localhost:5000  
        . affichage des utilisateurs de la base de donnée  
        . l'ajout d'un utilisateur pose problème et doit être fixé (problème dans la synthaxe SQL)

