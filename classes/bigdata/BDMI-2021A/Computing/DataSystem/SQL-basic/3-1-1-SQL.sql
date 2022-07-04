--创建创建数据表

CREATE TABLE table1		--表名
(
	c1  INT,		--列1
	c2  INT		--列2
);

--添加数据
INSERT INTO table1 VALUES(1, 2);
INSERT INTO table1 VALUES(1, 2),(2,3);
INSERT INTO table1 (c1) VALUES(1);
INSERT INTO table1 (c2) VALUES(1);

--修改表

ALTER TABLE table1 ADD c3 int; 

ALTER TABLE table1 MODIFY COLUMN c3 varchar; 

alter TABLE table1 drop COLUMN c3; 

ALTER TABLE table1 ADD PRIMARY KEY (c1); 




--查询数据

SELECT * FROM table1;		--查询所有行所有列

SELECT c1 FROM table1;		--查询所有行的c1列

SELECT c1, c2 FROM table1;		--查询所有行的c1,c2列

SELECT * FROM table1 WHERE c1 >= 1000000;	--查询满足c1=1条件的行

--更新数据
UPDATE table1 SET c1 = 1;		--更新所有行的c1列为1

UPDATE table1 SET c1 = 3 where c2=2;		--更新c1列为3 满足c2=2条件

UPDATE table1
	SET c1 = 3		--要更新的列
	WHERE c2 = 3;	--更新条件

--删除数据

DELETE FROM table1 where c2=3;		--删除满足条件的行

DELETE FROM table1
	WHERE c1 = 3;		--删除满足条件的行

DELETE FROM table1; 


-- 连接JOIN

CREATE TABLE A
(
	c1 INT
);

CREATE TABLE B
(
	c1 INT
);

INSERT INTO A VALUES(1),(2),(3);

INSERT INTO B VALUES(2),(3),(4);

select * from A inner join B on(A.c1=B.c1);

select * from A left join B on(A.c1=B.c1); 

select * from A right join B on(A.c1=B.c1); 

select * from A full join B on(A.c1=B.c1); 




