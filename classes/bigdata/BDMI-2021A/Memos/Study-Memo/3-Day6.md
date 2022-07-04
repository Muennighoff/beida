# WW6课堂小结

## SQL

- set operator
- 基础数据结构：
  - Multiset union cross-product 允许有重复值的集合
- 运算过程
  - cross-product
  - selection
  - projection
- 交集：intersect 做 multisets 的交集
- 并集：union 不允许重复； union all 允许重复
- Nested Query 嵌套查询
  - sub-queries需要用括号括起来
  - 需要使用distinct进行去重
  - where 
    - s > ALL sub-queries 大于所有的值
    - s > ANY sub-queries 大于至少一个值
    - EXISTS sub-queires 子查询中存在值
- 聚合与分组
  - avg() sum() count() min() max()
  - 计算过程
    - **from where** -> **group by** -> **select**
  - having 包括聚合后的条件，而 where对每一行进行操作

## Python SQLite
- cursor.execute() 执行sql命令
- cursor.commit() 将execute的操作提交到database
```python
import sqlite3
db = sqlite3.connect("university.db")
cursor = db.cursor()
cursor.execute("""DROP TABLE IF EXISTS enrolled""")
cursor.execute("""CREATE TABLE IF NOT EXISTS enrolled(student_id integer PRIMARY KEY,class_id integer NOT NULL,score float NOT NULL);""")
lst = [[1,1,90],[2,2,60]]
for each in lst:
    cursor.execute("""INSERT INTO enrolled VALUES({},{},{})""".format(each[0],each[1],each[2]))
    db.commit()
cursor.execute("""SELECT * from enrolled""")
print(cursor.fetchall())
db.close()
```

## 数据库系统
- 数据是客观事物的表示和记录
- 数据系统的定义：用于数据分析、管理、应用的计算机系统
- 关系型数据库
  - 表table 就是**关系**
  - table的列 就是 Schema 模式
  - 数据无关性：logical data independence(可以随意增加新的模式); physical data independence（不需要关心硬盘存储位置和索引）
  - 70年代解决并行、崩溃等问题，1980s 广泛应用
- NOSQL NewSQL HTAP的出现
  - 原因：关系型数据库weakness: 扩展互联网大数据速度慢，不能灵活改变Schema
- PLSQL procedure language SQL 是发展的方向
- 时间序列数据库是 发展的方向 -- 建立时间标签


## Postgresql
- % 读取一行的sql；%%读取多行的sql
- 安装，运行，与python的交互
- 使用localhost或者ip地址进行本地或者远程数据库的连接