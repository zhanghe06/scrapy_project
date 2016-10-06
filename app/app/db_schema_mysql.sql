DROP DATABASE IF EXISTS `test`;
CREATE DATABASE `test` /*!40100 DEFAULT CHARACTER SET utf8 */;


use test;


CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT '' COMMENT '姓名',
  `age` tinyint(2) DEFAULT '0' COMMENT '年龄',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';


CREATE TABLE `company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT '' COMMENT '名称',
  `site` varchar(45) DEFAULT '' COMMENT '网站',
  `address` varchar(100) DEFAULT '' COMMENT '地址',
  `industry` varchar(45) DEFAULT '' COMMENT '行业',
  `email` varchar(45) DEFAULT '' COMMENT '邮箱',
  `phone` varchar(45) DEFAULT '' COMMENT '电话',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司表';


CREATE TABLE `position` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT '' COMMENT '名称',
  `city` varchar(45) DEFAULT '' COMMENT '地区',
  `address` varchar(100) DEFAULT '' COMMENT '地址',
  `industry` varchar(45) DEFAULT '' COMMENT '行业',
  `email` varchar(45) DEFAULT '' COMMENT '邮箱',
  `phone` varchar(45) DEFAULT '' COMMENT '电话',
  `description` varchar(500) DEFAULT '' COMMENT '描述',
  `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='职位表';
