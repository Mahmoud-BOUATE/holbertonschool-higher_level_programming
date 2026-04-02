CREATE DATABASE IF NOT EXISTS DVD;

USE DVD;

DROP TABLES IF EXISTS locations, clients, realisateurs, genres_film, types_location, dvd, factures, genres;

CREATE TABLE IF NOT EXISTS clients (
    code_client INT AUTO_INCREMENT PRIMARY KEY ,
    titre VARCHAR(15) NOT NULL,
    nom VARCHAR(40) NOT NULL,
    prenom VARCHAR(40) NOT NULL,
    adresse_rue VARCHAR(100) NOT NULL,
    code_postal VARCHAR(10) NOT NULL,
    ville VARCHAR(40) NOT NULL,
    num_tel VARCHAR(10) NOT NULL,
    date_naissance DATE NOT NULL,
    enfants INT NOT NULL
)

CREATE TABLE IF NOT EXISTS factures (
    num_facture INT AUTO_INCREMENT PRIMARY KEY,
    code_client INT NOT NULL,
    date_facture DATE NOT NULL,

    FOREIGN KEY (code_client) REFERENCES clients(code_client)
)

CREATE TABLE IF NOT EXISTS types_location (
    code_type_location INT AUTO_INCREMENT PRIMARY KEY,
    libelle VARCHAR(50) NOT NULL,
    coefficient FLOAT NOT NULL,
    nb_jours INT NOT NULL
)

CREATE TABLE IF NOT EXISTS realisateurs (
    code_realisateur INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(40) NOT NULL,
    annee_naissance INT NOT NULL,
    pays VARCHAR(40) NOT NULL
)

CREATE TABLE IF NOT EXISTS genres_film (
    code_genre INT AUTO_INCREMENT PRIMARY KEY,
    signification VARCHAR(40) NOT NULL
)


CREATE TABLE IF NOT EXISTS dvd (
    num_dvd INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(15) NOT NULL,
    prix_base FLOAT NOT NULL,
    code_realisateur INT NOT NULL,
    code_genre INT NOT NULL,
    annee INT NOT NULL,
    descriptif TEXT(255) NOT NULL,
    duree INT NOT NULL,

    FOREIGN KEY (code_realisateur) REFERENCES realisateurs(code_realisateur),
    FOREIGN KEY (code_genre) REFERENCES genres_film(code_genre)
)

CREATE TABLE IF NOT EXISTS locations (
    num_facture INT NOT NULL,
    num_dvd INT NOT NULL,
    code_type_location INT NOT NULL,
    date_retour DATE NOT NULL,

    PRIMARY KEY (num_facture, num_dvd),
    FOREIGN KEY (num_facture) REFERENCES factures(num_facture),
    FOREIGN KEY (num_dvd) REFERENCES dvd(num_dvd),
    FOREIGN KEY (code_type_location) REFERENCES types_location(code_type_location)
)
