# 学习小结 20211013

#### 尹哲良

## SQL

### 集合算子

取两列数据交集的算法：遍历两列数据，如果有相同元素则放入结果中

连接运算OR按照嵌套运算进行

解决这一问题的办法：显示集合运算 INTERSECT, UNION, UNION ALL 

### 嵌套查询

所需查询的数据需要从另一个查询表中提取

```sql
SELECT c.city
FROM Company c
WHERE c.name IN (
	SELECT pr.maker
	FROM Purchase p,Product pr
	WHERE p.name=pr.product
		AND p.buyer='Mickey')
```

问题：可能返回重复值，所以需要添加 DISTINCT

ALL ANY 作用于一列数据，取出最极端的一个值

嵌套查询也可以实现交集和差集

### 聚合函数

GROUP BY

HAVING

## Python SQLite

```python
import sqlite3
db = sqlite3.connect("university.db")
cursor=db.cursor()
cursor.execute("""DROP TABLE IF EXISTS students;""")
cursor.execute("""CREATE TABLE IF NOT EXISTS students
(id integer PRIMARY KEY, name text NOT NULL, gender text NOT NULL, age ineger NOT NULL);""")
cursor.execute("""INSERT INTO students(id, name, gender, age) 
VALUES(1, 'zhangsan', 'male', 18)""")
cursor.execute("""INSERT INTO students(id, name, gender, age) 
VALUES(2, 'lisi', 'female', 19)""")
cursor.execute("""INSERT INTO students(id, name, gender, age) 
VALUES(3, 'wangwu', 'male', 17)""")
db.commit()
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())
db.close()
```

`db.commit()` 编辑数据库

`cursor.fetchall()` 输出查询结果

更多情况下，先把数据准备好，再通过格式化字符串操作SQL

## 数据系统

DBMS: Database Management System，管理数据库的软件

数据表体现了数据的关系，是关系型数据库的重要组成部分
