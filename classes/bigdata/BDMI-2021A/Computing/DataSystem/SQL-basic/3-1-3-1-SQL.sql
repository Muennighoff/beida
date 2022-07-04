--一个非直观的查询 

DROP TABLE IF EXISTS R; DROP TABLE IF EXISTS S; DROP TABLE IF EXISTS T;
CREATE TABLE R (A int); 
CREATE TABLE S (A int); 
CREATE TABLE T (A int);

INSERT INTO R VALUES (1),(2),(3),(4),(5);
INSERT INTO T VALUES (1),(4),(7),(10);

SELECT DISTINCT R.A FROM R, S, T
WHERE R.A=S.A OR R.A=T.A


SELECT DISTINCT R.A FROM R, S, T;


SELECT R.A FROM R, S WHERE R.A=S.A
UNION -- this is an explicit keyword!
SELECT R.A FROM R, T WHERE R.A=T.A


DROP TABLE IF EXISTS S; 
CREATE TABLE S (A int);

INSERT INTO S VALUES (1),(2),(3),(4),(5)


-- UNION ALL example- notice that 1 and 4 occur twice!
SELECT R.A FROM R, S WHERE R.A=S.A
UNION ALL
SELECT R.A FROM R, T WHERE R.A=T.A


SELECT R.A FROM R, S, T WHERE R.A = S.A
INTERSECT
SELECT R.A FROM R, S, T WHERE R.A = T.A


SELECT R.A FROM R, S, T WHERE R.A = S.A
EXCEPT
SELECT R.A FROM R, S, T WHERE R.A = T.A


-- Movies
DROP TABLE if exists Movies;

CREATE Table Movie
(
title varchar,
year1 int,
director varchar,
length1 int
);

INSERT into Movie
values
('射雕',1983,'张三',90),
('天龙',1997,'王一',90),
('射雕',1985,'李四',90),
('笑傲',1998,'赵五',90),
('笑傲',2007,'陈六',90);

--SELECT DISTINCT m1.title
SELECT m1.title, m1.director
FROM Movie m1, Movie m2
WHERE m1.title=m2.title and m1.year1<> m2.year1;


--SELECT DISTINCT title (Wrong)
SELECT title, director
FROM   Movie AS m
--WHERE  year1 <>  (
WHERE  year1 <> ANY (
SELECT  year1
FROM    Movie
WHERE  title =  m.title);


-- Nested QUERY 

pragma foreign_keys = ON; -- WARNING: by default off in sqlite

drop table if exists product; -- This needs to be dropped if exists, see why further down!
drop table if exists company;

create table company (
    cname varchar primary key, -- company name uniquely identifies the company.
    stockprice money, -- stock price is in money 
    country varchar); -- country is just a string

insert into company 
values 
('GizmoWorks', 25.0, 'USA'),
('Canon', 65.0, 'Japan'),
('Hitachi', 15.0, 'Japan');

create table product(
       pname varchar primary key, -- name of the product
       price money, -- price of the product
       category varchar, -- category
       manufacturer varchar, -- manufacturer
       foreign key (manufacturer) references company(cname));

insert into product 
values
('Gizmo', 19.99, 'Gadgets', 'GizmoWorks'),
('SingleTouch', 149.99, 'Photography', 'Canon'),
('PowerGizmo', 29.99, 'Gadgets', 'GizmoWorks'),
('MultiTouch', 203.99, 'Household', 'Hitachi');



SELECT * FROM Product;

SELECT pname,price FROM Product
ORDER BY pname

SELECT pname, price FROM Product
ORDER BY Price DESC 


SELECT distinct pname FROM Product
ORDER BY Price

drop table if exists purchase;

create table purchase(
name varchar,
store varchar,
buyer varchar
);

insert into purchase 
values
('Gizmo','Wiz','Mickey'), 
('Camera','Rit','Mickey'),
('Camera','Wiz','Bob');


SELECT c.country
FROM   Company c
WHERE  c.cname  IN (
	SELECT pr.manufacturer
    FROM   Purchase p, Product pr
    WHERE  p.name = pr.pname AND p.buyer = 'Mickey');


--简单销售示例，创建 Sales
-- Note that date is an int here just to simplify things

DROP TABLE IF EXISTS Sales;
CREATE TABLE sales (
	product TEXT, 
	date INT, 
	price INT, --float
	quantity INT
);

INSERT INTO sales 
VALUES 
('bagel', 21, 1, 20),
('banana', 3, 2, 10),
('banana', 10, 1, 10),
('bagel', 25, 1.5, 20),
('apple', 1, 3, 5),
('apple', 1, 3, 5);


--SUM

SELECT SUM(price * quantity)
FROM   Sales
WHERE  product = 'bagel';


--MIN
SELECT product, MIN(price*quantity) 
FROM sales
Group By product
HAVING SUM(quantity)>10


--MIN  
SELECT p.product, MIN(p.totalquantity)
FROM  
(SELECT product, SUM(quantity) as totalquantity 
FROM sales s
WHERE product=s.product
Group BY product
HAVING sum(quantity)>10) p
WHERE 1;

--MAX
SELECT product, MAX(price*quantity) 
FROM sales
Group By product
HAVING SUM(quantity)>10

--MAX
SELECT p.product, MAX(p.totalquantity)
FROM  
(SELECT product, SUM(quantity) as totalquantity 
FROM sales s
WHERE product=s.product
Group BY product
HAVING SUM(quantity)>10
) p
WHERE 1;


--AVG


--Group By
SELECT   product,
	     SUM(price * quantity) AS TotalSales
FROM     Sales
WHERE    date > 1
GROUP BY product;

--SUM 
SELECT   product,
	        SUM(price * quantity) AS TotalSales
FROM     Sales
WHERE    date > 1
GROUP BY product

--HAVING 
SELECT   product, SUM(price*quantity)
FROM     sales 
WHERE    date > 1
GROUP BY product
HAVING   SUM(quantity) > 10



-- 复杂销售示例， 创建franchise,  store,   bagel,   purchase

DROP TABLE IF EXISTS franchise;
CREATE TABLE franchise (name TEXT, db_type TEXT);
INSERT INTO franchise VALUES ('Bobs Bagels', 'NoSQL');
INSERT INTO franchise VALUES ('eBagel', 'NoSQL');
INSERT INTO franchise VALUES ('BAGEL CORP', 'MySQL');

DROP TABLE IF EXISTS store;
CREATE TABLE store (franchise TEXT, location TEXT);
INSERT INTO store VALUES ('Bobs Bagels', 'NYC');
INSERT INTO store VALUES ('eBagel', 'PA');
INSERT INTO store VALUES ('BAGEL CORP', 'Chicago');
INSERT INTO store VALUES ('BAGEL CORP', 'NYC');
INSERT INTO store VALUES ('BAGEL CORP', 'PA');

DROP TABLE IF EXISTS bagel;
CREATE TABLE bagel (name TEXT, price MONEY, made_by TEXT);
INSERT INTO bagel VALUES ('Plain with shmear', 1.99, 'Bobs Bagels');
INSERT INTO bagel VALUES ('Egg with shmear', 2.39, 'Bobs Bagels');
INSERT INTO bagel VALUES ('eBagel Drinkable Bagel', 27.99, 'eBagel');
INSERT INTO bagel VALUES ('eBagel Expansion Pack', 1.99, 'eBagel');
INSERT INTO bagel VALUES ('Plain with shmear', 0.99, 'BAGEL CORP');
INSERT INTO bagel VALUES ('Organic Flax-seed bagel chips', 0.99, 'BAGEL CORP');

DROP TABLE IF EXISTS purchase;
-- Note that date is an int here just to simplify things
CREATE TABLE purchase (bagel_name TEXT, franchise TEXT, date INT, quantity INT, purchaser_age INT);
INSERT INTO purchase VALUES ('Plain with shmear', 'Bobs Bagels', 1, 12, 28);
INSERT INTO purchase VALUES ('Egg with shmear', 'Bobs Bagels', 2, 6, 47);
INSERT INTO purchase VALUES ('Plain with shmear', 'BAGEL CORP', 2, 12, 24);
INSERT INTO purchase VALUES ('Plain with shmear', 'BAGEL CORP', 3, 1, 17);
INSERT INTO purchase VALUES ('eBagel Expansion Pack', 'eBagel', 1, 137, 5);
INSERT INTO purchase VALUES ('Plain with shmear', 'Bobs Bagels', 4, 24, NULL);


SELECT franchise FROM store WHERE location = 'NYC'
UNION
SELECT franchise FROM store WHERE location = 'PA';

 
SELECT b.name, b.price
FROM bagel b
WHERE b.made_by = 'eBagel'
  AND EXISTS (SELECT name FROM bagel WHERE made_by <> 'eBagel' AND price > b.price);

 

      
--JOIN

SELECT DISTINCT b.name 
FROM bagel b, purchase p 
WHERE b.name = p.bagel_name AND b.made_by = p.franchise;

SELECT DISTINCT b.name 
FROM bagel b
    INNER JOIN purchase p ON b.name = p.bagel_name AND b.made_by = p.franchise;

   
SELECT DISTINCT b.name 
FROM bagel b
    LEFT OUTER JOIN purchase p ON b.name = p.bagel_name AND b.made_by = p.franchise;

 
 

--MIN
 
SELECT MIN(price) FROM bagel WHERE made_by = 'eBagel';
 
--AVG
 
SELECT AVG(price) FROM bagel WHERE made_by = 'eBagel';

--MAX
 
SELECT MAX(price) FROM bagel WHERE made_by = 'eBagel';

--count

SELECT COUNT(*) AS "Number of Stores in PA" FROM store WHERE location = 'PA';

SELECT COUNT(location) FROM store;

SELECT COUNT(DISTINCT location) FROM store;

--SUM

SELECT SUM(b.price * p.quantity) AS net_sales
FROM bagel b, purchase p
WHERE b.name = p.bagel_name;

SELECT b.made_by, SUM(b.price * p.quantity) AS revenue
FROM bagel b, purchase p
WHERE b.made_by = p.franchise AND b.name = p.bagel_name
GROUP BY b.made_by;

SELECT b.name, SUM(b.price * p.quantity) AS sales
FROM bagel b, purchase p
WHERE b.name = p.bagel_name AND b.made_by = p.franchise
GROUP BY b.name
HAVING SUM(p.quantity) > 12;

SELECT *
FROM bagel b, purchase p
WHERE b.name = p.bagel_name AND b.made_by = p.franchise;



SELECT b.name, SUM(b.price * p.quantity) AS sales
FROM bagel b, purchase p
WHERE b.name = p.bagel_name AND b.made_by = p.franchise
GROUP BY b.name
HAVING SUM(p.quantity) > 12;

--LIKE

SELECT DISTINCT made_by FROM bagel WHERE name LIKE '%shmear%';

SELECT DISTINCT made_by
FROM bagel
WHERE made_by NOT IN (
    SELECT made_by
    FROM bagel
    WHERE name NOT LIKE '%shmear%');
   
SELECT * FROM purchase WHERE bagel_name LIKE '%shmear%';

SELECT * FROM purchase 
WHERE bagel_name LIKE '%shmear%' 
  AND (purchaser_age >= 5 OR purchaser_age < 5);
 

SELECT * FROM purchase
WHERE bagel_name LIKE '%shmear%'
  AND (purchaser_age >= 5 OR purchaser_age < 5 
       OR purchaser_age IS NULL);








