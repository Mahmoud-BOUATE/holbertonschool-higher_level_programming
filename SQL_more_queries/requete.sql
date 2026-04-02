SELECT titre, gf.signification
FROM dvd as d
JOIN genres_film as gf ON d.code_genre = gf.code_genre;


SELECT d.titre, r.nom ,r.pays, g.signification
FROM dvd as d
JOIN realisateurs as r ON d.code_realisateur = r.code_realisateur
JOIN genres_film as g ON g.code_genre = d.code_genre

SELECT c.nom, c.prenom
FROM clients as c
JOIN factures as f ON c.code_client = f.code_client
JOIN locations as l ON f.num_facture = l.num_facture
JOIN dvd as d ON l.num_dvd = d.num_dvd

WHERE  MONTH(f.date_facture) = 04 AND YEAR(f.date_facture) = 2026 AND DAY(f.date_facture) = 01


SELECT c.titre,c.nom, c.prenom, d.titre, d.duree, r.nom, r.annee_naissance, r.code_realisateur
FROM clients as c
JOIN factures as f ON c.code_client = f.code_client
JOIN locations as l ON f.num_facture = l.num_facture
JOIN dvd as d ON l.num_dvd = d.num_dvd
JOIN realisateurs as r ON d.code_realisateur = r.code_realisateur
