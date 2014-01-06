-- MySQL dump 10.13  Distrib 5.5.32, for Win32 (x86)
--
-- Host: localhost    Database: medusa
-- ------------------------------------------------------
-- Server version	5.5.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add content type',1,'add_contenttype'),(2,'Can change content type',1,'change_contenttype'),(3,'Can delete content type',1,'delete_contenttype'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add log entry',5,'add_logentry'),(14,'Can change log entry',5,'change_logentry'),(15,'Can delete log entry',5,'delete_logentry'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add checklist',7,'add_checklist'),(20,'Can change checklist',7,'change_checklist'),(21,'Can delete checklist',7,'delete_checklist'),(22,'Can add group',8,'add_group'),(23,'Can change group',8,'change_group'),(24,'Can delete group',8,'delete_group'),(25,'Can add checklist_step',9,'add_checklist_step'),(26,'Can change checklist_step',9,'change_checklist_step'),(27,'Can delete checklist_step',9,'delete_checklist_step'),(28,'Can add step_type',10,'add_step_type'),(29,'Can change step_type',10,'change_step_type'),(30,'Can delete step_type',10,'delete_step_type'),(31,'Can add checklist',11,'add_checklist'),(32,'Can change checklist',11,'change_checklist'),(33,'Can delete checklist',11,'delete_checklist'),(34,'Can add group',12,'add_group'),(35,'Can change group',12,'change_group'),(36,'Can delete group',12,'delete_group'),(37,'Can add checklist step',13,'add_checkliststep'),(38,'Can change checklist step',13,'change_checkliststep'),(39,'Can delete checklist step',13,'delete_checkliststep'),(40,'Can add step type',14,'add_steptype'),(41,'Can change step type',14,'change_steptype'),(42,'Can delete step type',14,'delete_steptype'),(43,'Can add user',15,'add_user'),(44,'Can change user',15,'change_user'),(45,'Can delete user',15,'delete_user'),(73,'Can add log checklist',25,'add_logchecklist'),(74,'Can change log checklist',25,'change_logchecklist'),(75,'Can delete log checklist',25,'delete_logchecklist'),(76,'Can add log bool',26,'add_logbool'),(77,'Can change log bool',26,'change_logbool'),(78,'Can delete log bool',26,'delete_logbool'),(79,'Can add log double',27,'add_logdouble'),(80,'Can change log double',27,'change_logdouble'),(81,'Can delete log double',27,'delete_logdouble'),(82,'Can add log text',28,'add_logtext'),(83,'Can change log text',28,'change_logtext'),(84,'Can delete log text',28,'delete_logtext'),(94,'Can add log file',32,'add_logfile'),(95,'Can change log file',32,'change_logfile'),(96,'Can delete log file',32,'delete_logfile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$KQkeRn3nlyLI$6dsx2TQkBnB1s3luR7Xs0zg0QqG4aqKj+4iwAoGVVsw=','2013-12-23 19:06:54',1,'admin','','','raytochina@gmail.com',1,1,'2013-12-22 15:13:03'),(2,'pbkdf2_sha256$12000$Jt2fQnPj4nFY$sronR9aCtkp/dQFrBlQ4gbgOW+QNYaMnQAFmoBRUpKs=','2013-12-22 15:15:02',1,'cyrano821','Cyrano','Bergerac','raytochina@gmail.com',1,1,'2013-12-22 15:14:11');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2013-12-22 15:14:11',1,4,'2','cyrano821',1,''),(2,'2013-12-22 15:14:35',1,4,'2','cyrano821',2,'Changed first_name, last_name, email, is_staff and is_superuser.'),(3,'2013-12-22 16:08:10',2,8,'1','Group object',1,''),(4,'2013-12-22 16:08:51',2,8,'2','Group object',1,''),(5,'2013-12-22 16:08:55',2,8,'2','Group object',2,'No fields changed.'),(6,'2013-12-22 16:09:45',2,8,'4','Group object',1,''),(7,'2013-12-22 16:10:36',2,7,'1','Checklist object',1,''),(8,'2013-12-22 16:23:14',2,10,'1','bool',1,''),(9,'2013-12-22 16:23:39',2,10,'2','double',1,''),(10,'2013-12-22 16:23:42',2,10,'3','text',1,''),(11,'2013-12-22 16:23:48',2,10,'4','picture',1,''),(12,'2013-12-22 16:23:52',2,10,'5','video',1,''),(13,'2013-12-22 16:23:57',2,10,'6','audio',1,''),(14,'2013-12-23 00:06:52',2,12,'1','Phizer',1,''),(15,'2013-12-23 00:07:27',2,12,'2','Merck',1,''),(16,'2013-12-23 00:08:16',2,12,'3','AstraZeneca',1,''),(17,'2013-12-23 00:12:41',2,11,'1','Labs Shutdown',1,''),(18,'2013-12-23 00:12:43',2,11,'1','Labs Shutdown',2,'No fields changed.'),(19,'2013-12-23 00:25:25',2,14,'1','bool',1,''),(20,'2013-12-23 00:25:40',2,14,'2','text',1,''),(21,'2013-12-23 00:26:58',2,14,'3','double',1,''),(22,'2013-12-23 00:27:04',2,14,'4','text',1,''),(23,'2013-12-23 00:27:12',2,14,'5','image',1,''),(24,'2013-12-23 00:27:14',2,14,'6','video',1,''),(25,'2013-12-23 00:27:17',2,14,'7','audio',1,''),(26,'2013-12-23 00:27:32',2,11,'1','Labs Shutdown',2,'No fields changed.'),(27,'2013-12-23 00:27:41',2,11,'1','Labs Shutdown',3,''),(28,'2013-12-23 00:30:56',2,11,'2','Shutting Down Lab 37',1,''),(29,'2013-12-23 00:40:51',2,13,'6','1 Employees have vacated',1,''),(30,'2013-12-23 00:42:01',2,13,'7','2 Live fridge temperature',1,''),(31,'2013-12-23 00:42:58',2,13,'8','3 Status of Cancer Cells',1,''),(32,'2013-12-23 00:43:23',2,13,'9','4 Live Mice Video',1,''),(33,'2013-12-23 00:47:07',2,11,'3','Caging the Monkey',1,''),(34,'2013-12-23 00:47:55',2,13,'10','1 Open Monkey Cage',1,''),(35,'2013-12-23 00:50:30',2,13,'11','2 Find Monkey',1,''),(36,'2013-12-23 00:51:02',2,13,'12','3 Weigh Monkey',1,''),(37,'2013-12-23 00:51:20',2,13,'13','4 Image of Monkey',1,''),(38,'2013-12-23 06:54:18',1,11,'4','Clean wetlab - Phizer',1,''),(39,'2014-01-05 02:27:24',2,13,'13','4 Image of Monkey',3,''),(40,'2014-01-05 02:27:24',2,13,'12','3 Weigh Monkey',3,''),(41,'2014-01-05 02:27:24',2,13,'11','2 Find Monkey',3,''),(42,'2014-01-05 02:27:24',2,13,'10','1 Open Monkey Cage',3,''),(43,'2014-01-05 02:27:24',2,13,'9','4 Live Mice Video',3,''),(44,'2014-01-05 02:27:24',2,13,'8','3 Status of Cancer Cells',3,''),(45,'2014-01-05 02:27:24',2,13,'7','2 Live fridge temperature',3,''),(46,'2014-01-05 02:27:24',2,13,'6','1 Employees have vacated',3,''),(47,'2014-01-05 02:27:44',2,14,'2','text',3,''),(48,'2014-01-05 03:11:52',2,14,'1','bool',1,''),(49,'2014-01-05 03:11:56',2,14,'2','double',1,''),(50,'2014-01-05 03:11:58',2,14,'3','text',1,''),(51,'2014-01-05 03:12:01',2,14,'4','image',1,''),(52,'2014-01-05 03:12:03',2,14,'5','audio',1,''),(53,'2014-01-05 03:12:04',2,14,'6','video',1,''),(54,'2014-01-05 03:12:56',2,12,'1','Phizer',1,''),(55,'2014-01-05 03:13:31',2,12,'2','Novartis',1,''),(56,'2014-01-05 03:13:50',2,12,'3','Merck & Co',1,''),(57,'2014-01-05 03:15:30',2,11,'1','Making Miso Chicken - Phizer',1,''),(58,'2014-01-05 03:15:46',2,11,'2','Calbi Beef - Phizer',1,''),(59,'2014-01-05 03:16:33',2,13,'1','1 Get Corckpot',1,''),(60,'2014-01-05 03:16:57',2,13,'2','2 Number of Chicken',1,''),(61,'2014-01-05 03:17:19',2,13,'3','3 Describe Vegetables',1,''),(62,'2014-01-05 03:17:47',2,13,'4','4 Power plugged in',1,''),(63,'2014-01-05 03:20:33',2,15,'1','User object',1,''),(64,'2014-01-05 03:20:57',2,25,'1','Making Miso Chicken',1,''),(65,'2014-01-05 14:41:56',2,26,'1','LogBool object',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'content type','contenttypes','contenttype'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'log entry','admin','logentry'),(6,'session','sessions','session'),(7,'checklist','sop_log','checklist'),(8,'group','sop_log','group'),(9,'checklist_step','sop_log','checklist_step'),(10,'step_type','sop_log','step_type'),(11,'checklist','soplog','checklist'),(12,'group','soplog','group'),(13,'checklist step','soplog','checkliststep'),(14,'step type','soplog','steptype'),(15,'user','soplog','user'),(25,'log checklist','soplog','logchecklist'),(26,'log bool','soplog','logbool'),(27,'log double','soplog','logdouble'),(28,'log text','soplog','logtext'),(32,'log file','soplog','logfile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'soplog','0001_initial','2014-01-05 02:56:56'),(2,'soplog','0002_checklistlog','2014-01-05 03:08:12'),(3,'soplog','0003_auto_20140104_1910','2014-01-05 03:10:12'),(4,'soplog','0004_logbool','2014-01-05 03:19:13'),(5,'soplog','0005_logaudio_logdouble_logimage_logtext_logvideo','2014-01-05 03:22:42'),(6,'soplog','0006_auto_20140105_2038','2014-01-06 04:38:15'),(7,'soplog','0007_auto_20140105_2042','2014-01-06 04:42:31'),(8,'soplog','0008_remove_logfile_value','2014-01-06 23:11:06');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('av800rwiy6m6dj65kotr6n9rjgispuas','ZTFlYmU2ZWRlMDQxZDJjMGRlNWJlOGQ0NDc5NzYzYjc2MDY1OTlhMzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-01-05 15:15:02'),('hj4vb8ywhja0p1lezh7f6pos30jqnoqw','ZTk3YjA1NjQ4ZTlmZGRiOGQ4NmNiM2MxNGY4NGMxMmY0OWE1ZmNkZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==','2014-01-06 19:06:54'),('mik9c5c4x51rj0e98cnvzskd00jlaony','ZTk3YjA1NjQ4ZTlmZGRiOGQ4NmNiM2MxNGY4NGMxMmY0OWE1ZmNkZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==','2014-01-06 02:35:48');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soplog_checklist`
--

DROP TABLE IF EXISTS `soplog_checklist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soplog_checklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_checklist_0e939a4f` (`group_id`),
  CONSTRAINT `soplog_checklist_group_id_52e8723b_fk_soplog_group_id` FOREIGN KEY (`group_id`) REFERENCES `soplog_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_checklist`
--

LOCK TABLES `soplog_checklist` WRITE;
/*!40000 ALTER TABLE `soplog_checklist` DISABLE KEYS */;
INSERT INTO `soplog_checklist` VALUES (1,'Making Miso Chicken','Miso Chicken',1),(2,'Calbi Beef','Calbi',1);
/*!40000 ALTER TABLE `soplog_checklist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soplog_checkliststep`
--

DROP TABLE IF EXISTS `soplog_checkliststep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soplog_checkliststep` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `stepNumber` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `checklist_id` int(11) NOT NULL,
  `stepType_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_checkliststep_690b1cb8` (`checklist_id`),
  KEY `soplog_checkliststep_ce53d143` (`stepType_id`),
  CONSTRAINT `soplog_checkliststep_stepType_id_1172326b_fk_soplog_steptype_id` FOREIGN KEY (`stepType_id`) REFERENCES `soplog_steptype` (`id`),
  CONSTRAINT `soplog_checklistst_checklist_id_7b84a1b8_fk_soplog_checklist_id` FOREIGN KEY (`checklist_id`) REFERENCES `soplog_checklist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_checkliststep`
--

LOCK TABLES `soplog_checkliststep` WRITE;
/*!40000 ALTER TABLE `soplog_checkliststep` DISABLE KEYS */;
INSERT INTO `soplog_checkliststep` VALUES (1,'Get Corckpot',1,'get crockpot',1,1),(2,'Number of Chicken',2,'Count chicken',1,2),(3,'Describe Vegetables',3,'Describing vegetables',1,3),(4,'Power plugged in',4,'PowerPlugged In',1,1);
/*!40000 ALTER TABLE `soplog_checkliststep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soplog_group`
--

DROP TABLE IF EXISTS `soplog_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soplog_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_group`
--

LOCK TABLES `soplog_group` WRITE;
/*!40000 ALTER TABLE `soplog_group` DISABLE KEYS */;
INSERT INTO `soplog_group` VALUES (1,'Phizer','is an American multinational pharmaceutical corporation headquartered in New York City,[2] and with its research headquarters in Groton, Connecticut, United States. It is one of the world\'s largest pharmaceutical companies by revenues.[3]\r\n\r\nPfizer develops and produces medicines and vaccines for a wide range of conditions including in the areas of immunology and inflammation, oncology, cardiovascular and metabolic diseases, neuroscience and pain. Pfizer\'s products include Lipitor (atorvastatin, used to lower LDL blood cholesterol); Lyrica (pregabalin, for neuropathic pain/fibromyalgia); Diflucan (fluconazole, an oral antifungal medication); Zithromax (azithromycin, an antibiotic); Viagra (sildenafil, for erectile dysfunction); and Celebrex/Celebra (celecoxib, an anti-inflammatory drug).\r\n\r\nPfizer was founded by cousins Charles Pfizer and Charles Erhart in New York City in 1849 as a manufacturer of fine chemicals. Pfizer\'s discovery of Terramycin (oxytetracycline) in 1950 put it on a path towards becoming a research-based pharmaceutical company. Pfizer has made numerous acquisitions, including of Warner–Lambert in 2000, Pharmacia in 2003 and Wyeth in 2009, the latter acquired for US$68 billion.[4][5] Pfizer is listed on the New York Stock Exchange and its shares have been a component of the Dow Jones Industrial Average since April 8, 2004.[6]\r\n\r\nIn September 2009, Pfizer pleaded guilty to the illegal marketing of the arthritis drug Bextra for uses unapproved by the U.S. Food and Drug Administration (FDA), and agreed to a $2.3 billion settlement, the largest health care fraud settlement at that time.[7] Pfizer also paid the U.S. government $1.3 billion in criminal fines related to the \"off-label\" marketing of Bextra, the largest penalty ever rendered for any crime.[8] Called a repeat offender, this was Pfizer\'s fourth such settlement with the U.S. Department of Justice in the previous ten years.['),(2,'Novartis',' is a Swiss multinational pharmaceutical company based in Basel, Switzerland, ranking number two in sales (46.806 billion US$) among the world-wide industry in 2010.[2]\r\n\r\nNovartis manufactures such drugs as clozapine (Clozaril), diclofenac (Voltaren), carbamazepine (Tegretol), valsartan (Diovan) and imatinib mesylate (Gleevec/Glivec). Additional agents include cyclosporin (Neoral/Sandimmun), letrozole (Femara), methylphenidate (Ritalin), terbinafine (Lamisil), and others.\r\n\r\nIn 1996 Ciba-Geigy merged with Sandoz, with the pharmaceutical and agrochemical divisions of both staying together to form Novartis. Other Ciba-Geigy and Sandoz businesses were sold off, or, like Ciba Specialty Chemicals, were spun off as independent companies. The Sandoz brand disappeared for 3 years, but was revived in 2003 when Novartis consolidated its generic drugs businesses into a single subsidiary and named it Sandoz. Novartis divested its agrochemical and genetically modified crops business in 2000 with the spinout of Syngenta, in partnership with AstraZeneca which also divested its agrochemical business.\r\n\r\nNovartis is a full member of the European Federation of Pharmaceutical Industries and Associations (EFPIA)[3] the International Federation of Pharmaceutical Manufacturers and Associations (IFPMA),[4] and t'),(3,'Merck & Co','Merck Sharp & Dohme, MSD outside the United States and Canada, is an American pharmaceutical company and is one of the largest pharmaceutical companies in the world. Merck headquarters is currently located in Whitehouse Station, New Jersey, though in 2013 the company announced it would be relocating to Kenilworth, New Jersey by 2015.[2] The company was established in 1891 as the United States subsidiary of the German company now known as Merck KGaA. Merck & Co. was confiscated by the US government during World War I and subsequently established as an independent American company. It is currently one of the world\'s seven largest pharmaceutical companies by market capitalization and revenue.\r\n\r\nMerck also publishes The Merck Manuals, a series of medical reference books for physicians, nurses, and technicians. These include the Merck Manual of Diagnosis and Therapy, the world\'s best-selling medical textbook, and the Merck Index, a compendium of chemical compounds.\r\n\r\nIn 2012 the company received the \"Facility of the Year\"-Category Winner for Facility Integration Award for the Vaccine Bulk Manufacturing Facility (VBF) Program of Projects in Durham, North Carolina, USA');
/*!40000 ALTER TABLE `soplog_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soplog_logbool`
--

DROP TABLE IF EXISTS `soplog_logbool`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soplog_logbool` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `checklistLog_id` int(11) NOT NULL,
  `value` tinyint(1) NOT NULL,
  `modifyTime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_logbool_94caf5ad` (`checklistLog_id`),
  CONSTRAINT `soplog_logboo_checklistLog_id_489bac3_fk_soplog_logchecklist_id` FOREIGN KEY (`checklistLog_id`) REFERENCES `soplog_logchecklist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_logbool`
--

LOCK TABLES `soplog_logbool` WRITE;
/*!40000 ALTER TABLE `soplog_logbool` DISABLE KEYS */;
INSERT INTO `soplog_logbool` VALUES (1,1,1,'2014-01-05 14:41:54');
/*!40000 ALTER TABLE `soplog_logbool` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soplog_logchecklist`
--

DROP TABLE IF EXISTS `soplog_logchecklist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soplog_logchecklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `checklist_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `startTime` datetime NOT NULL,
  `modifyTime` datetime NOT NULL,
  `endtime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_logchecklist_690b1cb8` (`checklist_id`),
  KEY `soplog_logchecklist_e8701ad4` (`user_id`),
  CONSTRAINT `soplog_logchecklist_user_id_5b2e0bff_fk_soplog_user_id` FOREIGN KEY (`user_id`) REFERENCES `soplog_user` (`id`),
  CONSTRAINT `soplog_logchecklis_checklist_id_4e5240b1_fk_soplog_checklist_id` FOREIGN KEY (`checklist_id`) REFERENCES `soplog_checklist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_logchecklist`
--

LOCK TABLES `soplog_logchecklist` WRITE;
/*!40000 ALTER TABLE `soplog_logchecklist` DISABLE KEYS */;
INSERT INTO `soplog_logchecklist` VALUES (1,1,1,'2014-01-05 03:20:48','2014-01-05 03:20:50','2014-01-05 03:20:55');
/*!40000 ALTER TABLE `soplog_logchecklist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soplog_logdouble`
--

DROP TABLE IF EXISTS `soplog_logdouble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soplog_logdouble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `checklistLog_id` int(11) NOT NULL,
  `value` double NOT NULL,
  `modifyTime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_logdouble_94caf5ad` (`checklistLog_id`),
  CONSTRAINT `soplog_logdo_checklistLog_id_73c7e678_fk_soplog_logchecklist_id` FOREIGN KEY (`checklistLog_id`) REFERENCES `soplog_logchecklist` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_logdouble`
--

LOCK TABLES `soplog_logdouble` WRITE;
/*!40000 ALTER TABLE `soplog_logdouble` DISABLE KEYS */;
/*!40000 ALTER TABLE `soplog_logdouble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soplog_logfile`
--

DROP TABLE IF EXISTS `soplog_logfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soplog_logfile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `checklistLog_id` int(11) NOT NULL,
  `modifyTime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_logfile_94caf5ad` (`checklistLog_id`),
  CONSTRAINT `soplog_logfi_checklistLog_id_4140df11_fk_soplog_logchecklist_id` FOREIGN KEY (`checklistLog_id`) REFERENCES `soplog_logchecklist` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_logfile`
--

LOCK TABLES `soplog_logfile` WRITE;
/*!40000 ALTER TABLE `soplog_logfile` DISABLE KEYS */;
/*!40000 ALTER TABLE `soplog_logfile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soplog_logtext`
--

DROP TABLE IF EXISTS `soplog_logtext`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soplog_logtext` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `checklistLog_id` int(11) NOT NULL,
  `value` longtext NOT NULL,
  `modifyTime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_logtext_94caf5ad` (`checklistLog_id`),
  CONSTRAINT `soplog_logtex_checklistLog_id_9ed85d4_fk_soplog_logchecklist_id` FOREIGN KEY (`checklistLog_id`) REFERENCES `soplog_logchecklist` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_logtext`
--

LOCK TABLES `soplog_logtext` WRITE;
/*!40000 ALTER TABLE `soplog_logtext` DISABLE KEYS */;
/*!40000 ALTER TABLE `soplog_logtext` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soplog_steptype`
--

DROP TABLE IF EXISTS `soplog_steptype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soplog_steptype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_steptype`
--

LOCK TABLES `soplog_steptype` WRITE;
/*!40000 ALTER TABLE `soplog_steptype` DISABLE KEYS */;
INSERT INTO `soplog_steptype` VALUES (1,'bool'),(2,'double'),(3,'text'),(4,'image'),(5,'audio'),(6,'video');
/*!40000 ALTER TABLE `soplog_steptype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soplog_user`
--

DROP TABLE IF EXISTS `soplog_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soplog_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `phone` int(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_user`
--

LOCK TABLES `soplog_user` WRITE;
/*!40000 ALTER TABLE `soplog_user` DISABLE KEYS */;
INSERT INTO `soplog_user` VALUES (1,'Default',12345,'test@ya.com');
/*!40000 ALTER TABLE `soplog_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-01-06 15:12:24
