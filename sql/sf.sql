-- MySQL dump 10.13  Distrib 5.1.66, for apple-darwin11.4.0 (i386)
--
-- Host: localhost    Database: sf
-- ------------------------------------------------------
-- Server version	5.1.66

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
-- Table structure for table `account_facebooksession`
--

DROP TABLE IF EXISTS `account_facebooksession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_facebooksession` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `access_token` varchar(103) NOT NULL,
  `expires` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `uid` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `access_token` (`access_token`),
  UNIQUE KEY `uid` (`uid`),
  UNIQUE KEY `user_id` (`user_id`,`uid`),
  UNIQUE KEY `access_token_2` (`access_token`,`expires`),
  KEY `account_facebooksession_fbfc09f1` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_facebooksession`
--

LOCK TABLES `account_facebooksession` WRITE;
/*!40000 ALTER TABLE `account_facebooksession` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_facebooksession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_mailingaddress`
--

DROP TABLE IF EXISTS `account_mailingaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_mailingaddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `address` varchar(200) NOT NULL,
  `address_2` varchar(200) DEFAULT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zip` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_mailingaddress_fbfc09f1` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_mailingaddress`
--

LOCK TABLES `account_mailingaddress` WRITE;
/*!40000 ALTER TABLE `account_mailingaddress` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_mailingaddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_userprofile`
--

DROP TABLE IF EXISTS `account_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `acct_type` varchar(50) DEFAULT NULL,
  `region` varchar(200) DEFAULT NULL,
  `about_me` longtext NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `use_gravatar` tinyint(1) NOT NULL,
  `birthday` date DEFAULT NULL,
  `date_founded` date DEFAULT NULL,
  `occupation` varchar(200) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `profile_type` varchar(20) DEFAULT NULL,
  `facebook_uid` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_userprofile`
--

LOCK TABLES `account_userprofile` WRITE;
/*!40000 ALTER TABLE `account_userprofile` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
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
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
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
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add migration history',8,'add_migrationhistory'),(23,'Can change migration history',8,'change_migrationhistory'),(24,'Can delete migration history',8,'delete_migrationhistory'),(25,'Can add contact',9,'add_contact'),(26,'Can change contact',9,'change_contact'),(27,'Can delete contact',9,'delete_contact'),(28,'Can add contact category',10,'add_contactcategory'),(29,'Can change contact category',10,'change_contactcategory'),(30,'Can delete contact category',10,'delete_contactcategory'),(31,'Can add user profile',11,'add_userprofile'),(32,'Can change user profile',11,'change_userprofile'),(33,'Can delete user profile',11,'delete_userprofile'),(34,'Can add facebook session',12,'add_facebooksession'),(35,'Can change facebook session',12,'change_facebooksession'),(36,'Can delete facebook session',12,'delete_facebooksession'),(37,'Can add mailing address',13,'add_mailingaddress'),(38,'Can change mailing address',13,'change_mailingaddress'),(39,'Can delete mailing address',13,'delete_mailingaddress'),(40,'Can add user social auth',14,'add_usersocialauth'),(41,'Can change user social auth',14,'change_usersocialauth'),(42,'Can delete user social auth',14,'delete_usersocialauth'),(43,'Can add nonce',15,'add_nonce'),(44,'Can change nonce',15,'change_nonce'),(45,'Can delete nonce',15,'delete_nonce'),(46,'Can add association',16,'add_association'),(47,'Can change association',16,'change_association'),(48,'Can delete association',16,'delete_association'),(49,'Can add static page',17,'add_staticpage'),(50,'Can change static page',17,'change_staticpage'),(51,'Can delete static page',17,'delete_staticpage'),(52,'Can add static content',18,'add_staticcontent'),(53,'Can change static content',18,'change_staticcontent'),(54,'Can delete static content',18,'delete_staticcontent'),(55,'Can add link',19,'add_link'),(56,'Can change link',19,'change_link'),(57,'Can delete link',19,'delete_link'),(58,'Can add tag',20,'add_tag'),(59,'Can change tag',20,'change_tag'),(60,'Can delete tag',20,'delete_tag'),(61,'Can add tagged item',21,'add_taggeditem'),(62,'Can change tagged item',21,'change_taggeditem'),(63,'Can delete tagged item',21,'delete_taggeditem');
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
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'admin','John','Chase','johnc@simpleunion.com','pbkdf2_sha256$10000$Zcn9R412ZYhv$euutLqsuVbb56XuUtEND658r6fQM3YrktaGI1SSIgrQ=',1,1,1,'2013-04-29 06:58:46','2013-04-26 00:21:19');
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
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
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
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_form_contact`
--

DROP TABLE IF EXISTS `contact_form_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact_form_contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(75) NOT NULL,
  `message` longtext NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_form_contact`
--

LOCK TABLES `contact_form_contact` WRITE;
/*!40000 ALTER TABLE `contact_form_contact` DISABLE KEYS */;
INSERT INTO `contact_form_contact` VALUES (1,'sdf','dat@vastbit.com','sd','2013-04-26 03:40:22'),(2,'sdf','dat@vastbit.com','sd','2013-04-26 03:42:54'),(3,'sdfsd','dat@vastbit.com','sdfsdf','2013-04-26 03:43:25'),(4,'sdfsd','ben@simpleunion.com','sdfsd','2013-04-26 03:45:19'),(5,'sdfsd','ben@simpleunion.com','sdfds','2013-04-26 03:47:19'),(6,'sdfds','thanh.nguyenvan@gmail.com','sdf','2013-04-26 03:49:52'),(7,'sdf','thanh.nguyenvan@gmail.com','sdf','2013-04-26 03:50:20');
/*!40000 ALTER TABLE `contact_form_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_form_contactcategory`
--

DROP TABLE IF EXISTS `contact_form_contactcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact_form_contactcategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `contact_page_content` longtext,
  `send_reply` tinyint(1) NOT NULL,
  `reply_subject` varchar(200) DEFAULT NULL,
  `reply_body` longtext,
  `recipients` varchar(200) NOT NULL,
  `msg_subject` varchar(200) NOT NULL,
  `msg_body` longtext,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_form_contactcategory`
--

LOCK TABLES `contact_form_contactcategory` WRITE;
/*!40000 ALTER TABLE `contact_form_contactcategory` DISABLE KEYS */;
INSERT INTO `contact_form_contactcategory` VALUES (1,'Contact',1,'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',1,'TBU','TBU','johnc@simpleunion.com, ben@simpleunion.com','TBU','TBU','2013-04-26 03:42:48');
/*!40000 ALTER TABLE `contact_form_contactcategory` ENABLE KEYS */;
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
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2013-04-26 03:42:48',1,10,'1','ContactCategory object',1,''),(2,'2013-04-26 03:43:17',1,10,'1','ContactCategory object',2,'Changed contact_page_content.'),(3,'2013-04-26 11:24:08',1,3,'4','thanh+test1@vastbit.com',3,''),(4,'2013-04-26 11:24:08',1,3,'5','thanh+test2@vastbit.com',3,''),(5,'2013-04-26 11:24:08',1,3,'3','thanh+test@vastbit.com',3,''),(6,'2013-04-26 11:24:08',1,3,'2','thanh@vastbit.com',3,''),(7,'2013-04-29 00:01:19',1,17,'1','FAQ',1,''),(8,'2013-04-29 00:03:15',1,18,'1','StaticContent object',1,''),(9,'2013-04-29 00:05:21',1,18,'1','StaticContent object',2,'Changed content.'),(10,'2013-04-29 01:05:31',1,17,'2','About',1,''),(11,'2013-04-29 01:07:15',1,17,'2','About',2,'Changed content for static content \"StaticContent object\".'),(12,'2013-04-29 01:28:57',1,17,'3','Term of Use',1,''),(13,'2013-04-29 01:57:59',1,17,'4','Privacy',1,''),(14,'2013-04-29 01:58:25',1,17,'2','About',2,'Changed url. Changed content for static content \"StaticContent object\".'),(15,'2013-04-29 06:45:59',1,3,'1','admin',2,'Changed password, first_name and last_name.'),(16,'2013-04-29 06:59:16',1,11,'1','thanh nguyen - thanh.nguyenvan@gmail.com',3,''),(17,'2013-04-29 06:59:25',1,3,'6','thanh.nguyenvan@gmail.com',3,''),(18,'2013-04-29 06:59:37',1,3,'1','admin',2,'Changed password, first_name and last_name.');
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
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'migration history','south','migrationhistory'),(9,'contact','contact_form','contact'),(10,'contact category','contact_form','contactcategory'),(11,'user profile','account','userprofile'),(12,'facebook session','account','facebooksession'),(13,'mailing address','account','mailingaddress'),(14,'user social auth','social_auth','usersocialauth'),(15,'nonce','social_auth','nonce'),(16,'association','social_auth','association'),(17,'static page','static_page','staticpage'),(18,'static content','static_page','staticcontent'),(19,'link','static_page','link'),(20,'tag','tagging','tag'),(21,'tagged item','tagging','taggeditem');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
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
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('e5f068cb071baa07d6a37adb9fc6e49f','NDkwYjdiYjFkM2RlODMzNGMwMjU3MmIzMzViNTRiYzFmMDVhZWU0ZTqAAn1xAShVDmZhY2Vib29r\nX3N0YXRlVSAxVktyREFscjFQNENSdDhMRk56ZnRIaXRmekk5N1FZMVUSX2F1dGhfdXNlcl9iYWNr\nZW5kcQJVKWRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kcQNVDV9hdXRo\nX3VzZXJfaWRxBIoBAXUu\n','2013-05-10 11:22:30'),('0b98bc1a618ebe23f32b7da9c057969b','ZTFhNWMxY2E4MGYxYTU4MmZlOTNhZjYxYjNmODVjNWViOTI4NjkwMDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2013-05-10 02:18:39'),('64d4adcb407a37440eb750d642ec3940','NjY2MjI4M2M4YjFhMTQ0MmIwOTI0OWZhMTQ4YmY0NzBlYzQ2ODNmYzqAAn1xAVUKdGVzdGNvb2tp\nZVUGd29ya2VkcQJzLg==\n','2013-05-10 11:55:53'),('a0a3c41b811ea5204ac320a641dba63d','ZTFhNWMxY2E4MGYxYTU4MmZlOTNhZjYxYjNmODVjNWViOTI4NjkwMDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2013-05-13 06:58:46');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_association`
--

DROP TABLE IF EXISTS `social_auth_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_association` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_url` varchar(135) NOT NULL,
  `handle` varchar(125) NOT NULL,
  `secret` varchar(255) NOT NULL,
  `issued` int(11) NOT NULL,
  `lifetime` int(11) NOT NULL,
  `assoc_type` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_association_handle_693a924207fa6ae_uniq` (`handle`,`server_url`),
  KEY `social_auth_association_5a32b972` (`issued`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_association`
--

LOCK TABLES `social_auth_association` WRITE;
/*!40000 ALTER TABLE `social_auth_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_nonce`
--

DROP TABLE IF EXISTS `social_auth_nonce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_nonce` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_url` varchar(200) NOT NULL,
  `timestamp` int(11) NOT NULL,
  `salt` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_nonce_timestamp_3833ba21ef52524a_uniq` (`timestamp`,`salt`,`server_url`),
  KEY `social_auth_nonce_67f1b7ce` (`timestamp`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_nonce`
--

LOCK TABLES `social_auth_nonce` WRITE;
/*!40000 ALTER TABLE `social_auth_nonce` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_nonce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_usersocialauth`
--

DROP TABLE IF EXISTS `social_auth_usersocialauth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_usersocialauth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `provider` varchar(32) NOT NULL,
  `uid` varchar(222) NOT NULL,
  `extra_data` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_usersocialauth_provider_2f763109e2c4a1fb_uniq` (`provider`,`uid`),
  KEY `social_auth_usersocialauth_fbfc09f1` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_usersocialauth`
--

LOCK TABLES `social_auth_usersocialauth` WRITE;
/*!40000 ALTER TABLE `social_auth_usersocialauth` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_usersocialauth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'account','0001_initial','2013-04-26 00:21:27'),(2,'account','0002_auto__add_field_userprofile_phone__add_field_userprofile_profile_type_','2013-04-26 00:21:27'),(3,'account','0003_auto__add_mailingaddress','2013-04-26 00:21:28'),(4,'social_auth','0001_initial','2013-04-26 00:21:28'),(5,'social_auth','0002_auto__add_unique_nonce_timestamp_salt_server_url__add_unique_associati','2013-04-26 00:21:28');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `static_page_link`
--

DROP TABLE IF EXISTS `static_page_link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `static_page_link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `static_page_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `static_page_link_309ee035` (`static_page_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `static_page_link`
--

LOCK TABLES `static_page_link` WRITE;
/*!40000 ALTER TABLE `static_page_link` DISABLE KEYS */;
/*!40000 ALTER TABLE `static_page_link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `static_page_staticcontent`
--

DROP TABLE IF EXISTS `static_page_staticcontent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `static_page_staticcontent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `language` varchar(10) NOT NULL,
  `static_page_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `static_page_staticcontent_309ee035` (`static_page_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `static_page_staticcontent`
--

LOCK TABLES `static_page_staticcontent` WRITE;
/*!40000 ALTER TABLE `static_page_staticcontent` DISABLE KEYS */;
INSERT INTO `static_page_staticcontent` VALUES (1,'FAQ','<div class=\"about-page-header hidden-phone hidden-tablet\">\r\n            \r\n             	\r\n	                <div class=\"transparent span1 general-page-header hidden-phone\">\r\n                    	<span class=\"red\">faq</span>\r\n                       \r\n                    </div><!--/transparent-->\r\n             \r\n        </div>\r\n\r\n<div class=\"container white-background general-hero\">\r\n	<div class=\"span11 general-margin-left\">\r\n		<h3 class=\"page-title\">\r\n			faq</h3>\r\n		<h4>\r\n			What is famdates?</h4>\r\n		<p>\r\n			- Thefamdates is the ultimate portal connecting sports, fitness, and nutrition enthusiasts globally, allowing for an interactive and informational forum encompassing their common interests and passions.</p>\r\n		<h4>\r\n			What is FanZone?</h4>\r\n		<p>\r\n			- Fan Zone is the feed on the site where sports fans all across the world come together to talk sports, connect with other fans online or at local events and pubs. Fan Zone will also, give you live score updates for all your favorite teams.</p>\r\n		<h4>\r\n			What is Fitness and Nutrition?</h4>\r\n		<p>\r\n			- Fitness &amp; Nutrition is the feed on the site where users can come together to discuss workouts, post workout tips and videos, discuss supplements and nutrition, find trainers, gyms, nutritionists all in your local area, or world wide.</p>\r\n		<h4>\r\n			What is Game Time?</h4>\r\n		<p>\r\n			- Game Time is the feed on the site where active people can find other active people who share similar interests to interact with. This feed allows users to find local pick up games, find leagues to join or coaches for their teams. Find local events such as marathons or tournaments and so on.</p>\r\n		<h4>\r\n			Who can join and/or use Thefamdates? Is there a fee to join?</h4>\r\n		<p>\r\n			-Thefamdates is open to all users 13 years of age and older. Joining TSF is free for all users.</p>\r\n		<h4>\r\n			What do I need to join?</h4>\r\n		<p>\r\n			- Information including images on a user profile are available to all TSF users. Please be sure to use good judgment when posting information and/or images on your profile.</p>\r\n		<h4>\r\n			Does Thefamdates sell my personal information?</h4>\r\n		<p>\r\n			- Rest assured, Thefamdates will never sell any personal information you provide while using our services to any 3rd party and/or company. In some instances, Thefamdates will use such information to improve our services to provide the best user experience to users.</p>\r\n		<h4>\r\n			How do I follow another user?</h4>\r\n		<p>\r\n			- All TSF users are able to search and/or follow one another. In order to find any follow another user, you can search for them by their name, username, geographic location, interests, expertise, etc. You may also use the import button in order to import friends from other networks. TSF will also match you with users of similar interests and give you suggestions on people you may be interested in following. After searching for and finding another user you would like to follow, you can click on the &ldquo;Subscribe&rdquo; button in order to follow that user.</p>\r\n	</div>\r\n</div>\r\n','en',1),(2,'About','<div class=\"about-page-header hidden-phone hidden-tablet\">\r\n	&nbsp;</div>\r\n<div class=\"container white-background about-hero\">\r\n	<div class=\"span11\">\r\n		<h3 class=\"page-title\">\r\n			About famdates</h3>\r\n		<p>\r\n			The Sports Freak is a social networking website that revolutionizes the way people connect and engage online about sports, fitness and nutrition. At The Sports Freak, we believe fans of all levels can learn, interact and live out their love of the game by connecting with a like-minded community interested in sports, fitness and nutrition.</p>\r\n		<p>\r\n			Take your active lifestyle to the next level: create your personal profile, connect with people online and offline, and discover the resources to live, breathe and love the life of a Sports Freak.</p>\r\n	</div>\r\n</div>\r\n<div class=\"container gray-background-about about-testimonial\">\r\n	<div class=\"about-logo\">\r\n		&nbsp;</div>\r\n	<div class=\"pagination-centered span11\">\r\n		<p>\r\n			The Sports Freak&rsquo;s mission is to bring together a community of active people to learn, interact and live out their love of the game by engaging with each other.</p>\r\n		<p>\r\n			The roots of The Sports Freak began in July 2012 with life-long friends Vahe Tashjian, Shant Panossian and Henrik Shahgholian. Born and raised in Silicon Valley, Tashjian, Panossian and Shahgholian wanted to create a new kind of social network for those interested and dedicated to an active, healthy lifestyle. For the founders, their love of sports, fitness and nutrition was more than a lifestyle; being a sports freak meant being part of a thriving culture of a global community.</p>\r\n		<p>\r\n			Based in the heart of Silicon Valley, the birthplace of such gamechangers as Google and Facebook, The Sports Freak brings social networking and the sports and fitness world together to revolutionize how we live an active lifestyle, online and offline. The Sports Freak site was officially launched in February 2013.</p>\r\n	</div>\r\n	<!--/pagination centered--></div>\r\n','en',2),(3,'Terms Of Use','<div class=\"container\">\r\n      		\r\n        <div class=\"about-page-header hidden-phone hidden-tablet\">\r\n            \r\n             	\r\n	                <div class=\"transparent span3 general-page-header hidden-phone\">\r\n                    	<span class=\"red\">terms of</span> use\r\n                       \r\n                    </div><!--/transparent-->\r\n             \r\n        </div> <!--/page header-->\r\n        \r\n        \r\n        </div>\r\n\r\n<div class=\"container white-background general-hero\">\r\n            \r\n            	<div class=\"span11 general-margin-left\">\r\n            <h3 class=\"page-title\">terms of use</h3>\r\n            <p>Thefamdates is a social networking service that allows members to create unique personal profiles online in order to find and communicate with old and new friends. The service is operated by Thefamdates. By using the Thefamdates Website you agree to be bound by these Terms of Use (this \"Agreement\"), whether or not you register as a member (\"Member\"). If you wish to become a Member, communicate with other Members and make use of the Thefamdates services (the \"Service\"), please read this Agreement and indicate your acceptance by following the instructions in the Registration process</p>\r\n              \r\n<p>This Agreement sets out the legally binding terms for your use of the Website and your Membership in the Service.</p>\r\n<p>Thefamdates may modify this Agreement from time to time and such modification shall be effective upon posting by Thefamdates on the Website. You agree to be bound to any changes to this Agreement when you use the Service after any such modification is posted. This Agreement includes Thefamdates\'s policy for acceptable use and content posted on the Website, your rights, obligations and restrictions regarding your use of the Website and the Service and Thefamdates\'s Privacy Policy.</p>\r\n                  \r\n<p>Please choose carefully the information you post on Thefamdates and that you provide to other Members. Any photographs posted by you may not contain nudity, violence, or offensive subject matter. Information provided by other Thefamdates Members (for instance, in their Profile) may contain inaccurate, inappropriate or offensive material, products or services and Thefamdates assumes no responsibility nor liability for this material.</p>\r\n          \r\n<p>Thefamdates reserves the right, in its sole discretion, to reject, refuse to post or remove any posting (including email) by you, or to restrict, suspend, or terminate your access to all or any part of the Website and/or Services at any time, for any or no reason, with or without prior notice, and without lability.</p>\r\n<p>By participating in any offline Thefamdates event, you agree to release and hold Thefamdates harmless from any and all losses, damages, rights, claims, and actions of any kind including, without limitation, personal injuries, death, and property damage, either directly or indirectly related to or arising from your participation in any such offline Thefamdates event. </p>\r\n \r\n\r\n \r\n\r\n\r\n           </div>\r\n           \r\n           \r\n            </div>\r\n\r\n<div class=\"container gray-background-about general-testimonial\">\r\n            \r\n            \r\n            \r\n            <div class=\"span11 general-margin-left\">\r\n          <h4>1) Your Interactions</h4>\r\n<p>You are solely responsible for your interactions and communication with other Members. You understand that Thefamdates does not in any way screen its Members, nor does Thefamdates inquire into the backgrounds of its Members or attempt to verify the statements of its Members. Thefamdates makes no representations or warranties as to the conduct of Members or their compatibility with any current or future Members. We do however recommend that if you choose to meet or exchange personal information with any member of Thefamdates then you should take it upon yourself to do a background check on said person.</p>\r\n           \r\n<p>In no event shall Thefamdates be liable for any damages whatsoever, whether direct, indirect, general, special, compensatory, consequential, and/or incidental, arising out of or relating to the conduct of you or anyone else in connection with the use of the Service, including without limitation, bodily injury, emotional distress, and/or any other damages resulting from communications or meetings with other registered users of this Service or persons you meet through this Service.   </p>\r\n \r\n \r\n<h4>2) Eligibility</h4>\r\n<p>Membership in the Service where void is prohibited. By using the Website and the Service, you represent and warrant that all registration information you submit is truthful and accurate and that you agree to maintain the accuracy of such information. You further represent and warrant that you are 18 years of age or older and that your use of the Thefamdates shall not violate any applicable law or regulation. Your profile may be deleted without warning, if it is found that you are misrepresenting your age. Your Membership is solely for your personal use, and you shall not authorize others to use your account, including your profile or email address. You are solely responsible for all content published or displayed through your account, including any email messages, and for your interactions with other members.</p>\r\n \r\n                          \r\n<h4>3) Term/Fees.</h4>\r\n<p>This Agreement shall remain in full force and effect while you use the Website, the Service, and/or are a Member. You may terminate your membership at any time. Thefamdates may terminate your membership for any reason, effective upon sending notice to you at the email address you provide in your Membership application or other email address as you may subsequently provide to Thefamdates. By using the Service and by becoming a Member, you acknowledge that Thefamdates reserves the right to charge for the Service and has the right to terminate a Member\'s Membership if Member should breach this Agreement or fail to pay for the Service, as required by this Agreement.</p>\r\n \r\n \r\n<h4>4) Non Commercial Use by Members</h4>\r\n<p>The Website is for the personal use of Members only and may not be used in connection with any commercial endeavors except those that are specifically endorsed or approved by the management of Thefamdates. Illegal and/or unauthorized use of the Website, including collecting usernames and/or email addresses of Members by electronic or other means for the purpose of sending unsolicited email or unauthorized framing of or linking to the Website will be investigated. Commercial advertisements, affiliate links, and other forms of solicitation may be removed from member profiles without notice and may result in termination of membership privileges. Appropriate legal action will be taken by Thefamdates for any illegal or unauthorized use of the Website.</p>\r\n \r\n \r\n<h4>5) Proprietary Rights in Content on Thefamdates.</h4>\r\n<p>Thefamdates owns and retains all proprietary rights in the Website and the Service. The Website contains copyrighted material, trademarks, and other proprietary information of Thefamdates and its licensors. Except for that information which is in the public domain or for which you have been given written permission, you may not copy, modify, publish, transmit, distribute, perform, display, or sell any such proprietary information.</p>\r\n \r\n \r\n<h4>6) Content Posted on the Site.</h4>\r\n<p>You understand and agree that Thefamdates may review and delete any content, messages, Thefamdates Messenger messages, photos or profiles (collectively, \"Content\") that in the sole judgment of Thefamdates violate this Agreement or which may be offensive, illegal or violate the rights, harm, or threaten the safety of any Member.</p>\r\n<p>You are solely responsible for the Content that you publish or display (hereinafter, \"post\") on the Service or any material or information that you transmit to other Members.</p>\r\n<p>By posting any Content to the public areas of the Website, you hereby grant to Thefamdates the non-exclusive, fully paid, worldwide license to use, publicly perform and display such Content on the Website. This license will terminate at the time you remove such Content from the Website.</p>\r\n<p>The following is a partial list of the kind of Content that is illegal or prohibited on the Website. Thefamdates reserves the right to investigate and take appropriate legal action in its sole discretion against anyone who violates this provision, including without limitation, removing the offending communication from the Service and terminating the membership of such violators. Prohibited Content includes Content that: is patently offensive and promotes racism, bigotry, hatred or physical harm of any kind against any group or individual:</p>\r\n\r\n<ul> \r\n<li>Harasses or advocates harassment of another person; </li>\r\n<li>Involves the transmission of \"junk mail\", \"chain letters,\" or unsolicited mass mailing or \"spamming\";</li>\r\n<li>Promotes information that you know is false or misleading or promotes illegal activities or conduct that is abusive, threatening, obscene, defamatory or libelous;</li>\r\n<li>Promotes an illegal or unauthorized copy of another person\'s copyrighted work, such as providing pirated computer programs or links to them, providing information to circumvent manufacture-installed copy-protect devices, or providing pirated music or links to pirated music files;</li>\r\n<li>Contains restricted or password only access pages or hidden pages or images (those not linked to or from another accessible page);</li>\r\n<li>Provides material that exploits people under the age of 18 in a sexual or violent manner, or solicits personal information from anyone under 18;</li>\r\n<li>Provides instructional information about illegal activities such as making or buying illegal weapons, violating someone\'s privacy, or providing or creating computer viruses;</li>\r\n<li>Solicits passwords or personal identifying information for commercial or unlawful purposes from other users;</li>\r\n<li>Involves commercial activities and/or sales without our prior written consent such as contests, sweepstakes, barter, advertising, or pyramid schemes.           </li>\r\n<li>You must use the Service in a manner consistent with any and all applicable laws and regulations.</li>\r\n<li>You may not engage in advertising to, or solicitation of, any Member to buy or sell any products or services through the Service.</li>\r\n<li>You may not transmit any chain letters or junk email to other Members.</li>\r\n<li>Although Thefamdates cannot monitor the conduct of its Members off the Website, it is also a violation of these rules to use any information obtained from the Service in order to harass, abuse, or harm another person, or in order to contact, advertise to, solicit, or sell to any Member without their prior explicit consent. In order to protect our Members from such advertising or solicitation, Thefamdates reserves the right to restrict the number of emails which a Member may send to other Members in any 24-hour period to a number which Thefamdates deems appropriate in its sole discretion.            </li>\r\n<li>You may not cover or obscure the banner advertisements on your personal profile page, or any Thefamdates page via HTML/CSS or any other means.               </li>\r\n<li>Any automated use of the system, such as using scripts to add friends, is prohibited.            </li>\r\n<li>You may not attempt to impersonate another user or person who is not a member of Thefamdates.</li>\r\n<li>You may not use the account, username, or password of another Member at any time nor may you disclose your password to any third party or permit any third party to access your account.</li>\r\n<li>You may not sell or otherwise transfer your profile.</li>\r\n</ul>\r\n \r\n \r\n<h4>7) Copyright Policy</h4>\r\n<p>You may not post, distribute, or reproduce in any way any copyrighted material, trademarks, or other proprietary information without obtaining the prior written consent of the owner of such proprietary rights. It is the policy of Thefamdates to terminate membership privileges of any member who repeatedly infringes copyright upon prompt notification to Thefamdates by the copyright owner or the copyright owner\'s legal agent. Without limiting the foregoing, if you believe that your work has been copied and posted on the Service in a way that constitutes copyright infringement, please provide our Copyright Agent with the following information: an electronic or physical signature of the person authorized to act on behalf of the owner of the copyright interest; a description of the copyrighted work that you claim has been infringed; a description of where the material that you claim is infringing is located on the Website; your address, telephone number, and email address; a written statement by you that you have a good faith belief that the disputed use is not authorized by the copyright owner, its agent, or the law; a statement by you, made under penalty of perjury, that the above information in your notice is accurate and that you are the copyright owner or authorized to act on the copyright owner\'s behalf. Thefamdates\'s Copyright Agent for notice of claims of copyright infringement can be reached via email address.</p>\r\n \r\n \r\n<h4>8) Member Disputes</h4>\r\n<p>You are solely responsible for your interactions with other Thefamdates Members. Thefamdates reserves the right, but has no obligation, to monitor disputes between you and other Members.</p>\r\n \r\n \r\n<h4>9) Disclaimers</h4>\r\n<p>Thefamdates is not responsible for any incorrect or inaccurate content posted on the Website or in connection with the Service provided, whether caused by users of the Website, Members or by any of the equipment or programming associated with or utilized in the Service. Thefamdates is not responsible for the conduct, whether online or offline, of any user of the Website or Member of the Service. Thefamdates assumes no responsibility for any error, omission, interruption, deletion, defect, delay in operation or transmission, communications line failure, theft or destruction or unauthorized access to, or alteration of, any user or Member communication. Thefamdates is not responsible for any problems or technical malfunction of any telephone network or lines, computer online systems, servers or providers, computer equipment, software, failure of any email or players due to technical problems or traffic congestion on the Internet or at any Website or combination thereof, including any injury or damage to users and/or Members or to any person\'s computer related to or resulting from participation or downloading materials in connection with the Website and/or in connection with the Service. Under no circumstances shall Thefamdates be responsible for any loss or damage, including personal injury or death, resulting from use of the Website or the Service or from any Content posted on the Website or transmitted to Members, or any interactions between users of the Website, whether online or offline. The Website and the Service are provided \"AS-IS\" and Thefamdates expressly disclaims any warranty of fitness for a particular purpose or non-infringement. Thefamdates cannot guarantee and does not promise any specific results from use of the Website and/or the Service.</p>\r\n\r\n               \r\n<h4>10) Limitation on Liability</h4>\r\n<p>IN NO EVENT SHALL Thefamdates BE LIABLE TO YOU OR ANY THIRD PARTY FOR ANY INDIRECT, CONSEQUENTIAL, EXEMPLARY, INCIDENTAL, SPECIAL OR PUNITIVE DAMAGES, INCLUDING LOST PROFIT DAMAGES ARISING FROM YOUR USE OF THE WEB SITE OR THE SERVICE, EVEN IF Thefamdates HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. NOTWITHSTANDING ANYTHING TO THE CONTRARY CONTAINED HEREIN, Thefamdates\'S LIABILITY TO YOU FOR ANY CAUSE WHATSOEVER AND REGARDLESS OF THE FORM OF THE ACTION, WILL AT ALL TIMES BE LIMITED TO AMOUNT PAID, IF ANY, BY YOU TO Thefamdates FOR THE SERVICE DURING THE TERM OF MEMBERSHIP.</p>\r\n\r\n          \r\n<h4>11) Disputes</h4>\r\n<p>If there is any dispute about or involving the Website and/or the Service, by using the Website, you agree that any dispute shall be governed by the laws of the area in which we are based without regard to conflict of law provisions and you agree to personal jurisdiction by and venue in the area in which we are based.</p>\r\n \r\n \r\n<h4>12) Indemnity</h4>\r\n<p>You agree to indemnify and hold Thefamdates, its subsidiaries, affiliates, officers, agents, and other partners and employees, harmless from any loss, liability, claim, or demand, including reasonable attorneys\' fees, made by any third party due to or arising out of your use of the Service in violation of this Agreement and/or arising from a breach of this Agreement and/or any breach of your representations and warranties set forth above.</p>\r\n\r\n                      \r\n<h4>13) Other</h4>\r\n<p>This Agreement is accepted upon your use of the Website and is further affirmed by you becoming a Member of the Service. This Agreement constitutes the entire agreement between you and Thefamdates regarding the use of the Website and/or the Service. The failure of Thefamdates to exercise or enforce any right or provision of this Agreement shall not operate as a waiver of such right or provision. The section titles in this Agreement are for convenience only and have no legal or contractual effect. Please contact us with any questions regarding this Agreement. Thefamdates is a trademark of .</p>\r\n<p>I HAVE READ THIS AGREEMENT AND AGREE TO ALL OF THE PROVISIONS CONTAINED ABOVE.</p>\r\n            \r\n            \r\n</div> <!--/span11-->\r\n \r\n            \r\n            </div>','en',3),(4,'Privacy Policy','<div class=\"container\">\r\n      		\r\n        <div class=\"about-page-header hidden-phone hidden-tablet\">\r\n            \r\n             	\r\n	                <div class=\"transparent span3 general-page-header hidden-phone\">\r\n                    	<span class=\"red\">privacy</span> policy\r\n                       \r\n                    </div><!--/transparent-->\r\n             \r\n        </div> <!--/page header-->\r\n        \r\n        \r\n        </div>\r\n\r\n<div class=\"container white-background general-hero\">\r\n            \r\n            	<div class=\"span11 general-margin-left\">\r\n            <h3 class=\"page-title\">privacy policy</h3>\r\n            <p>Thefamdates is the ultimate portal connecting sport, fitness, and nutrition enthusiasts globally, allowing for an interactive and informational forum encompassing their common interests and passions.</p>\r\n\r\n<p>This Privacy Policy describes how and when Thefamdates collects, uses and shares your information when you use our Services. Thefamdates receives your information through your public profile and/or our various websites, SMS, APIs, email notifications, applications, buttons, and widgets (the \"Services\" or \"Thefamdates\"). For example, you send us information when you use Thefamdates from our website, post on your public profile, via SMS, or access Thefamdates from an application such as Thefamdates for Mac, Thefamdates for Android or Thefamdates Mobile. When using any of our Services you consent to the collection, transfer, manipulation, storage, disclosure and other uses of your information as described in this Privacy Policy. Irrespective of which country you reside in or supply information from, you authorize Thefamdates to use your information in the United States and any other country or jurisdiction where Thefamdates operates.</p>\r\n \r\n<p>If you have any questions or comments about this Privacy Policy, please contact us at privacy@thefamdates.com or here.</p>\r\n \r\n\r\n           </div>\r\n           \r\n           \r\n            </div>\r\n<div class=\"container gray-background-about general-testimonial\">\r\n            \r\n            \r\n            \r\n            <div class=\"span11 general-margin-left\">\r\n           	<h3 class=\"page-title\">information collection and use</h3>\r\n            \r\n            <h4>Information Collected Upon Registration</h4>\r\n<p>When you create or reconfigure a Thefamdates account, you provide some personal information, such as your name, username, password, and email address. Some of this information, for example, your name and username, is listed publicly on our Services, including on your profile page and in search results. Some Services, such as search, public user profiles and viewing lists, do not require registration.</p>\r\n \r\n \r\n<h4>Additional Information</h4>\r\n<p>You may provide us with profile information to make public, such as a short biography, your location, your website, or a picture. You may provide information to customize your account, such as a cell phone number for the delivery of SMS messages. We may use your contact information to send you information about our Services or to market to you. You may use your account settings to unsubscribe from notifications from Thefamdates. You may also unsubscribe by following the instructions contained within the notification or the instructions on our website. We may use your contact information to help others find your Thefamdates account, including through third-party services and client applications. Your account settings control whether others can find you by your email address or cell phone number. If you email us, we may keep your message, email address and contact information to respond to your request. If you connect your Thefamdates account to your account on another service in order to cross-post between Thefamdates and that service, the other service may send us your registration or profile information on that service and other information that you authorize. This information enables cross-posting, helps us improve the Services, and is deleted from Thefamdates within a few weeks of your disconnecting from Thefamdates your account on the other service. Providing the additional information described in this section is entirely optional.</p>\r\n \r\n<h4>Posting, Following, Lists and other Public Information</h4>\r\n<p>Our Services are primarily designed to help you to connect and interact with other sport, fitness, and nutrition enthusiasts and share your common interests. Most of the information you provide us is information you authorize to become public. This includes not only your posts and the subsequent metadata provided with posting, such as when you created a post, but also the lists you create, the people you follow, and many other bits of information that result from your use of the Services. Our default is almost always to make the information you provide public for as long as you do not delete it from Thefamdates profile and/or account, but we generally give you settings to make the information more private if you want. Your public information is broadly and instantly disseminated. For instance, your public user profile information and information included within may be searchable by search engines and are immediately delivered via SMS and our APIs to a wide range of users and services. When you share information or content like photos, videos, and links via the Services, you should think carefully about the content and information you are making public.</p>\r\n \r\n<h4>Location Information</h4>\r\n<p>You may choose to publish your location in your posts and in your Thefamdates profile. You may also tell us your location when you set your trend location on Thefamdates or enable your computer or mobile device to send us location information. You can set your Thefamdates location preferences in your account settings and learn more about this feature here. Learn how to set your mobile location preferences here. We may use and store information about your location to provide features of our Servicesand to improve and customize the Services, for example, with more relevant content like local trends, stories, ads, and suggestions for people to follow.</p>\r\n<p>Links: Thefamdates may keep track of how you interact with links across our Services, including our email notifications, third-party services, and client applications, by redirecting clicks or through other means. We do this to help improve our Services, to provide more relevant advertising, and to be able to share aggregate click statistics such as how many times a particular link was clicked on.</p>\r\n            \r\n            \r\n</div> <!--/span11-->\r\n \r\n            \r\n            </div>','en',4);
/*!40000 ALTER TABLE `static_page_staticcontent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `static_page_staticpage`
--

DROP TABLE IF EXISTS `static_page_staticpage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `static_page_staticpage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) NOT NULL,
  `name` varchar(200) NOT NULL,
  `enable_comments` tinyint(1) NOT NULL,
  `template_name` varchar(70) NOT NULL,
  `registration_required` tinyint(1) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `order` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `static_page_staticpage_a4b49ab` (`url`),
  KEY `static_page_staticpage_63f17a16` (`parent_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `static_page_staticpage`
--

LOCK TABLES `static_page_staticpage` WRITE;
/*!40000 ALTER TABLE `static_page_staticpage` DISABLE KEYS */;
INSERT INTO `static_page_staticpage` VALUES (1,'/faq/','FAQ',0,'',0,NULL,NULL),(2,'/about-us/','About',0,'',0,NULL,NULL),(3,'/terms/','Term of Use',0,'',0,NULL,NULL),(4,'/privacy/','Privacy',0,'',0,NULL,NULL);
/*!40000 ALTER TABLE `static_page_staticpage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `static_page_staticpage_sites`
--

DROP TABLE IF EXISTS `static_page_staticpage_sites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `static_page_staticpage_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `staticpage_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `staticpage_id` (`staticpage_id`,`site_id`),
  KEY `static_page_staticpage_sites_41b2aa4f` (`staticpage_id`),
  KEY `static_page_staticpage_sites_6223029` (`site_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `static_page_staticpage_sites`
--

LOCK TABLES `static_page_staticpage_sites` WRITE;
/*!40000 ALTER TABLE `static_page_staticpage_sites` DISABLE KEYS */;
INSERT INTO `static_page_staticpage_sites` VALUES (1,1,1),(6,2,1),(4,3,1),(5,4,1);
/*!40000 ALTER TABLE `static_page_staticpage_sites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tagging_tag`
--

DROP TABLE IF EXISTS `tagging_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tagging_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tagging_tag`
--

LOCK TABLES `tagging_tag` WRITE;
/*!40000 ALTER TABLE `tagging_tag` DISABLE KEYS */;
INSERT INTO `tagging_tag` VALUES (30,'Benefits'),(49,'Beveiliging'),(48,'Bezienswaardigheden'),(32,'Boat Covers'),(33,'Boat Emergency Services'),(35,'Boat Repair'),(31,'Boat Storages'),(37,'Boot kopen'),(42,'Bootvervoer'),(23,'Bridge And Sluis Times'),(17,'Business'),(19,'Discounts/ Coupons'),(47,'Eten en drinken aan het water'),(20,'Events'),(16,'Information'),(15,'Inspiration'),(29,'Insurances'),(41,'Jachthavens'),(38,'Keuringen'),(26,'Marinas'),(39,'Motoren'),(46,'Musea'),(24,'News'),(40,'Onderdelen en accessoires'),(51,'Onderhoud en service'),(50,'Pechservice'),(36,'Restaurant'),(21,'Routes'),(27,'Rules On The Water'),(18,'Security'),(22,'Sightseeing Locations'),(34,'Technical Help'),(52,'Vaaropleidingen'),(43,'Verhuur & charter'),(53,'Verzekeringen'),(28,'Vip Treatments'),(44,'Watersportverenigingen'),(45,'Watersportwinkels'),(25,'Weather'),(54,'test');
/*!40000 ALTER TABLE `tagging_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tagging_taggeditem`
--

DROP TABLE IF EXISTS `tagging_taggeditem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tagging_taggeditem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tag_id` (`tag_id`,`content_type_id`,`object_id`),
  KEY `tagging_taggeditem_3747b463` (`tag_id`),
  KEY `tagging_taggeditem_e4470c6e` (`content_type_id`),
  KEY `tagging_taggeditem_829e37fd` (`object_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tagging_taggeditem`
--

LOCK TABLES `tagging_taggeditem` WRITE;
/*!40000 ALTER TABLE `tagging_taggeditem` DISABLE KEYS */;
INSERT INTO `tagging_taggeditem` VALUES (1,54,11,4);
/*!40000 ALTER TABLE `tagging_taggeditem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-04-29 21:00:47
