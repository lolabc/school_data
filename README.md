储存数据的表

CREATE TABLE `college` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `edu_level` varchar(255) DEFAULT NULL,
  `hot` varchar(255) DEFAULT NULL,
  `category_hot` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=2761 DEFAULT CHARSET=utf8;
