### 第1 Complex SQL statements


```sql

SELECT R.A FROM R, S WHERE R.A=S.A
UNION -- this is an explicit keyword!
SELECT R.A FROM R, T WHERE R.A=T.A

```

```sql

SELECT c.country
FROM   Company c
WHERE  c.cname  IN (
    SELECT pr.manufacturer
    FROM   Purchase p, Product pr
    WHERE  p.name = pr.pname AND p.buyer = 'Mickey'
);

```


### 第2 Python + SQL

- SQLite
- Also possible to use pSQL or other more complex SQL databases; SQLite is a simple baseline

```python
import sqlite3

conn = sqlite3.connect("university.db")
c = conn.cursor()

# Assuming we have a table called students
c.execute("""SELECT * FROM students""")

print(c.fetchall)
    
conn.commit()
conn.close()
```
