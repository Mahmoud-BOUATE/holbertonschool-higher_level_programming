INSERT INTO clients (titre, nom, prenom, adresse_rue, code_postal, ville, num_tel, date_naissance, enfants) VALUES
('M.', 'Dupont', 'Jean', '10 rue de Paris', '75001', 'Paris', '0600000001', '1985-06-15', 2),
('Mme', 'Martin', 'Sophie', '25 avenue Victor Hugo', '69000', 'Lyon', '0600000002', '1990-03-22', 1),
('M.', 'Durand', 'Paul', '5 rue Nationale', '59000', 'Lille', '0600000003', '1978-11-05', 3);
INSERT INTO realisateurs (nom, annee_naissance, pays) VALUES
('Steven Spielberg', 1946, 'USA'),
('Christopher Nolan', 1970, 'UK'),
('Quentin Tarantino', 1963, 'USA');
INSERT INTO genres_film (signification) VALUES
('Action'),
('Science-Fiction'),
('Drame'),
('Comédie');
INSERT INTO types_location (libelle, coefficient, nb_jours) VALUES
('Classique', 1.0, 3),
('Nouveauté', 1.5, 2),
('Longue durée', 0.8, 7);
INSERT INTO dvd (titre, prix_base, code_realisateur, code_genre, annee, descriptif, duree) VALUES
('Inception', 10.0, 2, 2, 2010, 'Film de rêves imbriqués', 148),
('Pulp Fiction', 8.0, 3, 3, 1994, 'Histoires croisées', 154),
('Jurassic Park', 9.0, 1, 2, 1993, 'Dinosaures recréés', 127),
('The Mask', 7.0, 1, 4, 1994, 'Comédie déjantée', 101);
INSERT INTO factures (code_client, date_facture) VALUES
(1, '2026-04-01'),
(2, '2026-04-02'),
(3, '2026-04-03');
INSERT INTO locations (num_facture, num_dvd, code_type_location, date_retour) VALUES
(1, 1, 2, '2026-04-03'),
(1, 2, 1, '2026-04-05'),
(2, 3, 3, '2026-04-10'),
(3, 4, 1, '2026-04-06');