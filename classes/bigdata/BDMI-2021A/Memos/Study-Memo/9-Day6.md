# 第6次课堂笔记

## 1. 课前注意

课后作业：
读：FCDB第1、2章；第六章：the database language SQL
写：学习小节

SQL有一个速查表：sqltutorial.org/sql-cheat-sheet

## 2. SQL学习3.0: 

## 2.1 Set Operators & nested queries: 集合算子和嵌套查询

回忆：
集合（set）和多集（multiset），与列表（list）不同的是，集合没有顺序。
集合之间，有合并运算、交叉积运算等等。

### 2.1.1 集合运算操作：

对S 、T、R三个集合的一个非直观查询：对S、T取并集后，再和R取交集，怎么实现？
```sql
SELECT DISTINCT R.A
FROM R, S, T
WHERE R.A = S.A OR R.A = T.A
```

上述代码翻译成Python中，是通过循环操作，对元素进行遍历，来实现所谓的集合操作的。语句变成：
```python
output = {}
for r in R:
	for s in S:
		for t in T:
			if r['A'] == s['A'] or r['A'] == t['A']:
				output.add(r['A'])
return list(output)
```
可见，如果S是空集，则第二个for循环就停止，最后会返回空集。这不是我们想要的。

交集的显式集合运算：
```sql
SELECT R.A
FROM R, S
WHERE R.A = S.A
INTERSECT
SELECT R.A
FROM R,T
WHERE R.A = T.A
```
并集的显式集合运算：
```sql
SELECT R.A
FROM R, S
WHERE R.A = S.A
UNION
SELECT R.A
FROM R, T
WHERE R.A = T.A
```
UNION是并集运算，会消除重复元素。如果想要保留重复元素，需要多集操作：UNION ALL

### 2.1.2嵌套查询 Nested query：

**嵌套查询是指：**子查询（sub-queries）是嵌套在较大查询中的SQL查询。
**子查询：**也称内部查询、内部选择；
子查询必须被括号括起来，通常会添加在SELECT语句的WHERE字句中。
**外部查询：**包含子查询的语句。子查询先于外部查询进行，以将子查询的结果返回给外部查询。

**下面给出了一个嵌套查询的代码示例：**
找出由Mickey购买的所有产品的生产商的地址
tables：
```sql
Company(name, city)--公司
Product(name, maker)--产品
Purchase(id, product, buyer)--买家
```
code（嵌套查询）:
```sql
SELECT c.city
FROM Company c
WHERE c.name IN(
	SELECT pr.maker
	FROM Purchase p, Product pr
	WHERE p.product = pr.name AND p.buyer = 'Mickey'
)
```
和下面的代码比较？
```sql
SELECT c.city
FROM Company c, Product pr, Purchase p
WHERE c.name = pr.maker AND pr.name = p.product AND p.buyer = 'Mickey'
```
事实上，这两个查询不等价。第二个查询回返回重复的结果。
需要添加集合语义！两种方式，都在SELECT后添加DISTINCT，就能一致（都使用了集合语义）。

**子查询的返回关系：**
ALL、ANY、EXIST
s > ALL R：大于R中元素的所有值
S < ANY R：至少小于R中一个元素的值
EXISTS R：R中存在的值
**示例1：**
```sql
Product(name, price, category, maker)
SELECT name
FROM Product
WHERE price > ALL(
	SELECT price
	FROM Product
	WHERE maker = 'Gizmo-works'
)
```
效果：选择出所有价格大于生产商为'Gizmo-works'的产品

**示例2：**
```sql
SELECT p1.name
FROM Product p1
WHERE p1.maker = 'Gizmo-works' AND EXISTS(
	SELECT p2.name
	FROM Product p2
	WHERE p2.maker <> 'Gizmo-works' AND p1.name = p2.name
)
```
效果：选择出所有和Gizmo-works公司的产品同名，但又不是他们公司生产的**产品名字**。

并且注意到，**嵌套查询就可以用于实现交集和差集**。
**交集：**
```sql
(SELECT R.A, R.B FROM R)INTERSECT(SELECT S.A, S.B FROM S)
--等于
SELECT R.A, R.B
FROM R
WHERE EXISTS(
	SELECT *
	FROM S
	WHERE R.A = S.A AND R.B = S.B
)
```
**差集：**
```sql
(SELECT R.A, R.B FROM R)EXCEPT(SELECT S.A, S.B FROM S)
--等于
SELECT R.A, R.B
FROM R
WHERE NOT EXISTS(
	SELECT *
	FROM S
	WHERE R.A = S.A AND R.B = S.B
)
```
**示例：找到所有出现次数一次以上的电影**
```sql
Movie(title, year, director, length)
SELECT DISTINCT title
FROM Movie AS m
WHERE year <> ANY(
	SELECT year
	FROM Movie--这里的Movie应用于内部查询（直指下方的title）
	WHERE title = m.title--这里的m是应用于外部查询的
)
```

## 2.2 Aggregation, Group by & Having: 聚合与分组
### 2.2.1 聚合函数算子：Aggregation operators
支持一些聚合操作，如：计数（COUNT）、求和（SUM）、求最值（MAX，MIN）、平均值（AVG）等等。例如：
```sql
SELECT AVG(price)
FROM Product
WHERE maker = "Toyota"

SELECT COUNT(category)--适用于重复值的计数
FROM Product
WHERE year > 1995

SELECT COUNT(DISTINCT category)--抛去重复值
FROM Product
WHERE year > 1995
```

**还可以进行运算求和**，属于**简单聚合**。例如销售统计的例子：
```sql
SELECT SUM(price*quantity)
FROM Purchase ——购买总额

SELECT SUM(price*quantity)
FROM Purchase
WHERE product = 'bagel' --某种产品的购买总额
```

**分组聚合，GROUPING & AGGREGATION：**
```sql
Purchase(product, date, price, quantity)
	--找出10/1/2005之后的每种产品的销售总额
SELECT product, SUM(price*quantity) AS TotalSales
FROM Purchase
WHERE data > '10/1/2005'
GROUP BY product
	--结果就能得到，按照product为属性进行分组，并有TotalSale属性的表格
```

**分组和嵌套查询的比较， GROUP BY v.s. Nested Queries：**
```sql
--嵌套查询的代码
SELECT x.product, (
	SELECT SUM(y.price*y.quantity) 
	FROM Purchase y
	WHERE x.product = y.product AND y.data > '10/1/2005')
FROM Purchase x
WHERE x.date > '10/1/2005'
```
可见，采用嵌套查询的逻辑和代码都比分组要复杂。


### 2.2.3 group by: with HAVING, semantics （分组：Having 字句，语义）

Having子句可以用来增加对聚合的限定条件。那么与WHERE有什么不同呢？WHERE条件是应用于每一个元组的。
**一个示例代码：**
```sql
SELECT product, SUM(price*quantity)
FROM Purchase
WHERE data > '10/1/2015'
GROUP BY product
HAVING SUM(quantity) > 100
```
现在，可以对上述代码的general form说明运算顺序了：
**1.**计算FROM、WHERE子句。即将WHERE中的条件，应用到FROM所涉及的范围上。
**2.**按照GROUP BY子句中的属性进行分组。
**3.**对每一个分组，进行HAVING子句的运算。
**4.**计算SELECT中（如果有的话）的聚合操作，然后返回结果。

## 3 Python中的SQLite操作
更便捷的操作数据库方法：将整个流程都集中在python代码中
可以：
```python
import sqlite3
with sqlite3.connect("PhoneBook.db") as db:
	cursor = db.cursor()
#连接数据库
```
然后就可以像读文件一样，去打开和操作db文件了。
采用的语言和SQL语言完全相同，只不过每次操作后，需要用db.commit()进行更新。

下面是一些代码示例：
```python
cursor.excute("""CREATE TABLE IF NOT EXISTS Names(
id integer PRIMARY KEY,
firstname text,
surname text,
phonenumber text);""")
#创建一个具有四个属性的表Name

cursor.excute("""INSERT INTO Names(id, firstname, surname, phonenumber) VALUES ("1","Simon","Pierre","0000001 0001")""")
db.commit()
#向表中插入一组数据，并且保存表格

cursor.excute("""SELECT * FROM Names""")
for x in cursor.fetchall():
	print(x)
#从表中读取所有数据，每次一行打印出来（逐个打印）
#也可以一次性读取：print(cursor.fetchall())

db.close()
```

**另一个示例：创建一个university数据库：**
```python
with sqlite3.connect('university.db') as db:
	cursor = db.cursor

cursor.excute("""create table if not exist students(
id integer primary key,
name text not null,
gender text not null,
age integer not null,
major integer not null)""")
db.commit()
```

上面涉及的插入数据的语句，都是插入了固定数据。如何插入可变的数据呢？
```python
newID = input("Enter ID number:")
newName = input("Enter name:")
newClass = input("Enter class:")
newGrade = input("Enter Grade:")
cursor.excute("""INSERT INTO students(id, name, class, grade) VALUES (?,?,?,?)""",(newID, newName, newClass, newGrade))
db.commit()
#这样做，就可从外界输入数据，然后再插入到数据库中了
```

现在，继续在原数据库的基础上，增加更新3个同学的数据；
建立class表格并更新数据（至少插入三门以上课程）；
```python
#先插入学生的数据
genders = ['male','female']
majors = ['Math','CS','Finance','Economics']

for i in range(20):
	name = ''.join(random.sample(string.ascii_lowercase, 5))
	gender = genders[random.randint(0,1)]
	age = random.randint(12,24)
	major = majors[random.randint(0,3)]
	cursor.excute("""insert into students (id, name, gender, age, major) values ({},"{}","{}",{},"{}")""".format(i+1, name, gender, age, major))
db.commit()

#创建更新class表
cursor.excute("""create table if not exist class(
	class_id integer primary key,
	class_name text,
	lecture text,
	credit integer)""")
	
classes = ['Python','Java','C++','C','R','Go']
lectures = ['Adam','Bob','Cyrus','Dan','Eric','Frank']
Credits = [3,2,3,2,1,1]
for i in range(6):
	cursor.excute("""insert into class (class_id, class_name, lecture, credit) values ({},"{}","{}",{})""".format(i+1, classes[i], lectures[i], Credits[i]))
db.commit()
```

增加选课表
```python
cursor.excute("""create table if not exists enrolled(
student_id integer,
class_id integer,
credit integer,
score integer,
primary key(student_id, class_id))""")

for i in range(20):
	student_id = i+1
	for j in range(random.randint(1,6)):
		class_id = j+1
		credit = Credits[j]
		score = random.randint(0,100)
		cursor.execute('insert into enrolled (student_id, class_id, credit, score) values ({},{},{},{})',format(student_id, class_id, credit, score))
db.commit()
```

使用内连接查询所有学生的个人信息和所选的每个课程的分数：
id, name, gender, class_id, credit, score
```python
cursor.excute("""select id, name, gender, class_id, credit, score from students s inner join (
	select student_id, class_id, class_name, c.credit, score from class c 
	inner join enrolled e 
	on c.class_id = e.class_id) tc
on s.id = tc.student_id""")
#共进行了两次内连接

for x in cursor.fetchall():
	print(x)
```

## 4 数据系统
是用于处理数据，进行数据管理，分析应用的计算机软硬件系统。
数据库管理系统（DBMS）：是一个用于存储和管理数据的软件。
数据库：既指数据，也指处理数据的软件。

**例如，课程管理系统：**
有许多实体（Entity）：例如学生、课程；和关系（Relationships）：例如Alice选了课程A。
**数据模型：**
在关系型数据库中，数据表就能表现数据的关系。通过表的组织和操作，来完成对数据的组织和操作。每个关系都有一个模式（schema）。

## 5 postgresql数据库

