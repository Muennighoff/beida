# 4-Day6

[TOC]

## SQL Set Algebra

多集multiset是允许有重复，但没有顺序的set

sql 中有交叉积 Cross-product

### 一些实例

```sql
SELECT DISTINCT R.A
FROM R,S,T
WHERE R.A = S.A OR R.A = T.A
```

这里若S为空集，则代码会直接停止

关于UNION和UNION ALL

```sql
SELECT R.A FROM R, S WHERE R.A=S.A
UNION -- this is an explicit keyword! union操作得到的元素没有重复
SELECT R.A FROM R, T WHERE R.A=T.A

DROP TABLE IF EXISTS S; 
CREATE TABLE S (A int);

INSERT INTO S VALUES (1),(2),(3),(4),(5)


-- UNION ALL example- notice that 1 and 4 occur twice!
SELECT R.A FROM R, S WHERE R.A=S.A
UNION ALL	--UNION ALL操作的结果允许有重复元素
SELECT R.A FROM R, T WHERE R.A=T.A
```

Nested Queries:

注意 IN语句为代表的嵌套查询会出现重复值，所以需要DISTINCT。但具体情况具体分析。

找到一类产品，这些产品的价格比“GW”公司生产的所有产品都要贵。

```sql
SELECT name
FROM Product 
WHERE price > ALL(
	SELECT price
	FROM Product
	WHERE maker = 'Gizmo-Works'
)
```

找到一类GW产品的山寨产品，即name一样但生产者不是GW。注意<>表示!=，EXISTS类似交集。

```sql
SELECT p1.name
FROM Product p1
WHERE p1.maker = "Gizmo-Works"
AND EXISTS(
	SELECT p2.name
	FROM Product p2
	WHERE p2.maker <> 'Gizmo-Works'
		AND p1.name = p2.name
)
```

找出所有电影，它的被翻拍过（名字一样，年份不一样）:

```sql
SELECT DISTINCT title
FROM   Movie AS m
WHERE  year1 <> ANY (
SELECT  year1
FROM    Movie
WHERE  title =  m.title);
```

### 聚合算法

```
SELECT COUNT(DISTINCT CATAGORY)
```

计算销售总额

```sql
SELECT SUM(price * quantity)
FROM purchase
```

计算某种产品的销售总额

```sql
SELECT SUM(price * quantity)
FROM purchase
WHERE product = 'bag'
```

按照product输出销量。注意这里输出中包含一个新列 TotalSales

```sql
SELECT   product,
	        SUM(price * quantity) AS TotalSales
FROM     Sales
WHERE    date > 1
GROUP BY product;
```

可以进一步使用having，注意having和where效果很像，只不过：

having子句可以让我们筛选成组后的各组数据

where子句在聚合前先筛选记录。也就是说where是作用在group by子句和having子句之前，而having子句是在聚合后对组记录进行筛选。即在结果中再筛选一次

```sql
SELECT   product, SUM(price*quantity)
FROM     sales 
WHERE    date >= 1
GROUP BY product
HAVING   SUM(quantity) > 10;
```

## 在Python中使用SQL

使用sqlite3 package。这里记录并注释一个典型的操作：

```python
import sqlite3
#sql模拟器

db = sqlite3.connect("university.db") #打开数据库，如果不存在则创建同名数据库
cursor=db.cursor() #创建一个光标，即模拟在sql中开始写代码
cursor.execute("""CREATE TABLE IF NOT EXISTS students
(id integer PRIMARY KEY, name text NOT NULL, gender text NOT NULL, age integer NOT NULL);""")
cursor.execute("""INSERT INTO students(id, name, gender, age) 
VALUES(1, 'zhangsan', 'male', 18)""")
cursor.execute("""INSERT INTO students(id, name, gender, age) 
VALUES(2, 'lisi', 'female', 19)""")
cursor.execute("""INSERT INTO students(id, name, gender, age) 
VALUES(3, 'wangwu', 'male', 17)""")
db.commit() #运行创建数据的操作时必须使用的代码。实际操作中最好一行一次。
cursor.execute("SELECT * FROM students")
print(cursor.fetchall()) # fetch all rows from the result set。
#在查询语句后使用
db.close() #一定记得关掉，不然可能出现冲突
```

## 数据库概念

数据库：一个巨大的、综合的数据集合

数据库管理系统（DBMS）：一个用于存储和管理数据的软件

### 关系型数据库

schema：模式 describes blueprint of the database

使用数据库系统的原因：数据无关性，即新增加数据（实体 entity）并不需要对整个应用进行调整。



