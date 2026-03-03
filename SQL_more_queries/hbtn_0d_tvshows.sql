-- MySQL dump 10.13 Distrib 5.7.8-rc, pour Linux (x86_64)
--
-- Hôte : localhost Base de données : hbtn_0d_tvshows
-- ------------------------------------------------------
-- Version du serveur 5.7.8-rc

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 DÉFINIR @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 DÉFINIR LES NOMS utf8 */;
/*!40103 DÉFINIR @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 DÉFINIR LE FUSEAU HORAIRE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Structure de la table `tv_genres`
--

SUPPRIMER LA TABLE SI ELLE EXISTE `tv_genres`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 DÉFINIR character_set_client = utf8 */;
CRÉER LA TABLE `tv_genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  CLÉ PRIMAIRE (`id`)
) MOTEUR=InnoDB AUTO_INCREMENT=9 JEU DE CARACTÈRES PAR DÉFAUT=latin1;
/*!40101 DÉFINIR character_set_client = @saved_cs_client */;

--
-- Exportation des données pour la table `tv_genres`
--

VERROUILLER LES TABLES `tv_genres` ÉCRIRE ;
/*!40000 ALTER TABLE `tv_genres` DISABLE KEYS */;
INSÉRER DANS `tv_genres` VALUES (1,'Drame'),(2,'Mystère'),(3,'Aventure'),(4,'Fantastique'),(5,'Comédie'),(6,'Crime'),(7,'Suspense'),(8,'Thriller');
/*!40000 ALTER TABLE `tv_genres` ENABLE KEYS */;
DÉVERROUILLER LES TABLES ;

--
-- Structure de la table `tv_show_genres`
--

SUPPRIMER LA TABLE SI ELLE EXISTE `tv_show_genres`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 DÉFINIR character_set_client = utf8 */;
CRÉER TABLE `tv_show_genres` (
  `show_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  CLÉ `show_id` (`show_id`),
  CLÉ `genre_id` (`genre_id`),
  CONTRAINTE `tv_show_genres_ibfk_1` CLÉ ÉTRANGÈRE (`show_id`) RÉFÉRENCES `tv_shows` (`id`),
  CONTRAINTE `tv_show_genres_ibfk_2` CLÉ ÉTRANGÈRE (`genre_id`) RÉFÉRENCES `tv_genres` (`id`)
) MOTEUR=InnoDB JEU DE CARACTÈRES PAR DÉFAUT=latin1 ;
/*!40101 DÉFINIR character_set_client = @saved_cs_client */;

--
-- Exportation des données pour la table `tv_show_genres`
--

VERROUILLER LES TABLES `tv_show_genres` ÉCRIRE ;
/*!40000 ALTER TABLE `tv_show_genres` DISABLE KEYS */;
INSERT INTO `tv_show_genres` VALUES (1,1),(1,2),(2,3),(2,1),(2,4),(3,5),(4,5),(5,5),(6,6),(6,1),(6,7),(6,8),(8,6),(8,1),(8,2),(8,7),(8,8),(10,5),(10,1);
/*!40000 ALTER TABLE `tv_show_genres` ENABLE KEYS */;
DÉVERROUILLER LES TABLES ;

--
-- Structure de la table `tv_shows`
--

SUPPRIMER LA TABLE SI ELLE EXISTE `tv_shows`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 DÉFINIR character_set_client = utf8 */;
CRÉER LA TABLE `tv_shows` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(256) NOT NULL,
  CLÉ PRIMAIRE (`id`)
) MOTEUR=InnoDB AUTO_INCREMENT=11 JEU DE CARACTÈRES PAR DÉFAUT=latin1;
/*!40101 DÉFINIR character_set_client = @saved_cs_client */;

--
-- Exportation des données de la table `tv_shows`
--

VERROUILLER LES TABLES `tv_shows` ÉCRIRE ;
/*!40000 ALTER TABLE `tv_shows` DISABLE KEYS */;
INSERT INTO `tv_shows` VALUES (1,'House'),(2,'Game of Thrones'),(3,'The Big Bang Theory'),(4,'New Girl'),(5,'Silicon Valley'),(6,'Breaking Bad'),(7,'Better Call Saul'),(8,'Dexter'),(9,'Homeland'),(10,'The Last Man on Earth');
/*!40000 ALTER TABLE `tv_shows` ENABLE KEYS */;
DÉVERROUILLER LES TABLES ;
/*!40103 DÉFINIR TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 DÉFINIR CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 DÉFINIR CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 DÉFINIR COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Opération terminée le 26/02/2017 à 20:57:02