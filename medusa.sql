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
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add content type',1,'add_contenttype'),(2,'Can change content type',1,'change_contenttype'),(3,'Can delete content type',1,'delete_contenttype'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add log entry',5,'add_logentry'),(14,'Can change log entry',5,'change_logentry'),(15,'Can delete log entry',5,'delete_logentry'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user',7,'add_user'),(20,'Can change user',7,'change_user'),(21,'Can delete user',7,'delete_user'),(22,'Can add group',8,'add_group'),(23,'Can change group',8,'change_group'),(24,'Can delete group',8,'delete_group'),(25,'Can add checklist',9,'add_checklist'),(26,'Can change checklist',9,'change_checklist'),(27,'Can delete checklist',9,'delete_checklist'),(28,'Can add checklist step',10,'add_checkliststep'),(29,'Can change checklist step',10,'change_checkliststep'),(30,'Can delete checklist step',10,'delete_checkliststep'),(31,'Can add step type',11,'add_steptype'),(32,'Can change step type',11,'change_steptype'),(33,'Can delete step type',11,'delete_steptype'),(34,'Can add log checklist',12,'add_logchecklist'),(35,'Can change log checklist',12,'change_logchecklist'),(36,'Can delete log checklist',12,'delete_logchecklist'),(37,'Can add log bool',13,'add_logbool'),(38,'Can change log bool',13,'change_logbool'),(39,'Can delete log bool',13,'delete_logbool'),(40,'Can add log double',14,'add_logdouble'),(41,'Can change log double',14,'change_logdouble'),(42,'Can delete log double',14,'delete_logdouble'),(43,'Can add log text',15,'add_logtext'),(44,'Can change log text',15,'change_logtext'),(45,'Can delete log text',15,'delete_logtext'),(46,'Can add log file',16,'add_logfile'),(47,'Can change log file',16,'change_logfile'),(48,'Can delete log file',16,'delete_logfile');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$hdKv1ckJKj3f$5f+EP5WY4zTd1fyLuHnp25Tb38bc648K6LfesdSwHVE=','2014-01-07 09:52:43',1,'cyrano821','','','',1,1,'2014-01-07 09:51:46');
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-01-08 18:24:23',1,7,'1','Default',1,''),(2,'2014-01-08 18:24:37',1,11,'1','bool',1,''),(3,'2014-01-08 18:24:48',1,11,'2','double',1,''),(4,'2014-01-08 18:24:54',1,11,'3','text',1,''),(5,'2014-01-08 18:25:29',1,11,'4','file',1,''),(6,'2014-01-08 18:26:21',1,8,'1','Phizer',1,''),(7,'2014-01-08 18:26:31',1,8,'2','merck',1,''),(8,'2014-01-08 18:26:44',1,8,'3','other pharmasuitical',1,''),(9,'2014-01-08 18:35:22',1,9,'1','1-Lab Chemicals - Phizer',1,''),(10,'2014-01-08 18:37:12',1,10,'1','1 Wear appropriate protective equipment-id:1',1,''),(11,'2014-01-08 18:39:57',1,10,'2','2 Gloves-id:2',1,''),(12,'2014-01-08 18:40:36',1,10,'3','3 first aid kit-id:3',1,''),(13,'2014-01-08 18:40:54',1,10,'4','4 telephone emergency-id:4',1,''),(14,'2014-01-08 18:41:48',1,10,'5','5 Fire alarm manual pull station-id:5',1,''),(15,'2014-01-08 18:46:15',1,12,'1','Lab Chemicals',1,''),(16,'2014-01-08 18:46:41',1,13,'1','LogBool object',1,''),(17,'2014-01-08 18:46:51',1,13,'2','LogBool object',1,''),(18,'2014-01-08 18:51:55',1,15,'1','LogText object',1,''),(19,'2014-01-08 19:22:48',1,12,'2','Lab Chemicals',1,'');
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'content type','contenttypes','contenttype'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'log entry','admin','logentry'),(6,'session','sessions','session'),(7,'user','soplog','user'),(8,'group','soplog','group'),(9,'checklist','soplog','checklist'),(10,'checklist step','soplog','checkliststep'),(11,'step type','soplog','steptype'),(12,'log checklist','soplog','logchecklist'),(13,'log bool','soplog','logbool'),(14,'log double','soplog','logdouble'),(15,'log text','soplog','logtext'),(16,'log file','soplog','logfile');
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'soplog','0001_initial','2014-01-07 09:51:19'),(2,'soplog','0002_checklistlog','2014-01-07 09:51:19'),(3,'soplog','0003_auto_20140104_1910','2014-01-07 09:51:20'),(4,'soplog','0004_logbool','2014-01-07 09:51:21'),(5,'soplog','0005_logaudio_logdouble_logimage_logtext_logvideo','2014-01-07 09:51:23'),(6,'soplog','0006_auto_20140105_2038','2014-01-07 09:51:24'),(7,'soplog','0007_auto_20140105_2042','2014-01-07 09:51:25'),(8,'soplog','0008_remove_logfile_value','2014-01-07 09:51:26'),(9,'soplog','0009_auto_20140106_1737','2014-01-07 09:51:26'),(10,'soplog','0010_auto_20140106_1739','2014-01-07 09:51:28'),(11,'soplog','0011_auto_20140106_1800','2014-01-07 09:51:28'),(12,'soplog','0012_logbool_step','2014-01-08 18:43:20'),(13,'soplog','0013_auto_20140108_1044','2014-01-08 18:44:21');
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
INSERT INTO `django_session` VALUES ('ca5acysm05f6w7rw0fjx9ymxfnr8qcr8','ZGFkN2I0Njk5YWYwZjk1ODFhOWY4ZTU1ZmZjMmU5OTk1N2Y4N2I2OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-01-21 09:52:43');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_checklist`
--

LOCK TABLES `soplog_checklist` WRITE;
/*!40000 ALTER TABLE `soplog_checklist` DISABLE KEYS */;
INSERT INTO `soplog_checklist` VALUES (1,'Lab Chemicals','Lab Chems',1);
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
  `order` int(11) DEFAULT NULL,
  `description` longtext NOT NULL,
  `checklist_id` int(11) NOT NULL,
  `stepType_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_checkliststep_690b1cb8` (`checklist_id`),
  KEY `soplog_checkliststep_ce53d143` (`stepType_id`),
  CONSTRAINT `soplog_checkliststep_stepType_id_1172326b_fk_soplog_steptype_id` FOREIGN KEY (`stepType_id`) REFERENCES `soplog_steptype` (`id`),
  CONSTRAINT `soplog_checklistst_checklist_id_7b84a1b8_fk_soplog_checklist_id` FOREIGN KEY (`checklist_id`) REFERENCES `soplog_checklist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_checkliststep`
--

LOCK TABLES `soplog_checkliststep` WRITE;
/*!40000 ALTER TABLE `soplog_checkliststep` DISABLE KEYS */;
INSERT INTO `soplog_checkliststep` VALUES (1,'Wear appropriate protective equipment',1,'Wearing protective items',1,1),(2,'Gloves',2,'Gloves on?',1,1),(3,'first aid kit',3,'Location of first aid kit',1,3),(4,'telephone emergency',4,'telephone',1,2),(5,'Fire alarm manual pull station',5,'location of fire alarm',1,3);
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
INSERT INTO `soplog_group` VALUES (1,'Phizer','This is a description about phizer'),(2,'merck','this is a description about merk'),(3,'other pharmasuitical','Other pharmasuitcal Description');
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
  `step_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_logbool_94caf5ad` (`checklistLog_id`),
  KEY `soplog_logbool_bef491d2` (`step_id`),
  CONSTRAINT `step_id_refs_id_7e23f3ff` FOREIGN KEY (`step_id`) REFERENCES `soplog_checkliststep` (`id`),
  CONSTRAINT `soplog_logboo_checklistLog_id_489bac3_fk_soplog_logchecklist_id` FOREIGN KEY (`checklistLog_id`) REFERENCES `soplog_logchecklist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_logbool`
--

LOCK TABLES `soplog_logbool` WRITE;
/*!40000 ALTER TABLE `soplog_logbool` DISABLE KEYS */;
INSERT INTO `soplog_logbool` VALUES (1,1,1,'2014-01-08 18:46:39',1),(2,1,1,'2014-01-08 18:46:49',2);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_logchecklist`
--

LOCK TABLES `soplog_logchecklist` WRITE;
/*!40000 ALTER TABLE `soplog_logchecklist` DISABLE KEYS */;
INSERT INTO `soplog_logchecklist` VALUES (1,1,1,'2014-01-08 18:46:09','2014-01-08 18:46:11','2014-01-08 18:46:13'),(2,1,1,'2014-01-08 19:22:43','2014-01-08 19:22:45','2014-01-08 19:22:47');
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
  `step_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_logdouble_94caf5ad` (`checklistLog_id`),
  KEY `soplog_logdouble_bef491d2` (`step_id`),
  CONSTRAINT `step_id_refs_id_4c096f12` FOREIGN KEY (`step_id`) REFERENCES `soplog_checkliststep` (`id`),
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
  `step_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_logfile_94caf5ad` (`checklistLog_id`),
  KEY `soplog_logfile_bef491d2` (`step_id`),
  CONSTRAINT `step_id_refs_id_520f44d` FOREIGN KEY (`step_id`) REFERENCES `soplog_checkliststep` (`id`),
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
  `step_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `soplog_logtext_94caf5ad` (`checklistLog_id`),
  KEY `soplog_logtext_bef491d2` (`step_id`),
  CONSTRAINT `step_id_refs_id_58aa604a` FOREIGN KEY (`step_id`) REFERENCES `soplog_checkliststep` (`id`),
  CONSTRAINT `soplog_logtex_checklistLog_id_9ed85d4_fk_soplog_logchecklist_id` FOREIGN KEY (`checklistLog_id`) REFERENCES `soplog_logchecklist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_logtext`
--

LOCK TABLES `soplog_logtext` WRITE;
/*!40000 ALTER TABLE `soplog_logtext` DISABLE KEYS */;
INSERT INTO `soplog_logtext` VALUES (1,1,'By the exit door 4 ft higher than normal','2014-01-08 18:51:53',3);
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soplog_steptype`
--

LOCK TABLES `soplog_steptype` WRITE;
/*!40000 ALTER TABLE `soplog_steptype` DISABLE KEYS */;
INSERT INTO `soplog_steptype` VALUES (1,'bool'),(2,'double'),(3,'text'),(4,'file');
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
INSERT INTO `soplog_user` VALUES (1,'Default',9494,'65+64');
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

-- Dump completed on 2014-01-08 11:25:23
