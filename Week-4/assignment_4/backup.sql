CREATE DATABASE  IF NOT EXISTS `assignment` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `assignment`;
-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (arm64)
--
-- Host: localhost    Database: assignment
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `article` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `content` text NOT NULL,
  `author` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (1,'Article 1 title','Article 1 content','author1'),(2,'Article 2 title','Article 2 content','author2'),(3,'Article 3 title','Article 3 content','author3'),(4,'Article 4 title','Article 4 content','author4'),(5,'Article 5 title','Article 5 content','author5'),(6,'Article 6 title','Article 6 content','author6'),(7,'Article 7 title','Article 7 content','author7'),(8,'Article 8 title','Article 8 content','author8'),(9,'Article 9 title','Article 9 content','author9'),(10,'Article 10 title','Article 10 content','author10'),(11,'Article 11 title','Article 11 content','author11'),(12,'Article 12 title','Article 12 content','author12'),(13,'Article 13 title','Article 13 content','author13'),(14,'Article 14 title','Article 14 content','author14'),(15,'Article 15 title','Article 15 content','author15'),(16,'Article 16 title','Article 16 content','author16'),(17,'Article 17 title','Article 17 content','author17'),(18,'Article 18 title','Article 18 content','author18'),(19,'Article 19 title','Article 19 content','author19'),(20,'Article 20 title','Article 20 content','author20'),(21,'Article 21 title','Article 21 content','author21'),(22,'Article 22 title','Article 22 content','author22'),(23,'Article 23 title','Article 23 content','author23'),(24,'Article 24 title','Article 24 content','author24'),(25,'Article 25 title','Article 25 content','author25'),(26,'Article 26 title','Article 26 content','author26'),(27,'Article 27 title','Article 27 content','author27'),(28,'Article 28 title','Article 28 content','author28'),(29,'Article 29 title','Article 29 content','author29'),(30,'Article 30 title','Article 30 content','author30');
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'example_user','user@example.com','password123'),(2,'user1','user1@user1.com','user'),(3,'asd','asd@asd.com','scrypt:32768:8:1$NmSoZ6ENDkZTybkx$e8aeef72a3109a39e2fbe3b09cbbcd8829e8f77f629422c9d7965852f6b9574255512ef703f664d2cde463fc7d973f30adb0df7cab4462a0db6cc6af6deef50a'),(4,'author1','author1@author1.com','scrypt:32768:8:1$HU6Sm8R3VidT33ek$5d699a367b7d06f3155379be91e62ab674ca8fe647db5b30181197075bad8180690d2c344ef018d9f8284a9342dcf75448c005aa3eea7779b8bc0ec5b3cdd1b9'),(5,'author6','author6@author6.com','scrypt:32768:8:1$O3VC2mQOW1P609xM$d5076cd1063926a39ab75092a6ca8a489efaa3121c5ed2b002041807d295a8fd69703bd255d70b9b257407b1bc586cd26b408f2fe01eff5463cefe1d9df36cca'),(6,'author10','author10@author10.com','scrypt:32768:8:1$gQpwrobQgoj6iJNm$fcd72d2c4240874ba2650558d9cd5a590efdcc77dbf28b78b102e57e573e06cded82fc36714008107243f41cb98a8750561e6c58f64b6bd47d9f68d65dbe150c'),(7,'author14','author14@author14.com','scrypt:32768:8:1$zkgHCe3gYEdCmYg5$463436d02211bd29a99ce74d33268cf10bc6831a842a687f4d21c37209bc203fea4ce134cf30b496c8b7f6f88abc1edfea8997423da748e18c0c1b2767c3fe4a');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-12 11:05:46
