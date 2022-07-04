### 第1 SQL

- Originally  SEQUEL (Structured English Query Language)
- 3 Subtypes: 
    - DDL
    - DML
    - DCL

几个commands：
选择
```sql
SELECT * FROM table
```
更新
```sql
UPDATE * FROM table
```
删除
```sql
DELETE FROM table WHERE c1=1
```

Avoiding ambiguity (e.g. two tables with same column names)
```sql
SELECT DISTINCT p.name, c.address
FROM Person p, Company c
WHERE p.worksfor = c.name
```

JOIN types:
- Inner JOIN
- Outer JOIN
- Left JOIN
- Right JOIN
- Full JOIN

- SQL commands are case-insensitive
- SQL values are case-sensitive



### 第2 Tkinter


Widgets:
- Menu
- Button
- Canvas
- Checkbutton
- Entry
- Label
- Frame
