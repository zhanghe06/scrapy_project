## MySQL

### 常用操作
```
# 登陆 MySQL:
mysql -u root -p
# 查看系统已存在的数据库
show databases;
# 删除名为 test 的空数据库
drop database test;
drop database if exists test;
# 建立名为 test 的数据库
create database test;
# 创建数据库并且指定指定字符集
create database test default character set utf8;
# 建立对 test 数据库有完全操作权限的名为 admin 的用户
grant all privileges on test.* to admin@localhost identified by 'password';
# 取消 admin 用户对数据库的操作权限
revoke all privileges on *.* from admin@localhost;
# 删除 admin 用户
delete from mysql.user where user='admin' and host='localhost';
# 增加一个用户 www 密码为 abc，让他可以在任何主机上登录，并对所有数据库有查询、插入、修改、删除的权限。
grant select,insert,update,delete on *.* to www@"%" Identified by "abc";
# 刷新,使所做的改动生效
flush privileges;
```

备份 mysqldump
```
-t 不输出建表信息，即只输出表数据
-d 不输出数据信息，即只输出表结构
# 备份表结构和数据到本地
mysqldump -h[host] -P[port] -u[user] -p[passwd] [db] [table] [--where=" 1=1"] --skip-lock-tables > /tmp/table.sql
```

导入
```
mysql -h[host] -P[port] -u[user] -p[pass] [db] < /tmp/table.sql
```


### 数据表建立

```
DROP DATABASE IF EXISTS `test`;
CREATE DATABASE `test` /*!40100 DEFAULT CHARACTER SET utf8 */;
use test;
```

```
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT '' COMMENT '姓名',
  `age` tinyint(2) DEFAULT '0' COMMENT '年龄',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';
```

```
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
```

```
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
```

### 数据表删除
```
DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `company`;
DROP TABLE IF EXISTS `position`;
```

### 忘记 MySQL 的 root 密码
```
# 如果 MySQL 正在运行，首先杀之
killall -TERM mysqld
# 启动 MySQL
PATH_TO_MYSQL/bin/mysqld --skip-grant-tables &
就可以不需要密码就进入 MySQL 了。
然后就是
mysql>use mysql
mysql>update user set password=password("new_pass") where user="root";
mysql>flush privileges;
重新杀 MySQL ，用正常方法启动 MySQL
一定注意：很多新手没有用password=password("...")，而是直接password="..."所以改掉密码不好使
```


## 高级功能

根据分隔符反转字符串
```
MariaDB [s2c]> select reverse(substring_index('aa,bb,cc,dd', ',', 4));
+-------------------------------------------------+
| reverse(substring_index('aa,bb,cc,dd', ',', 4)) |
+-------------------------------------------------+
| dd,cc,bb,aa                                     |
+-------------------------------------------------+
```

