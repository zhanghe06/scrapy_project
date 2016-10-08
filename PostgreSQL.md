## 安装启动

### Mac

安装
```
✗ brew install postgres
```

查看 postgres 相关操作
```
✗ brew info postgres
```

根据提示启动服务（测试不需要后台运行）
```
✗ postgres -D /usr/local/var/postgres
```

创建用户
```
✗ createuser postgres -P
Enter password for new role:[密码]
Enter it again:[密码]
```

创建数据库
```
✗ createdb test -O postgres -E UTF8 -e
```

连接数据库
```
✗ psql -U postgres -d test -h 127.0.0.1
psql (9.5.4)
Type "help" for help.

test=>
```


### Ubuntu

略...


## 数据类型

1. 数值类型

名字 | 存储空间 | 描述 | 范围
----|----|--------|------------
smallint | 2 字节 | 小范围整数 | -32768 到 +32767
integer | 4 字节 | 常用的整数 | -2147483648 到 +2147483647
bigint | 8 字节 | 大范围的整数 | -9223372036854775808 到 9223372036854775807
decimal | 变长 | 用户声明精度, 精确 | 无限制
numeric | 变长 | 用户声明精度, 精确 | 无限制
real | 4 字节 | 变精度, 不精确 | 	6 位十进制数字精度
double | 8 字节 | 变精度, 不精确 | 15 位十进制数字精度
serial | 4 字节 | 自增整数 | 1 到 +2147483647
bigserial | 8 字节 | 大范围的自增整数 | 1 到 9223372036854775807


在目前的 PostgreSQL 版本中, decimal 和 numeric 是等效的。

2. 字符类型

名字 | 描述
----|----
varchar(n) | 变长, 有长度限制
char(n) | 定长, 不足补空白
text | 变长, 无长度限制

3. 日期/时间类型

名字 | 存储空间 | 描述 | 最低值 | 最高值 | 分辨率
----|----|--------|----|----|----|
timestamp[无时区] | 8字节 | 包括日期和时间 | 4713 BC | 5874897AD | 1毫秒/14位
timestamp[含时区] | 8字节 | 日期和时间, 带时区 | 4713 BC | 5874897AD | 1毫秒/14位
interval | 12字节 | 时间间隔 | -178000000年 | 178000000年 | 1毫秒/14位
date | 4字节 | 只用于日期 | 4713 BC | 32767AD | 1天
time[无时区] | 8字节 | 只用于一日内时间 | 00:00:00 | 24:00:00 | 1毫秒/14位


## 建库、建表过程

```
$ sudo su postgres
$ createdb test
$ psql test
postgres=# \l
```


## 关于建表的一些常识

- 对于唯一约束的用途而言, 系统认为 NULL 数值是不相等的
- 从技术上讲, PRIMARY KEY 只是 UNIQUE 和 NOT NULL 的组合
- 推荐使用一个 SERIAL 或者其它序列发生器做表的主键
- PostgreSQL 自动为每个唯一约束和主键约束创建一个索引以确保唯一性。 因此, 我们不必为主键字段明确的创建索引。


## 索引

索引是我们经常使用的一种数据库搜索优化手段

PostgreSQL 索引类型: B-Tree、Hash、GiST 和 GIN

```
# 普通索引
CREATE INDEX table_column_idx ON table (column);
# 复合索引
CREATE INDEX table_column_a_b_idx ON table (column_a, column_b);
# 唯一索引
CREATE UNIQUE INDEX table_column_key ON table (column);
```
