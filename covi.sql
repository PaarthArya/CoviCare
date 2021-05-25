-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: covicare
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `bed`
--

DROP TABLE IF EXISTS `bed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bed` (
  `hospital_id` int NOT NULL,
  `hospital_name` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `type_of_bed` varchar(45) DEFAULT NULL,
  `no_of_beds` int DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`hospital_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bed`
--

LOCK TABLES `bed` WRITE;
/*!40000 ALTER TABLE `bed` DISABLE KEYS */;
INSERT INTO `bed` VALUES (1001,'Jyoti Trust Hospital','Mumbai','Kondaji Chawl No 2, 3 9 400 012, VL Pednekar Marg, Bhoiwada, Parel-400014','Oxygen',40,'9967281605'),(1002,'Lok Nayak Hospital','New Delhi','metro Station Central, Jawaharlal Nehru Marg, near Delhi Gate-110002','Oxygen',38,'8046820570'),(1003,'Naidu Hospital','Pune','Behind Pune Main Railway station, off, Wellesley Rd-411001','Non-Oxygen',70,'9371333533'),(1004,'Jaipuria Hospita;','Jaipur','Near Railway Cross , Malviya Nagar , Jaipur-302017','Oxygen',45,'1412552034'),(1005,'Badar Hospital','Mumbai','339, Nawayat Mohalla,, New Eidgah Road, Nala Sopara, Maharashtra-401203','Oxygen',34,'9225807866'),(1006,'Om Hospital','Pune','Anjali Apartment, Vetalbaba Chowk, Senapati Bapat Rd, Shivajinagar-411016','Non-Oxygen',72,'9689931118'),(1007,'Mahatma Gandhi Hospital','Jaipur','RIICO Institutional Area, Tonk Rd, Sitapura, Jaipur, Rajasthan-302022','Non-Oxygen',80,'141 277 0798'),(1008,'SMS Hospital','Ahmedabad','Near Tapovan Circle, Visat - Gandhinagar Hwy, Chandkheda-382424','Oxygen',35,'75739 49408');
/*!40000 ALTER TABLE `bed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blood`
--

DROP TABLE IF EXISTS `blood`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blood` (
  `donor_id` int NOT NULL,
  `donor_name` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `blood_type` varchar(10) DEFAULT NULL,
  `recovery` datetime DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`donor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blood`
--

LOCK TABLES `blood` WRITE;
/*!40000 ALTER TABLE `blood` DISABLE KEYS */;
INSERT INTO `blood` VALUES (1009,'Manish Jain','New Delhi','O+','2021-01-15 00:00:00','9771853435'),(1010,'Khushi Jain','Mumbai','AB+','2020-11-17 00:00:00','9899744434'),(1011,'Rohan Sharma','Mumbai','O-','2021-03-04 00:00:00','9781260154'),(1012,'Yuvraj Bhatnagar','Jaipur','A+','2021-04-22 00:00:00','7439264142'),(1013,'Sneha Nagpal','New Delhi','AB-','2021-02-21 00:00:00','9958378666'),(1014,'Aadya Singhal','Ahmedabad','B+','2021-03-12 00:00:00','7995204721'),(1015,'Aashish Malhotra','Jaipur','O+','2021-04-09 00:00:00','8447700514'),(1016,'Mehak Saluja','Ahmedabad','O-','2021-05-02 00:00:00','9821275522');
/*!40000 ALTER TABLE `blood` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment` (
  `equipment_id` int NOT NULL,
  `equipment_type` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `price` double(8,2) DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`equipment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment`
--

LOCK TABLES `equipment` WRITE;
/*!40000 ALTER TABLE `equipment` DISABLE KEYS */;
INSERT INTO `equipment` VALUES (1017,'Oxygen Cans','Chandigarh',70,2200.00,'9914401328'),(1018,'Oxygen Cans','New Delhi',90,3000.00,'8595629995'),(1019,'Oxygen Cans','Chandigarh',75,2500.00,'9915140300'),(1020,'Oxygen Concentrator','Pune',32,5000.00,'9175395460'),(1021,'Oxygen Concentrator','Mumbai',30,6000.00,'982786006'),(1022,'Oxygen Concentrator','New Delhi',25,4500.00,'8527710489'),(1023,'Oxygen Cylinder','New Delhi',12,3700.00,'8800886230'),(1024,'Oxygen Cylinder','Bhopal',15,3900.00,'9893590941');
/*!40000 ALTER TABLE `equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine`
--

DROP TABLE IF EXISTS `medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicine` (
  `medicine_id` int NOT NULL,
  `medicine_name` varchar(45) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `price` decimal(7,2) DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`medicine_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine`
--

LOCK TABLES `medicine` WRITE;
/*!40000 ALTER TABLE `medicine` DISABLE KEYS */;
INSERT INTO `medicine` VALUES (1025,'Azithromycin','Gurugram','Koyal Vihar, Sector 52-122022',400,850.00,'9811455332'),(1026,'Azithromycin','Mumbai','Shripal Building Chhaya Society Siom Tromday Road Near SBI Bank Cha-400071',350,950.00,'8048861728'),(1027,'Azithromycin','New Delhi','Shri Aurobindo Marg, Safdarjung Campus, Ansari Nagar West-110029',200,900.00,'9910160011'),(1028,'Bevacizumab','Mumbai','98/779,rashmi mansion,motilal nagar no1,goregaon west-400104',250,11000.00,'8048013167'),(1029,'Bevacizumab','Jaipur','Shop No. 378, Near Dalda Factory, Durgapura, Jaipur-302018',200,10000.00,'7457182862'),(1030,'Fabiflu','New Delhi','N-9, N Block, Rampuri, Kalkaji-110019',375,1300.00,'8929871978'),(1031,'Ivermectin','Jaipur','A-212, 80 Feet Rd, Mahesh Nagar, Gopal Pura Mode-302015',250,200.00,'9829610673'),(1032,'Remdesivir','Mumbai','98/779,rashmi mansion,motilal nagar no1,goregaon west-400104',300,900.00,'8048013167');
/*!40000 ALTER TABLE `medicine` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-26  0:49:39
