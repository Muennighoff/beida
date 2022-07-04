# Lecture 5 SQL Introduction

## 基本方法

SQL 一种关系型数据库的标配关系语言。分为三类语句：

* DDL 数据定义语言
* DML 数据操作语言
* DCL 数据控制语言

```sql
##
--
/*这些都是注释方法*/
SELECT --命令大小写不敏感
select
Select
CREATE DATABASE 创建一个表

CREATE TABLE table1		--表名
(
	c1  INT,		--列1
	c2  INT		--列2
);

--添加数据
INSERT INTO table1 VALUES(1, 2);
INSERT INTO table1 VALUES(1, 2),(2,3); --插入两行数据。第一行c1给1，c2给2；第二行c1给2 c2给3
INSERT INTO table1 (c1) VALUES(1); --默认给另一列填null
--INSERT INTO table1 (c2) VALUES(1);
INSERT INTO table1 VALUES(4,4); --默认给另一列填null

--修改表

ALTER TABLE table1 ADD c3 int;  --新增一列，全是null

ALTER TABLE table1 MODIFY COLUMN c3 varchar; --SQLite并不支持将小TABLE修改为可变字符串 varchar

alter TABLE table1 drop COLUMN c3; 

ALTER TABLE table1 ADD PRIMARY KEY (c1);  --设置为PRIMARY KEY的column必须无null

```

SQL的底层数据结构式多集MultiSet

## 查询语句 SFW语句

```sql
SELECT * --选择全部
FROM Product	--表的名称
WHERE Category = 'Gadgets'	--输出的结果不再是一个TABLE
```

## Like 的使用

```sql
SELECT * 
FROM Product	
WHERE PName LIKE '%gizmo_'
```

其中"%"表示任何字符串，"__"表示任何单一字符。

## 消除重复数据

```sql
SELECT DISTINCT Category
FROM Product
```

使用DISTINCT保证选取无重复值

## 排序

```sql
SELECT PName, Price, Manufacture
FROM Product
WHERE Category = 'Gadgets'
ORDER BY Price, PName --依次根据二者排序
```

## Python Tinker GUI

