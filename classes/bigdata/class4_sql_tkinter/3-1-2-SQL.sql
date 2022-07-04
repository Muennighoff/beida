--drop table if exists product;
drop table if exists product;


create table product(
       pname        varchar primary key, -- name of the product
       price        money,               -- price of the product
       category     varchar,             -- category
       manufacturer varchar NOT NULL     -- manufacturer
);

insert into product values('Gizmo', 19.99, 'Gadgets', 'GizmoWorks');
insert into product values('PowerGizmo', 29.99, 'Gadgets', 'GizmoWorks');
insert into product values('SingleTouch', 149.99, 'Photography', 'Canon');
insert into product values('MultiTouch', 203.99, 'Household', 'Hitachi');

select * from product;

SELECT * from Product 
WHERE category='Gadgets' and price > 20.0;

SELECT Pname, Price, Manufacturer
FROM Product;

SELECT Pname, Price, Manufacturer
FROM Product
WHERE category='Gadgets';

SELECT * FROM Product;

SELECT distinct p0.Manufacturer
     FROM Product p0
     WHERE p0.price < 20.00;


-- this is a nested query!
SELECT
    p.manufacturer, p.pname, p.price
FROM 
    (SELECT distinct p0.Manufacturer
     FROM Product p0
     WHERE p0.price < 20.00) cp, -- this is a nested query!
    Product p
WHERE 
    p.manufacturer = cp.manufacturer and p.price > 20.00;
   



SELECT *  FROM product
where pname LIKE '%Gizmo%';

SELECT category from product;

-- easy to remove duplicates, use the distinct keyword
SELECT DISTINCT category from product;
    
    
-- sometimes we want to order the results.
-- order by is ascending by default!
SELECT   pname, price, manufacturer
FROM     Product
WHERE    price > 50
ORDER BY  price DESC, pname;


-- sometimes we want to order the results.
-- can order like so, each component individually
SELECT   price, manufacturer
FROM     Product
-- the order is "dictionary order" in the clause.
ORDER BY   manufacturer ASC, price DESC;


drop table if exists product; -- This needs to be dropped if exists, see why further down!
drop table if exists company;

create table company (
    cname varchar primary key, -- company name uniquely identifies the company.
    stockprice money, -- stock price is in money 
    country varchar); -- country is just a string
insert into company values ('GizmoWorks', 25.0, 'USA');
insert into company values ('Canon', 65.0, 'Japan');
insert into company values ('Hitachi', 15.0, 'Japan');


select * from company;

drop table if exists product;
pragma foreign_keys = ON; -- WARNING by default off in sqlite
create table product(
       pname varchar primary key, -- name of the product
       price money, -- price of the product
       category varchar, -- category
       manufacturer varchar, -- manufacturer
       foreign key (manufacturer) references company(cname));

insert into product values('Gizmo', 19.99, 'Gadgets', 'GizmoWorks');
insert into product values('PowerGizmo', 29.99, 'Gadgets', 'GizmoWorks');
insert into product values('SingleTouch', 149.99, 'Photography', 'Canon');
insert into product values('MultiTouch', 203.99, 'Household', 'Hitachi');


insert into product values('MultiTouch', 203.99, 'Household', 'Google');


-- the update is rejected!


select * from product;

-- First option (default)- delete is disallowed
delete from company where cname = 'Hitachi';


SELECT pname, price
FROM product, company
where manufacturer=cname and country='Japan' and price <= 200;


SELECT distinct cname -- do we need distinct?
from company where country='Japan';


select distinct pname, price, manufacturer
from product
where price <= 200;


SELECT * 
FROM 
  (SELECT DISTINCT pname, price, manufacturer
   FROM product
   WHERE price <= 200) CheapProducts,
  (SELECT DISTINCT cname
   FROM company
   WHERE country='Japan') JapaneseProducts;
  
  
  
-- Combine them as a join!
SELECT DISTINCT pname, price
FROM 
  (SELECT DISTINCT pname, price, manufacturer
   FROM product
   WHERE price <= 200) CheapProducts,
  (SELECT distinct cname
   FROM company
   WHERE country='Japan') JapaneseProducts
WHERE cname = manufacturer;


-- duplicate answer
SELECT Country
FROM Product, Company
WHERE  Manufacturer=CName AND Category='Gadgets';


--inner Join ²Ù×÷1

drop table if exists product;
drop table if exists purchase;

create table product(
       pname varchar primary key, -- name of the product
       price money, -- price of the product
       category varchar -- category
);

insert into product values('Gizmo',10, 'Gadget'), ('Camera',20, 'photo'), ('OneClick',30, 'photo');

create table purchase(
name varchar,
store varchar
);

insert into purchase values('Gizmo','Wiz'), ('Camera','Rit'),('Camera','Wiz');

select p.pname, pu.store
from product p, purchase pu 
where p.pname = pu.name;


-- Left OutJoin²Ù×÷2


SELECT Product.pname, Purchase.store
FROM Product 
LEFT JOIN Purchase 
ON Product.pname = Purchase.name;

SELECT Product.pname, Purchase.store
FROM Product 
RIGHT JOIN Purchase 
ON Product.pname = Purchase.name;

SELECT Product.pname, Purchase.store
FROM Product 
FULL JOIN Purchase 
ON Product.pname = Purchase.prodName; 











