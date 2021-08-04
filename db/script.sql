CREATE SCHEMA IF NOT EXISTS mabdd;

USE mabdd;

CREATE TABLE IF NOT EXISTS adresses (
    id_adresse INT NOT NULL,
    ville VARCHAR(30) NULL DEFAULT NULL,
    code_postal INT NULL DEFAULT NULL,
    rue VARCHAR(68) NULL DEFAULT NULL,
    numero INT NULL DEFAULT NULL,
    PRIMARY KEY (`id_adresse`)
);

CREATE TABLE IF NOT EXISTS utilisateurs (
    id_utilisateur INT NOT NULL,
    nom VARCHAR(30) NULL,
    prenom VARCHAR(30) NOT NULL,
    id_adresse INT NULL,
    PRIMARY KEY (`id_utilisateur`),
    CONSTRAINT `id_adresse`
    FOREIGN KEY (`id_adresse`)
    REFERENCES adresses (`id_adresse`)
);

INSERT INTO adresses
    VALUES
    (1, "Lyon", "69008", "Paul Bert", 23),
    (2, "Nice", "43568", "Aime Cesar", 56)
;

INSERT INTO utilisateurs
    VALUES 
    (1, "Durand", "Diane", 1),
    (2, "Dupont", "Max", 2),
    (3, "Leroy", "Julie", null),
    (4, "Delbaere", "Ludovic", null)
    ;




