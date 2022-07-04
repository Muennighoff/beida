# 第六天课堂笔记 2021/10/20

## SQL Part 3

### 交叉积

```sql
SELECT DISTINCT R.A
FROM R, S,  T
WHERE R.A=S.A OR R.A=T.A
```

如果这里 S 为空集，则在进行交叉积时就是空集。

### 显式集合运算

INTERSECT，UNION 集合运算，结果没有重复。

UNION ALL：多集的操作。

```sql
SELECT R.A FROM R, S WHERE R.A=S.A
UNION -- this is an explicit keyword!
SELECT R.A FROM R, T WHERE R.A=T.A
```

### 子查询

```sql
SELECT c.country
FROM   Company c
WHERE  c.cname  IN (
    SELECT pr.manufacturer
    FROM   Purchase p, Product pr
    WHERE  p.name = pr.pname AND p.buyer = 'Mickey'
);
```

### 分组和聚合

```sql
--SUM

SELECT SUM(price * quantity)
FROM   Sales
WHERE  product = 'bagel';


--MIN
SELECT product, MIN(price*quantity) 
FROM sales
Group By product
HAVING SUM(quantity)>10
```

## Python 和 SQLLite

### 连接

```python
db = sqlite3.connect("university.db")
cursor=db.cursor()
db.close()
```

### 执行

```python
cursor.execute()
db.commit() # 提交事务
```

### 读取

```python
cursor.execute("""SELECT students.id, students.name, students.gender, students.age, enrolled.class, enrolled.grade FROM students JOIN enrolled on students.id = enrolled.student""")
print(cursor.fetchall())
```

## PostgreSQL

安装和使用
